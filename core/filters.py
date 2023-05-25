import django_filters
from django.db.models import Q

from core import models


class Appeal(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='declarer__name', label='Поиск по Фио', lookup_expr='icontains')

    class Meta:
        model = models.Appeal
        fields = ('services__cod', 'status')


class Declarer(django_filters.FilterSet):
    name = django_filters.CharFilter(method='name_or_lastname')
    phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')
    age = django_filters.DateFilter(field_name="age", lookup_expr='iexact')

    class Meta:
        model = models.Declarer
        fields = ()

    def name_or_lastname(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(last_name__icontains=value))