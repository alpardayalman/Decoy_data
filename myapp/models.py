from django.db import models

class SampleData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.value}"
