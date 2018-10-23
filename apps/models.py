from django.db import models

class Currency(models.Model):
	from_currency = models.CharField(max_length=10)
	to_currency = models.CharField(max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		managed = True
		db_table = 'currency'

class CurrencyRate(models.Model):
	date = models.DateField()
	from_currency_name = models.CharField(max_length=10)
	to_currency_name = models.CharField(max_length=10)
	rate = models.DecimalField(max_digits=10, decimal_places=5, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		managed = True
		db_table = 'currency_rate'
