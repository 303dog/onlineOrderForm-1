import os
import datetime
from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.datetime_safe import date
from django.views.generic import TemplateView
from easy_pdf.views import PDFTemplateView
from extras.utils import STAFF_EMAIL_ADR
from orderContact.models import OrderContactDeliveryAddresse
from orderForm.own_mixins import HashRequiredMixin
from security.models import LinkHash
from extras.utils import ERROR_CONTEXT
from orderContact.forms import InvoiceAddresseForm, DeliveryAddresseForm
from orderContact.models import OrderContactInvoiceAddresse
from orderForm import settings


class ThanksForOderView(HashRequiredMixin, TemplateView):
    template_name = 'thanks.html'
    obj = None

    def __init__(self, obj, template_name='thanks.html'):
        super(ThanksForOderView, self).__init__()
        self.obj = obj
        self.template_name = template_name

    def get_context_data(self, **kwargs):
        context = super(ThanksForOderView, self).get_context_data(**kwargs)
        context['pk'] = kwargs['pk']
        order = self.obj.objects.get(pk=kwargs['pk'])
        oldHash = get_object_or_404(LinkHash, hash=kwargs['hash'])
        _ = kwargs['hash'][: (-1) * len(kwargs['hash'][14:])]
        staff_initials = _[-2:]
        if staff_initials == 'CL':
            staff_initials = 'CLD'
        if oldHash:
            #oldHash.delete()
            subject = 'Online survey-order-' + str(order.order_no) + '-' + str(order.contacts_faktura_id) + '-' + str(order.customer_invoice_address.contact_person)
            send_mail(subject,
                      str(order.contacts_faktura_id) + ' Finished his order \n http://192.168.0.34:9003/sales/list-open-orders/',
                      'mail@foobar.com',
                      [
                          STAFF_EMAIL_ADR[staff_initials],
                      ],
                      fail_silently=False)
        return context


class PDFView(PDFTemplateView):

    template_name = ''
    obj = None
    pdf_filename = str(date.today()) +'.pdf'
    download_filename = str(date.today()) +'.pdf'

    def __init__(self, obj, template_name, pdf_filename='order_from', download_filename='order_from', **kwargs):
        super().__init__(**kwargs)
        self.obj = obj
        self.template_name = template_name
        self.pdf_filename = pdf_filename + self.pdf_filename
        self.download_filename = download_filename + self.download_filename

    # def dispatch(self, request, *args, **kwargs):
    #     return super(PDFView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PDFView, self).get_context_data(pagesize='A4')
        obj = get_object_or_404(self.obj, pk=kwargs['pk'])
        context['object'] = obj
        if('vertex_lite' in str(obj.__str__)):
            context['space'] = int(10 - (len(obj.vhf_beacon_frequency)) / 100)
        else:
            context['space'] = int(26 - (len(obj.vhf_beacon_frequency)) / 100)
        context['less_than_12_weeks'] = True if obj.delivery_time < (datetime.date.today() + datetime.timedelta(days=12*7)) else False
        context['customer_mail'] = STAFF_EMAIL_ADR[obj.customer_staff]
        #context['customer'] = Staff.objects.get(initialies=obj.customer_staff)
        # context['base_url'] = 'file://'.join(settings.STATIC_ROOT) + '/'
        return context


def get_address_fields(form):
    kwargs = {'org_name': form['organisation_name'].value(),
              'address': form['complete_addresse'].value(),
              'zip': form['zip_code'].value(),
              'city': form['city'].value(),
              'country': form['country'].value(),
              'contact': form['contact_person'].value(),
              'mail': form['email_addresse'].value(),
              'tel': form['telephone_nr'].value(),
              }
    return kwargs


def get_delivery_address_fields(form):
    kwargs = {'org_name': form['delivery_organisation_name'].value(),
              'address': form['delivery_complete_addresse'].value(),
              'zip': form['delivery_zip_code'].value(),
              'city': form['delivery_city'].value(),
              'country': form['delivery_country'].value(),
              'contact': form['delivery_contact_person'].value(),
              'mail': form['delivery_email_addresse'].value(),
              'tel': form['delivery_telephone_nr'].value(),
              }
    return kwargs


def create_delivery_address(object, kwargs):
    obj = object
    if obj.__class__ != OrderContactDeliveryAddresse:
        obj.organisation_name = kwargs['org_name']
        obj.complete_addresse =kwargs['address']
        obj.zip_code = kwargs['zip']
        obj.city = kwargs['city']
        obj.country = kwargs['country']
        obj.contact_person = kwargs['contact'].strip()
        obj.email_addresse = kwargs['mail']
        obj.telephone_nr = kwargs['tel']
        obj.save()
    else:
        obj.delivery_organisation_name = kwargs['org_name']
        obj.delivery_complete_addresse = kwargs['address']
        obj.delivery_zip_code = kwargs['zip']
        obj.delivery_city = kwargs['city']
        obj.delivery_country = kwargs['country']
        obj.delivery_contact_person = kwargs['contact']
        obj.delivery_email_addresse = kwargs['mail']
        obj.delivery_telephone_nr = kwargs['tel']
        obj.save()
    return obj


def check_delivery_addresse_form(kwargs):
    if len(kwargs['org_name']) > 1 and len(kwargs['address']) > 1 and \
                    len(kwargs['zip']) > 1 and len(kwargs['city']) > 1 and \
                    len(kwargs['country']) > 1 and len(kwargs['contact']) > 1 and \
                    len(kwargs['mail']) > 1 and len(kwargs['tel']) > 1:
        return True


def get_address_form(request, hash, form_class, pk, obj):
    if get_object_or_404(LinkHash, hash=hash):
        model_name = obj.__repr__(obj)
        data = {
            'delivery_time': datetime.datetime.today() + datetime.timedelta(days=12 * 7)
        }
        context = {
            'invoice_address': InvoiceAddresseForm,
            'delivery_form': DeliveryAddresseForm,
            'payment_form': form_class(initial=data),
            'hash': hash,
            'pk': pk,
            'model': str(model_name)+':'+str(model_name)+'_customer_form',
        }
        return render(request, 'surveyDeliveryAddress.html', context)
    else:
        raise 404


def customer_deliver_address_function(request, hash, pk, obj, success_url, form_class):
    '''
    :param request:
    :param hash:
    :param pk:
    :param obj: = Model from object
    :param success_url: = bsp 'sruvey:thanks' without args and kwargs its not neccessarry
    :param form_class -> for payment options
    :return: if success redirect to success_url else to template_name with error context
    '''
    if request.method != 'POST':
        return get_address_form(request, hash, form_class, pk, obj)
    else:
        invoice_form = InvoiceAddresseForm(request.POST)
        delivery_form = DeliveryAddresseForm(request.POST)
        payment_form = form_class(request.POST)
        order = obj.objects.get(pk=pk)
        error_context = ERROR_CONTEXT
        error_context['payment_form'] = form_class
        if payment_form.is_valid():
            order.payment_option = payment_form['payment_option'].value()
            order.order_no = payment_form['order_no'].value()
            order.as_post = payment_form['as_post'].value()
            order.as_email = payment_form['as_email'].value()
            order.vat_ein_number = payment_form['vat_ein_number'].value()
            order.delivery_time = payment_form['delivery_time'].value()
        if request.POST.get('same_address') == 'same':
            if invoice_form.is_valid():
                kwargs = get_address_fields(invoice_form)
                order.customer_invoice_address = create_delivery_address(OrderContactInvoiceAddresse(), kwargs)
                order.same_addr = True
                order.save()
                return redirect(reverse(success_url, kwargs={'hash': hash, 'pk': pk}))
            else:
                return render(request, 'surveyDeliveryAddress.html', error_context)
        else:
            if delivery_form.is_valid() and invoice_form.is_valid():
                if len(delivery_form['delivery_organisation_name'].value()) > 1:
                    kwargs_invoice = get_address_fields(invoice_form)
                    kwargs_delivery = get_delivery_address_fields(delivery_form)
                    if check_delivery_addresse_form(kwargs_delivery) and check_delivery_addresse_form(kwargs_invoice):
                        order.customer_invoice_address = create_delivery_address(OrderContactInvoiceAddresse(), kwargs_invoice)
                        order.delivery_addresse = create_delivery_address(OrderContactDeliveryAddresse(), kwargs_delivery)
                        order.same_addr = False
                        order.save()
                        return redirect(reverse(success_url, kwargs={'hash': hash, 'pk': pk}))
                    else:
                        return render(request, 'surveyDeliveryAddress.html', error_context)
                else:
                    return render(request, 'surveyDeliveryAddress.html', error_context)
        return render(request, 'surveyDeliveryAddress.html', error_context)


def download(request, path, name, file):
    path = path + '/' + name + '/' + file
    file_path = settings.BASE_DIR.replace('/orderForm', '') + '/' + path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            if '.pdf' in file:
                response['Content_Type'] = 'application/pdf'

            elif '.doc' in file:
                response['Content_Type'] = 'application/msword'

            elif '.vsgf' in file:
                response['Content_Type'] = 'application/msword'

            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def download_gps(request, path, name, file):
    path = path + '/' + name + '/gps_schedule/' + file
    file_path = settings.BASE_DIR.replace('/orderForm', '') + '/' + path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            if '.pdf' in file:
                response['Content_Type'] = 'application/pdf'
            elif '.doc' in file:
                response['Content_Type'] = 'application/msword'

            elif '.vsgf' in file:
                response['Content_Type'] = 'application/msword'
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404


def download_vhf(request, path, name, file):
    path = path + '/' + name + '/vhf_schedule/' + file
    file_path = settings.BASE_DIR.replace('/orderForm', '') + '/' + path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            if '.pdf' in file:
                response['Content_Type'] = 'application/pdf'

            elif '.doc' in file:
                response['Content_Type'] = 'application/msword'

            elif '.vsgf' in file:
                response['Content_Type'] = 'application/msword'

            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404