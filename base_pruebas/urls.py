from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^home/$', views.base_prueba, name='base_prueba'),
]
