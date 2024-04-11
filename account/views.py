from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from random import randint
# import ghasedakpack
# import requests


@require_http_methods(request_method_list=('GET','POST'))
def authentication(request):
    form = authForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        phone = f"0{data['phone']}"
        if User.objects.filter(phone=data['phone']).exists():
            user = authenticate(request, phone=phone)
            login(request, user)
            return redirect('home')
        else:
            random_code = randint(10000,99999)
            # sms = ghasedakpack.Ghasedak("Your APIKEY")
            # sms.send({'message': 'کد اعتبار سنجی فروشگاه شما: '+ random_code, 'receptor' : phone, 'linenumber': '300085858' })
            user = User.objects.create_user(phone=data['phone'],)
            user.save()
            messages.success(request, 'You made it')
            return redirect('home')
    return render(request, 'account/authentication.html',{'form':form})

def Profile(request):
    profile = User.objects.get(username=request.user)
    return render(request, 'account/profile.html', {'profile':profile})


@require_http_methods(request_method_list=('GET','POST'))
def update_profile(request):
    update = Update_ProfileForm(request.POST,instance=request.user)
    if update.is_valid():
        update.save()
        messages.success(request, '.اطلاعات کاربری شما بروزرسانی شد')
        return redirect('profile')
    return render(request, 'account/update_profile.html',{'update':update})
