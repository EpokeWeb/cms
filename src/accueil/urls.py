from django.conf.urls import url
from django.contrib import admin

from .views import (
	accueil_details,
	)

urlpatterns = [
	url(r'^$', accueil_details, name='acceuil'),
]
