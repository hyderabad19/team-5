from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_progman = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='topics')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ResourceType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="resources")
    created_at = models.DateTimeField(auto_now_add=True)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Comments')
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE, related_name='comments', default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.text


class Like(models.Model):
    user = models.ForeignKey(Teacher,on_delete=models.CASCADE, related_name='likes')
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.text


class Notification(models.Model):
    icon = models.FileField(null=True, blank=True)
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.text
       
class Video_log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
#     text = models.TextField('Question')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text
#
#
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
#     text = models.CharField('Answer', max_length=255)
#     is_correct = models.BooleanField('Correct answer', default=False)
#
#     def __str__(self):
#         return self.text
