# api_app/decorators.py
from django.http import HttpResponseForbidden

def require_api_password(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # You can choose where to pass the password.
        # Here, we're looking for a custom HTTP header called 'X-API-PASSWORD'
        password = request.META.get('HTTP_AUTH_APPLICATION')
        # Replace 'mysecretpassword' with your desired password.
        if password != 'mysecretpassword':
            return HttpResponseForbidden("Forbidden: Incorrect Password")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
