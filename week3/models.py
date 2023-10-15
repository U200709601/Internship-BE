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


class PortabilityDatabase(models.Model):

    # Relationships
    country = models.ForeignKey("utils.Country", on_delete=models.CASCADE)
    number_type = models.ForeignKey("utils.NumberType", on_delete=models.CASCADE)

    # Fields
    access_certificate = models.BinaryField(null=True, blank=True, editable=True)
    status = models.SmallIntegerField()
    access_credentials = models.JSONField(default=dict)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    access_type = models.SmallIntegerField()
    access_private_key = models.BinaryField(null= True, blank= True, editable=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("operator_PortabilityDatabase_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("operator_PortabilityDatabase_update", args=(self.pk,))
        

class NetworkOperator(models.Model):

    # Relationships
    country = models.ForeignKey("utils.Country", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.SmallIntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=60)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("operator_NetworkOperator_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("operator_NetworkOperator_update", args=(self.pk,))

