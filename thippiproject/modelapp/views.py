from django.shortcuts import render
from modelapp.forms import ProjectForm
from modelapp.models import Project
# Create your views here.

def index(request):
    return render(request,'modelapp/index.html')

def listproject(request):
    projectlist = Project.objects.all()
    return render(request,'modelapp/listproject.html',{'project':projectlist})

def addproject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    print("nothing Saved")
    return render(request,'modelapp/addproject.html',{'form':form}) 