from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction, IntegrityError
from django.template.loader import render_to_string

from shorturls.app.models import Link
from shorturls.app.helpers.encoder import encode,decode
from shorturls.app.helpers import url_validator




def create_link(request):
    if request.method == 'GET':
        return render(request,'new_link.html')
    elif request.method == 'POST':
        context = dict()
        long_url = request.POST['real_url']
        is_valid, valid_url = url_validator.prep_url(long_url)
        suggested_short = request.POST.get('suggested_short','')
        if not is_valid:
            return JsonResponse({'valid':str(is_valid)})
        try:
            with transaction.atomic():
                link,created = Link.objects.get_or_create(
                    real_url = valid_url
                )
                valid_short = url_validator.validate_short_url(suggested_short)
                if created or valid_short:
                    if valid_short:
                        taken = Link.objects.filter(short_url=suggested_short).exists()
                        link.short_url = encode(link.id) if taken else suggested_short
                        if taken:
                            print 'Entered taken'
                            context['message'] = ('Your desired url ' + 
                                    suggested_short + 
                                    ' is not available. Use this instead.')
                    else: 
                        link.short_url = encode(link.id)
                        if suggested_short:
                            context['message'] = ('Your desired url ' + 
                                        suggested_short + 
                                        ' is invalid. Use this instead.')
                    link.save()     
                context['short_url'] = link.short_url
                if request.is_ajax():
                    print 'here'
                    print context
                    html = render_to_string('finished.html', context)
                    return JsonResponse({'valid':str(is_valid),'html':html})
                else:
                    print ' or here'
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

def validate_url(request):
    if request.method=='GET':
        context = {'message': 'Forbidden'}
        return render(request,'error.html',context)
    if request.method=='POST':
        is_valid = url_validator.is_valid(request.POST['url'])
        return JsonResponse({'valid':is_valid})

