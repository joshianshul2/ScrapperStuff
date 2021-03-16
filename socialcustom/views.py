from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.views.generic import ListView
import bcrypt
from .models import User,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster
from .tables import simple_list,SomeTable
import schedule
import time
# Scrapper
import requests
import csv
import time
import pdb
import operator
import  csv
import random
import re
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from .serializers import JournalSerializer



from django_tables2 import SingleTableView



def index(request):
    return render(request, 'index2.html')
def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    # hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
    # password= User.objects.create()
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def job(request):
        a=0
        print("I'm Anshul...")

        zipcode_list = [78880]
        # with open("datafile") as myfile:
        #     head = [next(myfile) for x in range(N)]
        # with open('zip_code_database.csv', 'r') as file:
        #     # head = [next(myfile) for x in range(N)]
        #     reader = csv.reader(file)
        #     for row in range(30):
        #         print(row)
                # zipcode_list = [75002, 75006, 75007, 75009, 75010, 75013, 75019, 75020, 75021, 75022, 75024, 75028, 75032,
                #                 75034, 75035, 75038, 75040, 75041, 75043, 75044, 75048, 75050, 75051, 75056, 75057, 75058,
                #                 75061, 75063, 75065, 75067, 75068, 75069, 75070, 75071, 75074,75076, 75077, 75078, 75080, 75081, 75083, 75087, 75088, 75089, 75090, 75092, 75093, 75097, 75098, 75102, 75103, 75104, 75105, 75109, 75110, 75114, 75115, 75116, 75117, 75119, 75124, 75126, 75135, 75142, 75143, 75144, 75147, 75148, 75154, 75156, 75159, 75160]

        headers = {
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
              "Accept-Encoding": "*",
              "Connection": "keep-alive"
                }
        try:

            for zip in zipcode_list:
                        if len(str(zip)) == 4:
                            zip = "0" + str(zip)
                        n = 0
                        url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                              str(zip) + "/land/listed-1-day"
                        page = 0
                        # print(url)
                        page = requests.get(url, headers=headers)
                        # time.sleep(random.randrange(1, 2))
                        while (page == 0):
                            page = requests.get(url, headers=headers)
                            time.sleep(random.randrange(1, 5))
                        data = page.json()
                        print(data['searchResults']['locationSeo']['pageHeaderCount'])
                        countListing = data['searchResults']['locationSeo']['pageHeaderCount']
                        countListing = re.findall(r'\d+', countListing)
                        print(countListing)
                        if len(countListing) == 3:
                            page_count = int(int(countListing[2]) / 25 + 2)
                        else:
                            page_count = 2
                        # print(countListing)

                        for i in range(1, page_count):
                            url = "https://www.landwatch.com/api/property/search/1113/zip-" + \
                                  str(zip) + "/land/listed-1-day/page-" + str(i)
                            # print(url)
                            page = 0
                            page = requests.get(url, headers=headers)
                            # time.sleep(random.randrange(1, 2))
                            while (page == 0):
                                page = requests.get(url, headers=headers)
                                time.sleep(random.randrange(1, 5))
                            data = page.json()
                            # print("Length of data : ",len(data))
                            print("Rishu")
                            for item in data['searchResults']['propertyResults']:
                                a=a+1
                                prop = PropertyMaster.objects.create(accountId=item['accountId'], acres=item['acres'],
                                                                 adTargetingCountyId=item['adTargetingCountyId'],
                                                                 address=item['address'], baths=item['baths'],
                                                                 beds=item['beds'], brokerCompany=item['brokerCompany'],
                                                                 brokerName=item['brokerName'],
                                                                 Url="Url: ""https://www.landwatch.com" + item['canonicalUrl'],
                                                                 city=item['city'],
                                                                 cityID=item['cityID'],
                                                                 companyLogoDocumentId=item['companyLogoDocumentId'],
                                                                 county=item['county'], countyId=item['countyId'],
                                                                 description=item['description'], hasHouse=item['hasHouse'],
                                                                 hasVideo=item['hasVideo'],
                                                                 hasVirtualTour=item['hasVirtualTour'],
                                                                 imageCount=item['imageCount'],
                                                                 imageAltTextDisplay=item['imageAltTextDisplay'],
                                                                 isHeadlineAd=item['isHeadlineAd'],
                                                                 lwPropertyId=item['lwPropertyId'], isALC=item['isALC'],
                                                                 latitude=item['latitude'],state=item['state'],
                                                                 longitude=item['longitude'], price=item['price'],
                                                                 status=item['status'], zip=item['zip'],

                                                                            )

                                # for line in item['types']:
                                #     Type = line.split(",")
                                #     types = item[line]
                                #     # y = Type[2]
                                #     print(line)



                                    # types = item['types'].split(","),

                                try:
                                    prop = PropertyMaster.objects.create(Rate = item['price'] / item['acres'])
                                    obj = PropertyMaster.objects.get(pk=item['lwPropertyId'])

                                except :
                                    Rate= 0
                                    print("Hello")
                                if PropertyMaster.objects.filter(pk=item['lwPropertyId']).exists():
                                ###do something###
                                    print("Rishu")
                                else:
                                    print("Aj")
                                prop.delete()
                                prop.save()
                                entry = TypeMaster.objects.all()
                                # entry.Property_TypeMaster.add(joe)
                                # cheese_blog = TypeMaster.objects.get(TypeName="Rishu")
                                # entry.key2_id = cheese_blog
                                # entry.key2_id.add(cheese_blog)
                                # p1 = PropertyMaster.objects.get(lwPropertyId=item['lwPropertyId'])
                                # print(p1)
                                # p2 = TypeMaster.objects.get(TypeId=1)
                                # # p1.save()
                                a2 = Property_TypeMaster(Prop_Id2=item['lwPropertyId']+1, Type_Id2=100)
                                a2.save()
                                # a2.Prop_Id.add(p1,p2)
                                # typeprop = Property_TypeMaster.objects.create()
                                # typeprop.save()


                                n = n + 1
                        # print("n=",n)
                        print(n, " records found in zipcode : ", zip)

        finally:

                zip_code_last = zip
                print("Completed")
                print(a)
                # allvideos = PropertyMaster.objects.all()
                # context = {'allvideos': allvideos}
                # qs = PropertyMaster.objects.all()
                # txtsearch = request.GET.get('title_or_author')
                #
                # if txtsearch != '' and txtsearch is not None:
                #     qs = filter(city__icontains=txtsearch)
                # context = {
                #     'queryset': qs,
                #     # 'allvideos': PropertyMaster.objects.all()
                # }
                # return render(request, "bootstrap_form.html", context)
                #

                qs = filter(request)
                # auths = PropertyMaster.objects.order_by('acres')
                # ordered = sorted(auths, key=operator.attrgetter('acres'))
                context = {
                    'queryset': qs,
                    # 'acres': ordered,
                }
        return render(request, "bootstrap_form.html", context)
        # return render(request, "bootstrap_form.html")


