from django.conf.urls import url
from django.contrib import admin

from .views import (
	coaching_details,
	)

urlpatterns = [
	url(r'^$', coaching_details, name='details'),
]
