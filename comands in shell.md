# News
1.	Создать двух пользователей (с помощью метода User.objects.create_user('username')). 

from news.models import User

user1 = User.objects.create_user('Bill Totonto')
user2 = User.objects.create_user('Guy Richy')

2.	Создать два объекта модели Author, связанные с пользователями.
from news.models import Author

Author.objects.create(author = user1)
Author.objects.create(author = user2)

3.	Добавить 4 категории в модель Category
from NewsPaper.models import Category
Category.objects.create(article_category = 'sport') # (id=1)
Category.objects.create(article_category = 'politics')
Category.objects.create(article_category = 'education')
Category.objects.create(article_category = 'culture')# (id=4).
4.	Добавить 2 статьи и 1 новость.
from news.models import Post
author = Author.objects.get(id=1)

Post.objects.create(
post_author = author, 
category = 'A', 
title = 'The Record', 
content = 'Long text'
)

Post.objects.create(
post_author = author, 
category = 'A', 
title = 'The Magic', 
content = 'Not very long story'
)


Post.objects.create(
post_author = author, 
category = 'N', 
title = 'Some news', 
content = 'We have launched a new project'
)


5.	Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))

Post.objects.get(id=1).post_category.add(Category.objects.get(id=4))
6.	Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
from news.models import *
Comment.objects.create(
                      comment_post=Post.objects.get(id=1),
                      comment_user=Author.objects.get(id=1).author, 
                      feedback_text = 'Very interesting article'
                      )

Comment.objects.create(
                      comment_post=Post.objects.get(id=2), 
                      comment_user = Author.objects.get(id=1).author,
                      feedback_text = 'It is interesting'
                      )

Comment.objects.create(
                      comment_post = Post.objects.get(id=3), 
                      comment_user = Author.objects.get(id=2).author, feedback_text = "Wow, that's awesome"
                      )

Comment.objects.create(
                      comment_post=Post.objects.get(id=1), 
                      comment_user = Author.objects.get(id=2).author, feedback_text = 'It is okay'
                      )

7.	Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Comment.objects.get(id=1).like()
Post.objects.get(id=1).dislike()
Post.objects.get(id=3).like()

8.	Обновить рейтинги пользователей.
u1 = Author.objects.get(id=1)
u1.update_rating()
u1.user_rate

u2 = Author.objects.get(id=2)
u2.update_rating()
u2.user_rate


9.	Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
s = Author.objects.order_by('user_rate')
for i in s:
	i.user_rate
	i.author.username

10.	Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
p = Post.objects.order_by('-post_rate')
for i in p[:1]:
	i.date_created
	i.post_author.author
	i.post_rate
	i.title
	i.preview()

11.	Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Post.objects.all().order_by('-post_rate')[0].comment_set.values(
'comment_date_created', 
'comment_user', 
'comment_rate', 'feedback_text'
)


