from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
dict_ = {
		'name':"Vardges",
		"last_name":"Chandoyan",
		}


def home(request):
	content = {'name': dict_} # any way for dict
	return render(request,'admin_app/welcome.html',content)