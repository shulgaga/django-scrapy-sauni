import django_filters
from .models import NewInfo, OldInfo, ISTOCHNIKI_CHOICES


class InfoFilter(django_filters.FilterSet):

    class Meta:
        model = NewInfo
        fields = ['city', 'name']


class UnsortedFilter(django_filters.FilterSet):
    istochnik = django_filters.ChoiceFilter(choices=ISTOCHNIKI_CHOICES)

    class Meta:
        model = OldInfo
        fields = ('city', 'name', 'istochnik', 'date')
