
#import necessary libaries

from rest_framework import generics
from django.db.models import Q
from .models import Whiskybase
from .serializers import WhiskybaseSerializer
from django.shortcuts import render
from django.http import JsonResponse

class WhiskybaseList(generics.ListAPIView):
    serializer_class = WhiskybaseSerializer

    def get_queryset(self):
        queryset = Whiskybase.objects.all()

         # get query params

        size = self.request.query_params.get('size', None)
        distillery  = self.request.query_params.get('distillery', None)
        bottler  = self.request.query_params.get('bottler', None)
        strength  = self.request.query_params.get('strength', None)
        vintage  = self.request.query_params.get('vintage', None)
        stated_age  = self.request.query_params.get('stated_age', None)
        bottled  = self.request.query_params.get('bottled', None)
        bottling_serie  = self.request.query_params.get('bottling_serie', None)
        casktype  = self.request.query_params.get('casktype', None)
        Title  = self.request.query_params.get('Title', None)

        # filter queryset

        if size:
            queryset = queryset.filter(size=size)
        
        if distillery:
            queryset = queryset.filter(distillery=distillery)

        if bottler:
            queryset = queryset.filter(bottler=bottler)

        if strength:
            queryset = queryset.filter(strength=strength)

        if vintage:
            queryset = queryset.filter(vintage=vintage)
        
        if stated_age:
            queryset = queryset.filter(stated_age=stated_age)
        
        if bottled:
            queryset = queryset.filter(bottled=bottled)

        if bottling_serie:
            queryset = queryset.filter(bottling_serie=bottling_serie)

        if casktype:
            queryset = queryset.filter(casktype=casktype)
        
        if Title:
            queryset = queryset.filter(Q(Title__icontains=Title))

        return queryset

# functions to get unique values for filters
def get_unique_bottlers(request):
    bottlers = Whiskybase.objects.values_list('bottler', flat=True).distinct()
    return JsonResponse({'bottlers': list(bottlers)})

def get_unique_distillery(request):
    distillery = Whiskybase.objects.values_list('distillery', flat=True).distinct()
    return JsonResponse({'distillery': [distillery.split(" (")[0] for distillery  in distillery]})


def get_unique_strength(request):
    strength = Whiskybase.objects.values_list('strength', flat=True).distinct()
    return JsonResponse({'strength': [strength.split(" (")[0] for strength in strength]})

def get_unique_vintage(request):
    vintage = Whiskybase.objects.values_list('vintage', flat=True).distinct()
    return JsonResponse({'vintage': [vintage.split(" (")[0] for vintage in vintage]})

def get_unique_size(request):
    size = Whiskybase.objects.values_list('size', flat=True).distinct()
    return JsonResponse({'size': [size.split(" (")[0] for size in size]})

def get_unique_stated_age(request):
    stated_age = Whiskybase.objects.values_list('stated_age', flat=True).distinct()
    return JsonResponse({'stated_age': [stated_age.split(" (")[0] for stated_age in stated_age]})

def get_unique_casktype(request):
    casktype = Whiskybase.objects.values_list('casktype', flat=True).distinct()
    return JsonResponse({'casktype': [casktype.split(" (")[0] for casktype in casktype]})

def get_unique_bottled(request):
    bottled = Whiskybase.objects.values_list('bottled', flat=True).distinct()
    return JsonResponse({'bottled': [bottled.split(" (")[0] for bottled in bottled]})

def get_unique_bottle_sere(request):
    bottling_serie = Whiskybase.objects.values_list('bottling_serie', flat=True).distinct()
    return JsonResponse({'bottling_serie': [bottling_serie.split(" (")[0] for bottling_serie in bottling_serie]})