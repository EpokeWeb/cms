from django.conf.urls import url
from django.contrib import admin

from .views import (
	blogue_list,
	blogue_details,
	)

urlpatterns = [
	url(r'^$', blogue_list, name='liste'),
	url(r'^article$', blogue_details, name='details'),
]
