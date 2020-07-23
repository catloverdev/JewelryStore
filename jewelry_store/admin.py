from django.contrib import admin
from django.utils.safestring import mark_safe

from jewelry_store.models import *
# Register your models here.


# декоратор
@admin.register(CategoriesProduct)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name", )
    search_fields = ("name", )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id_product", "title", "get_latest_price", "material", "get_image", "with_gems")
    list_display_links = ("title",)
    list_filter = ("category", "material", "with_gems")
    search_fields = ("title", "material__id")
    save_as = True
    save_on_top = True
    readonly_fields = ('get_latest_price', 'get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="90"')

    get_image.short_description = "Изображение"


@admin.register(ProductPrice)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("product", "price", "date")
    list_filter = ("date", )
    search_fields = ("product", "date")
    readonly_fields = ("product", "price", "date")


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "probe")
    list_filter = ("name", "probe")
    search_fields = ("name", "probe")


@admin.register(Gems)
class GemsAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name", )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id_purchase", 'client', 'date')
    list_filter = ("id_purchase",)
    search_fields = ("id_purchase",)
    readonly_fields = ("id_purchase", 'client', 'date')


@admin.register(AllPurchases)
class AllPurchasesAdmin(admin.ModelAdmin):
    list_display = ("purchase", 'product', 'price', 'amount')
    list_filter = ("purchase",)
    search_fields = ("purchase",)
    readonly_fields = ("purchase", 'product', 'price', 'amount')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("purchase", 'date', 'status')
    list_filter = ("purchase", 'status')
    search_fields = ("purchase",)
    readonly_fields = ("purchase", 'date', 'status')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'phone')
    search_fields = ('id', 'phone',)
    readonly_fields = ("name", 'email', 'phone')


admin.site.site_title = "Ювелирный магазин"
admin.site.site_header = "Ювелирный магазин"
