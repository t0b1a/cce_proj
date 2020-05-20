from django.shortcuts import render
from .models import Job #da models.py importo Job

def home(request):
	jobs = Job.objects #chiamo jobs gli oggetti del db importati da Job
	return render(request, 'jobs/home.html', {'jobs':jobs}) #metto un dizionario