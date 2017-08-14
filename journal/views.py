from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student, Subject, Mark
from rest_framework import viewsets
from .serializers import StudentSerializer, SubjectSerializer, MarkSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marks to be viewed or edited.
    """
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

def home(request):
	context = {}
	if request.user.is_authenticated():
		return render(request,"journal/app.html",context)
	return redirect('sign_in')

def sign_in(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
        context = {
                "error" : True
            }   
    return render(request,"journal/login.html",context)