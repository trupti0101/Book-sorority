from django import forms
from .models import Books
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Book Title',
			}
		))
	image = forms.ImageField()
	price = forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Price',
			}
		))
	author=forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Author Name',
			}
		))
	genre=forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Genre',
			}
		))
	isbn=forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'ISBN',
			}
		))
	edition=forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Edition',
			}
		))
	publisher=forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Publisher',
			}
		))
	publishyear=forms.CharField(widget=forms.TextInput(
			attrs={
				'placeholder': 'Publish Year',
			}
		))

	class Meta:
		model=Books
		fields=('name', 'image', 'price', 'author', 'genre', 'isbn', 'edition', 'publisher', 'publishyear')

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(CreateForm, self).__init__(*args, **kwargs)

	def save(self,commit=True, *args):
		book=super(CreateForm,self).save(commit=False)
		book.user_id=self.request.session['user_id']
		book.sold=0
		if(commit):
			book.save()
		return book