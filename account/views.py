from rest_framework import generics, status
from rest_framework.response import Response
from .models import UserBase
from .serializers import UserSignUpSerializer, VerifyTokenSerializer, ProfileSerializer
from .utils import verify_token
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsOwnerOfProfile


# USER SIGN UP API VIEW
class UserSingUpApiView(generics.CreateAPIView):
    """
    API endpoint for user sign-up.

    This view allows users to sign up by creating a new UserBase object.
    The provided user information is validated and saved to the database.

    Inherits from:
        generics.CreateAPIView

    Required view attributes:
        - `queryset`: A queryset representing the collection of UserBase objects.
        - `serializer_class`: The serializer class used to serialize UserSignUpSerializer instances.

    Supported HTTP Methods:
        - POST: Creates a new user by processing the sign-up request.

    Returns:
        A response with the status code 201 (HTTP_CREATED) upon successful registration.
        The response includes a success message, the serialized user data, and a status indicator.

    Raises:
        N/A
    """
    queryset = UserBase.objects.all()
    serializer_class = UserSignUpSerializer


    def create(self, request, *args, **kwargs):
       response = super().create(request, *args, **kwargs)
       return Response(
        {
        'status': 201,
        'message': 'Registered successfully. Please verify your account.',
        'data': response.data
       },
       status=status.HTTP_201_CREATED
       )
# END USER SIGN UP API VIEW


# VERIFY TOKEN API VIEW
class VerifyTokenApiView(generics.UpdateAPIView):
    """
    API endpoint for verifying a token and generating new access and refresh tokens.

    This view allows users to verify a phone token and obtain new access and refresh tokens.
    The phone token is validated against the provided phone number, and if valid, new tokens are generated.

    Inherits from:
        generics.UpdateAPIView

    Required view attributes:
        - `queryset`: A queryset representing the collection of UserBase objects.
        - `serializer_class`: The serializer class used to serialize VerifyTokenSerializer instances.

    Supported HTTP Methods:
        - POST: Verifies the phone token and generates new access and refresh tokens.

    Returns:
        If the token is valid, a response containing new access and refresh tokens is returned.
        The access token is required for authenticating subsequent API requests.
        The refresh token can be used to obtain a new access token when the current one expires.

    Raises:
        - serializers.ValidationError: If the token is invalid or expired.
    """
    queryset = UserBase.objects.all()
    serializer_class = VerifyTokenSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        phone_token = serializer.validated_data.get('phone_token')
        phone_number = serializer.validated_data.pop('number')
        account = verify_token(phone_token, phone_number)
        if account:
            refresh = RefreshToken.for_user(account)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response({'status': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)
# END VERIFY TOKEN API VIEW


# PROFILE API VIEW
class ProfileApiView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving a user's profile information.

    Inherits from:
        generics.RetrieveAPIView

    Required view attributes:
        - `queryset`: A queryset representing the collection of UserBase objects.
        - `serializer_class`: The serializer class used to serialize UserBase instances.
        - `permission_classes`: A list of permission classes applied to the view.

    Supported HTTP Methods:
        - GET: Retrieves the profile information of the authenticated user.

    Permissions:
        - IsOwnerOfProfile: Only the owner of the profile can access the view.

    Returns:
        A serialized representation of the user's profile information.

    Raises:
        N/A
    """
    queryset = UserBase.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOfProfile]
# END PROFILE API VIEW




