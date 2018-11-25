from django.test import TestCase
from vertexLite.forms import VertexLiteCreateForm


class VertexLiteFormsTest(TestCase):

    def test_form_minimal_selection_success(self):
        data = {
            'animal_species': 'wolf',
            'number_of_collars': '3$4$',
            'battery_size': '1C$1C$',
            'belt_shape': 'round-shaped',
            'belt_width': '25 mm',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': 'round',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), True)

    def test_form_minimal_selection_missing_num_of_collars_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '',
            'battery_size': '1C$1C$',
            'belt_shape': 'round-shaped',
            'belt_width': '25 mm',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': 'round',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)

    def test_form_minimal_selection_missing_battery_size_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '1$1$',
            'battery_size': '',
            'belt_shape': 'round-shaped',
            'belt_width': '25 mm',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': 'round',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)

    def test_form_minimal_selection_missing_belt_shape_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '1$1$',
            'battery_size': '1C$2D$',
            'belt_shape': '',
            'belt_width': '25 mm',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': 'round',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)

    def test_form_minimal_selection_missing_belt_width_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '1$1$',
            'battery_size': '1C$2D$',
            'belt_shape': 'round-shaped',
            'belt_width': '',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': 'round',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)

    def test_form_minimal_selection_missing_belt_thickness_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '1$1$',
            'battery_size': '1C$2D$',
            'belt_shape': 'round-shaped',
            'belt_width': '25 mm',
            'belt_thickness': '',
            'belt_edge': 'round',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)

    def test_form_minimal_selection_missing_belt_edge_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '1$1$',
            'battery_size': '1C$2D$',
            'belt_shape': 'round-shaped',
            'belt_width': '25 mm',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': '',
            'belt_colour': 'black',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)

    def test_form_minimal_selection_missing_belt_color_raise_error(self):
        data = {
            'animal_species': 'Wolf',
            'number_of_collars': '1$1$',
            'battery_size': '1C$2D$',
            'belt_shape': 'round-shaped',
            'belt_width': '25 mm',
            'belt_thickness': '3.4 mm (SF/SF)',
            'belt_edge': 'round',
            'belt_colour': 'Other',
            'vhf_beacon_frequency': '12233. 12123, 123123, 123',
            'mortality_sensor': '23',
            'notification_mail': 'test@test.com',
            'utc_lmt': 'utc',
            'gps_schedule': '2',
            'vhf_beacon_schedule': '2',
            'globalstar': True,
        }
        self.assertEqual(VertexLiteCreateForm(data=data).is_valid(), False)