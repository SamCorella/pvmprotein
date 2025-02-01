from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255) # Plant or Meat
    
    # protein and other nutrient info ...

    def __str__(self):
        return self.name