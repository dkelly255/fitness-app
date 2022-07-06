from django.db import models


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Enquiries'

    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.email
