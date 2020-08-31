from django.urls import path
from django.contrib import admin
from . import views

app_name = 'soil_test'
urlpatterns = [
    path('',views.lab_view,name="labs"),
    path('display_andhrapradesh/',views.display_andhrapradesh,name='ap'),
    path('display_assam/',views.display_assam,name='assam'),
    path('display_bihar/',views.display_bihar,name='bihar'),
    path('display_chandigarh/',views.display_chandigarh,name='chd'),
    path('display_chhatisgarh/',views.display_chhatisgarh,name='chtt'),
    path('display_delhi/',views.display_delhi,name='delhi'),
    path('display_goa/',views.display_goa,name='goa'),
    path('display_gujarat/',views.display_gujrat,name='gujarat'),
    path('display_haryana/',views.display_haryana,name='hry'),
    path('display_himanchal/',views.display_himanchal,name='hp'),
    path('display_jharkhand/',views.display_jharkhand,name='jkd'),
    path('display_karnataka/',views.display_karnataka,name='kar'),
    path('display_kerala/',views.display_kerala,name='ker'),
    path('display_madhyapradesh/',views.display_madhyapradesh,name='mp'),
    path('display_maharastra/',views.display_maharastra,name='maharashtra'),
    path('display_meghalaya/',views.display_meghalaya,name='meg'),
    path('display_mizoram/',views.display_mizoram,name='mizoram'),
    path('display_odisha/',views.display_odisha,name='odisha'),
    path('display_punjab/',views.display_punjab,name='pun'),
    path('display_rajasthan/',views.display_rajasthan,name='rajasthan'),
    path('display_sikkim/',views.display_sikkim,name='sikkim'),
    path('display_tamilnadu/',views.display_tamilnadu,name='tamil'),
    path('display_telangana/',views.display_telangana,name='telangana'),
    path('display_tripura/',views.display_tripura,name='tripura'),
    path('display_uttarpradesh/',views.display_uttarpradesh,name='up'),
    path('display_uttarakhand/',views.display_uttarakhand,name='ukd'),

]
