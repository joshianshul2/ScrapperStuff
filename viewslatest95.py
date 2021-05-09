from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
#from .serializers import JournalSerializer
from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib import messages
#from django.views.generic import ListView
import bcrypt
from .models import UserRishu,UserManager,PropertyMaster,Property_TypeMaster,TypeMaster,Description,AvgMaster,RatioDetails
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
#from .serializers import JournalSerializer
import pandas as pd
import json
import numpy as np
from datetime import datetime,timedelta
from django.core import mail
from django.template.loader import render_to_string
import csv
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
import functools

from django.core import mail
from django.template.loader import render_to_string

from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail



data2 = []



def index(request):
    return render(request, 'index2.html')



def disjunction(*conditions):
    return functools.reduce(np.logical_or, conditions)

def Alert(request):
    dfp = pd.read_csv("rishu777.csv")
    df = pd.read_csv("Alert2.csv")
    if request.method == 'GET':
        title_contains_query = request.GET.get('title_contains')
        id_exact_query = request.GET.get('id_exact')
        title_or_author_query = request.GET.get('title_or_author')
        view_count_min = request.GET.get('view_count_min')
        view_count_max = request.GET.get('view_count_max')
        date_min = request.GET.get('date_min')
        date_max = request.GET.get('date_max')
        Udate_min = request.GET.get('date_min2')
        Udate_max = request.GET.get('date_max2')
        view_acres = request.GET.get('view_acres')
        status = request.GET.get('status')
        title2_contains_query = request.GET.get('title2_contains')
        view_state = request.GET.get('view_state')
        types = request.GET.get('types')
        view_percentage = request.GET.get('view_percentage')
        rto=RatioDetails.objects.create(state=view_state ,percentage=view_percentage)
        rto.save()
        print("Done")
        print(view_percentage)

        x = 1 - float(get_float(view_percentage)/100)
        print("Rishuuu",x)
        # akp1 =True
        akp2 = True
        akp3 = True
        print("Available Field",view_state)
        # (1) Condition for State , County and City
        if (view_state and view_percentage) is not None :
            print(df)
            print(dfp)
            akp1 = compute_county_wise_price(df, dfp, view_state, x);
            # print(df1)
            df1=dfp.loc[akp1, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]

        else:
            df1 = dfp

        print("DF1",df1)
        print("ALert", df1)
        # df1.to_csv('')
        df1.to_csv(r'static/CheapLandSearchALert.csv', index=False)
        json_records = df1.reset_index().to_json(orient='records')
        data = []

        data = json.loads(json_records)
        data2 = data
        # psg(request,data)
        getfile(request, data)
        # print("ANJI",data)
        # if title_contains_query is None:
        #     title_contains_query = ""
        # anji = '?title_contains=' + title_contains_query
        page = request.GET.get('page')
        # page2 = anji + "1"
        count = request.GET.get('count', 100)
        # print("ARnay", title_contains_query)
        # if request.GET.get(request.method == 'GET'+'/page',1) :
        # anji= '?title_contains=Texas&view_count_min=&w=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres='

        # print (anji)

        types = ""
        view_state = "State"
        paginator = Paginator(data, 2000)
        # page = request.GET.get('?title_contains=Texas&view_count_min=&view_count_max=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres=&page')
        # page = request.GET.get('title_contains')
        # page = request.GET.get('title_contains=Texas&view_count_min=&view_count_max=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres&page', 3)
        # paginator = Paginator(data, 500)
        print("Anshul", view_state)
        try:
            print(page)
            users = paginator.get_page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages(10))
        # qs = PropertyMaster.objects.all()
        context = {

            'users': users,

            'view_state' : view_state,
            'view_percentage' : view_percentage,
            'types': types,

        }

    return render(request, 'bootstrap_form.html', context)


