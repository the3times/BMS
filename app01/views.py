from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from app01 import models
from app01 import my_forms
from utils.pagination import get_page_queryset
from utils.login_auth import login_auth


def register(request):
    form_obj = my_forms.UserRegForm()
    if request.method == 'POST':
        form_obj = my_forms.UserRegForm(request.POST)
        if form_obj.is_valid():
            form_obj.cleaned_data.pop('re_password')
            print(form_obj.cleaned_data)
            models.User.objects.create(**form_obj.cleaned_data)
            return redirect('index')

    return render(request, 'register.html', locals())


def login(request):
    form_obj = my_forms.UserLogForm()
    if request.method == 'POST':
        form_obj = my_forms.UserLogForm(request.POST)
        if form_obj.is_valid():
            name = form_obj.cleaned_data.get('username')
            pawd = form_obj.cleaned_data.get('password')
            if models.User.objects.filter(username=name, password=pawd).exists():
                target_url = request.GET.get('next') or 'index'    # 登录前要访问的页面或者直接到index
                request.session['login_auth_key'] = 'is_login'
                request.session['username'] = name
                return redirect(target_url)
            login_error = '用户名或密码错误'

    return render(request, 'login.html', locals())


@login_auth
def logout(request):
    request.session.flush()
    return HttpResponse('OK')


def index(request):
    return render(request, 'index.html', locals())


@login_auth
def book_list(request):
    book_queryset = models.Book.objects.all()
    page_obj, page_queryset = get_page_queryset(request, book_queryset)
    return render(request, 'book_list.html', locals())


@login_auth
def book_add(request):

    form_obj = my_forms.BookAddForm()
    if request.method == 'POST':
        form_obj = my_forms.BookAddForm(request.POST)
        if form_obj.is_valid():
            author_pk_list = form_obj.cleaned_data.pop('author')
            new_book_obj = models.Book.objects.create(**form_obj.cleaned_data)
            # 手动加第三张关系表(半自动表关系)
            book2author_list = []
            for author_id in author_pk_list:
                book2author_obj = models.Book2Author(book_id=new_book_obj.pk, author_id=author_id)
                book2author_list.append(book2author_obj)
            models.Book2Author.objects.bulk_create(book2author_list)
            return redirect('book_list')

    return render(request, 'book_add.html', locals())


@login_auth
def book_edit(request, edit_id):
    if request.method == 'GET':
        book_obj = models.Book.objects.filter(pk=edit_id).first()
        publish_queryset = models.Publish.objects.all()
        author_queryset = models.Author.objects.all()
        return render(request, 'book_edit.html', locals())

    name = request.POST.get('name')
    price = request.POST.get('price')
    publish_date = request.POST.get('publish_date')
    publish_id = request.POST.get('publish')
    author_list = request.POST.getlist('authors')
    models.Book.objects.filter(pk=edit_id).update(name=name,
                                                  price=price,
                                                  publish_date=publish_date,
                                                  publish_id=publish_id)
    models.Book2Author.objects.filter(book_id=edit_id).delete()
    book2author_list = []
    for author_id in author_list:
        book2author_obj = models.Book2Author(book_id=edit_id, author_id=author_id)
        book2author_list.append(book2author_obj)
    models.Book2Author.objects.bulk_create(book2author_list)
    return redirect('book_list')


@login_auth
def book_delete(request):
    back_msg = {'status_code': 1111, 'msg': ''}
    try:
        delete_id = request.POST.get('delete_id')
        models.Book.objects.filter(pk=delete_id).delete()
        back_msg['msg'] = '删除成功'
    except:
        back_msg['status_code'] = 2222
        back_msg['msg'] = '删除失败'
    # 级联删除
    return JsonResponse(back_msg)


@login_auth
def author_list(request):
    author_queryset = models.Author.objects.all()
    page_obj, page_queryset = get_page_queryset(request, author_queryset)
    return render(request, 'author_list.html', locals())


@login_auth
def author_add(request):
    if request.method == 'GET':
        return render(request, 'author_add.html')

    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    info = request.POST.get('info')
    models.Author.objects.create(name=name, age=age, gender=gender, info=info)
    return redirect('author_list')


@login_auth
def author_edit(request, edit_id):
    if request.method == 'GET':
        author_obj = models.Author.objects.filter(pk=edit_id).first()
        return render(request, 'author_edit.html', locals())
    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    info = request.POST.get('info')
    models.Author.objects.filter(pk=edit_id).update(name=name, age=age, gender=gender, info=info)
    return redirect('author_list')


@login_auth
def author_delete(request):
    back_msg = {'status_code': 1111, 'msg': ''}
    try:
        delete_id = request.POST.get('delete_id')
        models.Author.objects.filter(pk=delete_id).delete()
        back_msg['msg'] = '删除成功'
    except:
        back_msg['status_code'] = 2222
        back_msg['msg'] = '删除失败'

    return JsonResponse(back_msg)
