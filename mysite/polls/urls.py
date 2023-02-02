from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('raw', views.RawSQL.as_view())
]