# howdy/urls.py

from django.urls import include, path
from api import views
from .views import api
from .models import Companies

urlpatterns = [
	path('', views.hello),
	#path('companies', views.api),
	path('companies/', views.api),
]
