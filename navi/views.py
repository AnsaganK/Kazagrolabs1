from django.shortcuts import render, redirect,HttpResponse
from .myDecorators import hasGroups, writeUserActivity
from .forms import *
from .models import *
from itertools import chain
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

import datetime as dt
import random
from django.contrib.auth.models import Group

def login(request):
    return render(request, 'login.html')

@login_required(redirect_field_name='login')
def statistics(request):
    if request.GET:
        print(request.GET)
        day = request.GET['day']
        day = int(day)
    else:
        day = 30
    time = (datetime.now()-timezone.timedelta(days=day)).date()

    s = Selection.objects.filter(date__gte=time).filter(date__lte=datetime.now().date())

    s1 = fors(s.filter(status="Поступило"))
    s2 = fors(s.filter(status="В процессе"))
    s3 = fors(s.filter(status="Готово"))
    p = Preparation.objects.filter(date__gte=time).filter(date__lte=datetime.now().date())
    p1 = fors(p.filter(status="Поступило"))
    p2 = fors(p.filter(status="В процессе"))
    p3 = fors(p.filter(status="Готово"))
    l = Laboratory.objects.filter(date__gte=time).filter(date__lte=datetime.now().date())
    l1 = fors(l.filter(status="Поступило"))
    l2 = fors(l.filter(status="В процессе"))
    l3 = fors(l.filter(status="Готово"))
    a = Agrohym.objects.filter(date__gte=time).filter(date__lte=datetime.now().date())
    a1 = a.filter(status="Поступило").count
    a2 = a.filter(status="В процессе").count
    a3 = a.filter(status="Готово").count

    xCorS = []
    yCor1S = []
    yCor2S = []
    yCor3S = []
    xCorP = []
    yCor1P = []
    yCor2P = []
    yCor3P = []
    xCorL = []
    yCor1L = []
    yCor2L = []
    yCor3L = []
    xCorA = []
    yCor1A = []
    yCor2A = []
    yCor3A = []
    stime = time
    ptime = time
    ltime = time
    atime = time
    while stime!=datetime.now().date():
        stime += timezone.timedelta(days=1)
        data1 = fors(s.filter(date=stime).filter(status='Поступило'))
        data2 = fors(s.filter(date=stime).filter(status='В процессе'))
        data3 = fors(s.filter(date=stime).filter(status='Готово'))
        yCor1S.append(data1)
        yCor2S.append(data2)
        yCor3S.append(data3)
        xCorS.append(stime)
    while ptime!=datetime.now().date():
        ptime += timezone.timedelta(days=1)
        data1 = fors(p.filter(date=ptime).filter(status='Поступило'))
        data2 = fors(p.filter(date=ptime).filter(status='В процессе'))
        data3 = fors(p.filter(date=ptime).filter(status='Готово'))
        yCor1P.append(data1)
        yCor2P.append(data2)
        yCor3P.append(data3)
        xCorP.append(ptime)
    while ltime!=datetime.now().date():
        ltime += timezone.timedelta(days=1)
        data1 = fors(l.filter(date=ltime).filter(status='Поступило'))
        data2 = fors(l.filter(date=ltime).filter(status='В процессе'))
        data3 = fors(l.filter(date=ltime).filter(status='Готово'))
        yCor1L.append(data1)
        yCor2L.append(data2)
        yCor3L.append(data3)
        xCorL.append(ltime)
    while atime!=datetime.now().date():
        atime += timezone.timedelta(days=1)
        data1 = a.filter(date=atime).filter(status='Поступило').count()
        data2 = a.filter(date=atime).filter(status='В процессе').count()
        data3 = a.filter(date=atime).filter(status='Готово').count()
        yCor1A.append(data1)
        yCor2A.append(data2)
        yCor3A.append(data3)
        xCorA.append(atime)

    return render(request, 'statistics.html', {'day':day,
        's':(s1+s2+s3), 's1':s1, 's2':s2, 's3':s3,
        'p':(p1+p2+p3), 'p1':p1, 'p2':p2, 'p3':p3,
        'l':(l1+l2+l3), 'l1':l1, 'l2':l2, 'l3':l3,
        'a':len(a), 'a1':a1, 'a2':a2, 'a3':a3,
        'xCorS':xCorS, 'yCor1S':yCor1S, 'yCor2S':yCor2S, 'yCor3S':yCor3S,
        'xCorP': xCorP, 'yCor1P': yCor1P, 'yCor2P': yCor2P, 'yCor3P': yCor3P,
        'xCorL': xCorL, 'yCor1L': yCor1L, 'yCor2L': yCor2L, 'yCor3L': yCor3L,
        'xCorA': xCorA, 'yCor1A': yCor1A, 'yCor2A': yCor2A, 'yCor3A': yCor3A,
})

