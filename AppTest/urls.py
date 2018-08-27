from django.conf.urls import url,include

from AppTest import views
app_name='AppTest'
urlpatterns=[
    url(r"^$", views.index),
    url(r"^pay/", views.pay),
    url(r"^check_pay/", views.check_pay),
    url('check/',views.check)

]