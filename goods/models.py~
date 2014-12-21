from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import pre_save


class Bases(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")
	size = models.CharField(max_length=50,verbose_name="Розмір",help_text="Якщо декілька то через Х, вводити у см")

	class Meta:
		verbose_name="Основа"
		verbose_name_plural="Основи"

	def __str__(self):
		return self.name +", Размер :" + self.size + " см"

class Technics(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")

	class Meta:
		verbose_name="Техніка"
		verbose_name_plural="Техніки"

	def __str__(self):
		return self.name

class Materials(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")	

	class Meta:
		verbose_name="Матеріал"
		verbose_name_plural="Матеріали"

	def __str__(self):
		return self.name

class Colors(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")

	class Meta:
		verbose_name="Колір"
		verbose_name_plural="Кольори"

	def __str__(self):
		return self.name

class Holidays(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")
	date = models.CharField(max_length=100,verbose_name="Дата проходження",help_text="Приклад: c 19 января по 25 марта")

	class Meta:
		verbose_name="Свято"
		verbose_name_plural="Свята"

	def __str__(self):
		return self.name + " : " + self.date

class Styles(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")

	class Meta:
		verbose_name="Стиль"
		verbose_name_plural="Стилі"

	def __str__(self):
		return self.name

 
class Goods(models.Model):
	name = models.CharField(max_length=100,verbose_name="Назва")
	base = models.ForeignKey(Bases,verbose_name="Основа")
	technic = models.ForeignKey(Technics,verbose_name="Техніка")
	price = models.PositiveSmallIntegerField(verbose_name="Ціна")
	material = models.ManyToManyField(Materials,verbose_name="Матеріал")
	description = RichTextField(verbose_name="Опис")
	color = models.ForeignKey(Colors,verbose_name="Колір")
	holiday = models.ForeignKey(Holidays,verbose_name="Свято")
	
	CHILD = 'C'
	TINAGER = 'T'
	MID = 'M'
	HIGH = 'H'
	OVER = 'O'
	AGES_CHOICES = ((CHILD, 'Для детей') , (TINAGER,'Для подростков'), (MID, 'Для молодых'), (HIGH, 'Для среднего возраста'), (OVER, 'Для пожилых'))
	age = models.CharField(max_length=1,choices=AGES_CHOICES,default=MID,verbose_name="Вік")
	
	MAN = 'M'
	WOMAN = 'W'
	US = 'U' 
	CONSUMER_CHOICES = ((MAN, 'Мужчине') , (WOMAN,'Женщине'), (US, 'Унисекс'))
	consumer = models.CharField(max_length=1,choices=CONSUMER_CHOICES,default=US,verbose_name="Пол")
	pub_date = models.DateTimeField(default=timezone.now(),verbose_name="Дата публікації") # date published on site
	count = models.SmallIntegerField(default=-1,verbose_name="Кількість")
	visites = models.PositiveIntegerField(default=0,verbose_name="Відвідування")
	buys = models.PositiveIntegerField(default=0,verbose_name="Покупки")
	style = models.ForeignKey(Styles,verbose_name="Стилі")
	avatar = models.ImageField(upload_to="goods", verbose_name="Фото")#change on server

	class Meta:
		verbose_name="Товар"
		verbose_name_plural="Товари"

	def __str__(self):
		return self.name

	def visitesUp(self):
		pass
		self.visites += 1

	def buysUp(self):
		self.buys += 1

	def save(self):
		self.pub_date = timezone.now()
		super(Goods, self).save()

	def is_visible(self):
		if self.count >= 0: return self
	#Image Magic
