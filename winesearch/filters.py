import django_filters
from django.db.models import F
from winesearch.models import Country, Province, Region1, Region2, Variety, Wine, Winery, Taster, VarietyRegion1, VarietyRegion2, WineryVariety, WineTaster

# (1) field_name --> The name of the model field that is filtered against. If this argument is not provided,
# it defaults the filter's attribute name on the FilterSet class. Field names can traverse relationships
# by joining the related parts with the ORM lookup separator (__). e.g., a product's manufacturer__name.
# (2) label --> The label as it will appear in the HTML, analogous to a form field's label argument.  If a label is
# not provided, a verbose label will be generated based on the field field_name and the parts of the lookup_
# expr (see: FILTERS_VERBOSE_LOOKUPS).
# (3) lookup_expr --> The field lookup that should be performed in the filter call. Defaults to exact.
# The lookup_expr can contain transforms if the expression parts are joined by the ORM lookup separator (__).
# <e.g.> filter a datetime by its year part year__gt.

class WineFilter(django_filters.FilterSet):
    wine_name = django_filters.CharFilter(
        field_name='wine',
        label='Wine',
        lookup_expr='icontains'
    )
    # Adding wine(label), description, variety, region2, region1, province, and country:
    # winery = django_filters.ModelChoiceFilter(
    #     field_name='wine__winery__winery_name',
    #     label='Winery',
    #     queryset=Winery.objects.all(),
    #     lookup_expr='exact'
    # )

    # description = django_filters.CharFilter(
    #     field_name='description',
    #     label='Description',
    #     lookup_expr='icontains',
    # )
    #
    # variety = django_filters.ModelChoiceFilter(
    #     field_name='variety',
    #     label='Variety',
    #     lookup_expr='exact',
    # )
    #
    # sub_region = django_filters.ModelChoiceFilter(
    #     field_name='region2',
    #     label='Sub Region',
    #     lookup_expr='exact',
    # )
    country = django_filters.ModelChoiceFilter(
        field_name='country',
        label='Country',
        lookup_expr='exact',
        queryset=Country.objects.all()
    )

    province = django_filters.ModelChoiceFilter(
        field_name='province',
        label='Province',
        lookup_expr='exact',
        queryset=Province.objects.all()
    )

    region = django_filters.ModelChoiceFilter(
        field_name='region1',
        label='Region',
        lookup_expr='exact',
        queryset=Region1.objects.all()
    )

    price = django_filters.NumberFilter(
        field_name='price',
        label='Price',
        lookup_expr='exact'
    )

    # price2 = django_filters.RangeFilter(
    #     field_name='price',
    #     label='Price',
    #     lookup_expr='exact'
    #
    #
    #
    # )
    # p2 = Wine.objects.all().order_by( 'price' )
    #
    # # Range: Wines between 0 and 20 dollars
    # f = F( {'price_min': '0', 'price_max': '25'}, queryset=p2 )
    # f = F( {'price_min': '26', 'price_max': '50'}, queryset=p2 )
    # f = F( {'price_min': '51', 'price_max': '75'}, queryset=p2 )
    # f = F( {'price_min': '76', 'price_max': '100'}, queryset=p2 )
    # # Min-Only: Books costing more the 11€
    # f = F( {'price_min': '101'}, queryset=p2 )


    class Meta:
        model = Wine
        #form = SearchForm
        #fields [] is required, even if empty.
        fields = []




class WineryFilter(django_filters.FilterSet):
    winery_name = django_filters.CharFilter(
        field_name='winery',
        label='Winery',
        lookup_expr='icontains'
    )

