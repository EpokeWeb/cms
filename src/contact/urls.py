from django.conf.urls import url
from django.contrib import admin

from .views import (
	contact_details,
	)

urlpatterns = [
	url(r'^$', contact_details, name='details'),
]
