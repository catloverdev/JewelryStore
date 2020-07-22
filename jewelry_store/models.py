from django.db import models
from datetime import date


# Create your models here.
from django.urls import reverse


class Material(models.Model):
    """Материалы"""
    name = models.CharField("Имя", max_length=149)
    probe = models.PositiveSmallIntegerField("Проба", default=0)

    def __str__(self):
        return f"{self.name}, {self.probe}"

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"


class Gems(models.Model):
    """Драгоценные камни"""
    id_gem = models.AutoField("Номер вставки", primary_key=True)
    name = models.CharField("Камень", max_length=149, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Драгоценный камень"
        verbose_name_plural = "Драгоценные камни"


class Client(models.Model):
    """"Клиент"""
    name = models.CharField("Имя", max_length=149)
    email = models.EmailField()
    phone = models.CharField("Телефон", max_length=16, unique=True)

    def __str__(self):
        return f"{self.name}, {self.phone}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class CategoriesProduct(models.Model):
    """Категории"""
    # parent_category = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL,
    #                                     blank=True, null=True)
    name = models.CharField("Категория", max_length=149)
    url = models.SlugField(max_length=199, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_list", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """"Продукты"""
    id_product = models.AutoField("Артикул", primary_key=True)
    category = models.ManyToManyField(CategoriesProduct, verbose_name="Категория", related_name="product_categories")
    material = models.ForeignKey(Material, verbose_name="Материал", on_delete=models.SET_NULL, null=True)
    gems = models.ManyToManyField(Gems, verbose_name="Драгоценные камни", related_name="product_gems", blank=True)
    with_gems = models.BooleanField("Со вставками", default=True)
    title = models.CharField("Название", max_length=149)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="products/")
    url = models.SlugField(max_length=199, unique=True)
    weight_material = models.FloatField("Вес металла", default=0, help_text="граммы")
    weight_one_gem = models.FloatField("Вес одного камня", default=0, help_text="караты")
    amount = models.PositiveSmallIntegerField("Количество камней (данного типа)", default=0, help_text="шт")

    def __str__(self):
        return f"Артикул: {self.id_product} ({self.title})"

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    def get_stone(self):
        return self.gems.first()

    def get_latest_price(self):
        return self.productprice_set.latest('date').price

    get_latest_price.short_description = "Цена"

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"


class Purchase(models.Model):
    """"Покупка"""
    id_purchase = models.AutoField("Номер покупки", primary_key=True)
    client = models.ForeignKey(Client, verbose_name="Номер клиента", on_delete=models.CASCADE)
    date = models.DateField("Дата покупки", default=date.today)
    product = models.ManyToManyField(Product, verbose_name="товары в покупке",
                                     related_name="product_purchases", through='AllPurchases')

    def __str__(self):
        return f"{self.id_purchase}, {self.client}, {self.date}"

    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"


class AllPurchases(models.Model):
    """"Все покупки"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField("Количество товара", default=0)

    def __str__(self):
        return f"{self.product} {self.purchase} {self.amount}"

    class Meta:
        verbose_name = "Все покупки"
        verbose_name_plural = "Все покупки"
        constraints = [
            models.UniqueConstraint(fields=['product', 'purchase'], name='unique purchases')
        ]


class ProductPrice(models.Model):
    """Цены"""
    product = models.ForeignKey(Product, verbose_name="Номер продукта", on_delete=models.CASCADE)
    date = models.DateField("Дата изменения", default=date.today)
    price = models.PositiveIntegerField("Цена", default=0, help_text="руб.")

    def __str__(self):
        return f"{self.product} {self.date} {self.price}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
        constraints = [
            models.UniqueConstraint(fields=['product', 'date'], name='unique price')
        ]


class Status(models.Model):
    """Статус покупки"""
    purchase = models.ForeignKey(Purchase, verbose_name="Номер покупки", on_delete=models.CASCADE)
    date = models.DateField("Дата изменения", default=date.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.purchase} {self.date} {self.status}"

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"
        constraints = [
            models.UniqueConstraint(fields=['purchase', 'date'], name='unique status')
        ]
