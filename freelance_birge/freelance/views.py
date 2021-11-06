from requests import Response
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsExecutor(permissions.BasePermission):
    """Permission для проверки пользователя для редактирования"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ExecutorListView(generics.ListAPIView):
    """View для просмотра всех исполнителей"""

    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class ExecutorRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одного исполнителя"""

    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class ExecutorUpdateView(generics.UpdateAPIView):
    """View для редактирования информации про исполнителя"""

    serializer_class = CreateExecutorSerializer
    permission_classes = (IsExecutor, )

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Executor.objects.filter(user=user)

        raise PermissionDenied()


class ExecutorCreateView(generics.CreateAPIView):
    """View для создания исполнителя"""

    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


class CustomerListView(generics.ListAPIView):
    """View для просмотра всех исполнителей"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одного исполнителя"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(generics.UpdateAPIView):
    """View для редактирования информации про исполнителя"""

    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class CustomerCreateView(generics.CreateAPIView):
    """View для создания исполнителя"""

    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


class OrderRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одной услуги для заказа"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    """View для редактирования услуги для заказа"""

    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderCreateView(generics.CreateAPIView):
    """View для создания услуги для заказа"""

    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderListView(generics.ListAPIView):
    """View для просмотра всех услуг для заказа"""

    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        customer = params.get('customer', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        return queryset


class ServiceRetrieveView(generics.RetrieveAPIView):
    """View для просмотра услуги исполнителя"""

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateView(generics.UpdateAPIView):
    """View для редактирования услуги исполнителя"""

    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceCreateView(generics.CreateAPIView):
    """View для создания услуги исполнителя"""

    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceListView(generics.ListAPIView):
    """View для просмотра всех услуг исполнителя"""

    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        executor = params.get('executor', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        return queryset


class TagRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одного тега"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    """View для редактирования информации тега"""

    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TagCreateView(generics.CreateAPIView):
    """View для создания тега"""

    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TagListView(generics.ListAPIView):
    """View для просмотра всех тегов"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class OrderingRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одного заказа"""

    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingUpdateView(generics.UpdateAPIView):
    """View для редактирования информации про заказ"""

    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderingCreateView(generics.CreateAPIView):
    """View для создания заказа"""

    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderingListView(generics.ListAPIView):
    """View для просмотра всех заказов"""

    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class MessageRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одного сообщения"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):
    """View для редактирования сообщения"""

    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageCreateView(generics.CreateAPIView):
    """View для создания сообщения"""

    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageListView(generics.ListAPIView):
    """View для просмотра всех сообщений"""

    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params

        executor = params.get('executor', None)
        customer = params.get('customer', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        if from_date:
            queryset = queryset.filter(msg_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(msg_date__lte=to_date)

        return queryset


class TicketRetrieveView(generics.RetrieveAPIView):
    """View для просмотра одного тикета"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketUpdateView(generics.UpdateAPIView):
    """View для редактирования информации про тикет"""

    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketCreateView(generics.CreateAPIView):
    """View для создания тикета"""

    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketListView(generics.ListAPIView):
    """View для просмотра всех тикетов"""

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ReviewRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """View для просмотра одного отзыва"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewCreateView(generics.CreateAPIView):
    """View для создания отзыва"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewListView(generics.ListAPIView):
    """View для просмотра всех отзывов"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AuthoringRetrieveView(generics.RetrieveAPIView):
    """View для просмотра сформированного отзыва"""

    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


class AuthoringUpdateView(generics.UpdateAPIView):
    """View для редактирования сформированного отзыва"""

    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringCreateView(generics.CreateAPIView):
    """View для создания сформированного отзыва"""

    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringListView(generics.ListAPIView):
    """View для просмотра всех сформированных отзывов"""

    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer
