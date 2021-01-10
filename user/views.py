from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from user.models import UserInfo


class CreatUser(View):

    def post(self, request):

        params = request.POST

        UserInfo.objects.create(
            name=params.get('name'),
            permission=params.get('permission'),
            password=params.get('password'),
            gender=params.get('gender'),
        )
        return HttpResponse("Add user succeed")


class UserLogin(View):

    def post(self, request):

        params = request.POST
        user = UserInfo.objects.filter(name=params.get('name'),
                                password=params.get('password'))
        if user:
            return HttpResponse("1")
        else:
            return HttpResponse("system not this user")


class AlertPermission(View):

    def post(self, request):

        params = request.POST
        users = UserInfo.objects.filter(id=params.get('id')).update(
            permission=params.get('permission')
        )
        if users:
            return HttpResponse("1")
        else:
            return HttpResponse("system not this user")

