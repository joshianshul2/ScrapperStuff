# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.db.models.functions import Lower
# from django.contrib.auth.models import User,auth
# from .models import User
# from django import forms
# # from .forms import UserLogin
# from django.contrib.auth import authenticate, login
# from django.db.models.functions import Lower
# from django.contrib import  messages
#
# # from django.contrib.auth import (
# #     authenticate,
# #     get_user_model,
# #     login,
# #     logout
# # )
#
# from .forms import UserLoginForm, UserRegisterForm
#
# # Create your views here.
# def signup(request):
#     if request.method == 'POST' :
#         user1=request.POST['Username']
#         # name1=request.POST['name']
#         email1 = request.POST['email']
#         password1 = request.POST['password']
#         # password22 = request.POST['password2']
#         # if password1 == password22 :
#         anji=User(Username=user1,email=email1,password=password1)
#         anji.save()
#         return redirect(index)
#
#     return render(request,'aj.html')
#
#
# def index(request):
#     return render(request,"index.html")
#
# def enter(request):
#     return render(request,"login.html")
#
# def login(request):
#
#     if request.method == 'POST':
#         username= request.POST['username']
#         password= request.POST['password']
#         print(Username)
#         print(password)
#         print(User.object.all())
#         x = auth.authenticate(Username=username, password=password)
#         print("hiii")
#         print(Username)
#         print(password)
#         print(x)
#         return redirect(login)
#         print(x)
#         # if x is  None :
#         #     auth.login(request,x)
#         #     # # return redirect(index)
#         #     return redirect(index)
#         # else:
#         #     messages.info(request,'invalid Credentilas')
#         #     return redirect(index)
#             # print("Anji")
#             # return redirect("https://www.google.com/?client=safari&channel=mac_bm")
#
#     # #
#     else :
#         return render(request,'login.html')
#
#
# # def login_view(request):
# #     next = request.GET.get('next')
# #     form = UserLoginForm(request.POST or None)
# #     if form.is_valid():
# #         username = form.cleaned_data.get('username')
# #         password = form.cleaned_data.get('password')
# #         user = authenticate(username=username, password=password)
# #         login(request, user)
# #         if next:
# #             return redirect(next)
# #         return redirect('/')
# #
# #     context = {
# #         'form': form,
# #     }
# #     return render(request, "login.html", context)
# #
# #
# #
# # def logout_view(request):
# #     logout(request)
# #     return redirect('/')
#
#
#
# def dsa(request) :
#
#     # data = User.objects.all()
#      # data = Students.objects.all()
#     print(objects.Username)
#     data1 = User.objects.order_by(Lower('Username'))
#     # MyModel.objects.order_by(Lower('myfield'))
#     print(User.objects.all())
#     stu = {
#          "dsa1": data1
#          }
#
#     return render(request,"login.html", stu)
from django.http import JsonResponse