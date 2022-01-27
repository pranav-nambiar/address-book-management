from django.urls import path
from .views import ContactAll, ContactOne

urlpatterns = [
    path('contactlist/', ContactAll.as_view()),
    path('modifycontact/<int:item_id>', ContactOne.as_view())
]
