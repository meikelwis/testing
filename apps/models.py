from django.db import models

# Create your models here.
class CubeDetail(models.Model):
	cube_header = models.ForeignKey('CubeHeader', models.DO_NOTHING)
	currency = models.CharField(max_length=10)
	rate = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		managed = True
		db_table = 'cube_detail'



class CubeHeader(models.Model):
	time = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		managed = True
		db_table = 'cube_header'
