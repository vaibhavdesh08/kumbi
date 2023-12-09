from django.shortcuts import render
from .models import UserProfile

# Create your views here.

def home(request):
    return render(request,'home.html')

# def register(request):
#     return render(request,'register.html')

def login(request):
    return render(request,'login.html')

# views.py

# from django.shortcuts import render
from .utils import send_verification_email, generate_verification_code

def register(request):
    if request.method == 'POST':
        # Process signup form data
        fullname = request.POST['fullname']
        email    = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']

        # Send verification email to the user

        user_email = request.GET['email']  # User's email address
        verification_code = generate_verification_code()
        send_verification_email(user_email, verification_code)
        # Rest of the signup process
        # ...

    return render(request, 'register.html')


# def profile(request):
#     user = request.user

#     context = {
#         "user": user,
#     }

#     return render(request, "profile.html", context)