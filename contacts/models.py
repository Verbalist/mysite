from django.db import models
from ckeditor.fields import RichTextField

class Contacts(models.Model):
	name = models.CharField(max_length=100,verbose_name="Повне Ім’я")
	tel = models.CharField(blank=True,max_length=20,verbose_name="Телефон")
	email = models.EmailField(verbose_name="Email")
	address = models.CharField(blank=True,max_length=100,verbose_name="Адреса",help_text="Назва вулиці, номер будинку ")
	description = RichTextField(verbose_name="Опис")
	avatar = models.ImageField(upload_to="contacts",verbose_name="Фото")#change on server
	socialNetwork = models.URLField(verbose_name="Cоцмережа",help_text="Декілька через /")
	isPartner = models.BooleanField(verbose_name="Чи є партнером?")

	class Meta:
		verbose_name = "Контакт"
		verbose_name_plural = "Контакти"

	def __str__(self):
		if self.isPartner:
			return "Партнер : "+ self.name
		else:
			return self.name
	
