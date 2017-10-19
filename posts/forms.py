from django import forms
from .models import posts

class PostAdd_form(forms.ModelForm):
	class Meta:
		model = posts
		fields = ['post',
				  'title',
				  'sub_title',
				  'image']
		exclude = ['posted_by',
				   'posted_on']
