from django.conf.urls import url
from django.contrib import admin

from .views import (
	service_liste,
	service_audit_web,
	service_seo,
	service_medias_sociaux,
	service_courriels,
	service_developpement_web,
	service_cms
	)

urlpatterns = [
	url(r'^$', service_liste, name='liste'),
	url(r'audit-web/$', service_audit_web, name='audit_web'),
	url(r'seo/$', service_seo, name='seo'),
	url(r'medias-sociaux/$', service_medias_sociaux, name='medias_sociaux'),
	url(r'campagne-courriel/$', service_courriels, name='courriels'),
	url(r'developpement-web/$', service_developpement_web, name='developpement_web'),
	url(r'plateforme-gestion-de-contenu/$', service_cms, name='cms'),
]
