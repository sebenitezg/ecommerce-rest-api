from django.http.response import HttpResponseNotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, TestUserSerializer

@api_view(['GET', 'POST'])
def user_api_view(request):
    """
    Retrieve all users, or create a new user
    """
    # List
    if request.method == 'GET':
        # Queryset
        users = User.objects.all()
        # Here, an object list is serialized, i.e., 
        # the object is a list of two or more
        # objects (table elements). Then, many 
        # parameter is set as True (many=True)
        serializer = UserSerializer(users, many=True)

        #------ Test for understanding serilizers operation
        #print(TestUserSerializer())

        test_data = {
            'name':'Usertest',
            'email': 'usertest@test.com'
        } 

        test_serializer = TestUserSerializer(data=test_data)
        if test_serializer.is_valid():
            print("Validation is passed")

        #---------------------------------------------------

        return Response(serializer.data)
    
    # Create
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        # Validation
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successful user creation', 'User information':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk):
    ''' 
    Retrieve, update or delete a user 
    '''
    # Queryset
    user = User.objects.filter(id=pk).first()

    # Validation
    if user:
        # Retrieve
        if request.method == 'GET':
            # Here, an object is serialized, i.e., 
            # and element of table is serilized. 
            # Then, many parameter is set as False
            # (many=False is the defaul value)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        # Update
        elif request.method == 'PUT':
            serializer = UserSerializer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Successful user delete'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'message':'User not found'}, status=status.HTTP_400_BAD_REQUEST)
