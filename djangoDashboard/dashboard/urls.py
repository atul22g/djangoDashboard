from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("contact", views.contact, name="contact"),
]
