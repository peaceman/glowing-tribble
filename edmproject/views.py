from django.shortcuts import render
from django.views.generic import CreateView
from edmproject.models import ProjectFile


class ProjectFileCreate(CreateView):
    model = ProjectFile
