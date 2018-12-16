# https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html
# Django MySQL notes: https://docs.djangoproject.com/en/2.1/ref/databases/#version-support

import csv
from django.core.management.base import BaseCommand, CommandError
from winesearch.models import Country, Province, \
    Region1, Region2, Taster, Variety, Wine, Winery, WineTaster, WineryVariety


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
        global winery_name
        print(options['file'])
        counter = 0
        with open(options['file']) as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                counter += 1
                if counter % 1000 == 0:
                    print(counter)
                country_name = row[COUNTRY_COL]
                price = row[PRICE_COL]
                province_name = row[PROVINCE_COL]
                region1_name = row[REGION_1_COL]
                region2_name = row[REGION_2_COL]
                taster_name = row[TASTER_NAME_COL]
                twitter_handles = row[TASTER_TWITTER_HANDLE_COL]
                variety_name = row[VARIETY_COL]
                winery_name = row[WINERY_COL]
                wine_name = row[TITLE_COL]
                description = row[DESCRIPTION_COL]
                designation = row[DESIGNATION_COL]
                points = row[POINTS_COL]

                country = None
                province = None
                region1 = None
                region2 = None
                taster = None
                variety = None
                winery = None



                if country_name:
                    country, _ = Country.objects.get_or_create(country_name=country_name)


                if country_name and province_name:
                    province, _ = Province.objects.get_or_create(province_name=province_name, country=country)


                if province_name and region1_name:
                    region1, _ = Region1.objects.get_or_create(region1_name=region1_name, province=province)


                if region1_name and region2_name:

                    region2, _ = Region2.objects.get_or_create(region2_name=region2_name, region1=region1)


                if taster_name:
                    taster, _ = Taster.objects.get_or_create(taster_name=taster_name,
                                                                  twitter_handles=twitter_handles,
                                                                  points=points)


                if variety_name:
                    variety, _ = Variety.objects.get_or_create(variety_name=variety_name)


                if winery_name:
                    winery, _ = Winery.objects.get_or_create(winery_name=winery_name)


                if not price:
                    price = None
                else:
                    price = float(price)

                if wine_name:
                    try:
                        wine, _ = Wine.objects.get_or_create(
                            wine=wine_name,
                            description=description,
                            designation=designation,
                            price=price,
                            winery=winery,
                            country=country,
                            province=province,
                            region1=region1,
                            region2=region2,
                            variety=variety,
                        )
                        if taster:
                            wine_taster, _ = WineTaster.objects.get_or_create(wine=wine, taster=taster)
                        if winery and variety:
                            winery_variety, _ = WineryVariety.objects.get_or_create(winery=winery, variety=variety)
                    except ValueError:
                        print(wine_name, description, designation, price, country, province, region1, region2, variety_name)





















