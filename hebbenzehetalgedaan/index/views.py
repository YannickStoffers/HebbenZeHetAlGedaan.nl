from django.http import HttpResponse
import datetime
from django.shortcuts import render
from .models import Entry

def index (request):
	result = Entry (count = 0)
	results = Entry.objects.filter (name1 = 'name1', name2 = 'name2')
	if (results):
		result = results[0]
	return render (request, 'index/results.html', {'results': result})
