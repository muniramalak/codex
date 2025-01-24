from django.shortcuts import redirect, render
from codex.forms import ContactForm
from codex.models import Contact
# Create your views here.
def home(request):
    return render(request,'home.html')
def client(request):
    return render(request,"client.html")
def solutions(request):
    return render(request,"solutions.html")
def surveysol(request):
    return render(request,"surveysol.html")
def services(request):
    return render(request,"services.html")
def aboutus(request):
    return render(request,"aboutus.html")
def contact(request):
    contactform=ContactForm(request.POST or None)
    if contactform.is_valid():
        contactform.save()
        return redirect("home")
    return render(request,"contact.html",{'forms':contactform})
