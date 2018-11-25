import datetime
import re
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import UpdateView
from orderForm.own_decorator import hash_is_allowed
from orderForm.own_mixins import HashRequiredMixin
from extras.views import PDFView
from extras.views import ThanksForOderView
from extras.views import customer_deliver_address_function
from orderForm.own_mixins import ProveHashMixin
from .forms import SurveyCreateForm, ArticleForm, BaseArticleForm, PaymentOptionForm
from .models import SurveyOrderModel


@hash_is_allowed
def surveyForm(request, hash):
    pk = re.sub(r'[^0-9]', '', hash[13:])
    return redirect(reverse('survey:survey_customer_form',
                                kwargs={'hash': hash,
                                        'pk': pk}
                                ))


class CustomerSurveyUpdate(HashRequiredMixin, ProveHashMixin, UpdateView):
    model = SurveyOrderModel
    form_class = SurveyCreateForm
    template_name = 'surveyForm.html'
    formset_error = ''

    def get_context_data(self, **kwargs):
        context = super(CustomerSurveyUpdate, self).get_context_data(**kwargs)
        ArticleFormSet = formset_factory(ArticleForm, extra=4)
        initial = []
        if self.object.battery_size:
            for i in range(0, len(self.object.battery_size.split('$')) - 1):
                initial.append({'battery_size': self.object.battery_size.split('$')[i],
                                'number_of_collars': self.object.number_of_collars.split('$')[i],
                                'nom_collar_circumference': self.object.nom_collar_circumference.split('$')[i], })
        context['com_type_gl'] = self.object.globalstar
        context['com_type_ir'] = self.object.iridium
        context['formset'] = ArticleFormSet(initial=initial)
        context['formset_error'] = self.formset_error
        return context

    def get_initial(self):
        initial = super(CustomerSurveyUpdate, self).get_initial()
        return initial

    def get_success_url(self, **kwargs):
        return reverse('survey:survey_delivery_form', kwargs={'hash': self.kwargs['hash'],
                                                'pk': self.kwargs['pk']})

    def form_valid(self, form):
        article_form_set = formset_factory(ArticleForm, min_num=1, validate_min=True, formset=BaseArticleForm)
        data = {
            'form-TOTAL_FORMS': '4',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '0',
            'form-0-battery_size': self.request.POST['form-0-battery_size'],
            'form-0-number_of_collars': self.request.POST['form-0-number_of_collars'],
            'form-0-nom_collar_circumference': self.request.POST['form-0-nom_collar_circumference'],
            'form-1-battery_size': self.request.POST['form-1-battery_size'],
            'form-1-number_of_collars': self.request.POST['form-1-number_of_collars'],
            'form-1-nom_collar_circumference': self.request.POST['form-1-nom_collar_circumference'],
            'form-2-battery_size': self.request.POST['form-2-battery_size'],
            'form-2-number_of_collars': self.request.POST['form-2-number_of_collars'],
            'form-2-nom_collar_circumference': self.request.POST['form-2-nom_collar_circumference'],
            'form-3-battery_size': self.request.POST['form-3-battery_size'],
            'form-3-number_of_collars': self.request.POST['form-3-number_of_collars'],
            'form-3-nom_collar_circumference': self.request.POST['form-3-nom_collar_circumference'],
        }
        formset = article_form_set(data)
        batterie_sizes_string = ''
        num_collars_string = ''
        circumference_string = ''
        if formset.is_valid():
            for f in formset.cleaned_data:
                    if len(f) > 1 is not None:
                        batterie_sizes_string += f['battery_size'] + '$'
                        num_collars_string += str(f['number_of_collars']) + '$'
                        circumference_string += f['nom_collar_circumference'] + '$'
        else:
            self.formset_error = 'error'
            return super(CustomerSurveyUpdate, self).form_invalid(form)
        instance = form.save(commit=False)
        instance.number_of_collars = num_collars_string
        instance.battery_size = batterie_sizes_string
        instance.nom_collar_circumference = circumference_string
        instance.save()
        return super(CustomerSurveyUpdate, self).form_valid(form)


def customer_deliver_address(request, hash, pk):
    return customer_deliver_address_function(request, hash, pk, SurveyOrderModel, 'survey:thanks', PaymentOptionForm)


class ThanksView(ThanksForOderView):
    def __init__(self):
        super(ThanksView, self).__init__(SurveyOrderModel)


class SurveyPDFView(PDFView):
    def __init__(self):
        super(SurveyPDFView, self).__init__(SurveyOrderModel, 'surveyHtml4Pdf.html', 'order_from')

