from django.db import models
from workshops.models import Workshops
from ckeditor.fields import RichTextField
from django.utils import timezone

class News(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")
	workshop = models.ForeignKey(Workshops,verbose_name="Майстер клас",blank=True)
	description = RichTextField(verbose_name='Опис')
	pub_date = models.DateTimeField(verbose_name='Дата створення', default=timezone.now()) # date published on site
	avatar = models.ImageField(verbose_name="Фото", upload_to="news")#change on server

	class Meta:
		verbose_name='Новина'
		verbose_name_plural='Новини'

	ordering = ['pub_date']

	def __str__(self):
		return self.name + " : "+str(self.pub_date)

	def save(self):
		self.pub_date = timezone.now()
		super(News, self).save()
