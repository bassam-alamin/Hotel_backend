from rest_framework import generics
from .serializers import *
from rest_framework.permissions import AllowAny


class UserApiView(generics.ListCreateAPIView):
    lookup_field = "pk"
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class UserRudApiView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return User.objects.all()


class CategoryApiView(generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Category.objects.all()


class CategoryRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Category.objects.all()


class FoodApiView(generics.ListAPIView):
    lookup_field = "food_category"
    serializer_class = FoodSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        category = self.kwargs.get("food_category")
        query = Food.objects.filter(food_category=category)
        return query


class FoodRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = FoodSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Food.objects.all()


class OrderApiView(generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = OrderSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Order.objects.all()


class OrderRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = OrderSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return Order.objects.all()
