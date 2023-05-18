from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100)
    matn = models.TextField()
    rasm = models.FileField(null=True, blank=True)
    sana = models.DateField()
    def __str__(self):
        return self.sarlavha

