from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField('Mavzu', max_length=50, null=True, blank=True)
	author = models.CharField('Muallif', max_length=50, default="Nomalum", blank=True)
	image = models.FileField('Rasm', null=True, blank=True)
	text = models.TextField('Matn', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])


