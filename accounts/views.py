from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from accounts.models import UserProfile
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
            info = "Username or Password is invalid"
            #print("Username or Password is invalid")
            return render(request, 'signIn.html',{"info":info})
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
                return render(request, 'register.html',{"info":info})
            elif User.objects.filter(email=email):
                info = "Email Already Used"

                print("Email Already Used")
                return render(request, 'register.html',{"info":info})
            else:
                user_data = User.objects.create_user(first_name=firstname, last_name=lastname, password=password,
                                                     email=email, username=username)
                user_data.save()
                return redirect("login")
        else:
            info="Password didn't match"
            return render(request, 'register.html',{"info":info})
    else:

        return render(request, 'register.html',{"messages":messages})



def logout(request):
    auth.logout(request)
    return redirect("/")


def profile(request):
    if request.method == "POST":
        try:
            image = request.FILES['image']
            #image = request.POST.get('image')#['image']
            print(image)
            if image:
                UserProfile.objects.create(user=User.objects.get(id=request.user.id), avatar=image)
                #user_image=UserProfile.objects.get(user_id=request.user.id)
        except Exception as e:
            print(e)

        return redirect("/accounts/profile")
    else:
        try:
            profile = UserProfile.objects.filter(user_id=request.user.id).order_by('-id')[:1]
            print(profile[0])
            return render(request,"profile.html",{"profile":profile[0]})
        except:
            return render(request, "profile.html")