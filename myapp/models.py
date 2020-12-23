from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.name, self.address)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']