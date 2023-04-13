from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.serializers import serialize
# from .filters import FilterKarzav
from django.views import View
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView
from invtech.models import invtech_info
from invtech.serializers import InvtechSerializers
from invtech.pagination import StandardResultsSetPagination
from django.db.models import Q
from django.http import HttpResponse
import os
from django.conf import settings


def invtech_list(request):
    return render(request, "invtech/invtech_list.html", {})


class InvtechListing(ListAPIView):
    # установить класс нумерации страниц и сериализатора
    pagination_class = StandardResultsSetPagination
    serializer_class = InvtechSerializers

    def get_queryset(self):
        # фильтровать набор запросов на основе примененных фильтров
        queryList = invtech_info.objects.all()

        invtech = self.request.query_params.get('invtech', None)
        status = self.request.query_params.get('status', None)
        usingarea = self.request.query_params.get('usingarea', None)
        prov_name = self.request.query_params.get('prov_name', None)
        prod_name = self.request.query_params.get('prod_name', None)

        sort_by = self.request.query_params.get('sort_by', None)
        search = self.request.query_params.get('search', None)

        if search:
            queryList = queryList.filter(
                Q(invtech__icontains=search) |
                Q(usingarea__icontains=search) |
                Q(prov_name__icontains=search) |
                Q(prod_name__icontains=search)
            )

        if invtech:
            queryList = queryList.filter(invtech=invtech)
        if status:
            queryList = queryList.filter(status=status)
        if usingarea:
            queryList = queryList.filter(usingarea=usingarea)
        if prov_name:
            queryList = queryList.filter(prov_name=prov_name)
        if prod_name:
            queryList = queryList.filter(prod_name=prod_name)

        if sort_by == "by_invtech":
            queryList = queryList.order_by("invtech")
        elif sort_by == "by_usingarea":
            queryList = queryList.order_by("usingarea")
        elif sort_by == "by_providers":
            queryList = queryList.order_by("prov_name")
        elif sort_by == "by_producers":
            queryList = queryList.order_by("prod_name")

        return queryList


def getTechnologies(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        technologies = invtech_info.objects.filter().order_by('invtech').values_list('invtech').distinct()
        technologies = [i[0] for i in list(technologies)]
        data = {
            "technologies": technologies,
        }
        return JsonResponse(data, status=200)


def getStatus(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        statusy = invtech_info.objects.filter().order_by('status').values_list('status').distinct()
        statusy = [i[0] for i in list(statusy)]
        data = {
            "statusy": statusy,
        }
        return JsonResponse(data, status=200)


def getUsingareas(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        usingareas = invtech_info.objects.filter().order_by('usingarea').values_list('usingarea').distinct()
        usingareas = [i[0] for i in list(usingareas)]
        data = {
            "usingareas": usingareas,
        }
        return JsonResponse(data, status=200)


def getProviders(request):
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        providers = invtech_info.objects.filter().order_by('prov_name').values_list('prov_name').distinct()
        providers = [i[0] for i in list(providers)]
        data = {
            "providers": providers,
        }
        return JsonResponse(data, status=200)


def getProducers(request):
    # получить все producers из БД, за исключением нулевых и пустых значений
    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        producers = invtech_info.objects.filter().order_by('prod_name').values_list('prod_name').distinct()
        producers = [i[0] for i in list(producers)]
        data = {
            "producers": producers,
        }
        return JsonResponse(data, status=200)


def invtech_infov(request):
    # invtechs = invtech_info.objects.all()
    linkres2 = request.COOKIES.get('alink2')
    invtechs = invtech_info.objects.filter(invtech=linkres2)
    filename = invtech_info.objects.filter(invtech=linkres2).values_list('full_hars', flat=True)[0]
    itfile = invtech_info.objects.filter(invtech=linkres2).values_list('invtech', flat=True)[0]
    pdffile = '/static/files/invtech_files/' + itfile + '/' + filename
    #print(pdffile)
    images = invtechs.first().images
    image_list = []
    if images is not None:
        image_list = images.split(',') if ',' in images else [images]
        for i in range(len(image_list)):
            image = '/static/files/invtech_files/' + itfile + '/' + image_list[i]
            image_list[i] = image

    context = {
        'invtechs': invtechs,
        'image_list': image_list,
        'pdffile': pdffile,
    }
    return render(request, 'invtech/invtech_info.html', context)


def invtech_delete(request):
    if request.method == 'POST':
        invtech = request.POST.get('invtech')
        try:
            invtech_info1 = invtech_info.objects.filter(invtech=invtech)
            invtech_info1.delete()
            return redirect('polls:profile')
        except invtech_info.DoesNotExist:
            return render(request, 'invtech/invtech_delete.html', {'error': 'Данная инновационная технология не '
                                                                            'существует'})
    return render(request, 'invtech/invtech_delete.html')
