from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from instawork_assignment.contrib.models import BaseModel


class Member(BaseModel):

    '''
        Member class, columns on db table
        first_name, last_name, email, phone, role, id, created, updated
    '''

    ADMIN = 'admin'
    REGULAR = 'regular'
    ROLE_CHOICE = (
        (ADMIN, 'Admin'),
        (REGULAR, 'Regular')
    )

    first_name = models.CharField(
        'First Name',
        max_length=127,
        blank=True
    )
    last_name = models.CharField(
        'Last Name',
        max_length=127,
        blank=True
    )
    email = models.EmailField(
        'Email',
        max_length=254,
        null=True,
        blank=True,
        default=None,
        help_text='Required. A valid email address.',
        error_messages={
            'unique': "A user with that email id already exists.",
        },
    )
    phone = PhoneNumberField(
        blank=True,
        help_text='A Valid phone number',
    )

    role = models.CharField(
        'Role',
        max_length=127,
        choices=ROLE_CHOICE,
        default=REGULAR
    )

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