def fors(data):
    zero = 0
    for i in data:
        a = i.countSamples
        zero += a
    return zero

@login_required(redirect_field_name='login')
def table(request):
    time = timezone.now()
    day = time.day
    month = time.month
    year = time.year
    s = Selection.objects.all().filter(date = dt.date(year, month, day))
    s1 = fors(s.filter(status="Поступило"))
    s2 = fors(s.filter(status="В процессе"))
    s3 = fors(s.filter(status="Готово"))
    p = Preparation.objects.all().filter(date = dt.date(year, month, day))
    p1 = fors(p.filter(status="Поступило"))
    p2 = fors(p.filter(status="В процессе"))
    p3 = fors(p.filter(status="Готово"))
    l = Laboratory.objects.all().filter(date = dt.date(year, month, day))
    l1 = fors(l.filter(status="Поступило"))
    l2 = fors(l.filter(status="В процессе"))
    l3 = fors(l.filter(status="Готово"))
    a = Agrohym.objects.all().filter(date = dt.date(year, month, day))
    a1 = a.filter(status="Поступило").count
    a2 = a.filter(status="В процессе").count
    a3 = a.filter(status="Готово").count
    return render(request, 'table.html',{
        'time':time,
        's':(s1+s2+s3), 's1':s1, 's2':s2, 's3':s3,
        'p':(p1+p2+p3), 'p1':p1, 'p2':p2, 'p3':p3,
        'l':(l1+l2+l3), 'l1':l1, 'l2':l2, 'l3':l3,
        'a':len(a), 'a1':a1, 'a2':a2, 'a3':a3,
    })

@login_required(redirect_field_name='login')
def general(request):
    querySet = []
    s = Selection.objects.all()
    s1 = fors(s.filter(status="Поступило"))
    s2 = fors(s.filter(status="В процессе"))
    s3 = fors(s.filter(status="Готово"))
    p = Preparation.objects.all()
    p1 = fors(p.filter(status="Поступило"))
    p2 = fors(p.filter(status="В процессе"))
    p3 = fors(p.filter(status="Готово"))
    l = Laboratory.objects.all()
    l1 = fors(l.filter(status="Поступило"))
    l2 = fors(l.filter(status="В процессе"))
    l3 = fors(l.filter(status="Готово"))
    a = Agrohym.objects.all()
    a1 = a.filter(status="Поступило").count
    a2 = a.filter(status="В процессе").count
    a3 = a.filter(status="Готово").count
    querySet.append(s)
    querySet.append(p)
    querySet.append(l)
    querySet.append(a)
    final_set = list(chain(*querySet))
    final_set.sort(key=lambda x: x.nowTime, reverse=True)

    return render(request, 'general.html',{
        's':(s1+s2+s3), 's1':s1, 's2':s2, 's3':s3,
        'p':(p1+p2+p3), 'p1':p1, 'p2':p2, 'p3':p3,
        'l':(l1+l2+l3), 'l1':l1, 'l2':l2, 'l3':l3,
        'a':len(a), 'a1':a1, 'a2':a2, 'a3':a3,
        'final':final_set[:5],
    })

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Почвоотбор'])
def addSelection(request):
    if request.method == "POST":
        form = SelectionForm(request.POST)
        form.save(commit=False)
        #form.nowTime = timezone.now()
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user, "Добавлено в почвоотбор {0} проб({2}) из {1}".format(data['countSamples'],
                                                                                                 Samples.objects.get(pk=data['samples']),
                                                                                                 data['status']))
            parent = Selection.objects.last()
            if request.POST["status"] == "Готово":
                client = Client.objects.get(pk=data['nameClient'])
                samples = Samples.objects.get(pk=data['samples'])
                Preparation.objects.create(nameClient = client, countSamples=data['countSamples'],
                                           samples = samples, date = data['date'], parent = parent,
                                           status = "Поступило",
                                           )
            return redirect('selection')

