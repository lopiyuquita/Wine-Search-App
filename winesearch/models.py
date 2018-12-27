# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# Reference: https://docs.djangoproject.com/en/2.1/ref/models/options/#unique-together
from django.db import models
from django.urls import reverse


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=45, unique=True) #outhgt to be unique

    class Meta:
        db_table = 'country'

    def __str__(self):
        return '{}'.format(self.country_name)


class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_name = models.CharField(max_length=45)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = [['country', 'province_name']]
        db_table = 'province'


    def __str__(self):
        return '{}, {}'.format(self.province_name, self.country.country_name)


class Region1(models.Model):
    region1_id = models.AutoField(primary_key=True)
    region1_name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = [['province', 'region1_name']]
        db_table = 'region1'

    def __str__(self):
        return '{}, {}'.format(self.region1_name, self.province.province_name)


class Region2(models.Model):
    region2_id = models.AutoField(primary_key=True)
    region2_name = models.CharField(max_length=100)
    region1 = models.ForeignKey(Region1, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = [['region1', 'region2_name']]
        db_table = 'region2'

    def __str__(self):
        return '{}'.format(self.region2_name)


class Variety(models.Model):
    variety_id = models.AutoField(primary_key=True)
    variety_name = models.CharField(max_length=45, unique=True)

    region1 = models.ManyToManyField(Region1, through='VarietyRegion1')
    region2 = models.ManyToManyField(Region2, through='VarietyRegion2')

    class Meta:
        db_table = 'variety'

    def __str__(self):
        return '{}'.format(self.variety_name)


class VarietyRegion1(models.Model):     #Joint model between Region1 and Variety
    region1 = models.ForeignKey(Region1, on_delete=models.DO_NOTHING)
    variety = models.ForeignKey(Variety, on_delete=models.DO_NOTHING)
    variety_region1_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'variety_region1'

class VarietyRegion2(models.Model):     #Joint model between Region2 and Variety
    variety = models.ForeignKey(Variety, on_delete=models.DO_NOTHING)
    region2 = models.ForeignKey(Region2, on_delete=models.DO_NOTHING)
    variety_region2_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'variety_region2'


class Taster(models.Model):
    taster_id = models.AutoField(primary_key=True)
    taster_name = models.CharField(max_length=45)
    twitter_handles = models.CharField(max_length=45, blank=True, null=True)
    points = models.SmallIntegerField(blank=True, null=True, default=0)

    class Meta:
        db_table = 'taster'

    def __str__(self):
        return '{}'.format(self.taster_name)


class Wine(models.Model):
    wine_id = models.AutoField(primary_key=True)
    wine = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    winery = models.ForeignKey('Winery', models.DO_NOTHING)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.DO_NOTHING)
    province = models.ForeignKey(Province, blank=True, null=True, on_delete=models.DO_NOTHING)
    region1 = models.ForeignKey(Region1, blank=True, null=True, on_delete=models.DO_NOTHING)
    region2 = models.ForeignKey(Region2, blank=True, null=True, on_delete=models.DO_NOTHING)
    variety = models.ForeignKey(Variety, blank=True, null=True, on_delete=models.DO_NOTHING)

    taster = models.ManyToManyField(Taster, through='WineTaster', blank=True, related_name='wines')

    class Meta:
        managed = False
        db_table = 'wine'
        ordering = ['wine']
        verbose_name = 'Wine'
        verbose_name_plural = 'Wines'


    def __str__(self):
        return '{}, {}, {}, {}'.format(self.wine, self.description, self.designation, self.price)

    def get_absolute_url(self):
        # return reverse('wine_detail', args=[str(self.id)])
        return reverse('wine_detail', kwargs={'pk': self.pk})

    # For filters.py: wine(label), description, variety, region2, region1, province, country, winery, price, points:
    # @property
    # def winery_names(self):
    #     wineries = self.winery.select_related('wine__winery').order_by('wine__winery__winery_name')
    #
    #     winery_names = []
    #     for winery in wineries:
    #         winery_name = winery.winery_name
    #         if winery_name is None:
    #             continue
    #         if winery_name not in winery_names:
    #             winery_names.append(winery_name)
    #     return winery_names

    @property
    def province_names(self):
        """
        Returns a list of Province (names only) associated with a Wine.
        Not all Wine are associated with a Province. In such cases the
        Queryset will return as <QuerySet [None]> and the list will need to be checked for
        None or a TypeError (sequence item 0: expected str instance, NoneType found) runtime
        error will be thrown.
        :return: string
        """
        countries = self.province.select_related('country__province').order_by(
            'country__province__province_name')

        province_names = []

        for country in countries:
            if not country.province:
                continue
            province_name = country.province.province_name
            if province_name not in province_names:
                province_names.append(province_name)
        return ', '.join(province_names)


class WineTaster(models.Model):     #Joint model between Wine and Taster
    wine_taster_id = models.AutoField(primary_key=True)
    taster = models.ForeignKey(Taster, on_delete=models.DO_NOTHING, related_name='related_taster')
    wine = models.ForeignKey(Wine, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'wine_taster'


class Winery(models.Model):
    winery_id = models.AutoField(primary_key=True)
    winery_name = models.CharField(max_length=100, blank=True, null=True)
    # Can't do select_related for many-to-many.
    # Intermediate model (Winery -> WineryVariety <- Variety)
    variety = models.ManyToManyField(Variety, through='WineryVariety')

    class Meta:
        db_table = 'winery'

    def __str__(self):
        return '{}'.format(self.winery_name)


class WineryVariety(models.Model):      #Joint model between Winery and Variety
    variety = models.ForeignKey(Variety, on_delete=models.DO_NOTHING)
    winery = models.ForeignKey(Winery, on_delete=models.DO_NOTHING)
    winery_variety_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'winery_variety'



















