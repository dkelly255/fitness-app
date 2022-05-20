from django.db import models


class Contact(models.Model):
    
    class Meta:
        verbose_name_plural = 'Enquiries'
    
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email