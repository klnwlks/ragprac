from .models import Conversation
from .serializers import ConvSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def convo(request):
  # v simple implementation
  # i get a message, i run the message thru the database, it returns a message for me to display
  if request.method == 'POST':
    data = request.data
  