def Alert2(view_state,view_percentage):
    dfp = pd.read_csv("rishu777.csv")
    df = pd.read_csv("FunCall2.csv")

    print("Done")
    print(type(view_percentage))

    x = 1 - float(view_percentage) / 100
    print("Rishuuu", x)

    akp2 = True
    akp3 = True
    print("Available Field", view_state)
        # (1) Condition for State , County and City
    if (view_state and view_percentage) is not None:
            print(df)
            print(dfp)
            akp1 = compute_county_wise_price(df, dfp, view_state, x);
            # print(df1)
            df1 = dfp.loc[
                akp1, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",
                       'types', 'status', 'created_at', 'updated_at']]

    else:
        df1 = dfp

    print("DF1", df1)
    print("ALert", df1)
    file_name = view_state + "_" + view_percentage + ".csv"
    # df1.to_csv(file_name, index=False)
    testemail(df1,file_name)
    print("BYE")
    # return render(request, 'bootstrap_form.html', context)

# def E_mail():
#     print("Rishuuu")
#     subject = 'welcome to Cheap Land Seach Testing world'
#     message = 'Tension mtt lena testing krr raha hu mail jayada aayenge rishiii .'
#     recipient_list = ["joshi.kush500@gmail.com","rishikabhataniya03@gmail.com"]
#     send_mail(subject, message, "joshi.anshul2@gmail.com", recipient_list)
#
#
#


def E_mail() :
    # print("RAm Sharma")

        # for i in akp:
        #     print(i['state'])
    # r= AvgMaster.objects.all()
    # print(r)
    # df = pd.read_csv("core/FunCall.csv")
    df = pd.read_csv("rishu777.csv")
    print ("Email 2", df)
    # print (r)
    # akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue')).values()
    # print(akp)
    subject = 'Anshul'
    akp = data_cmp_date(df)
    df2 = df.loc[akp, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url", 'types', 'status', 'created_at', 'updated_at']]
    print("Data Frame 2",df2)
    json_records = df2.reset_index().to_json(orient='records')
    data = []
    # print (a)
    data = json.loads(json_records)
    context  = {

        'users': data,
    }

# context ="Rishu"
    html_message = render_to_string('user_list.html',context)
    plain_message = strip_tags(html_message)
    from_email = 'joshi.anshul2@gmail.com'
    recipient_list = ["joshi.kush500@gmail.com", "anshulanjint110@gmail.com"]
    to = 'joshi.kush500@gmail.com',
    mail.send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)



def data_cmp_date(df):
    created_dates = [date.split()[0] for date in df['updated_at']]
    # present = datetime.now()
    # print("Present Date in System",present)

    present = datetime(2021, 4, 20)

    d = datetime.today() - timedelta(days=1)
    # min_d = datetime.strptime(present, '%Y-%m-%d')

    # present
    present = present - timedelta(days=1)

    # max_d = datetime.strptime(present-1, '%Y-%m-%d')
    results = []
    for date in created_dates:
        date = datetime.strptime(date, '%Y-%m-%d')
        # date += timedelta(days=1)
        if (date == present):

            results.append(True)
        else:
            results.append(False)
    return results


def compute_county_wise_price(df1, df2, state, x):
    netprice_per_county = df1[df1['state'] == state]
    netprice_per_county = netprice_per_county.drop('state', axis=1)

    print(x)
    print(netprice_per_county)
    price_per_county = {row[0]: row[1]*x for row in netprice_per_county.values}
    results = []

    for index, row in df2.iterrows():
        if ((row['state'] == state) and (price_per_county[row['county']] > row['Rate'])):
            results.append(True)
        else:
            results.append(False)
    return results
from django.contrib.auth.decorators import login_required

def rks(request):
    # return redirect('http://127.0.0.1:8000/static/CheapLandSearch.csv')
    return redirect('http://www.cheaplandsearch.com/static/CheapLandSearch.csv')


def rks2(request):
    # return redirect('http://127.0.0.1:8000/static/CheapLandSearchALert.csv')
    return redirect('http://www.cheaplandsearch.com/static/CheapLandSearchALert.csv')

def drpt(request):
    if request.method == 'POST':
        Descrpt = request.POST.get('Descrpt')
        Description.objects.create(Descrpt=Descrpt)
        Description.save()
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# def Loader():
#         schedule.every(10).seconds.do(sm)
#         # schedule.every(10).seconds.do(load_scrapper)
#         # schedule.every(1).minutes.do(Rishu,'request')
#         # schedule.every().hour.do(job)
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

