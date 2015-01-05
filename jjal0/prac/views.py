# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from prac.models import Jjal
from prac.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Jjal(files = request.FILES['files'],jjal_text = request.POST["jjal_text"])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('prac.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    files = Jjal.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'prac/list.html',
        {'files': files, 'form': form},
        context_instance=RequestContext(request)
    )