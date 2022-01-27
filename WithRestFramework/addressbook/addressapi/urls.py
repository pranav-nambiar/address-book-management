from django.urls import path, include
from rest_framework.routers import DefaultRouter
from addressapi import views

router = DefaultRouter()
router.register(r'addresses', views.AddressViewSet)

urlpatterns = [
    path('', include(router.urls))
]
