from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Cart, Notification
from books.models import Books
from django.contrib.auth.models import User

@login_required()
def buy(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			item = Books.objects.get(id = request.GET.get('bid', ''))
			notification = Notification(buyer_id=request.session['user_id'], book_id=request.GET.get('bid', ''), seller=request.GET.get('sid', ''))
			notification.save()
			if item is not None and notification is not None:
				arg={'item': item}
				return render(request,'cart/bought.html', arg)
			else:
				return render(request, 'cart/buy.html')
	else:
		try:
			n = Notification.objects.get(buyer_id=request.session['user_id'], book_id=request.GET.get('bid', ''), seller=request.GET.get('sid', ''))
			return render(request, 'cart/buy.html', {'sent':'sent'})
		except:
			return render(request, 'cart/buy.html')

def notification(request):
	if request.user.is_authenticated:
		u = request.session['user_id']
		n = Notification.objects.all().filter(seller=u)
		user_list=User.objects.all()
		arg={'n':n,'user_list':user_list}
		return render(request,'cart/notifications.html',arg)

def myorders(request):
    cart = Cart.objects.all().filter(user_id=request.session['user_id'])
    return render(request, 'cart/myorders.html', {'cart':cart})

def delete(request):
	if request.method == 'POST':
		b = Books.objects.get(pk = request.GET.get('b', ''))
		b.sold=1
		b.save()
		notification = Notification.objects.get(book_id = request.GET.get('b', ''))
		item=Cart(user_id=notification.buyer_id, book_id=request.GET.get('b', ''))
		item.save()
		n = Notification.objects.filter(book_id = request.GET.get('b', ''))
		n.delete()
		return HttpResponseRedirect('/books/list')
	else:
		return render(request, 'cart/delete.html', {'msg':'This will delete the book and the notification.'})

def deletenotification(request):
	if request.method == 'POST':
		n = Notification.objects.filter(book_id = request.GET.get('b', ''))
		n.delete()
		return HttpResponseRedirect('/cart/notify')
	else:
		return render(request, 'cart/delete.html', {'msg':'This will delete the notification.'})