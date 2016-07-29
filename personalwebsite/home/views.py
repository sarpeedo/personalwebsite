from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

def resume(request):
    return render_to_response('home/resume.html', context_instance=RequestContext(request))

def projects(request):
    return render_to_response('home/projects.html', context_instance=RequestContext(request))

def biography(request):
    return render_to_response('home/biography.html', context_instance=RequestContext(request))

def contact(request):
    return render_to_response('home/contact.html', context_instance=RequestContext(request))
