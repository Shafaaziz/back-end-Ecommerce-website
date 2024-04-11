from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def home(request):
    sub_category = Sub_Category.objects.all()
    return render(request, 'shop/home.html', {'sub_category':sub_category})

@login_required
def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        body = subject +'\n'+ email+'\n'+message
        form = EmailMessage(
            'contact form',
            body,
            'test',
            ('Alirezaazizishafa0936@gmail.com',)
        )
        form.send(fail_silently=False)
        return render(request, 'shop/contact.html')
    return render(request, 'shop/contact.html')


def product(request,slug=None,id=None):
    product = Product.objects.all()
    category = Category.objects.all()
    form = SearchForm()
    sub_category = Sub_Category.objects.all()
    if slug and id:
        data = get_object_or_404(Sub_Category,slug=slug,id=id)
        product = product.filter(category=data)
    context = {'product':product, 'category':category,'sub_category':sub_category,'form':form}
    return render(request, 'shop/products.html', context )

def detail(request,id):
    product = get_object_or_404(Product,id=id)
    comment_form = CommentForm()
    replyform = ReplyForm()
    comment = Comment.objects.filter(product_id=id,is_reply=False)
    is_like = False
    if product.like.filter(id=request.user.id).exists():
        is_like = True
    is_unlike = False
    if product.unlike.filter(id=request.user.id).exists():
        is_unlike = True
    if product.status != None:
        if request.method == 'POST':
            variant = Variant.objects.filter(product_variant_id=id)
            var_id = request.POST.get('selected')
            variants = Variant.objects.get(id=var_id)
        else:
            variant = Variant.objects.filter(product_variant_id=id)
            variants = Variant.objects.get(id=variant[0].id) 
        context = {'product':product, 'variant':variant,'variants':variants,'is_like':is_like,'is_unlike':is_unlike,'comment_form':comment_form,
                   'comment':comment,'replyform':replyform}
        return render(request, 'shop/detail.html',context)
    else:
        return render(request, 'shop/detail.html',{'product':product,'is_like':is_like,'is_unlike':is_unlike,'comment_form':comment_form,
                        'comment':comment,'replyform':replyform})

@login_required
def productLike(request,id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product,id=id)
    is_like = False
    if product.like.filter(id=request.user.id).exists():
        product.like.remove(request.user)
        is_like = False
    else:
        product.like.add(request.user)
        is_like = True
        messages.success(request, 'نظر شما ثبت شد.','success')
    return redirect(url)

@login_required
def productUnlike(request,id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product,id=id)
    is_unlike = False
    if product.unlike.filter(id=request.user.id).exists():
        product.unlike.remove(request.user)
        is_unlike = False
    else:
        product.unlike.add(request.user)
        is_unlike = True
        messages.success(request, 'نظر شما ثبت شد.','success')
    return redirect(url)


@require_http_methods(request_method_list=('GET','POST'))
@login_required
def product_comment(request,id):
    url = request.META.get('HTTP_REFERER')
    comment = CommentForm(request.POST)
    if comment.is_valid():
        data = comment.cleaned_data
        Comment.objects.create(comment=data['comment'],rate=data['rate'],user_id=request.user.id,product_id=id)
    return redirect(url)

@require_http_methods(request_method_list=('GET','POST'))
@login_required
def comment_reply(request,id,comment_id):
    url = request.META.get('HTTP_REFERER')
    replyform = ReplyForm(request.POST)
    if replyform.is_valid():
        data = replyform.cleaned_data
        Comment.objects.create(comment=data['comment'],product_id=id,user_id=request.user.id,reply_id=comment_id,is_reply=True)
        messages.success(request, 'نظر شما ثبت شد!')
        return redirect(url)
    
def product_search(request):
    if request.method == 'POST':
        product = Product.objects.all()
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data is not None:
                product = product.filter(name=data)
            return render(request, 'shop/products.html',{'form':form})


