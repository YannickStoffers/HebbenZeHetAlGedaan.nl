from django.http 		import HttpResponse
from django.shortcuts 	import render

def index (request):
	return render (request, 'index/index.html')

def thank_you_screen (request, name1, name2):
	return render (request, 'index')
