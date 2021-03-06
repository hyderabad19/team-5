from django.contrib import admin
from .models import Category, Topic, ResourceType, Resource, User, Comment


# Register your models here.
class TopicInline(admin.StackedInline):
    model = Topic


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Resource)
admin.site.register(ResourceType)
admin.site.register(Topic)
admin.site.register(User)
admin.site.register(Comment)

admin.site.site_header = "Learnovate Admin"
admin.site.site_title = "Learnovate Admin"
admin.site.index_title = "Welcome to Learnovate Admin Portal"
