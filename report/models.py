from django.db import models

class createreport(models.Model):
    title = models.CharField(max_length=122)
    description = models.TextField()

    def __str__(self):
        return self.title