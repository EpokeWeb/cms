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
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
#from .forms import CommentForm
#from .models import Comment

def contact_details(request):
	today = timezone.now().date()
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_name = form.cleaned_data.get("contact_name")
		form_phone = form.cleaned_data.get("contact_phone")
		form_url = form.cleaned_data.get("contact_url")
		form_email = form.cleaned_data.get("contact_email")
		form_talk = form.cleaned_data.get("learn_seowave")
		form_interest = form.cleaned_data.get("interested_in")
		form_message = form.cleaned_data.get("addInfos")
		#print (form_name, form_phone, form_url, form_email, form_talk, form_interest, form_message)
		subject = 'Message client - Site'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "Nom: %s, Téléphone: %s, Site Web: %s, Adresse courriel: %s, Entendu parlé de: %s, Intéressé par: %s, Message: %s"%( 
				form_name, 
				form_phone, 
				form_url,
				form_email,
				form_talk,
				form_interest,
				form_message)
		 # some_html_message = """
		 # <h1>hello</h1>
		 # """

		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				# html_message=some_html_message,
				fail_silently=True)

	context = {
	#"form": form,
	"title": "Contact",
	"today": today,
	"page_active": "Nous contacter",
	}
	return render(request, "contact/details.html", context)
