# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField("Название категории",
                            max_length=128)
    description = models.TextField("Описание категории",
                                   blank=True)

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"

    def __unicode__(self):
        return self.name


class ProductAttributes(models.Model):
    name = models.CharField("Характеристика товара",
                            max_length=128,
                            help_text="Страна, материал и т.п.")
    value = models.CharField("Значение",
                             max_length=128)

    class Meta:
        verbose_name = "Характеристика товара"
        verbose_name_plural = "Характеристики товаров"

    def __unicode__(self):
        return "{} - {}".format(self.name, self.value)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 related_name="products",
                                 verbose_name="Категория товара")
    name = models.CharField("Название",
                            max_length=128)
    slug = models.SlugField('Ссылка-метка',
                            max_length=64,
                            unique=True)
    photo = models.ImageField("Изображение",
                              upload_to='products')
    code = models.CharField("Код (Артикул)",
                            max_length=128,
                            unique=True)
    external_link = models.URLField("Ссылка на товар",
                                    blank=True,
                                    help_text='Ссылка на товар с сайта missmexx.ru')
    description = models.TextField("Описание",
                                   blank=True)
    size = models.CharField("Размер",
                            max_length=128,
                            blank=True)
    price = models.DecimalField("Цена",
                                max_digits=12,
                                decimal_places=2,
                                blank=True,
                                null=True)
    attributes = models.ManyToManyField(ProductAttributes,
                                        related_name="products",
                                        verbose_name="Дополнительные атрибуты",
                                        blank=True,
                                        null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __unicode__(self):
        return self.name