from django.contrib import admin

# Register your models here.
from testapp.models  import  Author,Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','subject']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','release_date','rating']



admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)


