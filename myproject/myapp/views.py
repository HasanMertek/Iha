from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import IHA, Rental, Customer  # Customer modeli eklendi
from .forms import IHAForm, RentalForm, CustomerForm  # CustomerForm eklendi
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return JsonResponse({'message': 'Customer deleted successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

def iha_list(request):
    ihalar = IHA.objects.all()
    return render(request, 'iha_list.html', {'ihalar': ihalar})
def customer_edit(request, pk):
    
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list or another appropriate URL
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_edit.html', {'form': form})

def customers(request):
    customers = Customer.objects.all()  # customer_list yerine Customer kullanıldı
    return render(request, 'customer_list.html', {'customers': customers})  # customer_list yerine customers düzeltildi

@login_required
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Müşteri eklendikten sonra listeye yönlendirme yapın
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

@login_required
def iha_add(request):
    if request.method == 'POST':
        form = IHAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IHAForm()
    return render(request, 'iha_form.html', {'form': form})

@login_required
def iha_edit(request, pk):
    iha = get_object_or_404(IHA, pk=pk)
    if request.method == 'POST':
        form = IHAForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            return redirect('iha_list')
    else:
        form = IHAForm(instance=iha)
    return render(request, 'iha_form.html', {'form': form})

@login_required
@csrf_exempt
def iha_delete(request, pk):
    if request.method == 'POST':
        iha = get_object_or_404(IHA, pk=pk)
        iha.delete()
        return JsonResponse({'message': 'İHA başarıyla silindi.'})
    return JsonResponse({'error': 'Geçersiz istek.'}, status=400)

@login_required
def rental_create(request, iha_id):
    iha = get_object_or_404(IHA, id=iha_id)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.iha = iha
            rental.user = request.user
            rental.save()
            return redirect('iha_list')
    else:
        form = RentalForm()
    return render(request, 'rental_form.html', {'form': form, 'iha': iha})

def iha_list_search(request):
    iha_list = IHA.objects.all().values(
        "id", "isim", "model", "saatlik_fiyat", "mevcut"
    )
    data = list(iha_list)
    response = {
        "draw": request.GET.get('draw', 1),
        "recordsTotal": len(data),
        "recordsFiltered": len(data),
        "data": data 
    }
    return JsonResponse(response)
