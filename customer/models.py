from django.db import models
from django.urls import reverse
from drug.models import User


AGE_GROUP = (
    ('Adult', 'Adult'),
    ('Child', 'Child'),
)


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=50)
    customer_second_name = models.CharField(max_length=50, blank=True, null=True)
    customer_last_name = models.CharField(max_length=50)
    customer_email = models.EmailField(blank=True, null=True)
    customer_age_bracket = models.CharField(choices=AGE_GROUP, max_length=10, )
    customer_added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_added_on = models.DateTimeField(auto_now_add=True)
    customer_order_stat = models.BooleanField(default=False)

    # customer_phone_number = models.CharField()

    @property
    def get_full_name(self):
        full_name = self.customer_first_name + '_' + self.customer_last_name
        return full_name

    def get_absolute_url(self):
        return reverse('customer:customer_detail', kwargs={
            'customer_name': self.get_full_name,
            'pk': self.pk,
        })

    def __str__(self):
        return self.customer_last_name
