from django.urls import path
from .views import (
    WhiskybaseList,
    get_unique_bottlers,
    get_unique_distillery,
    get_unique_strength,
    get_unique_vintage,
    get_unique_size,
    get_unique_stated_age,
    get_unique_casktype,
    get_unique_bottled,
    get_unique_bottle_sere
)

urlpatterns = [
    #url to filter  table 
    path('whiskybase/', WhiskybaseList.as_view(), name='whiskybase-list'),  
    # url to get the unique value
    path('getbottler/', get_unique_bottlers, name='get_unique_bottlers'),
    path('getdistillery/', get_unique_distillery, name='get_unique_distillery'),
    path('getabv/', get_unique_strength, name='get_unique_strength'),
    path('getvintage/', get_unique_vintage, name='get_unique_vintage'),
    path('getsize/', get_unique_size, name='get_unique_size'),
    path('getage/', get_unique_stated_age, name='get_unique_size'),
    path('getcasktype/', get_unique_casktype, name='get_unique_size'),
    path('getbottled/', get_unique_bottled, name='get_unique_bottled'),
    path('getbottle_sere/', get_unique_bottle_sere, name='get_unique_bottle_sere')
]
