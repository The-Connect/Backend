# api.py in your app
from ninja import Router
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from ninja.security import HttpBearer

router = Router()
# security = HttpBearer()

@router.post("/register/")
# So the funny thing is that if you just do the username and password, it puts the password through as an email 
def register_user(request, username: str, email: str, password: str):
    # Check if a user with the same username or email already exists
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return {"detail": "User with this username or email already exists"}, 400

    # Create a new user
    user = User.objects.create_user(username, email, password)
    user.save()

    return {"message": "User registered successfully"}

@router.post("/login/")
def login_user(request, username: str, password: str):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return {"message": "Login successful"}
    else:
        return {"detail": "Invalid credentials"}, 400

