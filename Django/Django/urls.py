from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('oauth_login')

urlpatterns = [
    path('', redirect_to_login, name='home'),
    path('', include('oauth.urls')),  # 这行让你可以直接访问 /login 和 /callback
]