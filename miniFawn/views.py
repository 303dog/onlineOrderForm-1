from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from orderForm.own_decorator import hash_is_allowed
from extras.views import customer_deliver_address_function, ThanksForOderView, PDFView
from miniFawn.models import MiniFawnOrderModel
from orderForm.own_mixins import HashRequiredMixin
from miniFawn.forms import MFPaymentOptionForm
from miniFawn.forms import MFArticleForm
from miniFawn.forms import MFBaseArticleForm
from miniFawn.forms import MiniFawnCreateForm
from collar.models import Staff
from orderForm.own_mixins import ProveHashMixin


@hash_is_allowed
def miniFawnForm(request, hash):
    return redirect(reverse('miniFawn:miniFawn_customer_form',
                                kwargs={'hash': hash,
                                        'pk': hash[14:]}
                                ))


class CustomerMiniFawmUpdate(HashRequiredMixin, ProveHashMixin, UpdateView):
    model = MiniFawnOrderModel
    form_class = MiniFawnCreateForm
    template_name = 'minFawnForm.html'
    formset_error = ''

    def get_context_data(self, **kwargs):
        context = super(CustomerMiniFawmUpdate, self).get_context_data(**kwargs)
        ArticleFormSet = formset_factory(MFArticleForm, extra=4)
        initial = []
        if self.object.min_belt_circumference:
            for i in range(0, len(self.object.min_belt_circumference.split('$')) - 1):
                initial.append({'number_of_collars': self.object.number_of_collars.split('$')[i],
                                'min_belt_circumference': self.object.min_belt_circumference.split('$')[i],
                                'max_belt_circumference': self.object.max_belt_circumference.split('$')[i], })
        context['com_type_gl'] = self.object.globalstar
        context['com_type_ir'] = self.object.iridium
        context['formset'] = ArticleFormSet(initial=initial)
        context['formset_error'] = self.formset_error
        return context

    def get_initial(self):
        initial = super(CustomerMiniFawmUpdate, self).get_initial()
        return initial

    def get_success_url(self, **kwargs):
        return reverse('miniFawn:miniFawn_delivery_form', kwargs={'hash': self.kwargs['hash'],
                                                'pk': self.kwargs['pk']})

    def form_valid(self, form):
        article_form_set = formset_factory(MFArticleForm, min_num=1, validate_min=True, formset=MFBaseArticleForm)
        data = {
            'form-TOTAL_FORMS': '4',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '0',
            'form-0-number_of_collars': self.request.POST['form-0-number_of_collars'],
            'form-0-min_belt_circumference': self.request.POST['form-0-min_belt_circumference'],
            'form-0-max_belt_circumference': self.request.POST['form-0-max_belt_circumference'],
            'form-1-number_of_collars': self.request.POST['form-1-number_of_collars'],
            'form-1-min_belt_circumference': self.request.POST['form-1-min_belt_circumference'],
            'form-1-max_belt_circumference': self.request.POST['form-1-max_belt_circumference'],
            'form-2-number_of_collars': self.request.POST['form-2-number_of_collars'],
            'form-2-min_belt_circumference': self.request.POST['form-2-min_belt_circumference'],
            'form-2-max_belt_circumference': self.request.POST['form-2-max_belt_circumference'],
            'form-3-number_of_collars': self.request.POST['form-3-number_of_collars'],
            'form-3-min_belt_circumference': self.request.POST['form-3-min_belt_circumference'],
            'form-3-max_belt_circumference': self.request.POST['form-3-max_belt_circumference'],
        }
        formset = article_form_set(data)
        num_collars_string = ''
        min_collar_circumference = ''
        max_collar_circumference = ''
        print(formset.errors)
        print(formset.is_valid())
        if formset.is_valid():
            for f in formset.cleaned_data:
                    if len(f) > 1 is not None:
                        min_collar_circumference += f['min_belt_circumference'] + '$'
                        max_collar_circumference += f['max_belt_circumference'] + '$'
                        num_collars_string += str(f['number_of_collars']) + '$'
        else:
            self.formset_error = 'error'
            return super(CustomerMiniFawmUpdate, self).form_invalid(form)
        instance = form.save(commit=False)
        instance.number_of_collars = num_collars_string
        instance.min_belt_circumference = min_collar_circumference
        instance.max_belt_circumference = max_collar_circumference
        instance.save()
        return super(CustomerMiniFawmUpdate, self).form_valid(form)

    def form_invalid(self, form):
        return super(CustomerMiniFawmUpdate, self).form_invalid(form)


def customer_deliver_address(request, hash, pk):
    return customer_deliver_address_function(request, hash, pk, MiniFawnOrderModel, 'miniFawn:thanks', MFPaymentOptionForm)


class ThanksView(ThanksForOderView):
    def __init__(self):
        super(ThanksView, self).__init__(MiniFawnOrderModel, 'minifawn_thanks.html')


class VertexLitePDFView(PDFView):
    def __init__(self):
        super(VertexLitePDFView, self).__init__(MiniFawnOrderModel, 'miniFawnHtml4Pdf.html', 'order_from')