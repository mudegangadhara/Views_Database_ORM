from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input("Enter the Topic:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Insert_Topic')




def insert_webpages(request):
    tn=input("Enter the topic_name:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input("Enter the name:")
    u=input("Enter the url:")
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    WO1=Webpage.objects.get_or_create(topic_name= TO,name=n,url=u)[0]
    WO1.save()

    return HttpResponse("this is webpage insretion")



def insert_accessmode(request):
    tn=input("Enter the Topic_name:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    na=input("Enter the name:")
    ur=input("Enter the url:")

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    d=input("enter the date:")
    au=input("Enter the author:")
    AM=Accessmode.objects.get_or_create(name=WO,date=d,author=au)[0]
    AM.save()

    return HttpResponse("THIS IS a access mode page")


