import django_filters as filters
from karzav.models import karzav_card


class FilterKarzav(filters.FilterSet):
    all_fields = filters.CharFilter(label='Поиск')
    #comp_name = filters.CharFilter(label='Компания')
    #vn_name = filters.CharFilter(label='Вид нидропользования')
    #status = filters.CharFilter(label='Статус')
    #oblast = filters.ModelMultipleChoiceFilter(label='Область', queryset= karzav_card.objects.filter().values_list('oblast').distinct())
    #raion = filters.CharFilter(label='Район')

    class Meta:
        model = karzav_card
        fields = ['mst_name', 'comp_name', 'vn_name', 'status', 'oblast', 'raion',]
