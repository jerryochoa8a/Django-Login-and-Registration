from django.shortcuts import render, redirect 
from login_app.models import User
from django.contrib import messages
#from twilio.rest import TwilioRestClient #this is for text
import bcrypt

# Create your views here.

def index(request):
    return render(request, "login_page.html")

def new_user(request):# creating a user
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')               #checks if there any errors if not then it will create a new user
    else:
        password =request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()          
        User.objects.create(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'], 
            email=request.POST['email'], 
            password= pw_hash ) 
    return redirect('/')# going back to the home page

 
##############  LOGIN CHECK   #######################
def user_login(request):
    user = User.objects.filter(email=request.POST['login_email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['login_pw'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id  #this is going to the "success" function
            return redirect(f'/success')
    else:
        messages.error(request, "Wrong email or password")
    return redirect('/')
################################################

def success(request):
    if request.session['userid']:  #this is from the "user_login" function
        messages.error(request, "Successfully registered (or logged in)!") 
        return render(request, 'success.html',
        {"user": User.objects.get(id=request.session['userid'])})
    else:
        return redirect('/')


######### logout ################

def logout(request):
    request.session['userid'] = None # we are taking the user out of the session
    #client.sendMessage()
    messages.error(request, "You have successfully logged out")
    return redirect('/')
 


