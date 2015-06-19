from django.views.generic.base import View
from django.shortcuts import render, redirect
from app.forms import PersonaForm
from app.models import Persona
from django.core.urlresolvers import reverse

def home(request):
	return render(request, 'index.html')

class NuevaPersona(View):
	template_name = "nuevo_registro.html"
	def get(self, request):
		form = PersonaForm()
		return render(request, self.template_name, locals())

	def post(self, request):
		datos = request.POST
		form = PersonaForm(datos)
		if form.is_valid():
			form.save()
			return redirect(reverse('personas'))
		else:
			return render(request, template_name, locals())


def consultar_personas(request):
	personas = Persona.objects.all()
	return render(request, 'personas.html', locals())
