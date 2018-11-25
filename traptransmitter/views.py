from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from orderForm.own_decorator import hash_is_allowed
from extras.views import customer_deliver_address_function, ThanksForOderView, PDFView
from orderForm.own_mixins import HashRequiredMixin
from traptransmitter.forms import TrapTransmitterCreateForm
from traptransmitter.models import TrapTransmitterOrderModel
from traptransmitter.forms import TTPaymentOptionForm
from orderForm.own_mixins import ProveHashMixin


@hash_is_allowed
def trapTransmitterForm(request, hash):
    return redirect(reverse('trapTransmitter:trapTransmitter_customer_form',
                                kwargs={'hash': hash,
                                        'pk': hash[14:]}
                                ))


class CustomerTrapTransmitterUpdate(HashRequiredMixin, ProveHashMixin, UpdateView):
    model = TrapTransmitterOrderModel
    form_class = TrapTransmitterCreateForm
    template_name = 'trapTransmitterForm.html'
    formset_error = ''

    def get_context_data(self, **kwargs):
        context = super(CustomerTrapTransmitterUpdate, self).get_context_data(**kwargs)
        context['com_type_gl'] = self.object.globalstar
        context['com_type_ir'] = self.object.iridium
        return context

    def get_initial(self):
        initial = super(CustomerTrapTransmitterUpdate, self).get_initial()
        return initial

    def get_success_url(self, **kwargs):
        return reverse('trapTransmitter:trapTransmitter_delivery_form', kwargs={'hash': self.kwargs['hash'],
                                                'pk': self.kwargs['pk']})

    def form_valid(self, form):
        return super(CustomerTrapTransmitterUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CustomerTrapTransmitterUpdate, self).form_invalid(form)


def customer_deliver_address(request, hash, pk):
    return customer_deliver_address_function(request, hash, pk, TrapTransmitterOrderModel, 'trapTransmitter:thanks', TTPaymentOptionForm)


class ThanksView(ThanksForOderView):
    def __init__(self):
        super(ThanksView, self).__init__(TrapTransmitterOrderModel, 'trapTransmitter_thanks.html')


class VertexLitePDFView(PDFView):
    def __init__(self):
        super(VertexLitePDFView, self).__init__(TrapTransmitterOrderModel, 'trapTransmitterHtml4Pdf.html', 'order_from')