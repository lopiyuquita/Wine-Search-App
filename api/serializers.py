from winesearch.models import Country, Province, Region1, Region2, \
    Variety, Wine, Winery, Taster, VarietyRegion1, VarietyRegion2, WineTaster, WineryVariety
from rest_framework import response, serializers, status


class CountrySerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Country
        fields = ('country_id', 'country_name')

# Province has a ForeignKey, country:
class ProvinceSerializer ( serializers.ModelSerializer ):
    country = CountrySerializer ( many=False, read_only=True )
    country_id = serializers.PrimaryKeyRelatedField (
        allow_null=False,
        many=False,
        write_only=True,
        queryset=Country.objects.all (),
        source='country'
    )

    class Meta:
        model = Province
        fields = ('province_id',
                  'province_name',
                  'country_id',
                  'country'
                  )

# Region1 has a ForeignKey, province
class Region1Serializer ( serializers.ModelSerializer ):
    province = ProvinceSerializer ( many=False, read_only=True )
    province_id = serializers.PrimaryKeyRelatedField (
        allow_null=False,
        many=False,
        write_only=True,
        queryset=Province.objects.all (),
        source='province'
    )
    class Meta:
        model = Region1
        fields = ('region1_id',
                  'region1_name',
                  'province_id',
                  'province'
                  )

# Region2 has a ForeignKey, region1:
class Region2Serializer ( serializers.ModelSerializer ):
    region1 = Region1Serializer ( many=False, read_only=True )
    region1_id = serializers.PrimaryKeyRelatedField (
        allow_null=False,
        many=False,
        write_only=True,
        queryset=Region1.objects.all (),
        source='region1'
    )
    class Meta:
        model = Region2
        fields = ('region2_id',
                  'region2_name',
                  'region1',
                  'region1_id')

class VarietyRegion1Serializer(serializers.ModelSerializer):
    variety_id = serializers.ReadOnlyField ( source='variety.variety_id' )
    region1_id = serializers.ReadOnlyField ( source='region1.region1_id' )
    class Meta:
        model = VarietyRegion1
        fields = ('variety_id',
                  'region1_id'
                  )

class VarietyRegion2Serializer(serializers.ModelSerializer):
    variety_id = serializers.ReadOnlyField(source='variety.variety_id')
    region2_id = serializers.ReadOnlyField(source='region2.region1_id')
    class Meta:
        model = VarietyRegion2
        fields = ('variety_id',
                  'region2_id'
                  )

class VarietySerializer ( serializers.ModelSerializer ):
    varietyregion1 = VarietyRegion1Serializer (
        source='variety_region1_set',  # Note use of _set
        many=True,
        read_only=True
    )
    varietyregion1_ids = serializers.PrimaryKeyRelatedField (
        many=True,
        write_only=True,
        queryset=Region1.objects.all (),
        source='varietyregion1'
    )
    varietyregion2 = VarietyRegion2Serializer (
        source='variety_region2_set',  # Note use of _set
        many=True,
        read_only=True
    )
    varietyregion2_ids = serializers.PrimaryKeyRelatedField (
        many=True,
        write_only=True,
        queryset=Region2.objects.all (),
        source='varietyregion2'
    )
    class Meta:
        model = Variety
        fields = ('variety_id',
                  'variety_name',
                  'varietyregion1',
                  'varietyregion1_ids',
                  'varietyregion2',
                  'varietyregion2_ids'
                  )

class WinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Winery
        fields = ('winery_id',
                  'winery_name'
                  )

class WineryVarietySerializer(serializers.ModelSerializer):
    variety_id = serializers.ReadOnlyField(source='variety.variety_id' )
    winery_id = serializers.ReadOnlyField(source='winery.winery_id' )

    class Meta:
        model = WineryVariety
        fields = ('variety_id',
                  'winery_id'
                  )

class TasterSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Winery
        fields = ('taster_id',
                  'taster_name',
                  'twitter_handles',
                  'points'
                  )

class WineTasterSerializer ( serializers.ModelSerializer ):
    wine_id = serializers.ReadOnlyField ( source='wine.wine_id' )
    taster_id = serializers.ReadOnlyField ( source='taster.taster_id' )
    class Meta:
        model = WineTaster
        fields = ('wine_id',
                  'taster_id'
                  )

