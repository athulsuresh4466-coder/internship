from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def page1(request):
    return HttpResponse("Hello world!")

def page2(request):
    return HttpResponse("Hello")

def page2(request):
    return render (request,'myfile.html')

def page3(request):
    return render (request,'loginpage.html')

def page4(request):
    return render (request,'index.html')

def page5(request):
    return render (request,'new.html')

from .models import Member,Member


def page6(request):
    members = Member.objects.all()
    return render(request, 'sql.html', {'members': members})









from .models import Service

def page5(request):
    servicesFeatures = Service.objects.all()   # get data from DB
    return render(request, 'new.html', {
        'services': servicesFeatures
    })








from .models import Service, HomeService

def page5(request):
    services = Service.objects.all()
    home_services = HomeService.objects.filter(is_active=True)

    return render(request, "new.html", {
        "services": services,
        "home_services": home_services,
    })












from .models import ContactMessage
def page5(request):
    services = Service.objects.all()
    home_services = HomeService.objects.filter(is_active=True)

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            service=request.POST.get("service"),
            message=request.POST.get("message"),
        )

    return render(request, "new.html", {
        "services": services,
        "home_services": home_services,
    })










from .forms import Inputforms

def home_views(request):
    if request.method == "POST":
        form = Inputforms(request.POST)
        if form.is_valid():
            form.save()   # ✅ SAVES TO SQLITE
            form = Inputforms()  # reset form
    else:
        form = Inputforms()

    return render(request, "home.html", {"form": form})







