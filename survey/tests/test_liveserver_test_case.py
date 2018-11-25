from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from security.utils import createHash
from security.models import LinkHash
from survey.models import SurveyOrderModel


class SurveyOrderTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(SurveyOrderTestCase, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SurveyOrderTestCase, cls).tearDownClass()

    def create_order_obj(self):
        return SurveyOrderModel.objects.create(customer_staff='SF',
                                               customer_faktura_id=999,
                                               globalstar=True,
                                               inc_or_gmbh='gmbh')

    def create_hash_obj(self, obj):
        hash = createHash()
        new_hash = f'{hash}{obj.customer_staff}{obj.pk}'
        return LinkHash.objects.create(hash=new_hash)

    def create_hash(self, obj):
        hash = self.create_hash_obj(self.create_order_obj())
        order_obj = obj.objects.get(customer_faktura_id=999)
        return (hash.hash, order_obj.customer_staff, order_obj.pk)

    def test_fillout_order(self):
        hash = self.create_hash(SurveyOrderModel)
        url = 'http://localhost:8000/survey/HRGO_eeWcIXUTT15'
        self.selenium.get(url)
        self.selenium.find_element_by_id('id_other_color')
