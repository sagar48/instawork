
from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    '''
        Member class data serializer,
        validate data on post, put, patch
    '''

    class Meta:
        model = Member
        fields = (
            'id', 'first_name', 'last_name', 'phone', 'email', 'role'
        )
        read_only_fields = ('id', )
