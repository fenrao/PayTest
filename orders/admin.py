from django.contrib import admin

from . import models


#向管理员页面添加OrderInfo模型
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'name',
        'password',
        'school',
        'subject',
        'status',
    )
    list_filter = ['status']

                        #admin.site.register(models.OrderInfor)

admin.site.register(models.OrderInfor, OrderAdmin)
# Register your models here.
