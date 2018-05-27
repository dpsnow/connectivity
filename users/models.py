from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
# import uuid


class User(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                       help_text="Unique ID for this particular user")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('user-data', args=[str(self.id)])
