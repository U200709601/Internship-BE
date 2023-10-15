from rest_framework import serializers

from . import models



class GlobalOperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.GlobalOperator
        fields = [
            "created",
            "status",
            "fqdn",
            "name",
            "last_updated",
        ]

