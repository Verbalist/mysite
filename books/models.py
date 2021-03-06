from django.db import models
from goods.models import Colors, Styles, Technics, Goods, Bases

class Books(models.Model):
	technic = models.ForeignKey(Technics,verbose_name="Техніка")
	base = models.ForeignKey(Bases,verbose_name="Основа")
	style = models.ForeignKey(Styles,verbose_name="Стиль")
	description = models.CharField(max_length=1000,verbose_name="Опис товару")
	telephone = models.CharField(max_length=20,verbose_name="Телефон",blank=True)
	email = models.EmailField(verbose_name="Email")
	color = models.ForeignKey(Colors,verbose_name="Колір",blank=True)
	address = models.CharField(max_length=200,blank=True)
	age = models.CharField(max_length=1,choices=Goods.AGES_CHOICES,default=Goods.MID,verbose_name="Вік")
	price = models.PositiveSmallIntegerField(verbose_name="Ціна")
	pub_date = models.DateTimeField(verbose_name="Дата заказу")

	class Meta:
		verbose_name="Замовлення"
		verbose_name_plural="Замовлення"		

	def __str__(self):
		self.book + "-> ціна:" + str(self.price)
	
	def save(self):
		self.pub_date = timezone.now()
		super(Books, self).save()