def testemail(df1,file_name):
    # dfp = pd.read_csv("rishu777.csv")
    # df = pd.read_csv("Alert2.csv")
    # print ("Email 2", df)
    # # print (r)
    # # akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue')).values()
    # # print(akp)
    # subject = 'Anshul'
    # akp = data_cmp_date(df)
    # df2 = df.loc[
    #     akp, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url", 'types',
    #           'status', 'created_at', 'updated_at']]
    # print("Data Frame 2", df2)
    # json_records = df2.reset_index().to_json(orient='records')
    # data = []
    # # print (a)
    # data = str(json.loads(json_records))
    # file_name
    # file_name = view_state + "_" + view_percentage + ".csv"
    df1.to_csv(file_name, index=False)
    print("FILE NAME",file_name)
    email = EmailMessage('Cheap Land Search ', 'Alert', 'joshi.anshul2@gmail.com', ['joshi.kush500@gmail.com'])
    # email.attach('rishu777.csv',rishu777.csv,'text/csv')
    email.attach_file(file_name)
    email.send()

    # assigned_leads = lead.objects.filter(assigned_to__in=usercompany).distinct()

def show(request):

    testemail()
    print("DODIDDONE")
    # print("Email Starting")
    # E_mail()
    df = pd.read_csv("bckp.csv")
    # pd.df['created_at'].date()

    if request.method == 'GET':
        title_contains_query = request.GET.get('title_contains')
        if title_contains_query is None:
            title_contains_query = ""
        else:
            title_contains_query = request.GET.get('title_contains').title()
        print("pyyyyyyy",title_contains_query)
        id_exact_query = request.GET.get('id_exact')
        title_or_author_query = request.GET.get('title_or_author')
        view_count_min = request.GET.get('view_count_min')
        view_count_max = request.GET.get('view_count_max')
        date_min = request.GET.get('date_min')
        date_max = request.GET.get('date_max')
        Udate_min = request.GET.get('date_min2')
        Udate_max = request.GET.get('date_max2')
        view_acres = request.GET.get('view_acres')
        status = request.GET.get('status')
        title2_contains_query = request.GET.get('title2_contains')
        view_state = request.GET.get('view_state')
        types = request.GET.get('types')
        view_percentage = request.GET.get('view_percentage')
        Descrpt = request.GET.get('Descrpt')
        print("Anshul Dta ",Descrpt)
        print("DAte HAI NAA ",date_min)
        print(date_min)
        # akp1 = df['state']== 'Anji'
        akp1 =True
        akp2 = True
        akp3 = True

        if title_contains_query and  title_or_author_query and view_count_min and view_count_max and  date_min and date_max and Udate_min and Udate_max and view_acres and status and types :
            redirect('show3')
        # df['lwPropertyId']=, 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]
        print("Available Field",title_contains_query)
        # (1) Condition for State , County and City
        if title_contains_query  is not None :
            # rishu=df['created_at'].dt.date()
            # print("Date rishu",rishu)
            akp1 = (df['state'] == title_contains_query ) | (df['city'] == title_contains_query) | (df['county'] == title_contains_query)
            # df['created_at'] = df['created_at'].strftime('%m-%d-%Y')

            # df['created_at'] = pd.to_datetime(df["created_at"].dt.strftime('%Y-%m'))
            # created_at = data_within_date2(df)
            # print("CRETED AT ",created_at)


            # print(df1)
            # created_at =get_date(created_at)
            # print(created_at)
            df1=df.loc[akp1, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]

        else:
            df1 =df
            # pd.to_datetime(df['created_at']).apply(lambda x: x.date())
        print("DF1",df1)
        # (2) Condition for Types
        if types is not None :
            # df['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            akp2 = (df1['types'].str.contains(types , na=False))
            # akp2 = (df1['types'] == types)
            df2=df1.loc[akp2, ["lwPropertyId", 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]

        else :
            df2 =df1
            # pd.to_datetime(df['created_at']).apply(lambda x: x.date())

        print("DF2",df2)

        # (3) Condition for Status
        if status is not "" :
            print(status)
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            akp3 = (df2['status'] == status)
            # pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            df3 = df2.loc[akp3, ["lwPropertyId", 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]
        else :
            df3 = df2
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
        print("DF3",df3)

        # print(view_acres)
        # (4) Condition For Min Price :

        if view_count_min is not None :
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            akp4 = df3['price'] >= get_float(view_count_min)
            df4 = df3.loc[akp4, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",
                       'types', 'status', 'created_at', 'updated_at']]
        else :
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            df4 = df3
        print("DF4",df4)

        # (5) Condition For Max Price :

        if view_count_max  is "100000":
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            print("word",view_count_max)
            akp5 = df4['price'] <= get_float(view_count_max)
            df5 = df4.loc[
                akp5, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",
                       'types', 'status', 'created_at', 'updated_at']]
        else:
            print("Hello",view_count_max)
            # df['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            df5 = df4
        print("DF5",df5)

        #(6) Condition for Area :

        if view_acres is not None :
            # df['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            akp6 = df5['acres'] >= get_float(view_acres)
            df6 = df5.loc[akp6, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",
                       'types', 'status', 'created_at', 'updated_at']]
            # print(df5)
        else :
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            df6 = df5

        print("DF6",df6)

        # (7) Condition For Publish Date :

        if date_min  is "2000-01-01" and date_max is "2050-01-01":
            # df['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            print("RishuuuDAte")
            print(date_min)
            print(date_max)
            akp7 = data_within_date(df6, date_min, date_max)
            df7 = df6.loc[akp7, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]
        else:
            print("NA Date",date_min)
            # df['created_at'] = pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            df7 = df6
        print("DF7",df7)

        # (7) Condition For Update Date :

        if Udate_min is "2000-01-01" and Udate_max is "2050-01-01":
            akp8 = data_within_date(df7, Udate_min, Udate_max)
            df8 = df7.loc[
                akp8, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",
                       'types', 'status', 'created_at', 'updated_at']]
        else:
            print("NA Date", Udate_min)
            # df7['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
            df8 = df7
        print("DF8", df8)
        # df8['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
        df9 = df8.sort_values(by="created_at",ascending=False)
        print("Ansjiuu")
        print(df9)
        # df9 = df8.loc[akp9, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",'types', 'status', 'created_at', 'updated_at']]
        print("Rishuuu@",df9)
        # download(df8)
        # testrishu(df8)
        print("DFFFFFFDFSGDGDGD",df9)
        # anji23 = df9['created_at']=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
        # print("Indian Army",anji23)
        df9.to_csv(r'static/CheapLandSearch.csv', index=False)
        json_records = df9.reset_index().to_json(orient='records')
        # data2 =df8
        data = []

        data = json.loads(json_records)
        data2 =data
        # psg(request,data)
        getfile(request,data)
        # print("ANJI",data)
        if title_contains_query is None :
            title_contains_query = ""
        anji = '?title_contains=' + title_contains_query
        page =request.GET.get('page')
        page2 = anji+"1"
        count = request.GET.get('count', 100)
        print("ARnay",title_contains_query)
        # if request.GET.get(request.method == 'GET'+'/page',1) :
        # anji= '?title_contains=Texas&view_count_min=&w=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres='

        print (anji)

        types = ""
        status = ""
        paginator = Paginator(data, 2000)
        # page = request.GET.get('?title_contains=Texas&view_count_min=&view_count_max=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres=&page')
        # page = request.GET.get('title_contains')
        # page = request.GET.get('title_contains=Texas&view_count_min=&view_count_max=&date_min=2000-05-05&date_max=2050-05-05&types=&date_min2=2000-05-05&date_max2=2000-05-05&status=&view_acres&page', 3)
        # paginator = Paginator(data, 500)
        print("Anshul",title_contains_query)
        try:
            print(page)
            users = paginator.get_page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages(10))
        # qs = PropertyMaster.objects.all()

        # d=Description.objects.create(Descrpt=Descrpt)
        # d.save()
        print("OKKKKK")
        context = {

                 'users': users,
                 # 'anji': anji23,
                 'title_contains' : title_contains_query,
                 'view_count_min' : view_count_min ,
                 'view_count_max': view_count_max,

                 'date_max': date_max,
                 'date_min': date_min,
                 'date_min2' : Udate_min,
                 'date_max2': Udate_max,
                 'view_acres': view_acres,
                 'status': status,
                 'types' : types ,
                 # 'Descrpt' : Descrpt,


        }

    return render(request, 'bootstrap_form.html',context)


