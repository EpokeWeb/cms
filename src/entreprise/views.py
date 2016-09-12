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

def entreprise_details(request):

	today = timezone.now().date()

	context = {
	"title": "Entreprise",
	"today": today,
	"page_active": "À propos",
	}
	return render(request, "entreprise/entreprise.html", context)


