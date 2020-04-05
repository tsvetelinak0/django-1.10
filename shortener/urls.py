from django.urls import path, re_path

from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    re_path(r'^(?P<shortcode>[\w-]+)/$', views.URLRedirectView.as_view(), name='scode'),

]