from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=255) # Plant or Meat
    protein = models.IntegerField(default=0) # Grams of protein
    cost = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)
    
    # Other nutrient info ...

    def __str__(self):
        return self.name