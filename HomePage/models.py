from django.db import models

# Create your models here.
#Create test db
class Article(models.Model):
	"""docstring for Article"""
	class Meta():
		db_table = 'article'
			
	article_titel = models.CharField(max_length = 200)
	article_rate = models.CharField(max_length = 200)

	def __str__(self):
		return self.article_titel + '___' + self.article_rate
#Create Followers db
class Followers(models.Model):
	"""docstring for Followers"""
	class Meta():
		db_table = 'Followers'
			
	user_email = models.CharField(max_length = 200)
	user_name = models.CharField(max_length = 200)

	def __str__(self):
		return self.user_email
		