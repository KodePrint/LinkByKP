from django.db import models

# Create your models here.


class Detail(models.Model):
    """Model definition for Detail."""

    # TODO: Define fields here
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        """Meta definition for Detail."""

        verbose_name = 'Detail'
        verbose_name_plural = 'Details'

    def __str__(self):
        """Unicode representation of Detail."""
        pass


