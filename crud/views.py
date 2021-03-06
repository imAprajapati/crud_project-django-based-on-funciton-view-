from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'crud/addshow.html',{'form':fm,'st':stud})


def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'crud/update.html',{'form':fm,'sti':pi})


def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')