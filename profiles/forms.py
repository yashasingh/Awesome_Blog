from django import forms
from django.contrib.auth.models import User

class signup_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name',
				  'last_name',
				  'username',
				  'password',
				  'email']