def get_date(df):
    aj=pd.to_datetime(df['created_at']).apply(lambda x: x.date())
    return aj

def desp(request):
   # list = get_object_or_404 ( student, pk=student_id)
   if request.method == 'POST' :
      aj = request.POST.get('Descrpt')
      prop2 = Description.objects.create(Descrpt=aj)
      print("Bhalaaa")
      prop2.save()
   # return HttpResponseRedirect("")
   return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



def psg(request):
# Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=quiz.csv'
# Create the CSV writer using the HttpResponse as the "file"
    writer = csv.writer(response)
    writer.writerow(['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url",
                       'types', 'status', 'created_at', 'updated_at'])
    print (data2)
    print("Nikallllll")
    writer.writerow(data2.address)
    writer.writerow(data2.status)

    return response

def RatioDetailsTemp(request):
    df = pd.read_csv("core/rishuuu.csv")
    view_state = 'State'
    print("Query Execution")
    p=PropertyMaster.objects.raw('SELECT DISTINCT state FROM PropertyMaster')
    print(p)
    view_percentage = 0.00
    if request.method == 'POST':
        view_state = request.POST.get('view_state')
        view_percentage = request.POST.get('view_percentage')
        rto=RatioDetails.objects.create(state=view_state ,percentage=view_percentage)
        rto.save()
        print("Done")
        print(float(view_percentage))
        print("GO FOR ALERT 2")
        Alert2(view_state,view_percentage)

    rto = RatioDetails.objects.all()
    # if rto.filter(state=view_state ,percentage=view_percentage).exists() :
    #     print("okkkkk")
    #     RatioDetails.objects.filter(state=view_state ,percentage=view_percentage).delete()
        # rto.delete()
    for row in RatioDetails.objects.all().reverse():
        if RatioDetails.objects.filter(state=view_state ,percentage=view_percentage).count() > 1:
            row.delete()
    # RatioDetails.objects.filter(state=view_state ,percentage=view_percentage).exists()


    # else :
    #     print("AJJJJ")

    # anji = AvgMaster.objects.filter()
    # print("TEst",anji)
    # anji = PropertyMaster.objects.raw("SELECT DISTINCT state FROM core_propertymaster WHERE state='Texas' ")
    # print("Anji SELECT Query Execution",anji)
    # for p in AvgMaster.objects.raw('SELECT * FROM core_propertymaster '):
    #     print(p.state)
    # p=AvgMaster.objects.all()
    # print (p)
    context = {

            'users': rto,
            # 'anji' : anji,
        }

    return render(request, 'alertbootstrap.html', context)


