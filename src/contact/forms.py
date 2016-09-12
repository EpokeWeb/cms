from django import forms

class ContactForm(forms.Form):
	contact_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom'}), required=False)
	contact_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(123) 456-7890'}), required=False)
	contact_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'http://www.votresite.com'}), required=False)
	contact_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Adresse courriel'}))
	learn_seowave = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom'}), required=False) 
	interested_in = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom'}), required=False) 
	addInfos = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message','rows':'4'}))

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = ""
		self.fields['contact_phone'].label = ""
		self.fields['contact_url'].label = ""
		self.fields['contact_email'].label = ""
		self.fields['interested_in'].label = ""
		self.fields['addInfos'].label = ""
