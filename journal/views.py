from django.shortcuts import render
from django.contrib.auth import authenticate, login


def home(request):
	context = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
	if request.user.is_authenticated():
		return render(request,"journal/app.html",context)
	return render(request,"journal/login.html",context)

