from django.urls import path, include
from rest_framework.routers import DefaultRouter
from addressapi import views

router = DefaultRouter()
router.register(r'addresses', views.AddressViewSet)

urlpatterns = [
    path('addresses/filter/', views.FilteredView.as_view()),
    path('', include(router.urls)),
]
