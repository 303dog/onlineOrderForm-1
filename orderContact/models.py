from django.db import models
from django.urls import reverse


class OrderContactInvoiceAddresse(models.Model):
    organisation_name = models.CharField(max_length=355, null=True)
    complete_addresse = models.CharField(max_length=355, null=True)
    zip_code = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    contact_person = models.CharField(max_length=355, null=True)
    email_addresse = models.EmailField(null=True)
    telephone_nr = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.organisation_name

    def get_update_link(self):
        return reverse('collar:orderinvoiceaddressupdate', kwargs={'pk': self.pk})


class OrderContactDeliveryAddresse(models.Model):
    delivery_organisation_name = models.CharField(max_length=355, null=True, blank=True)
    delivery_complete_addresse = models.CharField(max_length=355, null=True, blank=True)
    delivery_zip_code = models.CharField(max_length=15, null=True, blank=True)
    delivery_city = models.CharField(max_length=255, null=True, blank=True)
    delivery_country = models.CharField(max_length=255, null=True, blank=True)
    delivery_contact_person = models.CharField(max_length=255, null=True, blank=True)
    delivery_email_addresse = models.EmailField(null=True, blank=True)
    delivery_telephone_nr = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.delivery_organisation_name if self.delivery_organisation_name else 'Same as invoice'

    def get_update_link(self):
        return reverse('collar:orderdeliveryaddressupdate', kwargs={'pk': self.pk})
