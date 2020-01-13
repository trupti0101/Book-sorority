from django.conf.urls import url
from logintestapp.views import login, confirmlogout, logout, register

urlpatterns = [	
	url(r'^login/$', login, name='login'),
	url(r'^confirmlogout/$', confirmlogout, name='confirmlogout'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^register/$', register, name='register'),	
]