def number_gte(model, data, count=0):
    pkPrep = data['selfParent']
    prep = model.get(pk=pkPrep)
    zero = 0
    for i in prep.selfChildren.all():
        zero += i.countSamples
    zero += int(data['countSamples'])
    zero -= count
    if zero > prep.countSamples:
        return True
    return False

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Пробоподготовка'])
def addPreparation(request):
    if request.method == "POST":
        form = PreparationForm(request.POST)

        #form.nowTime = timezone.now()
        if number_gte(Preparation.objects.all(), request.POST):
            return HttpResponse("Это число больше положенноог")
        if form.is_valid():
            form.save()
            sP = request.POST["selfParent"]
            p = Preparation.objects.get(pk = sP)
            smpl = Samples.objects.get(pk=p.samples.id)
            parent = Preparation.objects.last()
            data = request.POST
            writeUserActivity(request.user,
                              "Добавлено в пробоподготовку {0} проб({2}) из {1}".format(data['countSamples'],
                                                                                        smpl,
                                                                                        data['status']))
            if request.POST["status"] == "Готово":
                client = Client.objects.get(pk=data['nameClient'])

                Laboratory.objects.create(nameClient = client, countSamples=data['countSamples'],
                                         samples = smpl,
                                           date = data['date'], parent = parent,
                                           status = "Поступило",
                                           )
            return redirect('preparation')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def addLaboratory(request):
    if request.method == "POST":
        form = LaboratoryForm(request.POST)
        form.save(commit = False)
        #form.nowTime = timezone.now()
        if number_gte(Laboratory.objects.all(), request.POST):
            return HttpResponse("Это число больше положенного")
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user,
                              "Добавлено в лабораторию {0} проб({2}) из {1}".format(data['countSamples'],
                                                                                        Laboratory.objects.get(pk=data['selfParent']).samples,
                                                                                        data['status']))
            return redirect('laboratory')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Агрохим'])
def addAgrohym(request):
    if request.method == "POST":
        form = AgrohymForm(request.POST)
        form.save(commit = False)
        #form.nowTime = timezone.now()
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user,"Добавлено в агрохимию {0} проб({2}) из {1}".format(data['countSamples'], Samples.objects.get(pk=data['samples']), data['status']))
            return redirect('agrohym')



