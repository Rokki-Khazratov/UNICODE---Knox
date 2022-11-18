from django.contrib import admin
from .models import Components,Users,Tags,Site


admin.site.register(Components)
admin.site.register(Users)
admin.site.register(Tags)
admin.site.register(Site)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
