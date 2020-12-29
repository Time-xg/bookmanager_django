from django.urls import path
import user.views


urlpatterns = [

    path('creatUser/', user.views.CreatUser.as_view()),

]