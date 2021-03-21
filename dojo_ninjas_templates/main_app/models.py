from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    desc= models.CharField(max_length=45, null=True)
    def __repr__(self):
        return f"Dojo  {self.name}  {self.city}  {self.state}  {self.desc}"


class Ninja(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    dojos=models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    def __repr__(self):
        return f"Ninja  {self.first_name}  {self.last_name}"