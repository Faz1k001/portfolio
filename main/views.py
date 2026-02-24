from django.shortcuts import render
from .models import Profile, Project, Skill

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all().order_by("-level")
    return render(request, "home.html", {   # ✅ shu yer o'zgardi
        "profile": profile,
        "projects": projects,
        "skills": skills
    })