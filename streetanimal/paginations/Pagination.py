from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class AnimalPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

    def paginate_queryset(self, queryset, request, view=None):
        if 'all' in request.query_params:
            return None

        return super().paginate_queryset(queryset, request, view)

