from django.test import TestCase

from survey.forms import SurveyCreateForm


class SurveryOrderFormTest(TestCase):
    def test_form_without_entries(self):
        data = {}
        form = SurveyCreateForm(data=data)
        self.assertFalse(form.is_valid())

    # def test_valid_form_without_optionals(self):
    #     data = {
    #         'animal_species': 'TestFox',
    #         'belt_shape': ' round-shaped',
    #         'belt_width': '25 mm',
    #         'belt_thickness': '3.4 mm (SF/SF)',
    #         'belt_edge': 'round',
    #         'belt_colour': 'black',
    #         'other_color': None,
    #         'belt_labeling': False,
    #         'belt_labeling_instructions': None,
    #         'belt_plates': False,
    #         'belt_plates_instructions': None,
    #         'reflective_stripes': False,
    #         'vhf_beacon_frequency': '1234',
    #         'mortality_sensor': 22,
    #         'notification_mail': 'test@test.com',
    #         'notification_sms': '1222222',
    #         'utc_lmt': 'utc',
    #         'utc_correction': None,
    #         'gps_schedule': 'schedulig',
    #         'vhf_beacon_schedule': 'some other schedule',
    #         'id_tag': False,
    #         'globalstar': True,
    #         'iridium': False,
    #         'iridium_num_of_fixes_gps': None,
    #         'contact_name_airtime_fee': 'name',
    #         'contact_mail_airtime_fee': 'rest@test.com',
    #         'airtime_contract': None,
    #         'external_dropoff': False,
    #         'external_dropoff_controll': None,
    #         'external_dropoff_real_time': None,
    #         'external_dropoff_abs_time': None,
    #         'comment': None,
    #         'battery_size': None,
    #         'number_of_collars': None,
    #         'nom_collar_circumference': None,
    #     }
    #
    #     form = SurveyCreateForm(data=data)
    #     print(form)
    #     self.assertTrue(form.is_valid())
