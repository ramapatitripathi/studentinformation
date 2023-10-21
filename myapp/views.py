from django.shortcuts import render,redirect
from . models import Student
# Create your views here.
def index(request):
    msg=''
    if request.method=='POST':
        stname=request.POST['stname']
        stroll=request.POST['stroll']
        stbranch=request.POST['stbranch']
        styear=request.POST['styear']
        stadress=request.POST['staddress']
        st=Student(stname=stname,stroll=stroll,stbranch=stbranch,styear=styear,staddress=stadress)
        st.save()
        msg='student information registered'
    stinfo=Student.objects.all()    
    return render(request,"index.html",{'msg':msg,'stinfo':stinfo})

def deletestu(request,stroll):
    stu=Student.objects.get(stroll=stroll)
    stu.delete()
    return redirect('index') 
def updatestu(request,stroll):
    stu=Student.objects.get(stroll=stroll)
    return render(request,"updatestu.html",{'stu':stu})
def update(request):
    stname=request.POST['stname']
    stroll=request.POST['stroll']
    stbranch=request.POST['stbranch']
    styear=request.POST['styear']
    staddress=request.POST['staddress']
    Student.objects.filter(stroll=stroll).update(stname=stname,stbranch=stbranch,styear=styear,staddress=staddress)
    return redirect('index')

