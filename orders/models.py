from django.db import models

# Create your models here.

class OrderInfor(models.Model):

    PAY_METHOD_CHOICES = {
        ('1','支付宝')
    }
    ORDER_STATUS_ENUM={
        'UNPAID':1,
        'UNSEND':2,
        'FINISHED':3,
    }
    ORDER_STATUS_CHOICES =(
        ('1','未支付'),
        ('2','已支付'),
        ('3','订单信息出现问题'),
        ('4','已完成'),
    )
    plat=(
        ('1','超星'),
        ('2', '智慧树'),
        ('3', '高校邦'),
    )
    order_id = models.CharField(max_length=30, primary_key=True, verbose_name="订单号")
    platform=models.CharField(choices=plat,max_length=1,default='1',verbose_name='平台')
    school=models.CharField(max_length=40,verbose_name='学校')
    name=models.CharField(max_length=20,verbose_name='刷客帐号')
    password=models.CharField(max_length=20,verbose_name='帐号密码')
    subject=models.CharField(max_length=40,verbose_name='课目')
    total_amount=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总金额")
    pay_method = models.CharField(choices=PAY_METHOD_CHOICES,max_length=5, default='1', verbose_name="支付方式")
    status = models.CharField(choices=ORDER_STATUS_CHOICES,max_length=5, default='1', verbose_name="订单状态")
    remask=models.CharField(max_length=100,verbose_name='备注',blank=True)

    class Meta:
        db_table = "order"
        verbose_name='订单'

    @staticmethod
    def create(order_id, school,platform,name,password,subject,total_amount):
        order = OrderInfor(
            order_id=order_id,
            school=school,
            platform=platform,
            name=name,
            password=password,
            subject=subject,
            total_amount=total_amount,
            pay_method='1',
            status='1',
            )
        order.save()
        # for item in items:
        #     item.order = order
        #     item.save()
