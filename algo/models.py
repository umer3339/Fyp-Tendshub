from django.db import models

# Create your models here.

class Feedback(models.Model):
    post_id=models.IntegerField()
    username=models.CharField(max_length=255)
    feedback_comment=models.CharField(max_length=255)

    def __str__(self):
        return "Post_id : " + str(self.post_id) + " Username :"+self.username


class ContactForm(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    messege=models.TextField()

    def __str__(self):
        return "Name : "+self.name + " Subject : "+self.subject