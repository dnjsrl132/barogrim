from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from commentapp.models import Comments

def comment_ownership_required(func):
    def decorated(request,*args, **kwargs):
        comment=Comments.objects.get(pk=kwargs['pk'])
        if not comment.writer==request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated

