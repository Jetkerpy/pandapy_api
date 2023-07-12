from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer



class ProductListApiView(generics.ListAPIView):
    """
    API endpoint for retrieving a list of products.

    This view allows users to retrieve a list of products.
    The products can be viewed by both authenticated users and unauthenticated users,
    but only authenticated users can perform write operations.

    Inherits from:
        generics.ListAPIView

    Required view attributes:
        - `queryset`: A queryset representing the collection of Product objects.
        - `serializer_class`: The serializer class used to serialize Product instances.
        - `permission_classes`: A list of permission classes applied to the view.

    Supported HTTP Methods:
        - GET: Retrieves a paginated list of products.

    Permissions:
        - IsAuthenticatedOrReadOnly: Authenticated users can perform write operations,
                                     while unauthenticated users can only perform read operations.

    Returns:
        A paginated response containing a serialized representation of the product list.
        Each product includes fields such as 'name', 'price', 'description', and more.

    Raises:
        N/A
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetailApiView(generics.RetrieveAPIView):
    """
    API endpoint for retrieving detailed information about a product.

    This view allows authenticated users to retrieve detailed information about a specific product.
    The product is retrieved based on its unique slug identifier.

    Inherits from:
        generics.RetrieveAPIView

    Required view attributes:
        - `queryset`: A queryset representing the collection of Product objects.
        - `serializer_class`: The serializer class used to serialize Product instances.
        - `lookup_field`: The field used to retrieve the product (in this case, 'slug').
        - `permission_classes`: A list of permission classes applied to the view.

    Supported HTTP Methods:
        - GET: Retrieves detailed information about a product.

    Permissions:
        - IsAuthenticated: Only authenticated users can access this view.

    Returns:
        A serialized representation of the product, including detailed information such as 'name', 'price',
        'description', and other relevant fields.

    Raises:
        N/A
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated]



