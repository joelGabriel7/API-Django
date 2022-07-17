from django.urls import path

from countries import views

urlpatterns = [

    path('api/countries', views.countries_list),
    path('api/countries/<pk>', views.countries_detail),
]
