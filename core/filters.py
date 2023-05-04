import django_filters
from core import models


class Appeal(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='declarer__name', lookup_expr='icontains', label='Поиск по Фио')

    class Meta:
        model = models.Appeal
        fields = ('declarer', 'services__cod', 'status')


class Declarer(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')
    age = django_filters.DateFilter(field_name="age", lookup_expr='exact')

    class Meta:
        model = models.Declarer
        fields = ('name', 'phone',)
