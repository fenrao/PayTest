# PayTest
Django实现的订单支付网站
##
   ##开发环境  python3.6+Django2.0+python-alipay-sdk

## 主要功能： ##
- 下单，支付。对订单状态查询。
- 后台管理员查看，修改订单信息。


## 配置： ##
setting.py文件中。

支付宝配置：

ALIPAY_APPID=''

ALIPAY_URL=''


## 运行 ##
进入到程序根目录 运行: python3 manage.py runserver 127.0.0.0:8000