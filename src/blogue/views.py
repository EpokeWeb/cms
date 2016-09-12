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

def blogue_list(request):
	today = timezone.now().date()

	context = {
	"title": "Blogue",
	"today": today,
	"page_active": "Nos articles",
	}
	return render(request, "blogue/liste.html", context)

def blogue_details(request):
	today = timezone.now().date()

	context = {
	"title": "Titre de l'article",
	"today": today,
	"page_active": "Titre de l'article",
	}
	return render(request, "blogue/article.html", context)
