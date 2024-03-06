from django.db import models

class CRUD(models.Model):
    name=models.CharField(max_length=150, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
#     {self.id}


