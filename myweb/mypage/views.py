from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import hashlib
from mypage.models import *

def index(request):
    return render(request, 'mypage/index.html')

def about(request):
    return render(request, 'mypage/about.html')

def home(request):
    return render(request, 'mypage/home.html')

def login(request):
    if request.method != "POST":
        return HttpResponse('Unsupported Method')
    username = request.POST.get("username")
    password = hashlib.sha256(request.POST.get("password").encode()).hexdigest()
    try:
        user = User.objects.get(username=username, password=password)
    except User.DoesNotExist:
        return HttpResponse('No such user')
    request.session['username'] = user.username
    return HttpResponse('<script>location.href=\'/mypage/admin\'</script>')

def submit(request):
    if request.method != "POST":
        return HttpResponse("Unsupported Metdho")
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    message = request.POST.get("message")
    c = Contact(name=name, email=email, phone=phone, message=message)
    c.save()
    if c.id:
        return HttpResponse("Success")
    else:
        return HttpResponse("Failed")

def admin(request):
    if not request.session.get('username'):
        return render(request, 'mypage/login.html')
    c = Contact.objects.all()
    return render(request, 'mypage/admin.html', {'contacts':c})
