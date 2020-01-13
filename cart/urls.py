from django.urls import path
from . import views

urlpatterns = [
	path('buy', views.buy, name='buy'),
	path('notify', views.notification, name='notify'),
	path('deletenotification', views.deletenotification, name='deletenotification'),
    path('myorders', views.myorders, name='myorders'),
	path('delete', views.delete, name='delete')
]