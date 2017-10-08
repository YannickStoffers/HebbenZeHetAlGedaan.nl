from django.conf.urls 	import url
from results 			import views

urlpatterns = [
	url (r'^$', views.default, name = 'default'),
	url (r'^(?P<name_1>[\w-]+)/(?P<name_2>[\w-]+$)$', views.results, name = 'results'),
	url (r'^post/(?P<name_1>[\w-]+)/(?P<name_2>[\w-]+$)$', views.thank_you_screen, name = 'thank_you_screen'),
]
