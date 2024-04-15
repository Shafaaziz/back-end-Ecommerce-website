from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product
from .models import *
from django.contrib import messages

def basket_detail(request):
    basket = Sales.objects.filter(user_id=request.user.id)
    total = 0
    for p in basket:
        if p.product.status != None:
            total += p.variant.total_price * p.quantity
        else:
            total += p.product.total_price * p.quantity
    return render(request, 'sales_basket/basket_detail.html', {'basket':basket,'total':total})


def add_basket(request,id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product,id=id)
    if product.status != None:
        var_id = request.POST.get('selected')
        data = Sales.objects.filter(user_id=request.user.id,variant_id=var_id)
        if data:
            check = True
        else:
            check = False
    else:
        data = Sales.objects.filter(user_id=request.user.id,product_id=id)
        if data:
            check = True
        else:
            check = False
    if request.method == 'POST':
        var_id = request.POST.get('selected')
        form = SalesForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data['quantity']
            if check == True:
                if product != None:
                    basket = Sales.objects.get(user_id=request.user.id,product_id=id,variant_id=var_id)
                    messages.success(request, '!محصول به سبد شما اضافه شد')
                else:
                    basket = Sales.objects.get(user_id=request.user.id,product_id=id)
                    messages.success(request, '!محصول به سبد شما اضافه شد')

                basket.quantity += clean_data
                basket.save()

            else:
                Sales.objects.create(user_id=request.user.id,product_id=id,variant_id=var_id,quantity=clean_data)
                messages.success(request, 'محصول به سبد شما اضافه شد!')
        return redirect(url)
    
def remove_basket(request,id):
    url = request.META.get('HTTP_REFERER')
    Sales.objects.filter(id=id).delete()
    return redirect(url)