from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf import settings
import requests
import json


@login_required
def basket_detail(request):
    basket = Sales.objects.filter(user_id=request.user.id)
    form = OrderForm()
    user = request.user
    total = 0
    for p in basket:
        if p.product.status != None:
            total += p.variant.total_price * p.quantity
        else:
            total += p.product.total_price * p.quantity

    context = {'basket':basket,'total':total,'form':form,'user':user}
    return render(request, 'sales_basket/basket_detail.html',context )

@login_required
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

def order(request,order_id):
    order = Order.objects.get(id=order_id)
    context = {'order':order}
    return render(request, 'sales_basket/order.html',context)


@require_http_methods(request_method_list=('GET','POST'))
def order_create(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        order = Order.objects.create(user_id=request.user.id,email=data['email'],first_name=data['first_name']
                            ,last_name=data['last_name'],phone=data['phone'],address=data['address'],IP_address=data['IP_address'])

        basket = Sales.objects.filter(user_id=request.user.id)
        for basket in basket:
            ItemOrder.objects.create(order_id=order.id,user_id=request.user.id,product_id=basket.product_id,
                                     variant_id=basket.variant_id,quantity=basket.quantity)
        return redirect('sale:order',order.id)
    





if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"


description = "تراکنش شما با موفقیت انجام شد"
CallbackURL = 'http://127.0.0.1:8080/sale:verify/'


def send_request(request,price):
    global amount
    amount = price
    phone = str(request.user.phone)
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response
    
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response