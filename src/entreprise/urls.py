from django.conf.urls import url
from django.contrib import admin

from .views import (
	entreprise_details,
	)

urlpatterns = [
	url(r'^$', entreprise_details, name='details'),
]
