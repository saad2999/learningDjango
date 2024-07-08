from django.shortcuts import render, get_object_or_404 
from .models import chaiVarity,Store
from .forms import chaiVarityForm



def all_chai(request):
    chais = chaiVarity.objects.all()
    return render(request, 'chai/all_chai.html',{'chais': chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(chaiVarity,pk=chai_id)
    return render(request, 'chai/chai_details.html', {'chai': chai})

def chai_store_view(request):
    stores=None
    form=chaiVarityForm()
    if request.method == 'POST':
        form=chaiVarityForm(request.POST)
    if form.is_valid():
        chai_varity=form.cleaned_data['chai_varity']
        stores=Store.objects.filter(chai_Varieties=chai_varity)
    
    return render(request, 'chai/chai_stores.html',{'stores': stores,'form':form})
