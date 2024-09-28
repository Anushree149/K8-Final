from django.contrib import admin
from.models import Todo,Feedback
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','assign_to','title','deadline','company_name']

admin.site.register(Todo,TodoAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display=['user','experience','type']

admin.site.register(Feedback,FeedbackAdmin)




