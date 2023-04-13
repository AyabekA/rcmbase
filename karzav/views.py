from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
# from .filters import FilterKarzav
from django.views import View
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView
from karzav.models import karzav_card
from karzav.serializers import KarzavSerializers
from karzav.pagination import StandardResultsSetPagination
from django.db.models import Q


def karzav_list(request):
    return render(request, 'karzav/karzav_list.html', {})


class KarzavListing(ListAPIView):
    # установить класс нумерации страниц и сериализатора
    pagination_class = StandardResultsSetPagination
    serializer_class = KarzavSerializers

    def get_queryset(self):
        # фильтровать набор запросов на основе примененных фильтров
        queryList = karzav_card.objects.all()
        oblast = self.request.query_params.get('oblast', None)
        raion = self.request.query_params.get('raion', None)
        status = self.request.query_params.get('status', None)
        nedrouser = self.request.query_params.get('nedrouser', None)
        sort_by = self.request.query_params.get('sort_by', None)
        search = self.request.query_params.get('search', None)

        if search:
            # print('search = ', search)
            queryList = queryList.filter(
                Q(nedrouser__icontains=search) |
                Q(mestorojdenie__icontains=search) |
                Q(material__icontains=search)
            )

        if oblast:
            queryList = queryList.filter(oblast=oblast)
        if raion:
            queryList = queryList.filter(raion=raion)
        if status:
            queryList = queryList.filter(status=status)
        if nedrouser:
            queryList = queryList.filter(nedrouser=nedrouser)

        if sort_by == "by_nedrouser":
            queryList = queryList.order_by("nedrouser")
        elif sort_by == "by_mestorojdenie":
            queryList = queryList.order_by("mestorojdenie")
        elif sort_by == "by_material":
            queryList = queryList.order_by("material")

        return queryList


def getOblasti(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        oblasti = karzav_card.objects.filter().order_by('oblast').values_list('oblast').distinct()
        # print("oblasti = ", oblasti)
        oblasti = [i[0] for i in list(oblasti)]
        data = {
            "oblasti": oblasti,
        }
        return JsonResponse(data, status=200)


def getRaiony(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        oblast = request.GET.get('oblast')
        print("oblast --- ", oblast)
        raiony = karzav_card.objects.filter(oblast=oblast).order_by('raion').values_list('raion').distinct()
        # raiony = karzav_card.objects.filter().order_by('raion').values_list('raion').distinct()
        print("raiony = ", raiony)
        raiony = [i[0] for i in list(raiony)]
        data = {
            "raiony": raiony,
        }
        return JsonResponse(data, status=200)


def getStatus(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        statusy = karzav_card.objects.filter().order_by('status').values_list('status').distinct()
        # print("statusy = ", statusy)
        statusy = [i[0] for i in list(statusy)]
        data = {
            "statusy": statusy,
        }
        return JsonResponse(data, status=200)


def getNedrousers(request):
    # получить все nedrousers из БД, за исключением нулевых и пустых значений
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        nedrousers = karzav_card.objects.filter().order_by('nedrouser').values_list('nedrouser').distinct()
        # print("nedrousers = ", nedrousers)
        nedrousers = [i[0] for i in list(nedrousers)]
        data = {
            "nedrousers": nedrousers,
        }
        return JsonResponse(data, status=200)


def karzav_cardv(request):
    nedrousers = karzav_card.objects.values_list('nedrouser', flat=True)
    # print('nedrousers = ', nedrousers)
    materials = karzav_card.objects.values_list('material', flat=True)
    # print('materials = ', materials)

    link_kzcv = request.COOKIES.get('link_kzcv')
    # print("link_kzcv = ", link_kzcv)

    # if link_kzcv in nedrousers:
    karzavs = karzav_card.objects.filter(nedrouser=link_kzcv)
    context = {
        'karzavs': karzavs,
    }
    return render(request, 'karzav/karzav_card.html', context)


def fizmeh_harv(request):
    # materials = karzav_card.objects.values_list('material', flat=True)
    # print('materials = ', materials)

    link_fmhv = request.COOKIES.get('link_fmhv')
    print("link_fmhv = ", link_fmhv)

    # if link_fmhv and link_fmhv in materials:
    karzavs = karzav_card.objects.filter(material=link_fmhv)
    filename = karzav_card.objects.filter(material=link_fmhv).values_list('files', flat=True)[0]

    pdffile = '/static/files/' + filename

    images = karzavs.first().images
    image_list = []
    if images is not None:
        image_list = images.split(',') if ',' in images else [images]
        for i in range(len(image_list)):
            image = '/static/files/' + image_list[i]
            image_list[i] = image

    context = {
        'karzavs': karzavs,
        'pdffile': pdffile,
        'image_list': image_list,
    }
    return render(request, 'karzav/fizmeh_har.html', context)


def fizmeh_harvv(request):
    # materials = karzav_card.objects.values_list('material', flat=True)
    # print('materials = ', materials)
    link_fmhvv = request.COOKIES.get('link_fmhvv')
    # print("link_fmhvv1 = ", link_fmhvv)

    # if link_fmhvv and link_fmhvv in materials:
    karzavs = karzav_card.objects.filter(material=link_fmhvv)
    filename = karzav_card.objects.filter(material=link_fmhvv).values_list('files', flat=True)[0]

    pdffile = '/static/files/' + filename
    
    images = karzavs.first().images
    image_list = []
    if images is not None:
        image_list = images.split(',') if ',' in images else [images]
        for i in range(len(image_list)):
            image = '/static/files/' + image_list[i]
            image_list[i] = image

    context = {
        'karzavs': karzavs,
        'pdffile': pdffile,
        'image_list': image_list,
    }
    return render(request, 'karzav/fizmeh_har.html', context)


def karzav_delete(request):
    if request.method == 'POST':
        nedrouser = request.POST.get('nedrouser')
        try:
            karzav_card1 = karzav_card.objects.filter(nedrouser=nedrouser)
            karzav_card1.delete()
            return redirect('polls:profile')
        except karzav_card.DoesNotExist:
            return render(request, 'karzav/karzav_delete.html', {'error': 'Данный объект не существует'})
    return render(request, 'karzav/karzav_delete.html')


def karzav_material_delete(request):
    if request.method == 'POST':
        nedrouser = request.POST.get('nedrouser')
        mestorojdenie = request.POST.get('mestorojdenie')
        material = request.POST.get('material')
        try:
            karzav_card1 = karzav_card.objects.filter(nedrouser=nedrouser, mestorojdenie=mestorojdenie,
                                                      material=material)
            karzav_card1.delete()
            return redirect('polls:profile')
        except karzav_card.DoesNotExist:
            return render(request, 'karzav/karzav_material_delete.html', {'error': 'Данный объект не существует'})
    return render(request, 'karzav/karzav_material_delete.html')
