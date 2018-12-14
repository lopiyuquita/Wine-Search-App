# https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html
# Django MySQL notes: https://docs.djangoproject.com/en/2.1/ref/databases/#version-support

import csv
from django.core.management.base import BaseCommand, CommandError
from winesearch.models import Country, Province, \
    Region1, Region2, Taster, Variety, VarietyRegion1, VarietyRegion2, WineTaster, Winery, WineryVariety


COUNTRY_COL = 1
DESCRIPTION_COL = 2
DESIGNATION_COL = 3
POINTS_COL = 4
PRICE_COL = 5
PROVINCE_COL = 6
REGION_1_COL = 7
REGION_2_COL = 8
TASTER_NAME_COL = 9
TASTER_TWITTER_HANDLE_COL = 10
TITLE_COL = 11
VARIETY_COL = 12
WINERY_COL = 13


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        print(options['file'])
        with open(options['file']) as f:
            reader = csv.reader(f)

            for row in reader:
                country_name = row[COUNTRY_COL]
                if country_name:
                    country, _ = Country.objects.get_or_create(country_name=country_name)

                province_name = row[PROVINCE_COL]
                if country_name and province_name:
                    province, _ = Province.objects.get_or_create(province_name=province_name, country=country)

                region1_name = row[REGION_1_COL]
                if province_name and region1_name:
                    region1, _ = Region1.objects.get_or_create(region1_name=region1_name, province=province)

                region2_name = row[REGION_2_COL]
                if region1_name and region2_name:
                    region2, _ = Region2.objects.get_or_create(region2_name=region2_name, region1=region1)

                taster_name = row[TASTER_NAME_COL]
                twitter_handles = row[TASTER_TWITTER_HANDLE_COL]

                if taster_name:
                    taster_name, _ = Taster.objects.get_or_create(taster_name=taster_name, twitter_handles=twitter_handles)

                variety_name = row[VARIETY_COL]
                if variety_name:
                    variety_name, _ = Variety.objects.get_or_create(variety_name=variety_name)

                wine = row[TITLE_COL]
                description = row[DESCRIPTION_COL]
                designation = row[DESIGNATION_COL]
                price = row[PRICE_COL]
                winery = row[WINERY_COL]
                if wine:
                    wine, _ = Wine.objects.get_or_create(wine=wine)
                    description, _ = Wine.objects.get_or_create(description=description)
                    designation, _ = Wine.objects.get_or_create(designation=designation)
                    price, _ = Wine.objects.get_or_create(price=price)
                    winery, _ = Wine.objects.get_or_create(winery=winery)























