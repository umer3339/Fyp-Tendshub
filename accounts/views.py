from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        user_name = request.POST["username"]
        password = request.POST["password"]

        user_login = auth.authenticate(username=user_name, password=password)

        if user_login is not None:
            auth.login(request, user_login)
            return redirect("/")
        else:
            print("Username or Password is invalid")
            return redirect("login")
    else:
        return render(request, 'signIn.html')

    #return render(request,"signIn.html")

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']

        if password == confirmPassword:
            if User.objects.filter(username=username):

                info = "Username Already Taken"
                print("Username Already Taken")
                return render(request, 'register.html',{"messages":info})
            elif User.objects.filter(email=email):
                info = "Email Already Used"

                print("Email Already Used")
                return render(request, 'register.html',{"messages":info})
            else:
                user_data = User.objects.create_user(first_name=firstname, last_name=lastname, password=password,
                                                     email=email, username=username)
                user_data.save()
                return redirect("login")
        else:
            info="Confirmation password didnot matched"

            return render(request, 'register.html',{"messages":info})


    else:

        return render(request, 'register.html',{"messages":messages})



def logout(request):
    auth.logout(request)
    return redirect("/")