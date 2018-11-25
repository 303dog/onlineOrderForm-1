import datetime
import re
import urllib

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from security.utils import createHash
from security.models import LinkHash
from survey.models import SurveyOrderModel


class SurveyOrderViewTest(TestCase):
    c = Client()

    def create_hash_obj(self, obj):
        hash = createHash()
        new_hash = f'{hash}{obj.customer_staff}{obj.pk}'
        return LinkHash.objects.create(hash=new_hash)

    def create_survey_order(self, operation_number):
        return SurveyOrderModel.objects.create(as_post=False,
                                               as_email=False,
                                               customer_faktura_id=1234,
                                               contacts_faktura_id=4444,
                                               same_addr=False,
                                               customer_staff='SF',
                                               external_dropoff=False,
                                               globalstar=False,
                                               iridium=False,
                                               belt_labeling=False,
                                               belt_plates=False,
                                               created_at=datetime.date.today(),
                                               order_acceptet=False,
                                               operation_Number=operation_number
                                               )

    def get_test_data(self):
        obj = self.create_survey_order(147)
        h = self.create_hash_obj(obj)
        return (obj, h)

    def get_logo_in_html(self):
        return '<img src="https://www.vectronic-aerospace.com/wp-content/uploads/2016/04/logo180.gif"'

    def get_test_update_url(self, *args):
        d = args[0]
        return f'/survey/update-order-form/{d[1].hash}/{d[0].pk}/'

    def get_test_delivery_url(self, *args):
        d = args[0]
        return f'/survey/delivery-address/{d[1].hash}/{d[0].pk}/'

    def test_update_view_with_invalid_hash(self):
        obj = self.create_survey_order(1234)
        response = self.client.get(obj.get_sells_update_url('absdefgh362880q'))
        self.assertEqual(response.status_code, 404)

    def test_client_landing_page_redirect(self):
        d = self.get_test_data()
        response = self.c.get(f'/survey/{d[1].hash}/')
        self.assertEqual(response.status_code, 302)

    def test_client_update_page(self):
        response = self.c.get(self.get_test_update_url(self.get_test_data()), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_surveyform_exists_in_update_url(self):
        response = self.c.get(self.get_test_update_url(self.get_test_data()), follow=True)
        html = response.content.decode()
        self.assertIn(self.get_logo_in_html(), html)
        self.assertTemplateUsed(response, 'surveyForm.html')
        self.assertEqual(response.status_code, 200)

    def test_images_exists(self):
        response = self.c.get(self.get_test_update_url(self.get_test_data()), follow=True)
        html = response.content.decode()
        self.assertIn('Belt_Edge_round.png', html)
        self.assertIn('Belt_Edge_smooth.png', html)
        self.assertIn('vertex_survey_round.png', html)
        self.assertIn('vertex_survey_drop.png', html)
        self.assertIn('survey_collar_colors2.png', html)

    def test_flyer_links(self):
        response = self.c.get(self.get_test_update_url(self.get_test_data()), follow=True)
        html = response.content.decode()
        links = re.findall(r'<a href=[\'"]?([^\'">]+)', html)
        for link in links:
            if 'https://' in link:
                if 'Flyer_' in link:
                    request_info = dict(urllib.request.urlopen(link).info())
                    self.assertIn('application/pdf', request_info['Content-Type'])

    def test_deliveryAddressForm_exists_in_delivery_address(self):
        response = self.c.get(self.get_test_delivery_url(self.get_test_data()), follow=True)
        html = response.content.decode()
        self.assertIn(self.get_logo_in_html(), html)
        self.assertTemplateUsed(response, 'surveyDeliveryAddress.html')
        self.assertEqual(response.status_code, 200)