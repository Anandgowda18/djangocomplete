from django import forms
from django.db import models
from django.db.models import fields
from modelapp.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'