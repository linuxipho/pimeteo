from django.conf.urls import url

from pimeteo import views

urlpatterns = [
    url(r'^historique', views.historique, name='historique'),
    url(r'^$', views.index, name='index'),
]