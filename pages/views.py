from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>")

	#O caminho para o arquivo html está setado no arquivo settings (Templates -> DIR)
	return render(request, "home.html", {})



def about_view(request, *args, **kwargs):
	my_context = {
		"my_text" : "Learning to use context",
		"my_age" : 28,
		"my_list" : ["Brazil", "Russia", "France", "USA", "Canada"]

	}
	return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})
