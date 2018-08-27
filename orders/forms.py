from django import forms

class Createselltement(forms.Form):
    SUBJECT_CHOICES = (
        ('1', '超星'),
        ('2', '智慧树'),
        ('3', '高校邦'),
    )

    school=forms.CharField(
        max_length=20,
        required=True,
        label='学校',
        # widget=forms.TextInput(attrs={
        #     'id':'inputuser',
        #     'placeholder':'',
        # })

    )
    amount=forms.IntegerField(
        label='下单数量',
        min_value=1,

    )
    platform=forms.ChoiceField(
        choices=SUBJECT_CHOICES,label='平台',required=True
    )
    subject = forms.CharField(
        max_length=40, required=True, label='课程'
    )
    name=forms.CharField(
        max_length=20,required=True,label='账户'
    )
    password = forms.CharField(
        max_length=20, required=True, label='密码'
    )

class Search(forms.Form):
    order_id = forms.CharField(
        max_length=20, required=True, label='请输入订单号'
    )