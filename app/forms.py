from app.models import Persona
from django import forms

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona