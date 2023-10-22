from ninja import Router
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from pydantic import BaseModel
from datetime import datetime

router = Router()

@router.get("/home")
def home(request):
    return "ninja ninja"

class RegistrationModel(BaseModel):
    username: str
    email: str
    age: int
    password: str

#create new user profile
@router.post("/register")
def register_user(request, registration_data: RegistrationModel):
    user = User.objects.create_user(
        username=registration_data.username,
        email=registration_data.email,
        password=registration_data.password
    )
    user.profile.age = registration_data.age
    user.profile.registration_timestamp = datetime.now()
    user.profile.save()
    user.save()

    return{"message": "You did it!"}