def delete(request):
    if request.method == 'POST':
        rishu = request.POST.get('rishu')
        print("Anshul Joshi FAther ",rishu)
    RatioDetails.objects.filter(id=rishu).delete()
    rto = RatioDetails.objects.all()
    context = {

        'users': rto,
    }

    return render(request, 'alertbootstrap.html', context)


def AlertTODO(request):
    df = pd.read_csv("rishu.csv")
    print ("Email 2", df)
    # print (r)
    # print(r)
    print("Hero")
    # akp = AvgMaster.objects.filter(Rate__gte=F('FinaleValue')).values()
    # print(akp)
    subject = 'Anshul'
    akp = data_cmp_date(df)
    df2 = df.loc[
        akp, ['lwPropertyId', 'address', 'city', 'state', 'county', 'zip', 'price', 'acres', "Rate", "Url", 'types',
              'status', 'created_at', 'updated_at']]
    print("Test DF2", df2)
    json_records = df2.reset_index().to_json(orient='records')
    data = []
    # print (a)
    data = json.loads(json_records)
    context = {

        'users': data,
    }

    return render(request,'alertbootstrap.html',context)


def testrishu(df8) :
    print("Done")
    df8.to_csv(r'NITK.csv', index=False)
    print("DO IT FAST")

print("DATA FRAM @@@@@ ",data2)
def getfile(request,data):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file321.csv"'
    writer = csv.writer(response)
    writer.writerow(data)
    # writer.writerow(['1001', 'John', 'Domil', 'CA'])
    # writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    return response

