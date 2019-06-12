
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Member
from .serializers import MemberSerializer


class MemberListCreateView(ListCreateAPIView):

    '''
        Fetch members list on GET method
        Create new member on POST method, required JSON data in request body
    '''

    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    '''
        Fetch member detail on GET method
        Update member detail, partial update on PUT & PATCH
        Delete member on DELETE method
    '''

    serializer_class = MemberSerializer
    queryset = Member.objects.all()
