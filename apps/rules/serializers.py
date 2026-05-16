from rest_framework import serializers

from .models import BlockingRule


class BlockingRuleSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = BlockingRule

        fields = "__all__"