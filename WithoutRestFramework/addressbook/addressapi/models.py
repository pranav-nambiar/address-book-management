from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
# Create your models here.

# def only_numeric_house_numbers(value):
#     pass


class Contact(models.Model):
    name = models.CharField(max_length=50, default=None)

    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                        message = 'Phone numbers must be 10 digits. Please omit the country code.')
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    # house_number = models.IntegerField(validators=[MinValueValidator(1)])
    house_number = models.PositiveIntegerField()
    address_line_1 = models.CharField(max_length=100, default=None)
    address_line_2  = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=20, default=None)
    country = models.CharField(max_length=20, default=None)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Contact, self).save(*args, **kwargs)