def login(request):
    if User.objects.filter(email=request.POST['login_email']).exists():
        user = User.objects.filter(email=request.POST['login_email'])[0]
        # if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
        if (request.POST['login_password'] == user.password):
            request.session['id'] = user.id
            return redirect('/job')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    job(request)

    return render(request, 'test111.html', context)

def set_password(self, pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    self.password_hash = pwhash.decode('utf8') # decode the hash to prevent is encoded twice

def simple_list(request):
    queryset = PropertyMaster.objects.all()
    table = PropertyMaster(queryset)
    return render(request, 'test111.html')

class SomeTableView(SingleTableView):
    model = PropertyMaster
    template_name = 'test111.html'
    table_class = SomeTable




# def showvideo(request):
#     allvideos = PropertyMaster.objects.all()
#     context = {'allvideos': allvideos}
#
#
#     return render(request,'test111.html', context)

# def Loader():
#         schedule.every(10).seconds.do(sm)
#         schedule.every(10).seconds.do(load_scrapper)
#         schedule.every(1).minutes.do(Rishu,'request')
#         schedule.every().hour.do(job)
#
#
#     # current_user = request.allviedo
#     # print(current_user.lwPropertyId)
#     # obj = AllDetails.objects.get(lwPropertyId=409616130)
#     # AllDetails.objects.filter(pk=obj.lwPropertyId).update(Descrpt=request.POST.get('Descrpt'))
#     # current_user.id = AllDetails.objects.create(Descrpt=request.POST.get('Descrpt'))
#     # obj.save()
# Loader()
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# Filter rishu

def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = PropertyMaster.objects.all()
    acres = PropertyMaster.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    acres = request.GET.get('category')
    reviewed = request.GET.get('reviewed')
    not_reviewed = request.GET.get('notReviewed')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(city__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(city__icontains=title_or_author_query)).distinct()
                       # | Q(author__name__icontains=title_or_author_query)


    if is_valid_queryparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    # if is_valid_queryparam(acres) :
    #     qs = qs.filter(acres__values=acres)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)

    elif not_reviewed == 'on':
        qs = qs.filter(reviewed=False)

    return qs


def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    return PropertyMaster.objects.all()[int(offset): int(offset) + int(limit)]


def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > PropertyMaster.objects.all().count():
        return False
    return True


# def BootstrapFilterView(request):
#     qs = filter(request)
#     context = {
#         'queryset': qs,
#         'acres': Category.objects.all()
#     }
#     return render(request, "bootstrap_form.html", context)


class ReactFilterView(generics.ListAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        qs = filter(self.request)
        return qs


class ReactInfiniteView(generics.ListAPIView):
    serializer_class = JournalSerializer

    def get_queryset(self):
        qs = infinite_filter(self.request)
        return qs

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response({
            "journals": serializer.data,
            "has_more": is_there_more_data(request)
        })

