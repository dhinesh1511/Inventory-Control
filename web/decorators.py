from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import redirect

def unauth(view_det):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_det(request, *args, **kwargs)
    return wrapper_fun

def allowed_usrs(allowed_roles = []):
    def decorators(view_det):
        def wrapper_fun(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_det(request, *args, **kwargs)
            else:
                return HttpResponse('You are not Authorized to access this Page')
        return wrapper_fun
    return decorators

def admin_only(view_det):
    def wrapper_fun(request, *args, **kwargs):
        grp = None
        if request.user.groups.exists():
            grp = request.user.groups.all()[0].name
        
        if grp == 'customer':
            return redirect('userpage')
        elif grp == 'admin':
            return view_det(request, *args, **kwargs)
        else:
            return HttpResponse('You are not Authorized to access this Page ')
    return wrapper_fun