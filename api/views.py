from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views import View
from .models import Company
import json
# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        #description,marca,serie,precio,cantidad,disponible
        if (id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) >0:
                company = companies[0]
                datos={
                    'message': 'Success',
                    'Product': company
                }
            else:
                datos={
                    'message': 'Product not found... '
                }
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies) > 0:
                datos={
                    'message': 'Success',
                    'Product': companies
                }
            else:
                datos={
                    'message': 'Product not found... '
                }
            return JsonResponse(datos)

    def post(sel,request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Company.objects.create(description=jd['description'],marca=jd['marca'],serie=jd['serie'],precio=jd['precio'],cantidad=jd['cantidad'],disponible=jd['disponible'])
            #description,marca,serie,precio,cantidad,disponible
        datos={'message': 'Success'}
        return JsonResponse(datos)

    def put(sel,request,id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) >0:
        #description,marca,serie,precio,cantidad,disponible
            company = Company.objects.get(id=id)
            company.description=jd['description']
            company.marca=jd['marca']
            company.serie=jd['serie']
            company.precio=jd['precio']
            company.cantidad=jd['cantidad']
            company.disponible=jd['disponible']
            company.save()
            datos = {'message':'Succes'}
        else :
            datos = {'message': 'Product not found... '}
        return JsonResponse(datos)

    def delete(sel,request,id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) >0:
            Company.objects.filter(id=id).delete()
            datos = {'message':'Succes'}
        else:
            datos = {'message': 'Product not found... '}
        return JsonResponse(datos)
