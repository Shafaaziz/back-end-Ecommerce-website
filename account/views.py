from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib import messages
from .forms import *
from .models import *
from random import randint
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# import ghasedakpack
# import requests



class authentication(View):
    template_name = 'account/authentication.html'
    form_class = authForm

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if User.objects.filter(phone=data).exists():
                user = authenticate(request, phone=data)
                login(request,user)
                return redirect('home')
            else:
                # random_code = randint(10000,99999)
                # sms = ghasedakpack.Ghasedak("Your APIKEY")
                # sms.send({'message': 'کد اعتبار سنجی فروشگاه شما: '+ random_code, 'receptor' : phone, 'linenumber': '300085858' })
                user = User.objects.create_user(phone=data)
                user.save()
                return redirect('home')
        return render(request,self.template_name,{'form':self.form_class})


@login_required
def Profile(request):
    profile = get_object_or_404(User,username=request.user)
    return render(request, 'account/profile.html', {'profile':profile})


class update_profile(LoginRequiredMixin,UpdateView):
    template_name = 'account/update_profile.html'
    fields = ['username', 'phone','email','address','IP_address']
    success_url = reverse_lazy('profile')

    def get_object(self):
        querySet = get_object_or_404(User,id=self.request.user.id)
        return querySet