from django.shortcuts import render
from .models import Profile, Project, Skill

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()[:3]   # home’da 3 tasini ko‘rsatamiz
    skills = Skill.objects.all().order_by("-level")
    return render(request, "home.html", {
        "profile": profile,
        "projects": projects,
        "skills": skills
    })

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request, "projects.html", {"profile": profile, "projects": projects})

def about(request):
    profile = Profile.objects.first()
    return render(request, "about.html", {"profile": profile})

def contact(request):
    profile = Profile.objects.first()
    return render(request, "contact.html", {"profile": profile})