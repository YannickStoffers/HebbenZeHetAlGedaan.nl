from django.http 		import HttpResponse
from django.shortcuts 	import render
from .models 			import Entry

def default (request):
	return render (request, 'results/results.html', {'results': Entry (name1 = 'Yannick Stoffers', name2 = 'Yannick Stoffers', count = 0)})

def results (request, name_1, name_2):
	print (name_1, name_2)
	result = Entry (count = 0)
	results = Entry.objects.filter (name1 = name_1, name2 = name_2)
	results = results | Entry.objects.filter (name1 = name_2, name2 = name_1)
	if (results):
		result = results[0]
	result.name1 = result.name1.replace ('-', ' ')
	result.name2 = result.name2.replace ('-', ' ')
	return render (request, 'results/results.html', {'results': result})

def thank_you_screen (request, name_1, name_2):
	entry = Entry (count = 0)
	entries = Entry.objects.filter (name1 = name_1, name2 = name_2)
	entries = entries | Entry.objects.filter (name1 = name_2, name2 = name_1)
	if entries:
		entry = entries[0]
		entry.count += 1
	else:
		entry = Entry (name1 = name_1, name2 = name_2, count = 1)
	entry.save ()
	return render (request, 'results/thank_you_screen.html')
