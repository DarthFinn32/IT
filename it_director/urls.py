from django.urls import path

from it_director.views import *


urlpatterns = [
    path('', main, name='main'),
    path('relevance', relevance, name='relevance'),
    path('location', location, name='location'),
    path('job_abilities', job_abilities, name='job_abilities'),
    path('recent_jobs', recent_jobs, name='recent_jobs'),
]