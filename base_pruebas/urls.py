from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.base_prueba, name='base_prueba'),
]
