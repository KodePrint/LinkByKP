from django.db import models
from core.models import Detail
from client.models import Branch

# Import Singnals
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Preform(models.Model):
    """Model definition for Preform."""

    STATUS_CHOICES = [
    (0, 'executed'),
    (1, 'Validated'),
    (2, 'Canceled'),
]

    # TODO: Define fields here
    identifier = models.PositiveSmallIntegerField(editable=False, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Branch, on_delete=models.CASCADE)
    total_cost = models.DecimalField(
        max_digits=8, decimal_places=2, editable=False,
        null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        """Meta definition for Preform."""

        verbose_name = 'Preform'
        verbose_name_plural = 'Preforms'

    def generateIdentifier(self):
        identifier = 'LPREF/'+ str(self.client.company.name) + str(self.id) + str(self.date)
        return identifier

    def generateTotalCost(self):
        details = DetailPreform.objects.filter(preform = self.id)
        if details == None:
            self.total_cost = 0
        else:
            for item in details:
                self.total_cost += item.cost


    def __str__(self):
        """Unicode representation of Preform."""
        return '%s, %s, %s' % (self.date, 'Lugar', self.total_cost)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generateTotalCost()



class DetailPreform(Detail):
    """Model definition for DetailPreform."""

    # TODO: Define fields here
    preform = models.ForeignKey(Preform, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for DetailPreform."""

        verbose_name = 'DetailPreform'
        verbose_name_plural = 'DetailPreforms'

    def __str__(self):
        """Unicode representation of DetailPreform."""
        pass

