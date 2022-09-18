# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from WSUCalz.forms import scraperForm
from WSUCalz.WSUSchedScraper import generalScraper

wsuHours =['0700','0800','0900','1000','1100','1200','1300','1400','1500','1600','1700','1800','1900','2000','2100','2200']
# Create your views here.

def home(response):
	return render(response, 'home.html', {})

def generalScrapeRoute(scrapeParams):
	return generalScraper(scrapeParams)

def classform(request):
	if request.method == 'POST':
		form = scraperForm(request.POST)
		if form.is_valid():
			campus_choice = form.cleaned_data.get("your_campus")
			classYear= form.cleaned_data.get("your_year")
			acadTerm = form.cleaned_data.get("your_term")
			subject = form.cleaned_data.get("your_subject")
			crn = form.cleaned_data.get("your_crn")
			letsFinallyScrape = generalScraper(campus_choice, classYear, acadTerm, subject, crn)
			secSchedList = letsFinallyScrape[0]
			secDayList = letsFinallyScrape[1]
			conUrl = letsFinallyScrape[2]
			context = {'form': form, 
			'campus_choice':campus_choice, 
			'classYear':classYear,
			'acadTerm':acadTerm,
			'subject':subject,
			'crn':crn, 
			'secSchedList': (secSchedList),
			'secDayList': (secDayList),
			'conUrl': str(conUrl),
			'letsFinallyScrape': letsFinallyScrape,
			'wsuHours': wsuHours,
			}
			return render(request, 'schedule.html', context)
	elif request.method == 'GET':
		form = scraperForm()
		return render(request, 'classform.html',{'form': form})


# def schedule(request):
# 	print('this is the schedule route')
# 	return render(request, 'schedule.html', {'form': form})