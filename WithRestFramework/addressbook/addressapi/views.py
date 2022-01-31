from rest_framework import viewsets
from .models import Address
from .serializers import AddressSerializer
from rest_framework.generics import ListAPIView

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class FilteredView(ListAPIView):
    serializer_class = AddressSerializer
    def get_queryset(self):
        country = self.request.query_params.get('country')
        state = self.request.query_params.get('state')
        pincode = self.request.query_params.get('pincode')
        city = self.request.query_params.get('city')
        queryset = Address.objects.all()
        if country:
            queryset = queryset.filter(country=country)
        if state:
            queryset = queryset.filter(state=state)
        if city:
            queryset = queryset.filter(city=city)
        if pincode:
            queryset = queryset.filter(pincode=pincode)
        return queryset
