import django_filters

from shareandcare.foodpost import models


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = models.FoodPost
        fields = [
            'country', 'city',
        ]
