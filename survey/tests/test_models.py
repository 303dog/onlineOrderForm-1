from django.test import TestCase

from survey.models import SurveyOrderModel


class SurveyOrderTest(TestCase):
    def setUp(self):
        SurveyOrderModel.objects.create(
            customer_faktura_id=1234,
        )

    def test_blank_survey_created(self):
        obj = SurveyOrderModel.objects.get(customer_faktura_id=1234)
        self.assertTrue(obj)

    # def test_finish_survey_order_without_address_success(self):
    #     obj = SurveyOrderModel.objects.get(customer_faktura_id=1234)
    #     obj.number_of_collars = '$1$2'
    #     obj.animal_species = 'wolf'
    #     obj.battery_size = '$2D$3D'
    #     obj.belt_shape = ''
    #     obj.nom_collar_circumference = '2'
    #     obj.vhf_beacon_frequency = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l'
    #     obj.mortality_sensor = 1
    #     obj.utc_lmt = 'utc'
    #     obj.globalstar = True
    #