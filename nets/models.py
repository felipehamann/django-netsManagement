from django.db import models

class Net(models.Model):
    net_id = models.CharField(max_length=20, unique=True)
    dimensions = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    movement = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.net_id} - {self.company}"