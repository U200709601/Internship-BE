from django.db import models
from django.urls import reverse
from django.contrib.postgres import fields as postgres_fields


class GlobalOperator(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.SmallIntegerField()
    fqdn = postgres_fields.ArrayField(models.CharField(max_length=255))
    name = models.CharField(max_length=60)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("operator_GlobalOperator_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("operator_GlobalOperator_update", args=(self.pk,))



