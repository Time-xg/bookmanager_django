from django.urls import path
import user.views


urlpatterns = [

    path('creatUser/', user.views.CreatUser.as_view()),
    path('userLogin/', user.views.UserLogin.as_view()),
    path('alertPermission/', user.views.AlertPermission.as_view()),

]