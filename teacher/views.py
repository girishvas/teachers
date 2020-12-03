from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import  ListView, TemplateView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q
# from django.contrib import messages

import io
import csv
import os
# import uuid
# import json
import sys
# import re

from .models import *
from .forms import *


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Teacher.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


def validate_mobile(request):
    mobile = request.GET.get('phone', None)
    data = {
        'is_taken': Teacher.objects.filter(phone_number__iexact=mobile).exists()
    }
    return JsonResponse(data)


class HomePage(ListView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):

        try:
            name = request.GET['search']
        except:
            name = ''
        if (name != ''):
            teachers = Teacher.objects.filter(
                Q(last_name__icontains=name) | Q(subjects__name__iexact=name)
            ).distinct()
        else:
            teachers = Teacher.objects.all().order_by('-id')

        paginator = Paginator(teachers, 20)
        page = request.GET.get('page')

        try:
            teachers = paginator.page(page)
        except PageNotAnInteger:
            teachers = paginator.page(1)
        except EmptyPage:
            teachers = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'teacher': teachers, 'search': name})


class AddTeacher(TemplateView):
    template_name = 'add-teacher.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': TeacherForm})

    def post(self, request, *args, **kwargs):
        if 'bulk' in request.POST:
            if not request.user.is_authenticated:
                return HttpResponseRedirect('/login/')

            file = request.FILES['bulk_csv']
            if not file.name.endswith('.csv'):
                return HttpResponse('Not a CSV file')

            data_set = file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)

            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                if column[3] and column[4]:
                    if Teacher.objects.filter(email=column[3]).count() == 0:
                        teacherObj = Teacher()
                        teacherObj.first_name = column[0]
                        teacherObj.last_name = column[1]
                        teacherObj.email = column[3]
                        teacherObj.phone_number = column[4]
                        teacherObj.room_number = column[5]
                        if not len(column[2]) == 1:
                            teacherObj.profile = 'profile/' + column[2]
                        else:
                            teacherObj.profile = 'profile/default.jpg'
                        teacherObj.save()
                        for idx, subject in enumerate(column[6:]):
                            _, created = Subject.objects.update_or_create(
                                name = subject.strip('"').strip().title()
                            )
                            if idx < 5:
                                teacherObj.subjects.add(_)
            return HttpResponseRedirect('/')
        else:
            form = TeacherForm(request.POST, request.FILES)
            if form.is_valid():
                teacher = form.save(commit=False)
                teacher.profile = form.cleaned_data['profile']
                teacher.save()
                form.save_m2m()
            else:
                form = TeacherForm()

        return HttpResponseRedirect('/')


class TeacherDetails(TemplateView):
    template_name = 'details.html'

    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        return render(request, self.template_name, {'teacher': teacher})


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect('/')

    def get(self, request):
        return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')