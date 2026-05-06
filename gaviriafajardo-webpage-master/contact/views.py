from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import ContactForm, JobForm


@csrf_exempt
def contact_create(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return HttpResponseRedirect("/")


def job_create(request):
    if request.method == "POST":
        job_form = JobForm(request.POST, request.FILES)
        if job_form.is_valid():
            job_form.save()
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return HttpResponseRedirect("/")
