from django.db import models

class SupportRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    issue = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
