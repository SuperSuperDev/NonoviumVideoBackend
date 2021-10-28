from rest_framework.views import APIView
from utils.requests import create, delete_one, favorite, get_all, get_one, update_one


class ListView(APIView):
    def __init__(self, model, serial):
        self.model = model
        self.serial = serial

    def get(self, _request):
        return get_all(self.model, self.serial)

    def post(self, request):
        return create(request, self.serial)


class DetailView(APIView):
    def __init__(self, model, populated_serial, serial):
        self.model = model
        self.populated_serial = populated_serial
        self.serial = serial

    def get(self, _request, pk):
        return get_one(self.model, self.populated_serial, pk)

    def delete(self, _request, pk):
        return delete_one(self.model, pk)

    def put(self, request, pk):
        return update_one(self.model, self.serial, request, pk)

class FavoriteView(APIView):
    def __init__(self, model, serial):
        self.model = model
        self.serial = serial

    def post(self, request, pk):
        print('here')
        return favorite(self.model, self.serial, request, pk)
