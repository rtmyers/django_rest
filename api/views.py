from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework import serializers
from .serializers import CompaniesSerialiser
from .models import Companies


#def api(request):
#	return HttpResponse(Companies.objects.all())

def hello(request):
	text = """<h1>welcome to my app !</h1>"""
	return HttpResponse(text)

def api(request):
	print("req", request);
	queryset = Companies.objects.all()
	print("queryset", queryset)
	companies = Companies.objects.all().order_by('name')
	json = serializers.Serializer('json', companies)
	return HttpResponse(json)

# Create your views here.
#class CreateView(generics.ListCreateAPIView):
#	"""This class defines the create behavior of our rest api."""
#	queryset = Companies.objects.all()
#	serializer_class = CompaniesSerialiser
#
#	def perform_create(self, serializer):
#		"""Save the post data when creating a new Companies."""
#		serializer.save()
