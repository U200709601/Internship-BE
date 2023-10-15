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


class PortabilityDatabaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PortabilityDatabase
        fields = [
            "access_certificate",
            "status",
            "access_credentials",
            "last_updated",
            "access_type",
            "access_private_key",
            "created",
            "country",
            "number_type",
        ]


class NetworkOperatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NetworkOperator
        fields = [
            "created",
            "status",
            "last_updated",
            "name",
            "country",
        ]
