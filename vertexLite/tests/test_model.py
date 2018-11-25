from django.test import TestCase
from vertexLite.models import VertexLiteOrderModel
from extras.utils import BELTSHAPES
from extras.utils import BELTWIDTH, BELTTHICKNESS, BELTEDGES, BELTCOLORS


class VertexLiteModelTest(TestCase):

    def get_new_created_model(self):
        vertex_lite_obj = VertexLiteOrderModel.objects.create(
            customer_faktura_id=1,
            iridium=True,
            customer_staff='SF',
            operation_Number='ABC_123'
        )
        return vertex_lite_obj

    def test_create_initial_model(self):
        vertex_lite_obj = self.get_new_created_model()
        self.assertTrue(vertex_lite_obj)

    def test_update_model_without_adresse(self):
        vertex_lite_obj = self.get_new_created_model()
        vertex_lite_obj.animal_species = 'wolf'
        vertex_lite_obj.battery_size = '1D$2D$3D$'
        vertex_lite_obj.number_of_collars = '2$2$2$'
        vertex_lite_obj.nom_collar_circumference = '20$23$21$'
        vertex_lite_obj.belt_shape = 'round'
        vertex_lite_obj.belt_width = '43'
        vertex_lite_obj.belt_thickness = '21'
        vertex_lite_obj.belt_edge = 'no'
        vertex_lite_obj.belt_colour = 'black'
        vertex_lite_obj.vhf_beacon_frequency = '1234, 31221., 121213,12312123,123123.123213,123231.213123'
        vertex_lite_obj.mortality_sensor = 12
        vertex_lite_obj.notification_mail = 'test@test.com'
        vertex_lite_obj.notification_sms = '+49512368452'
        vertex_lite_obj.utc_lmt = 'utc'
        vertex_lite_obj.gps_schedule = 'every 12'
        vertex_lite_obj.vhf_beacon_schedule = '21'
        vertex_lite_obj.iridium_num_of_fixes_gps = 4
        vertex_lite_obj.iridium_contract_type = 'my type'
        vertex_lite_obj.contact_name_airtime_fee = 'neuer contact'
        vertex_lite_obj.contact_mail_airtime_fee = 'test@test.com'
        vertex_lite_obj.save()
        self.assertIsNotNone(VertexLiteOrderModel.objects.get(animal_species='wolf'))

    def test_form_minimal_selection_gsm_mode_autocreate(self):
        vertex_lite_obj = self.get_new_created_model()
        vertex_lite_obj.animal_species = 'wolf'
        vertex_lite_obj.battery_size = '1D$2D$3D$'
        vertex_lite_obj.number_of_collars = '2$2$2$'
        vertex_lite_obj.nom_collar_circumference = '20$23$21$'
        vertex_lite_obj.belt_shape = 'round'
        vertex_lite_obj.belt_width = '43'
        vertex_lite_obj.belt_thickness = '21'
        vertex_lite_obj.belt_edge = 'no'
        vertex_lite_obj.belt_colour = 'black'
        vertex_lite_obj.vhf_beacon_frequency = '1234, 31221., 121213,12312123,123123.123213,123231.213123'
        vertex_lite_obj.mortality_sensor = 12
        vertex_lite_obj.notification_mail = 'test@test.com'
        vertex_lite_obj.notification_sms = '+49512368452'
        vertex_lite_obj.utc_lmt = 'utc'
        vertex_lite_obj.gps_schedule = 'every 12'
        vertex_lite_obj.vhf_beacon_schedule = '21'
        vertex_lite_obj.iridium = False
        vertex_lite_obj.gsm = True

        vertex_lite_obj.save()
        obj = VertexLiteOrderModel.objects.get(gsm=True)
        self.assertTrue(obj.gsm_vectronic_sim)
        self.assertEqual(obj.gsm_mode, '8')
