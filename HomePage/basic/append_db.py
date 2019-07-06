from HomePage.basic import pars
from HomePage.models import Article

#def test():
#	new_post = Article(article_titel = 'EU', article_rate = '200')
#	new_post.save()
#	posts = Article.objects.all()
#	return posts

def create():
	pars_list = pars.main()
	return pars_list