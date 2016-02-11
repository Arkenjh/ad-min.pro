from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

def h(request, template_name="index.html"):
	"""
	A index view.
	"""
	return render_to_response(template_name,context_instance=RequestContext(request))

def index(request):
	return render(request, 'index.html', dict())  