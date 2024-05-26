#进行users子应用的视图路由
from django.urls import path
from users.views import RegisterView
urlpatterns = [
    #参数①：路由
    #参数②：视图函数
    path('register/',RegisterView.as_view()),
]