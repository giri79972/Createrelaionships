from django.contrib import admin

# Register your models here.
from .models import Auther,Publisher,Student,Book
# Register your models here.

class AdminAuther(admin.ModelAdmin):
    list_display = ['aname','amail']
class AdminPublisher(admin.ModelAdmin):
    list_display = ['pname','copies']
class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','mobile']
class AdminBook(admin.ModelAdmin):
    list_display = ['bname','bcost']

admin.site.register(Auther,AdminAuther)
admin.site.register(Publisher,AdminPublisher)
admin.site.register(Student,AdminStudent)
admin.site.register(Book,AdminBook)

