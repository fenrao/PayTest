from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.
from . import forms
from django.contrib import messages
import time
import random
from . import models



class Settlement(View):
    def get(self,request):
        order_form=forms.Createselltement()
        return render(request,'settlement.html',{'order_form':order_form})

    def post(self,request):
        order_form=forms.Createselltement(request.POST)
        if order_form.is_valid():
            school=request.POST.get('school','')
            platform=request.POST.get('platform','')
            subject=request.POST.get('subject','')
            name=request.POST.get('name','')
            amount=request.POST.get('amount','')
            password=request.POST.get('password','')
            #messages.info(request, '注册')
            context={
                'order_id':time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))+str(random.randint(1,99)),
                "name":name,
                "amount":amount,
                'pay_method':1,
                'status':1,

            }
            #创建订单
            models.OrderInfor.create(
                order_id=context['order_id'],
                school=school,
                platform=platform,
                name=name,
                password=password,
                subject=subject,
                total_amount=str(int(amount)*15),
            )
            #return render(request, 'index.html',{'context':context})
            return HttpResponseRedirect('/apptest/?order_id='+context['order_id'])
            #return redirect('/apptest/',order_id=context['order_id'])
            #return HttpResponseRedirect('https://www.baidu.com')‘
        else:
             messages.info(request, '注册shibai')


class Settlement_vip(View):
    def get(self, request):
        order_form = forms.Createselltement()
        return render(request, 'settlement_vip.html', {'order_form': order_form})

    def post(self, request):
        order_form = forms.Createselltement(request.POST)
        if order_form.is_valid():
            school = request.POST.get('school', '')
            platform = request.POST.get('platform', '')
            subject = request.POST.get('subject', '')
            name = request.POST.get('name', '')
            amount = request.POST.get('amount', '')
            password = request.POST.get('password', '')
            # messages.info(request, '注册')
            context = {
                'order_id': time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(random.randint(1, 99)),
                "name": name,
                "amount": amount,
                'pay_method': 1,
                'status': 1,

            }
            # 创建订单
            models.OrderInfor.create(
                order_id=context['order_id'],
                school=school,
                platform=platform,
                name=name,
                password=password,
                subject=subject,
                total_amount=str(int(amount) * 5),
            )
            # return render(request, 'index.html',{'context':context})
            return HttpResponseRedirect('/apptest/?order_id=' + context['order_id'])
            # return redirect('/apptest/',order_id=context['order_id'])
            # return HttpResponseRedirect('https://www.baidu.com')‘
        else:
            messages.info(request, '注册shibai')


class Search(View):
    def get(self,request):
        search_form=forms.Search()
        return render(request,"search.html",{'search_form':search_form})

    def post(self,request):
        Search=forms.Search(request.POST)
        if Search.is_valid():
            oreder_id=request.POST.get('order_id','')
            select=models.OrderInfor.objects.get(order_id=oreder_id)
            print(select.name+'    '+select.password)
            return render(request,'search.html',{'select':select})


class Submit(View):
    def post(self,request):
        order_id=request.POST.get('order_id','')
        remask=request.POST.get('remask','')
        #oreder_id = request.POST.get('order_id', '')
        print(remask)
        print(order_id)
        models.OrderInfor.objects.filter(order_id=order_id).update(remask=remask)
        select = models.OrderInfor.objects.get(order_id=order_id)
        return render(request, 'search.html', {'select': select})