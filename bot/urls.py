from django.urls import path
from.import views  # import views from current directory

urlpatterns = [
    path('', views.index, name='index'),  # get request from user
    
    path('specific', views.specific, name='specific'),
    
    path('getResponse',views.getResponse,name='getResponse')
    #path('order/<int:order_id>',views.order,name='order') #add parameter to a url
]
