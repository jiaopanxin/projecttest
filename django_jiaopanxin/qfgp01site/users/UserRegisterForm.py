from django import forms
from django.forms import TextInput, NumberInput, PasswordInput
from users.models import UsersProfile
import re
gender_choice = (
    ('1', "男"),
    ('2', "女")
)

# 自定义一个forms 类  这个类可以帮我们生成响应的html标签


class RegiterUserForm(forms.Form):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),

    )
    mobile = forms.CharField(
        min_length=11,
        max_length=11,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1, max_value=100
    )
    gender = forms.ChoiceField(required=True,
                               choices=gender_choice,
                               widget=forms.RadioSelect(), initial='1'
                               )

    # 针对指定字段添加自定义验证
    # 方法名格式要求:  clean_字段名

    def clean_mobile(self):
        """
        验证手机号是否合法
        :return: 合法的数据或者错误信息
        """
        mobile = self.cleaned_data['mobile']
        PRGEX_MOBILE = r'^1[358]\d{9}|^147\d{8}|^176\d{8}$'
        regex = re.compile(PRGEX_MOBILE)
        if regex.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(
                '无效的手机号',
                code='mobile_invalid'
            )

#从模型中常见表单
class UserRegisterFrom(forms.ModelForm):
    class Meta:
        model = UsersProfile  # 需要校验的模型
        fields = ["username", "password", "mobile",
                  "age", "gender","avatar"]  # form表单需要校验的内容

        # 自定义小部件
        widgets = {
            "gender": forms.RadioSelect,
            # "username": TextInput(attrs={'class': 'form-control'}),
            # "password": PasswordInput(attrs={'class': 'form-control'}),
            # "mobile": TextInput(attrs={'class': 'form-control'}),
            # "age": NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_mobile(self):
        """
        验证手机号是否合法
        """
        mobile = self.cleaned_data['mobile']
        PRGEX_MOBILE = r'^1[358]\d{9}|^147\d{8}|^176\d{8}$'
        regex = re.compile(PRGEX_MOBILE)
        if regex.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(
                '无效的手机号',
                code='mobile_invalid'
            )


class MyForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="用户名", widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField()
    mobile = forms.CharField()
    age = forms.IntegerField()
    gender = forms.ChoiceField()
