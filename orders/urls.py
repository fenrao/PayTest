from django.conf.urls import url,include
from django.urls import path

from orders import views
app_name='orders'

urlpatterns = [
    path('settlement/',views.Settlement.as_view(),name='settlement'),
    path('search/',views.Search.as_view(),name='search'),
    path('submit/',views.Submit.as_view(),name='submit'),
    path('settlement_vip/2018111/vip',views.Settlement_vip.as_view(),name='settlement_vip')
]