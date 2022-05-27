from django.core.exceptions import ValidationError
from django.db import models


def split_value(value):
    if ',' not in value:
        raise ValidationError('Ingredients must be separated by ","')


class Recipe(models.Model):
    TITLE_MAX_LEN = 30
    INGREDIENTS_MAX_LEN = 250

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    image = models.URLField()

    description = models.TextField()

    ingredients = models.CharField(
        max_length=INGREDIENTS_MAX_LEN,
        validators=(
            split_value,
        ),
    )

    time = models.IntegerField()
