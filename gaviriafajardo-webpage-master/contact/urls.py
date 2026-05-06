from django.urls import path

from .views import job_create, contact_create

app_name = "contact"

urlpatterns = [
    path("contact-create/", contact_create, name="contact-create"),
    path("job-create/", job_create, name="job-create"),
]