def download(df):
    print(df)
    print("WE ARE NITKIANS")
    df.to_csv('rishuanjism.csv', index=False)




from django.contrib.auth.decorators import login_required

# @login_required(login_url='show3/')

def show3(request):
    print("Email Starting")
    # E_mail()
    return render(request,'bootstrap_form.html')

def get_float(s):
    ans_int = 0
    ans_float = 0
    divisor = 1

    int_part = s.split('.')[0]

    for d in int_part:
        ans_int = (ans_int * 10) + int(d)

    if (not s.find('.') == -1):

        float_part = s.split('.')[1]

        for d in float_part:
            ans_float = (ans_float * 10) + int(d)

        divisor = 10 ** len(float_part)

    ans = ans_int + (ans_float / divisor)

    return ans

def data_within_date(df, min_date, max_date):

    # created_dates = [date.split()[0] for date in df['created_at'].apply(lambda x: x.date())]
    created_dates = [date.split()[0] for date in pd.to_datetime(df['created_at'])]
    min_d = datetime.strptime(min_date, '%Y-%m-%d').date()
    max_d = datetime.strptime(max_date, '%Y-%m-%d').date()
    results = []
    for date in created_dates:
        date = datetime.strptime(date, '%Y-%m-%d')
        if (date >= min_d and date <= max_d):
            results.append(True)
        else:
            results.append(False)
    return results

# def data_within_date2(df):
#
#     # created_dates = [date.split()[0] for date in df['created_at'].apply(lambda x: x.date())]
#     created_dates = [date.split()[0] for date in df['created_at']]
#     # created_dates = pd.to_datetime(df['created_at'])
#     # min_d = datetime.strptime(min_date, '%Y-%m-%d').date()
#     # max_d = datetime.strptime(max_date, '%Y-%m-%d').date()
#     results = []
#     for date in created_dates:
#         date = datetime.strptime(date, '%Y-%m-%d').strftime('%m-%d-%Y')
#         results.append(date)

    # return results




def login(request):
    email = request.POST['login_email']
    password = request.POST['login_password']
    print(email)
    if UserRishu.objects.filter(email=email).exists()  and UserRishu.objects.filter(password =password).exists() :
        return redirect('/show3')
    return redirect('/')



def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    # job(request)

    return render(request, 'test111.html', context)

def set_password(self, pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    self.password_hash = pwhash.decode('utf8') # decode the hash to prevent is encoded twice


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter(request):
    qs = PropertyMaster.objects.all()
    category = PropertyMaster.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    view_acres = request.GET.get('view_acres')
    category = request.GET.get('category')
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
        qs = qs.filter(price__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(price__lt=view_count_max+"1")

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(price__name=category)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(view_acres):
        qs = qs.filter(acres__gte=view_acres)
    #
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

# class ReactFilterView(generics.ListAPIView):
#     serializer_class = JournalSerializer
#
#     def get_queryset(self):
#         qs = filter(self.request)
#         return qs


# class ReactInfiniteView(generics.ListAPIView):
#     serializer_class = JournalSerializer
#
#     def get_queryset(self):
#         qs = infinite_filter(self.request)
#         return qs
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset, many=True)
#         return Response({
#             "journals": serializer.data,
#             "has_more": is_there_more_data(request)
#         })


#




def logout(request):
    return render(request,'index2.html')
