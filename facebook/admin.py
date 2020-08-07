from django.contrib import admin
from .models import CategoriesProducts, ProductFB


# class AdminCategoriesFB(admin.ModelAdmin):
#     list_display = ['category']
#
#
# class AdminProductFB(admin.ModelAdmin):
#     list_display = ['name', 'price', 'count', 'description']
#     list_editable = ['price', 'count']


# admin.register(CategoriesProducts, AdminCategoriesFB)
# admin.register(ProductFB, AdminProductFB )


admin.site.register(CategoriesProducts)
admin.site.register(ProductFB)