from django.conf.urls import url

from login import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^login_action/$', views.login_action)
]