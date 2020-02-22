from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publisher', 'price', 'image')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendRegister(admin.ModelAdmin):
    pass

@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass