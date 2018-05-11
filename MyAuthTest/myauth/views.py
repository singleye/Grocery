import logging

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

from myauth.models import MyUser

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        login_status='Logged in'
    else:
        login_status='Logged out'
    return render(request, 'page.html', {'login_status':login_status})

def register(request):
    logger.info("register is called")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = MyUser.objects.get(username=username)
            return HttpResponse("User [%s] already exists!" % username)
        except MyUser.DoesNotExist:
            user = MyUser(username=username)
            user.username = username
            user.set_password(password)
            user.save()
            return HttpResponse("User [%s] is created!" % username)

    return HttpResponse('Registration failed!')

def login(request):
    logger.info("login is called")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            logger.info("User [%s] login successfully!" % username)
            auth.login(request, user)
            request.session.set_expiry(600)
            return HttpResponse('Login succeeded')
    return HttpResponse('Login failed')

def logout(request):
    logger.info("logout is called")
    auth.logout(request)
    return HttpResponse('Logout')

def authenticate(request):
    logger.info("authenticate is called")
    #token
    #check seesion against the token
    #backend.authenticate
    #user, token --> session  (login)
    return HttpResponse('')
