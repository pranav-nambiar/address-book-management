from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Contact
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class ContactAll(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        p_name = data.get('name')
        p_phone = data.get('phone_number')
        p_hn = data.get('house_number')
        p_a1 = data.get('address_line_1')
        p_a2 = data.get('address_line_2')
        p_c = data.get('city')
        p_s = data.get('state')
        p_cnt = data.get('country')

        contact = {
            'name': p_name,
            'phone_number': p_phone,
            'house_number': p_hn,
            'address_line_1': p_a1,
            'address_line_2': p_a2 or '',
            'city': p_c,
            'state': p_s,
            'country': p_cnt,
        }

        new_contact = Contact.objects.create(**contact)

        data = {
            'message': f'New contact added to address book with id: {new_contact.id}'
        }
        return JsonResponse(data, status=201)


    def get(self, request):
        contact_count = Contact.objects.count()
        contacts = Contact.objects.all()

        contactlist = []
        for contact in contacts:
            attributes = contact.__dict__
            attributecopy = attributes.copy()
            attributecopy.pop('_state')
            contactlist.append(attributecopy)

        data = {
            'contacts': contactlist,
            'count': contact_count
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ContactOne(View):
    def patch(self, request, item_id):
        data = json.loads(request.body.decode('utf-8'))
        contact = Contact.objects.get(pk=item_id)
        keylist = data.keys()
        for key in keylist:
            setattr(contact, key, data.get(key))
        contact.save()

        results = {
            'result': f'Contact {item_id} has been updated'
        }

        return JsonResponse(results, status=200)

    def get(self, request, item_id):
        contact = Contact.objects.get(pk=item_id)
        attributes = contact.__dict__
        attributecopy = attributes.copy()
        attributecopy.pop('_state')
        
        return JsonResponse({'result': attributecopy})

    def delete(self, request, item_id):
        contact = Contact.objects.get(id=item_id)
        contact.delete()

        data = {
            'message': f'Item {item_id} has been deleted' 
        }

        return JsonResponse(data)

