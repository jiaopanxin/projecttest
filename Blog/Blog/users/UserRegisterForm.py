from django import forms
from django.forms import TextInput, NumberInput, PasswordInput
from dbsqlite.models import UsersProfile
import re
gender_choice = (
    ('1', "男"),
    ('2', "女")
)


# 从模型中常见表单
class UserRegisterFrom(forms.ModelForm):
    class Meta:
        model = UsersProfile  # 需要校验的模型
        fields = ["username", "password", "mobile",
                  "age", "gender", "avatar"]  # form表单需要校验的内容

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
