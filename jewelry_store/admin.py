from django.contrib import admin
from django.utils.safestring import mark_safe

from jewelry_store.models import *
# Register your models here.


# декоратор
@admin.register(CategoriesProduct)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    list_display_links = ("name", )
    search_fields = ("name", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id_product", "title", "get_latest_price", "material", "get_image", "with_gems")
    list_display_links = ("title",)
    list_filter = ("category", "material", "with_gems")
    search_fields = ("title", "material__id")
    save_as = True
    readonly_fields = ('get_latest_price', 'get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="90"')

    get_image.short_description = "Изображение"


@admin.register(ProductPrice)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("product", "price", "date")
    list_filter = ("date", )
    search_fields = ("product", "date")
    list_editable = ("price", )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "probe")
    list_filter = ("name", "probe")
    search_fields = ("name", "probe")


@admin.register(Gems)
class GemsAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name", )


# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ("name",)
#     list_filter = ("name",)


admin.site.register(Purchase)
admin.site.register(AllPurchases)
admin.site.register(Status)
admin.site.register(Client)

admin.site.site_title = "Ювелирный магазин"
admin.site.site_header = "Ювелирный магазин"
