# Generated by Django 2.0.5 on 2018-08-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfor',
            fields=[
                ('order_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='订单号')),
                ('platform', models.CharField(choices=[('1', '超星'), ('2', '智慧树'), ('3', '高校邦')], default='1', max_length=1, verbose_name='平台')),
                ('school', models.CharField(max_length=40, verbose_name='学校')),
                ('name', models.CharField(max_length=20, verbose_name='刷客帐号')),
                ('password', models.CharField(max_length=20, verbose_name='帐号密码')),
                ('subject', models.CharField(max_length=40, verbose_name='课目')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='商品总金额')),
                ('pay_method', models.CharField(choices=[('1', '支付宝')], default='1', max_length=5, verbose_name='支付方式')),
                ('status', models.CharField(choices=[('1', '未支付'), ('2', '已支付'), ('3', '订单信息出现问题'), ('4', '已完成')], default='1', max_length=5, verbose_name='订单状态')),
                ('remask', models.CharField(blank=True, max_length=100, verbose_name='备注')),
            ],
            options={
                'verbose_name': '订单',
                'db_table': 'order',
            },
        ),
    ]