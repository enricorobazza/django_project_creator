from django.db import models

# Create your models here.
class Settings(models.Model):
    CHOICES = ((True, 'Sim'), (False, 'Não'))

    project_name = models.CharField(max_length=100)
    project_slug = models.CharField(max_length=100)
    heroku = models.BooleanField(max_length=100, choices=CHOICES)
    bootstrap = models.BooleanField(max_length=100, choices=CHOICES)
    custom_accounts = models.BooleanField(max_length=100, choices=CHOICES)

    def __str__(self):
        return self.project_name

    def as_dict(self):
        return {
            "project_name": "%s"%self.project_name,
            "project_slug": "%s"%self.project_slug,
            "heroku": self.heroku,
            "bootstrap": self.bootstrap,
            "custom_accounts": self.custom_accounts
        }