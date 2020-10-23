from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . import models
#from HomeApp.forms import Houses
from django.http import JsonResponse
def index(request):
    responsedata=models.usernames()
    responsedata= [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
    responsedata.save()
    return JsonResponse(responsedata)
class Homes1(ListView):
    context_object_name = 'details1'
    model=models.usernames
    template_name='home.html'
class Details(DetailView):
    context_object_name = 'details2'
    model=models.usernames
    template_name='details.html'
