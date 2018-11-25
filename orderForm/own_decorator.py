from django.shortcuts import get_object_or_404
from security.models import LinkHash


def hash_is_allowed(function):
    def wrap(request, *args, **kwargs):
        hash = get_object_or_404(LinkHash, hash=kwargs['hash'])
        if hash:
            return function(request, *args, **kwargs)
        else:
            raise 404
    # wrap.__doc__ = function.__doc__
    # wrap.__name__ = function.__name__
    return wrap