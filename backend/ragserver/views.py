from .models import Conversation
from .serializers import ConvSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', 'PUT'])
def conversation_list(request):

    # should return all conversation titles
    if request.method == 'GET':
        # if no specific convo to get, return all objects
        if request.param == 'wala':
          conversations = Conversation.objects.all()
          serializer = ConversationSerializer(conversations, many=True)
          return Response(serializer.data)

        cid = request.param.id 
        # find object
        # return object

    # should create a new conversation
    elif request.method == 'POST':
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # should update conversation with new messagea
    elif request.method == 'PUT':