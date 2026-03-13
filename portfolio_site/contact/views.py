# contact/views.py
from django.shortcuts import render
from contact.models import Message  # For contact form

def home_view(request):
    return render(request, "index.html")

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Message.objects.create(name=name, email=email, message=message)
        return render(request, "contact_success.html")  # you can create a success page
    return render(request, "contact.html")