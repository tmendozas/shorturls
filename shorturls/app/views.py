from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.db import transaction

from models import Link
from encoder import encode,decode


def create_link(request):
    if request.method == 'GET':
        return render(request,'new_link.html')
    elif request.method == 'POST':
        try:
            with transaction.atomic():
                # Save new/old url
                link = Link.objects.create(
                    real_url = request.POST['real_url'],
                )
                # id_str = str(link.id)
                # if len(id_str)%3!=0:
                #     mod_result = 3 - len(id_str)%3
                #     id_str = '0'*mod_result + id_str
                link.short_url = encode(link.id)
                link.save()
                context = {'short_url': link.short_url}
                return render(request,'finished.html', context)
        except Exception as e:
            print 'rollback' + str(e.message)
            transaction.rollback()
            context = {'message': e.message}
            return render(request,'error.html', context)


def redirect_link(request,short_url):
    try:
        link = Link.objects.get(short_url=short_url)
    except Link.DoesNotExist:
        context = {'message': 'This link does not exist or has expired.'}
        return render(request,'error.html',context)
    return HttpResponseRedirect(link.real_url)

def list_links(request):
    if request.method == 'GET':
        # Display template view
        links = Link.objects.all()[:50]
        data = []
        for link in links:
            data.append((link.short_url, link.real_url, link.creation_datetime))
        context = {'links':data}
        print context
        return render(request,'list.html',context)
    elif request.method == 'POST':
        context = {'message': 'Forbidden'}
        return render(request,'error.html',context)
