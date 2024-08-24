from django.shortcuts import render, redirect
from .models import CustomUser, UserProfile, Education, Certification, Experience, Project
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from .mail import send_mail
# Create your views here.


def SignUp(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        confirm_password  = request.POST["cpassword"]

        if CustomUser.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "user already taken"})
        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match.'})
        
        user = CustomUser(username = username, password = make_password(password))
        user.save()

        login(request,user)
        
        return redirect("profile")
    else:
        return render(request,"user/signup.html", {"error": "invalid username or pass"})
    
    return render(request, "user/signup.html")


def UserLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("hello")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            print(request.user)
            return redirect("account")
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'user/login.html')
    
    return render(request, 'user/login.html')

def UserLogout(request):
    logout(request)
    return redirect("login")

def index(request):
    print("heyy")
    user_id = request.user.id
    print("hello",user_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Fetch related data from other models
    edu = Education.objects.filter(user=request.user)
    cert = Certification.objects.filter(user=request.user)
    exper = Experience.objects.filter(user=request.user)
    proj = Project.objects.filter(user=request.user)

    # Create context dictionary to pass data to the template
    context = {
        "user": user_profile,
        "edu": edu,
        "cert": cert,
        "exper": exper,
        "proj": proj
    }

    #contact section

    if request.method == "POST":
        name = request.POST["name"]
        mail = request.POST["mail"]
        number = request.POST["number"]
        query = request.POST["query"]
        send_mail(name=name,mail=mail,msg=query,nmbr=number)
        print("mail sent successfull")



    return render(request,"user/account.html",context)

def enter_profiles(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        bio = request.POST["bio"]
        description = request.POST["description"]
        profile = request.FILES.get("image")

        #saving
        db = UserProfile(fullname=fullname,
                         bio=bio,
                         description=description,
                         profile=profile,
                         user=request.user
                        )
        
        db.save()
        print("data saved")

    return render(request, "user/profile.html")


def enter_experiance(request):
    if request.method == "POST":
        company_name = request.POST["company_name"]
        category = request.POST["category"]
        domain = request.POST["domain"]
        period = request.POST["period"]
        image = request.FILES.get("image")

        db = Experience(company_name=company_name,
                        category=category,
                        domain=domain,
                        period=period,
                        image=image,
                        user=request.user
                        )
        db.save()

    return render(request, "user/experiance.html")

def enter_education(request):
    if request.method == "POST":
        institute = request.POST["institute"]
        category = request.POST.get("category")
        course = request.POST["course"]
        city = request.POST.get("city")
        state = request.POST.get("state")
        image = request.FILES.get("image")
        
        db = Education(
            institute=institute,
            category=category,
            course=course,
            city=city,
            state=state,
            image=image,
            user=request.user
            )
        db.save()

    return render(request, "user/education.html")

def enter_certification(request):
    if request.method == "POST":
        domain = request.POST["domain"]
        category = request.POST["category"]
        center_name = request.POST["center"]
        duration = request.POST["duration"]
        image = request.FILES.get("image")

        db = Certification(
            domain=domain,
            category=category,
            center_name=center_name,
            duration=duration,
            image=image,
            user=request.user
        )

        db.save()
    
    return render(request,"user/certification.html")

def enter_project(request):
    if request.method == "POST":
        project_name = request.POST["project_name"]
        project_description = request.POST["project_description"]
        link = request.POST["link"]
        image = request.FILES.get("image")

        db = Project(project_name=project_name, 
                     project_description=project_description,
                     link=link,
                     image=image,
                     user=request.user
                     )
        
        db.save()

    return render(request, "user/projects.html")

