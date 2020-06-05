from django import forms
from django.core.validators import RegexValidator
from app01 import models


class UserRegForm(forms.Form):
    username = forms.CharField(max_length=32,
                               label='用户名',
                               error_messages={
                                   'required': '用户名不能为空'
                               },
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(min_length=4,
                               max_length=8,
                               label='密码',
                               error_messages={
                                   'min_length': '密码长度不能少于4位',
                                   'max_length': '密码长度不能多余于8位',
                                   'required': '密码不能为空'
                               },
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(min_length=4,
                               max_length=8,
                               label='确认密码',
                               error_messages={
                                   'min_length': '确认密码长度不能少于4位',
                                   'max_length': '确认密码长度不能多余于8位',
                                   'required': '确认密码不能为空'
                               },
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='邮箱',
                             error_messages={
                                 'required': '确认密码不能为空'
                             },
                             widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='手机号',
                            error_messages={
                                'required': '确认密码不能为空'
                            },
                            validators=[
                                RegexValidator(r'^1[3|4|5|6|8][0-9]\d{4,8}$', '手机号格式不正确')
                                ],
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if models.User.objects.filter(username=username).exists():
            self.add_error('username', '用户名已经存在')
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            self.add_error('re_password', '两次密码输入不一致')

        return self.cleaned_data


class UserLogForm(forms.Form):
    username = forms.CharField(max_length=32,
                               label='用户名',
                               error_messages={
                                   'required': '用户名不能为空'
                               },
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码',
                               error_messages={
                                   'required': '密码不能为空'
                               },
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'},
                                                                  render_value=True))


class BookAddForm(forms.Form):
    name = forms.CharField(label='图书名称',
                           error_messages={
                               'required': '图书名称不能为空'
                           },
                           widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    price = forms.DecimalField(label='价格',
                           error_messages={
                               'required': '图书价格不能为空'
                           },
                           widget=forms.widgets.TextInput(attrs={'class':'form-control'}))
    publish_date = forms.DateField(label='出版日期',
                               error_messages={'required': '出版日期不能为空'},
                               widget=forms.widgets.DateInput(attrs={'class':'form-control'})
                            )
    publish_id = forms.ChoiceField(label='出版社',
                                error_messages={'required':'出版社不能为空'},
                                widget=forms.widgets.Select(attrs={'class': 'form-control'})
                                )
    author = forms.MultipleChoiceField(
        label='作者',
        error_messages={'required':'作者不能为空'},
        widget=forms.widgets.SelectMultiple(attrs={'class':'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['publish_id'].choices = models.Publish.objects.values_list('pk', 'name')
        self.fields['author'].choices = models.Author.objects.values_list('pk', 'name')