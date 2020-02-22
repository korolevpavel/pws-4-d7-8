from django import forms
from p_library.models import Author, Book, BooksOnHand, UserProfile
from django.forms import formset_factory


class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BooksOnHandForm(forms.ModelForm):

    class Meta:
        model = BooksOnHand
        fields = '__all__'

class ProfileCreateForm(forms.ModelForm):  
  
    class Meta:  
        model = UserProfile  
        fields = '__all__'
