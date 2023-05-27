from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group





class Author(models.Model):

    user_rate = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        
        sum_rating = self.post_set.aggregate(post_rating=Sum('post_rate'))
        result_sum_rating = 0
        try:
            result_sum_rating += sum_rating.get('post_rating')
        except TypeError:
            result_sum_rating = 0

        
        sum_comment_rating = self.author.comment_set.aggregate(comment_rating=Sum('comment_rate'))
        result_sum_comment_rating = 0
        result_sum_comment_rating += sum_comment_rating.get('comment_rating')

        
        self.user_rate = result_sum_rating * 3 + result_sum_comment_rating
        
        self.save()

class Category(models.Model):
    article_category = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.article_category.title()

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    post_category = models.ManyToManyField(Category)

    article = 'A'
    news = 'N'

    POSITIONS = [
        (article, "Статья"),
        (news, "Новость"),
    ]


    category = models.CharField(max_length=1,
                                choices=POSITIONS
                                )


    date_created = models.DateField(auto_now_add=True)

    title = models.CharField(max_length=50)

    content = models.TextField()

    post_rate = models.IntegerField(default=0)

    def like(self):
        self.post_rate += 1

        self.save()



    def dislike(self):
        self.post_rate -= 1

        self.save()

    def __str__(self):
        return f'{self.title.title()}:\n ' \
               f'{self.content}, \n ' \
               f'{self.date_created::%d-%m-%Y}'


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])




    def preview(self):
        return self.content[:125]


class PostCategory(models.Model):
    post_category = models.ForeignKey(Post, on_delete=models.CASCADE)

    category_category = models.ManyToManyField(Category)




class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    comment_date_created = models.DateField(auto_now_add=True)
    comment_rate = models.IntegerField(default=0)


    def like(self):
        self.comment_rate += 1

        self.save()


    def dislike(self):
        self.comment_rate -= 1

        self.save()





class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
# Create your models here.


