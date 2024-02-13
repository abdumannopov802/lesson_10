from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home'),
    path('portfolio/', portfolioView, name='portfolio'),
    path('about/', aboutView, name='about'),
    path('service/', myserviceView, name='service'),
    path('resume/', resumeView, name='resume'),
    path('blog/', blogView, name='blog'),
    path('contact/', contactView, name='contact'),
]