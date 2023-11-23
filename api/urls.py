from django.contrib import admin
from django.urls import path,include
from api.views import InvoiceViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'invocies', InvoiceViewSet)


urlpatterns = [

    path('',include(router.urls))
   
]
