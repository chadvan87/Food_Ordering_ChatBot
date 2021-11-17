from django.urls import path
from.import views  # import views from current directory

urlpatterns = [
    path('', views.index, name='index'),  # get html file

    path('getResponse', views.getResponse,
         name='getResponse')  # get response from user

]
