from django.contrib import admin

from core.models import Blog, Recipe

# Register your models here.


class SlugConfig(admin.ModelAdmin):
    model = [Blog, Recipe]
    readonly_fields = ['slug', 'created_at', 'updated_at']


admin.site.register(Blog, SlugConfig)

admin.site.register(Recipe, SlugConfig)
