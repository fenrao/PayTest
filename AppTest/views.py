from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from alipay import AliPay
import os
from django.conf import settings
from orders import models
import json

def index(request):
    order_id=request.GET.get('order_id')
    context = models.OrderInfor.objects.get(order_id=order_id)
    # if (context.status =='2' ):
    #     return render(request,'search.html')
    return render(request, "index.html",{'context':context})


def pay(request):
    order_id = request.POST.get("order_id")
    platform = request.POST.get('platform')
    # 创建用于进行支付宝支付的工具对象
    context = models.OrderInfor.objects.get(order_id=order_id)
    amount=context.total_amount
    print(amount)
    alipay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "AppTest/app_private_key.pem"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "AppTest/alipay_public_key.pem"),
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=True  # 默认False  配合沙箱模式使用
    )
    if (platform =='2'):
        #电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=str(amount),  # 将Decimal类型转换为字符串交给支付宝
            subject="刷课订单",
            return_url="http://122.152.192.155:8000/orders/settlement/",
            notify_url=''  # 可选, 不填则使用默认notify url 异步跳转
        )
    else:
        order_string = alipay.api_alipay_trade_wap_pay(
            out_trade_no=order_id,
            total_amount=str(amount),
            subject="刷课订单",
            return_url='http://122.152.192.155:8000/orders/settlement/',
            notify_url=''  # 可选, 不填则使用默认notify url
        )

    # 让用户进行支付的支付宝页面网址
    url = settings.ALIPAY_URL + "?" + order_string
    print(url)
    return JsonResponse({"code": 0, "message": "请求支付成功", "url": url})

def check_pay(request):
    # 创建用于进行支付宝支付的工具对象
    order_id = request.GET.get("order_id")
    alipay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "AppTest/app_private_key.pem"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "AppTest/alipay_public_key.pem"),
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        sign_type="RSA2",  # RSA2,官方推荐，配置公钥的时候能看到
        debug=True  # 默认False  配合沙箱模式使用
    )

    while True:

     try:
        response = alipay.api_alipay_trade_query(order_id)  # response是一个字典
        # 判断支付结果
        code = response.get("code")  # 支付宝接口调用成功或者错误的标志
        trade_status = response.get("trade_status")  # 用户支付的情况
     except BaseException:
        print("a")

     if code == "10000" and trade_status == "TRADE_SUCCESS":
        # 表示用户支付成功
        # 返回前端json，通知支付成功
        #订单支付成功
        models.OrderInfor.objects.filter(order_id=order_id).update(status='2')
        print('zhifu wancheng ')
        return JsonResponse({"code": 0, "message": "支付成功"})


     elif code == "40004" or (code == "10000" and trade_status == "WAIT_BUYER_PAY"):
        # 表示支付宝接口调用暂时失败，（支付宝的支付订单还未生成） 后者 等待用户支付
        # 继续查询
        print(code)
        print(trade_status)
        continue


# Create your views here.

def check(request):

    trade_status = request.POST.get("trade_status",)
    print(trade_status)

    return JsonResponse({'trade_status':trade_status})
