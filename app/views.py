from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topic.html',d)


def display_webpage(request):
     LOW=Webpage.objects.all()
     LOW=Webpage.objects.filter(topic_name='Cricket')
     LOW=Webpage.objects.exclude(topic_name='Cricket')
     d={'webpage':LOW}
     return render(request,'display_webpage.html',context=d)


def display_accessrecords(request):
    LOA=AccessRecords.objects.all()
    d={'accessrecords':LOA}
    return render(request,'display_accessrecords.html',d)