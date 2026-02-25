from django.shortcuts import render, get_object_or_404
from .models import Profile, Project, Skill

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()[:3]
    skills = Skill.objects.all().order_by("-level")[:6]
    return render(request, "home.html", {"profile": profile, "projects": projects, "skills": skills})

def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by("-level")
    return render(request, "about.html", {"profile": profile, "skills": skills})

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request, "projects.html", {"profile": profile, "projects": projects})

def project_detail(request, pk):
    profile = Profile.objects.first()
    project = get_object_or_404(Project, pk=pk)
    return render(request, "project_detail.html", {"profile": profile, "project": project})

def contact(request):
    profile = Profile.objects.first()
    return render(request, "contact.html", {"profile": profile})