@login_required(redirect_field_name='login')
def selection(request):
    clients = Client.objects.all()
    samples = Samples.objects.all()
    title = 'Почвоотбор'
    action = "addSelection"
    delete = 'deleteSelection'
    update = 'selection'
    hasGroup = False
    for i in list(request.user.groups.all()):
        if str(i) == title or str(i) == 'Админ':
            hasGroup = True
    info = Selection.objects.all().order_by('-pk')

    paginator = Paginator(info, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    client = clients.first()
    context = {'title': title, 'info': data, 'action': action, 'delete': delete,'update':update, 'hasGroup': hasGroup, 'pg': pg, 'clients':clients, 'client':client, 'samples':samples}
    return render(request, 'index.html', context=context)

@login_required(redirect_field_name='login')
def preparation(request):

    samples = Samples.objects.all()
    clients = Client.objects.all()
    title = 'Пробоподготовка'
    action = "addPreparation"
    delete = 'deletePreparation'
    update = 'preparation'
    hasGroup = False

    for i in list(request.user.groups.all()):
        if str(i) == title or str(i) == 'Админ':
            hasGroup = True
    info = Preparation.objects.all().order_by('-pk')
    selfParents = info.exclude(parent=None)
    if selfParents.count == 0:
        selfParents = True
    #for i in selfParents:
    #    print(i.parent.countSamples)
    paginator = Paginator(info, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    client = clients.first()
    selfParent = selfParents.filter(nameClient=client)
    context = {'title': title, 'info': data, 'action': action, 'delete': delete,'update':update, 'hasGroup': hasGroup,
               'pg': pg, 'clients':clients, 'client':client, 'samples':samples, 'selfParents':selfParents, 'selfParent':selfParent}
    return render(request, 'index.html', context=context)

@login_required(redirect_field_name='login')
def laboratory(request):

    samples = Samples.objects.all()
    clients = Client.objects.all()
    title = 'Лаборатория'
    action = "addLaboratory"
    delete = 'deleteLaboratory'
    update = 'laboratory'
    hasGroup = False
    for i in list(request.user.groups.all()):
        if str(i) == title or str(i) == 'Админ':
            hasGroup = True
    info = Laboratory.objects.all().order_by('-pk')
    selfParents = info.exclude(parent=None)
    if selfParents.count == 0:
        selfParents = True
    paginator = Paginator(info, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    client = clients.first()
    selfParent = selfParents.filter(nameClient = client)
    context = {'title': title, 'info': data, 'action': action, 'delete': delete,'update':update, 'hasGroup': hasGroup,
               'pg': pg, 'clients':clients, 'client':client, 'samples':samples, 'selfParents':selfParents, 'selfParent':selfParent}
    return render(request, 'index.html', context=context)


@login_required(redirect_field_name='login')
def agrohym(request):
    fdate = timezone.now().date()
    clients = Client.objects.all()
    samples = Samples.objects.all()
    title = 'Агрохим'
    action = "addAgrohym"
    delete = 'deleteAgrohym'
    update = 'agrohym'
    hasGroup = False
    for i in list(request.user.groups.all()):
        if str(i) == title or str(i) == 'Админ':
            hasGroup = True
    info = Agrohym.objects.all().order_by('-pk').exclude(date__lt=fdate,status='Готово')
    paginator = Paginator(info, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    client = clients.first()
    context = {'title': title,'info': data, 'action': action, 'delete': delete,'update':update, 'hasGroup': hasGroup, 'pg': pg, 'clients':clients, 'client':client, 'samples':samples}
    return render(request, 'index.html', context=context)

@login_required(redirect_field_name='login')
def archiveAgroHym(request):
    fdate = timezone.now().date()

    title = 'Агрохим'
    delete = 'deleteArchiveAgrohym'
    update = 'agrohym'
    hasGroup = False
    for i in list(request.user.groups.all()):
        if str(i) == title:
            hasGroup = True
    info = Agrohym.objects.all().order_by('-pk').filter(date__lt=fdate)
    paginator = Paginator(info, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    title = "Архив агрохимии"
    context = {'title': title, 'info': data, 'delete': delete,'update':update, 'hasGroup': hasGroup, 'pg': pg}
    return render(request, 'archiveAH.html', context=context)



#@hasGroups(groups = ['Агрохим'])
#def updateSelection(request):
#    return redirect('selection')
@login_required(redirect_field_name='login')
@hasGroups(groups = ['Почвоотбор'])
def deleteSelection(request, pk):
    s = Selection.objects.get(pk=pk)
    writeUserActivity(request.user, "Удалена запись почвоотбора: {0}, {1} проб({2})".format(s.nameClient, s.countSamples, s.status))
    s.delete()
    return redirect('selection')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Пробоподготовка'])
def deletePreparation(request, pk):
    s = Preparation.objects.get(pk=pk)
    writeUserActivity(request.user, "Удалена запись пробоподготовки: {0}, {1} проб({2})".format(s.nameClient, s.countSamples, s.status))
    s.delete()
    return redirect('preparation')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def deleteLaboratory(request, pk):
    s = Laboratory.objects.get(pk=pk)
    writeUserActivity(request.user,"Удалена запись лаборатории: {0}, {1} проб({2})".format(s.nameClient, s.countSamples, s.status))
    s.delete()
    return redirect('laboratory')


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Агрохим'])
def deleteAgrohym(request, pk):
    s = Agrohym.objects.get(pk=pk)
    writeUserActivity(request.user,"Удалена запись агрохимии: {0}, {1} проб({2})".format(s.nameClient, s.countSamples, s.status))
    s.delete()
    return redirect('agrohym')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Агрохим'])
def deleteArchiveAgrohym(request, pk):
    s = Agrohym.objects.get(pk=pk)
    writeUserActivity(request.user,"Удалена запись агрохимии(архив): {0}, {1} проб({2})".format(s.nameClient, s.countSamples, s.status))
    s.delete()
    return redirect('archiveAgroHym')


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Почвоотбор'])
def detailSelection(request, pk):
    title = "Почвоотбор"
    update = 'updateSelection'
    s = Selection.objects.get(pk=pk)

    clients = Client.objects.all()
    client = s.nameClient
    samples = Samples.objects.filter(client=client)
    return render(request, 'detail.html', {'title':title, 's': s, 'update':update, 'samples':samples, 'clients':clients, 'client':str(client)})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Пробоподготовка'])
def detailPreparation(request, pk):
    title = "Пробоподготовка"
    update = 'updatePreparation'
    ss = Preparation.objects.all()
    s = ss.get(pk=pk)

    clients = Client.objects.all()
    client = s.nameClient
    samples = Samples.objects.filter(client=client)

    selfParents = ss.exclude(parent=None)
    selfParent = s.selfParent
    return render(request, 'detail.html', {'title':title, 's': s, 'update':update, 'samples':samples, 'clients':clients,'selfParents':selfParents,'selfParent':selfParent, 'client':str(client)})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def detailLaboratory(request, pk):
    title = "Лаборатория"
    update = 'updateLaboratory'
    ss = Laboratory.objects.all()
    s = ss.get(pk=pk)

    clients = Client.objects.all()
    client = s.nameClient
    samples = Samples.objects.filter(client=client)

    selfParents = ss.exclude(parent=None)
    selfParent = s.selfParent
    return render(request, 'detail.html', {'title':title, 's': s, 'update':update, 'samples':samples, 'clients':clients,'selfParents':selfParents,'selfParent':selfParent,  'client':str(client)})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Агрохим'])
def detailAgrohym(request, pk):
    title = "Агрохимия"
    update = 'updateAgrohym'
    s = Agrohym.objects.get(pk=pk)

    clients = Client.objects.all()
    client = s.nameClient
    samples = Samples.objects.filter(client = client)
    return render(request, 'detail.html', {'title':title, 's': s, 'update':update, 'samples':samples, 'clients':clients, 'client':str(client)})






@login_required(redirect_field_name='login')
@hasGroups(groups = ['Почвоотбор'])
def updateSelection(request, pk):
    if request.method == "POST":
        s = Selection.objects.get(pk=pk)
        form = SelectionForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            parent = Selection.objects.last()
            if request.POST["status"] == "Готово":
                data = request.POST
                client = Client.objects.get(pk=data['nameClient'])
                samples = Samples.objects.get(pk=data['samples'])
                Preparation.objects.create(nameClient=client, countSamples=data['countSamples'],
                                          samples=samples, date=data['date'], parent=parent,
                                          status="Поступило",
                                          )
            return redirect('selection')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Пробоподготовка'])
def updatePreparation(request, pk):
    if request.method == "POST":
        s = Preparation.objects.get(pk=pk)
        form = PreparationForm(request.POST, instance=s)
        if number_gte(Preparation.objects.all(), request.POST, count = s.countSamples):
            return HttpResponse("Это число больше положенного")
        if form.is_valid():
            form.save()
            parent = Preparation.objects.last()
            if request.POST["status"] == "Готово" and s.status != "Готово":
                data = request.POST
                client = Client.objects.get(pk=data['nameClient'])
                samples = Samples.objects.get(pk=data['samples'])
                Laboratory.objects.create(nameClient=client, countSamples=data['countSamples'],
                                          samples=samples, date=data['date'], parent=parent,
                                          status="Поступило",
                                          )
            return redirect('preparation')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def updateLaboratory(request, pk):
    if request.method == "POST":
        s = Laboratory.objects.get(pk=pk)
        form = LaboratoryForm(request.POST, instance=s)
        if number_gte(Laboratory.objects.all(), request.POST, count = s.countSamples):
            return HttpResponse("Это число больше положенного")
        if form.is_valid():
            form.save()
            return redirect('laboratory')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Агрохим'])
def updateAgrohym(request, pk):
    if request.method == "POST":
        s = Agrohym.objects.get(pk=pk)
        form = AgrohymForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return redirect('agrohym')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def signup(request):
    groups = Group.objects.all()
    return render(request, 'registration/signup.html',{"groups":groups})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def addUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        error = False
        error2 = False
        alls = User.objects.all()
        for i in alls:
            if i.username == request.POST['username']:
                error2 = True
                groups = Group.objects.all()
                return render(request,'registration/signup.html',{'error2':error2,'groups':groups})
        if request.POST['password1'] != request.POST['password2']:
            groups = Group.objects.all()
            error = True
            return render(request,'registration/signup.html',{'error':error,'groups':groups})
        print(form)
        if form.is_valid():#Если форма заполнена правильно
            form.save()#Создаем пользователя
            data = request.POST
            writeUserActivity(request.user, "Добавлен пользователь {0}({1} {2})".format(data['username'], data['first_name'], data['last_name']))
            username = form.cleaned_data.get('username')#с именем
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            groups = form.cleaned_data.get('groups')
            user = authenticate(username=username, password=password)
            user.firstname = first_name
            user.lastname = last_name
            for i in groups:
                user.groups.add(i)
            user.save()
        return redirect('general')



@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def listUser(request):
    dic = {}
    info = User.objects.all()

    for i in info:
        groups = i.groups.all()
        lst = []
        for j in groups:
            lst.append(j.name)
        dic[str(i.username),str(i.pk)] = lst
    return render(request, 'listUser.html', {'info':dic})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def clients(request):
    title = 'Клиенты'
    delete = 'deleteClient'
    update = 'detailClient'
    addClient = 'addClient'
    clients = Client.objects.all()
    hasGroup = True
    return render(request, 'clients.html', {'title': title, 'update': update, 'delete': delete, 'clients': clients,
                                            'addClient':addClient,'hasGroup':hasGroup})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def addClient(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user, "Добавлен клиент {0} ({1} проб) ".format(data['name'], data['countSamples']))
        return redirect('clients')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def detailClient(request, pk):
    update = 'updateClient'
    client = Client.objects.get(pk=pk)
    clientSamples = Samples.objects.filter(client = client)
    ostatok = client.countSamples
    zero = []
    for i in clientSamples:
        ostatok -= i.count
        for j in i.elements.all():
            zero.append(j.name)
    elCount = len(set(zero))
    return render(request, 'detailClient.html',{'update':update,
                                                'client':client,
                                                'clientSamples':clientSamples,
                                                'ostatok':ostatok,
                                                'elCount':elCount})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def deleteClient(request, pk):
    client = Client.objects.get(pk=pk)
    writeUserActivity(request.user, "Удален клиент {0}({1} проб)".format(client.name, client.countSamples))
    client.delete()
    return redirect('clients')


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def updateClient(request, pk):
    update = 'updateClient'
    if request.method == "POST":
        client = Client.objects.get(pk=pk)
        count = int(request.POST['countSamples'])
        clientSamples = Samples.objects.filter(client=client)
        for i in clientSamples:
            count-=i.count
        if count<0:
            errorZero = True
            return render(request, 'detailClient.html', {'update': update,
                                                         'client': client,
                                                         'clientSamples': clientSamples,
                                                         'errorZero':errorZero})
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return render(request, 'detailClient.html', {'update': update,
                                                         'client': client,
                                                         'clientSamples': clientSamples})
        return redirect('clients')

    elif request.method == "GET":
        client = Client.objects.get(pk=pk)
        return render(request, 'detailClient.html', {'update': update,
                                                     'client': client,})
@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def clientsCorms(request):
    title = 'Клиенты корма'
    delete = 'deleteClientCorms'
    update = 'detailClientCorms'
    addClient = 'addClientCorms'
    clients = ClientCorm.objects.all()
    hasGroup = True
    return render(request, 'clientsCorms.html', {'title': title, 'update': update, 'delete': delete, 'clients': clients,
                                            'addClient': addClient, 'hasGroup': hasGroup})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def addClientCorms(request):
    if request.method == "POST":
        form = ClientCormForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user, "Добавлен клиент {0} для корма ".format(data['name']))
        return redirect('clientsCorms')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def detailClientCorms(request, pk):
    update = 'updateClientCorms'
    client = ClientCorm.objects.get(pk=pk)
    return render(request, 'detailClientCorms.html',{'update':update,
                                                'client':client,})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def deleteClientCorms(request, pk):
    client = ClientCorm.objects.get(pk=pk)
    writeUserActivity(request.user, "Удален клиент {0} для корма".format(client.name))
    client.delete()
    return redirect('clientsCorms')


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def updateClientCorms(request, pk):
    update = 'updateClientCorms'
    if request.method == "POST":
        client = ClientCorm.objects.get(pk=pk)
        form = ClientCormForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clientsCorms')

        return render(request, 'detailClientCorms.html', {'update': update,
                                                     'client': client,})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def samples(request):
    samples = Samples.objects.all()
    clients = Client.objects.all()
    elements = elementsName.objects.all()
    for i in clients:
        counter = i.countSamples
        smpl = samples.filter(client = i)
        for i in smpl:
            counter-=i.count
        if counter>0:
            dt = i.date
            print(dt)
            return render(request, 'samples.html', {'samples':samples, 'clients':clients, 'dt':dt, 'elements':elements})
    return render(request, 'samples.html', {'samples': samples, 'clients': clients, 'elements': elements})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def addSample(request):
    if request.method == "POST":
        client = request.POST['client']
        client = Client.objects.get(pk=client)
        count = int(request.POST['count'])
        clientSamples = Samples.objects.filter(client=client)
        zero = 0
        for i in clientSamples:
            zero += i.count
        if (zero+count)>client.countSamples:
            samples = Samples.objects.all()
            clients = Client.objects.all()
            elements = elementsName.objects.all()
            errorMax = True
            for i in clients:
                counter = i.countSamples
                smpl = samples.filter(client=i)
                for i in smpl:
                    counter -= i.count
                if counter > 0:
                    dt = i.date
                    print(dt)
                    return render(request, 'samples.html',
                                  {'samples': samples, 'clients': clients, 'dt': dt, 'errorMax':errorMax,'elements': elements})
            return render(request, 'samples.html', {'samples': samples, 'clients': clients, 'errorMax':errorMax, 'elements': elements})
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user, "Добавлен вид пробы {0}({1} проб, {2} эл.)".format(data['client'],data['count'],len(form.cleaned_data.get('elements'))))
        return redirect('samples')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def updateSample(request, pk):
    if request.method == "POST":
        s = Samples.objects.get(pk=pk)
        form = SampleForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
    return redirect('samples')


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def deleteElement(request, pk):
    e = elementsName.objects.get(pk=pk)
    writeUserActivity(request.user, "Удален элемент {0}".format(e.name))
    e.delete()
    return redirect("listElement")


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def deleteSample(request, pk):
    s = Samples.objects.get(pk=pk)
    writeUserActivity(request.user, "Удалена вид пробы {0}({1} проб, {2} эл.)".format(s.client, s.count, s.elements.all().count()))
    s.delete()

    return redirect('samples')


def full(list,number):
    zero = 0
    for i in list:
        if isinstance(i[1],datetime):
            zero += i[0]
        elif type(i[1]) == str:
            zero+=int(i[1].replace(' | ',' ').split()[0])
        else:
            zero+=i[1]
    if zero<number:
        return True
    return False

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def newTable(request):
    s = Selection.objects.filter(status="                 ")
    p = Preparation.objects.all()
    l = Laboratory.objects.all()
    a = Agrohym.objects.all()
    clients = Client.objects.all()
    dic1 = {}
    icount=0
    for i1 in clients:
        print(i1.name)
        lst1 = []
        dic2 = {}
        icount+=1
        jcount=0
        for j1 in i1.samples.all():
            #print(' s ',j1.count, end=" | ")
            #print(len(j1.elements.all()))
            txt = ""
            for i in j1.elements.all():
                txt+=i.name+", "
            txt = txt[:-2]
            lst1.append(str(j1.count)+str(j1.elements.all().count))
            lst2 = []
            dic3 = {}
            jcount+=1
            kcount=0
            for k1 in j1.selection.filter(status="Готово"):
                print('   sel ',k1.countSamples)
                lst2.append(k1.countSamples)
                lst3 = []
                dic4 = {}
                kcount+=1
                lcount=0
                for l1 in k1.children.all():
                    for l2 in l1.selfChildren.all().filter(status="Готово"):
                        print('    pre  ', l2.countSamples)
                        lst3.append(l2.countSamples)
                        lst4 = []
                        lcount+=1
                        pcount=0
                        for p1 in l2.children.all():
                            for p2 in p1.selfChildren.all().filter(status="Готово"):
                                print('     lab   ', p2.countSamples)
                                lst4.append((p2.countSamples, p2.nowTime))
                                pcount+=1
                            dic4[(lcount,l2.countSamples,l2.nowTime,full(lst4,l2.countSamples))] = lst4
                    dic3[(kcount,k1.countSamples,k1.nowTime,full(dic4,k1.countSamples))] = dic4
            dic2[(jcount,str(j1.count)+" | "+str(j1.elements.all().count()),txt,full(dic3,j1.count))] = dic3
        dic1[(icount,i1.name+" | "+str(i1.countSamples),full(dic2,i1.countSamples),i1.date)] = dic2
    #print(dic1)


    return render(request, 'newTable.html', {"clients":clients,
                                             "dic1":dic1,
                                              's':s,'p':p,'l':l,'a':a,
                                              'detail':False})



@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def listElement(request):
    elements = elementsName.objects.all()
    return render(request,'elements.html',{"elements":elements})


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def addElement(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user, "Добавлен элемент {0}".format(data['name']))
        else:
            print(form.errors)
    return redirect("listElement")


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def updateElement(request):
    if request.method == "POST":
        s = elementsName.objects.get(pk=int(request.POST['oldName']))
        form = ElementForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('listElement')


@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def deleteUser(request,pk):
    user = User.objects.get(pk=pk)
    writeUserActivity(request.user, "Удален пользователь {0}({1} {2})".format(user.username, user.first_name, user.last_name))
    user.delete()
    return redirect('listUser')

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Админ'])
def zhournal(request, pk):
    user = User.objects.get(pk = pk)
    activity = Activity.objects.filter(user=user).order_by('-time')
    paginator = Paginator(activity, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    return render(request, "zhournal.html", {'user':user,'pg':pg,'activity': data})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def corms(request):
    allCorms = Corms.objects.all()
    corms = allCorms.filter(parent=None).order_by("-pk")
    clients = ClientCorm.objects.all()
    parents = corms.filter(status="Поступило").filter(children=None)
    paginator = Paginator(corms, 20)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
        pg = page
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
        pg = 1
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
        pg = 1
    try:
        selfParents = clients.first().corms.filter(status="Поступило").filter(children=None)
    except:
        selfParents = None
    return render(request, 'corms.html', {'allCorms':allCorms, "corms":data, 'clients':clients, 'parents':parents,'selfParents':selfParents, 'pg':pg})

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def addCorms(request):
    if request.method == "POST":
        form = CormsForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST
            writeUserActivity(request.user, "Добавлен корм {0} | {1} | {2}".format(ClientCorm.objects.get(pk=data['client']), data['count'], data['status']))
        else:
            print(form.errors)
        return redirect("corms")

@login_required(redirect_field_name='login')
@hasGroups(groups = ['Лаборатория'])
def deleteCorms(request, pk):
    corm = Corms.objects.get(pk=pk)
    corm.delete()
    return redirect("corms")


