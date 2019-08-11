from rest_framework import serializers, viewsets
from api.models import Companies

class CompaniesSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = [
			'name',
			'address',
			'city',
			'state',
			'created_at',
			'value',
			'date_modified'
		]