###############
class WineSerializer ( serializers.ModelSerializer ):
    wine = serializers.CharField (
        allow_blank=False,
        max_length=150
    )
    description = serializers.CharField (
        allow_blank=False,
        max_length=1000
    )
    designation = serializers.CharField (
        allow_blank=False,
        max_length=100
    )
    price = serializers.DecimalField (
        allow_null=True,
        max_digits=11,
        decimal_places=2
    )
    winery = WinerySerializer (
        many=False,
        read_only=True
    )
    winery_id = serializers.PrimaryKeyRelatedField (
        allow_null=False,
        many=False,
        write_only=True,
        queryset=Winery.objects.all (),
        source='winery'
    )
    country = CountrySerializer (
        many=False,
        read_only=True
    )
    country_id = serializers.PrimaryKeyRelatedField (
        required=False,
        allow_null=True,
        many=False,
        write_only=True,
        queryset=Country.objects.all (),
        source='country'
    )
    province = ProvinceSerializer (
        many=False,
        read_only=True
    )
    province_id = serializers.PrimaryKeyRelatedField (
        required=False,
        allow_null=True,
        many=False,
        write_only=True,
        queryset=Province.objects.all (),
        source='province'
    )
    region1 = Region1Serializer (
        many=False,
        read_only=True
    )
    region1_id = serializers.PrimaryKeyRelatedField (
        required=False,
        allow_null=True,
        many=False,
        write_only=True,
        queryset=Region1.objects.all (),
        source='region1'
    )
    region2 = Region2Serializer (
        many=False,
        read_only=True
    )
    region2_id = serializers.PrimaryKeyRelatedField (
        required=False,
        allow_null=True,
        many=False,
        write_only=True,
        queryset=Region2.objects.all (),
        source='region2'
    )
    variety = VarietySerializer (
        many=False,
        read_only=True
    )
    variety_id = serializers.PrimaryKeyRelatedField (
        required=False,
        allow_null=True,
        many=False,
        write_only=True,
        queryset=Variety.objects.all (),
        source='variety'
    )
    winetaster = WineTasterSerializer (
        source='wine_taster_set',  # Note: _set
        many=True,
        read_only=True
    )
    winetaster_ids = serializers.PrimaryKeyRelatedField (
        required=False,
        many=True,
        write_only=True,
        queryset=Taster.objects.all (),
        source='winetaster'
    )

    class Meta:
        model = Wine
        fields = (
            'wine_id',
            'wine',
            'description',
            'designation',
            'price',
            'winery',
            'winery_id',
            'country',
            'country_id',
            'province',
            'province_id',
            'region1',
            'region1_id',
            'region2',
            'region2_id',
            'variety',
            'variety_id',
            'winetaster_ids',
            'winetaster'
        )

    def create(self, validated_data):
        # This method persists a new Wine instance as well as adds all related
        # tasters to the winetaster table.  It does so by first removing (validated_
        # data.pop('winetaster')) from the validated data before the new Wine instance
        # is saved to the database. It then loops over the winetaster array in order to
        # extract each taster_id element and add entries to junction/associative
        # winetaster table.  :param validated_data:  :return: site

        # print(validated_data)

        tasters = validated_data.pop('wine_taster')
        wine = Wine.objects.create(**validated_data)

        if tasters is not None:
            for taster in tasters:
                WineTaster.objects.create(
                    wine_id=wine.wine_id,
                    taster_id=taster.taster_id
                )
        return wine

    def update(self, instance, validated_data):
        # site_id = validated_data.pop('wine_id')
        wine_id = instance.wine_id
        new_tasters = validated_data.pop('wine_taster')

        instance.wine = validated_data.get(
            'wine_name',
            instance.wine
        )
        instance.description = validated_data.get(
            'description',
            instance.description
        )
        instance.designation = validated_data.get(
            'designation',
            instance.designation
        )
        instance.price = validated_data.get(
            'date_inscribed',
            instance.price
        )
        instance.winery_id = validated_data.get(
            'winery_id',
            instance.winery_id
        )
        instance.country_id = validated_data.get(
            'country_id',
            instance.counry_id
        )
        instance.province_id = validated_data.get(
            'province_id',
            instance.province_id
        )
        instance.region1_id = validated_data.get(
            'region1_id',
            instance.region1_id
        )
        instance.region2_id = validated_data.get(
            'region2_id',
            instance.region2_id
        )
        instance.variety_id = validated_data.get(
            'variety_id',
            instance.variety_id
        )


        instance.save ()

        # If any existing wines are not in updated list, delete them
        new_ids = []
        old_ids = WineTaster.objects \
            .values_list ( 'wine_id', flat=True ) \
            .filter ( wine_id__exact=wine_id )

        # TODO Insert may not be required (Just return instance)

        # Insert new unmatched taster entries
        for taster in new_tasters:
            new_id = taster.taster_id
            new_ids.append ( new_id )
            if new_id in old_ids:
                continue
            else:
                WineTaster.objects \
                    .create ( wine_id=wine_id, taster_id=new_id )

        # Delete old unmatched taster entries
        for old_id in old_ids:
            if old_id in new_ids:
                continue
            else:
                WineTaster.objects \
                    .filter(wine_id=wine_id, taster_id=old_id) \
                    .delete()

        return instance


