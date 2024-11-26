from django.urls import path
from .views import *
urlpatterns = [
    path("", CarListAPIView.as_view(), name="car-list"),
    path("car/create", CarCreateAPIView.as_view(), name="car-create"),
    path("company/list", CompanyListAPIView.as_view(), name="company-list"),
    path("company/create", CompanyCreateAPIView.as_view(), name="company-crearte"),

]
