from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Solution(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	likes = models.IntegerField()
	hint = models.TextField()
	soultion = models.TextField()
	code = models.TextField()
	question = models.IntegerField(null = True)

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	level = models.IntegerField(default=0)
	solution_of = models.ForeignKey(Solution,on_delete=models.CASCADE)
	next_comment = models.ForeignKey('self',related_name='%(class)s_next_comment',on_delete=models.CASCADE,null=True,blank=True,default=None)
	last_comment = models.ForeignKey('self',related_name='%(class)s_last_comment',on_delete=models.SET_NULL,null=True,blank=True)
	# top = models.BooleanField(default = True)
	# parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)


	def __str__(self):
		return self.content

# class Reply(models.Model):
# 	user = models.ForeignKey(User,on_delete=models.CASCADE)
# 	content = models.TextField()
# 	likes = models.IntegerField()
# 	parent = models.ForeignKey(Comment,on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.content

class Liked_by(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	solution = models.ForeignKey(Solution,on_delete=models.CASCADE)
