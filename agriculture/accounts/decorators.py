from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                # grabbing the first element
                group = request.user.groups.all()[0].name

            if group == 'admin':
                return view_func(request, *args, **kwargs)
            if group == 'customers':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    'You Are Not Authorized To Access to this Page')

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customers':
            return redirect('dashboard:login')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
