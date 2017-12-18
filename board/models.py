from django.db import models
from django.utils import timezone
from django.urls import reverse
from django import forms

def min_length_3_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('3글자 이상 입력해주세요')


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, validators=[min_length_3_validator])
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    modified_date = models.DateTimeField(
            blank=True, null=True)

    def get_absolute_url(self): # redirect시 활용
        return reverse('board:post_detail', args=[self.id])

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     post = models.ForeignKey('board.Post', related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comment = True;
#         self.save()
    
#     def __str__(self):
#         return self.text