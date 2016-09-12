try:
    from urllib import quote_plus #python 2
except:
    pass

try:
    from urllib.parse import quote_plus #python 3
except: 
    pass
    from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

#from .forms import CommentForm
#from .models import Comment

def service_liste(request):
	context = {
	"title": "Services",
	"page_active": "Nos services numériques",
	}
	return render(request, "services/liste.html", context)


def service_audit_web(request):
	context = {
	"title": "Audit web",
	"page_active": "Nos services numériques",
	"lvl3": "oui",
	}
	return render(request, "services/audit_web.html", context)

def service_seo(request):
	context = {
	"title": "Services SEO",
	"page_active": "Nos services numériques",
	"lvl3": "oui",
	}
	return render(request, "services/seo.html", context)

def service_medias_sociaux(request):
	context = {
	"title": "Médias sociaux",
	"page_active": "Nos services numériques",
	"lvl3": "oui",
	}
	return render(request, "services/medias_sociaux.html", context)

def service_courriels(request):
	context = {
	"title": "Campagne courriels et de promotion",
	"page_active": "Nos services numériques",
	"lvl3": "oui",
	}
	return render(request, "services/courriels.html", context)

def service_developpement_web(request):
	context = {
	"title": "Développement web",
	"page_active": "Nos services numériques",
	"lvl3": "oui",
	}
	return render(request, "services/developpement_web.html", context)

def service_cms(request):
	context = {
	"title": "Plateforme de gestion de contenu",
	"page_active": "Nos services numériques",
	"lvl3": "oui",
	}
	return render(request, "services/cms.html", context)