import django_filters
from core import models


class Appeal(django_filters.FilterSet):

    class Meta:
        model = models.Appeal
        fields = '__all__'


class Declarer(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')

    class Meta:
        model = models.Declarer
        fields = ('name', 'phone',)
