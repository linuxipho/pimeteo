from django.db import models


class Mesure(models.Model):
    temp = models.DecimalField('température', max_digits=4, decimal_places=2)
    press = models.DecimalField('pression', max_digits=6, decimal_places=2)
    moist = models.DecimalField('humidité', max_digits=4, decimal_places=2)   
    dew = models.DecimalField('point de rosée', max_digits=4, decimal_places=2)
    time = models.DateTimeField('date')


class Live(models.Model):
    temp = models.DecimalField('température', max_digits=4, decimal_places=2)
    press = models.DecimalField('pression', max_digits=6, decimal_places=2)
    moist = models.DecimalField('humidité', max_digits=4, decimal_places=2)   
    dew = models.DecimalField('point de rosée', max_digits=4, decimal_places=2)
    time = models.DateTimeField('date')
