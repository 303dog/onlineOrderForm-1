from django import forms

from .models import OrderContactDeliveryAddresse
from .models import OrderContactInvoiceAddresse


class InvoiceAddresseForm(forms.ModelForm):
    class Meta:
        model = OrderContactInvoiceAddresse
        fields = '__all__'
        labels = {
            'complete_addresse': 'Street',
            'email_addresse': 'e-mail address',
            'telephone_nr': 'telephone'
        }


class DeliveryAddresseForm(forms.ModelForm):
    class Meta:
        model = OrderContactDeliveryAddresse
        fields = '__all__'
        labels = {
            'delivery_organisation_name': 'Dlvy org name',
            'delivery_complete_addresse': 'Dlvy street',
            'delivery_zip_code': 'Dlvy zip code',
            'delivery_city': 'Dlvy city',
            'delivery_country': 'Dlvy country',
            'delivery_contact_person': 'Dlvy contact person',
            'delivery_email_addresse': 'Dlvy e-mail address',
            'delivery_telephone_nr': 'Dlvy telephone',
        }

    def clean(self):
        cleaned_data = super(DeliveryAddresseForm, self).clean()
        organisation_name = cleaned_data.get('delivery_organisation_name')
        complete_addresse = cleaned_data.get('delivery_complete_addresse')
        zip_code = cleaned_data.get('delivery_zip_code')
        city = cleaned_data.get('delivery_city')
        country = cleaned_data.get('delivery_country')
        contact_person = cleaned_data.get('delivery_contact_person')
        email_addresse = cleaned_data.get('delivery_email_addresse')
        telephone_nr = cleaned_data.get('delivery_telephone_nr')
        belt_thickness = cleaned_data.get('delivery_belt_thickness')
        belt_colour = cleaned_data.get('delivery_belt_colour')

        if organisation_name is not None:
            if len(organisation_name) < 2:
                self.add_error('organisation_name', 'Please fill in your organisation name')
        if complete_addresse is not None:
            if len(complete_addresse) < 2:
                self.add_error('complete_addresse', 'Please check your address')
        if zip_code is not None:
            if len(zip_code) < 2:
                self.add_error('zip_code', 'Please check your zip code')
        if city is not None:
            if len(city) < 2:
                self.add_error('city', 'Please check your city')
        if country is not None:
            if len(country) < 2:
                self.add_error('country', 'Please check your country')
        if contact_person is not None:
            if len(contact_person) < 2:
                self.add_error('contact_person', 'Please check your contact person')
        if email_addresse is not None:
            if len(email_addresse) < 2 and '@' not in email_addresse:
                self.add_error('Please check your email address')
        if telephone_nr is not None:
            if len(telephone_nr) < 2:
                self.add_error('telephone_nr', 'Please check your telephone number')
        if belt_thickness is not None:
            if '-------' in belt_thickness:
                self.add_error('belt_thickness', 'Please select a valid choice')
        if belt_colour is not None:
            if '--------' in belt_colour:
                self.add_error('belt_colour', 'Please select a valid choice')