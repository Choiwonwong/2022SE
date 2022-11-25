from django.urls import include
from django.urls import path
# from django.contrib import admin

urlpatterns = [
    path('MrDae/', include('MrDae.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]