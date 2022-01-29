from distutils.command.upload import upload
from enum import unique
from django.db import models

from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel


class MeasureUnit(BaseModel):

    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):

    description = models.CharField(max_length=50, unique=True, null=False, blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE)

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Category Product '
        verbose_name_plural = 'Category Products'

    def __str__(self):
        return self.description


class Indicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default=0)
    cateory_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Offer Indicator'
        verbose_name_plural = 'Offer Indicators'

    def __str__(self):
        return f'Category offer {self.cateory_product}:{self.descount_value}%'


class Product(BaseModel):
    
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name