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
            gender=params.get('gender'),
        )
        return HttpResponse("Add user succeed")
