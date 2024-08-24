from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignUp, name="signup"),
    path("enter/", views.enter_profiles, name="enter"),
    path("login/", views.UserLogin, name="login"),
    path("logout/", views.UserLogout, name="logout"),
    path("account/", views.index, name="account"),
    path("profile/", views.enter_profiles, name="profile"),
    path("experiance/", views.enter_experiance, name="experiace"),
    path("education/", views.enter_education, name="education"),
    path("certification/", views.enter_certification, name="certification"),
    path("projects/", views.enter_project, name="projects")
]
