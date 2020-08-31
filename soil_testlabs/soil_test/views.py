from django.shortcuts import render

from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def lab_view(request):
    return render(request,'soil_test/index.html')
@login_required
def display_andhrapradesh(request):
    items = andhrapradesh.objects.all()
    context = {
        'items': items,
        'header': 'ANDRAPRADESH',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_assam(request):
    items = assam.objects.all()
    context = {
        'items': items,
        'header': 'ASSAM',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_bihar(request):
    items = bihar.objects.all()
    context = {
        'items': items,
        'header': 'BIHAR',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_chandigarh(request):
    items = chandigarh.objects.all()
    context = {
        'items': items,
        'header': 'CHANDIGARH',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_chhatisgarh(request):
    items = Chhattisgarh.objects.all()
    context = {
        'items': items,
        'header': 'CHHATTISGARH',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_delhi(request):
    items = delhi.objects.all()
    context = {
        'items': items,
        'header': 'DELHI',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_goa(request):
    items = goa.objects.all()
    context = {
        'items': items,
        'header': 'GOA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_gujrat(request):
    items = gujrat.objects.all()
    context = {
        'items': items,
        'header': 'GUJARAT',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_haryana(request):
    items = haryana.objects.all()
    context = {
        'items': items,
        'header': 'HARYANA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_himanchal(request):
    items = himachalpradesh.objects.all()
    context = {
        'items': items,
        'header': 'HIMACHAL PRADESH',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_jharkhand(request):
    items = jharkhand.objects.all()
    context = {
        'items': items,
        'header': 'JHARKHAND',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_karnataka(request):
    items = karnataka.objects.all()
    context = {
        'items': items,
        'header': 'KARNATAKA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_kerala(request):
    items = kerala.objects.all()
    context = {
        'items': items,
        'header': 'KERALA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_madhyapradesh(request):
    items = madhyapradesh.objects.all()
    context = {
        'items': items,
        'header': 'MADHYAPRADESH',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_maharastra(request):
    items = maharashtra.objects.all()
    context = {
        'items': items,
        'header': 'MAHARASHTRA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_meghalaya(request):
    items = meghalaya.objects.all()
    context = {
        'items': items,
        'header': 'MEGHALAYA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_mizoram(request):
    items = mizoram.objects.all()
    context = {
        'items': items,
        'header': 'MIZORAM',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_odisha(request):
    items = odisha.objects.all()
    context = {
        'items': items,
        'header': 'ODISHA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_punjab(request):
    items = punjab.objects.all()
    context = {
        'items': items,
        'header': 'PUNJAB',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_rajasthan(request):
    items = rajasthan.objects.all()
    context = {
        'items': items,
        'header': 'RAJASTHAN',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_sikkim(request):
    items = sikkim.objects.all()
    context = {
        'items': items,
        'header': 'SIKKIM',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_tamilnadu(request):
    items = tamilnadu.objects.all()
    context = {
        'items': items,
        'header': 'TAMIL NADU',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_telangana(request):
    items = telangana.objects.all()
    context = {
        'items': items,
        'header': 'TELANGANA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_tripura(request):
    items = tripura.objects.all()
    context = {
        'items': items,
        'header': 'TRIPURA',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_uttarpradesh(request):
    items = uttarpradesh.objects.all()
    context = {
        'items': items,
        'header': 'UTTAR PRADESH',
    }
    return render(request, 'soil_test/index.html', context)
@login_required
def display_uttarakhand(request):
    items = uttarakhand.objects.all()
    context = {
        'items': items,
        'header': 'UTTARAKHAND',
    }
    return render(request, 'soil_test/index.html', context)
