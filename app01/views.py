from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def index(request):
    return render(request, 'index.html')


def book_list(request):
    book_queryset = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


def book_add(request):
    if request.method == 'GET':
        publish_queryset = models.Publish.objects.all()
        author_queryset = models.Author.objects.all()
        return render(request, 'book_add.html', locals())

    name = request.POST.get('name')
    price = request.POST.get('price')
    publish_date = request.POST.get('publish_date')
    publish_id = request.POST.get('publish')
    author_list = request.POST.getlist('authors')
    new_book_obj = models.Book.objects.create(name=name,
                                              price=price,
                                              publish_date=publish_date,
                                              publish_id=publish_id)
    book2author_list = []
    for author_id in author_list:
        book2author_obj = models.Book2Author(book_id=new_book_obj.pk, author_id=author_id)
        book2author_list.append(book2author_obj)
    models.Book2Author.objects.bulk_create(book2author_list)
    return redirect('book_list')


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


def book_delete(request):
    delete_id = request.POST.get('delete_id')
    models.Book.objects.filter(pk=delete_id).delete()
    # 级联删除
    return HttpResponse('删除成功！！！')


def author_list(request):
    author_queryset = models.Author.objects.all()
    return render(request, 'author_list.html', locals())


def author_add(request):
    if request.method == 'GET':
        return render(request, 'author_add.html')

    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    info = request.POST.get('info')
    models.Author.objects.create(name=name, age=age, gender=gender, info=info)
    return redirect('author_list')


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


def author_delete(request, delete_id):

    models.Author.objects.filter(pk=delete_id).delete()
    return redirect('author_list')