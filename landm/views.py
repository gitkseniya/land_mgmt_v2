from django.shortcuts import render
from .models import UnitOwner, Owner, Unit

# Create your views here.


def index(request):
    data = Owner.objects.all()
    context = {'data': data}
    return render(request, 'landm/index.html', context)


def owner(request, owner_id):
    tu = UnitOwner.objects.filter(owner_id=owner_id).count()
    u = UnitOwner.objects.filter(owner_id=owner_id)
    o = Owner.objects.get(pk=owner_id)
    context = {
        'units': u,
        'owner': o,
        'total_units': tu
    }
    return render(request, 'landm/owner.html', context)


def unit(request, unit_id):
    u = Unit.objects.get(id=unit_id)
    # o = Owner.objects.get(pk=unit_id)
    o = UnitOwner.objects.filter(unit_id=unit_id)
    context = {
        'u': u,
        'owners': o,
    }
    return render(request, 'landm/unit.html', context)

def units(request):
     data = Unit.objects.all()
     context = {'data': data}
     return render(request, 'landm/units.html', context)

