from django.http import Http404
from orderForm.own_decorator import hash_is_allowed


class HashRequiredMixin(object):
    @hash_is_allowed
    def dispatch(self, *args, **kwargs):
        return super(HashRequiredMixin, self).dispatch(*args, **kwargs)


class ProveHashMixin(object):
    def get(self, request, *args, **kwargs):
        hash = kwargs['hash']
        pk = kwargs['pk']
        customer_staff = self.model.objects.get(pk=kwargs['pk']).customer_staff
        hash = hash[:len(pk) * -1]
        if customer_staff == hash[-2:] or hash[-2:] in 'CLD':
            return super(ProveHashMixin, self).get(request, *args, *kwargs)
        else:
            raise Http404