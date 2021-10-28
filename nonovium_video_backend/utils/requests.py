from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


def get_all(model, serial):
    data = model.objects.all()
    serialized_data = serial(data, many=True)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


def create(request, serial):
    serialized_data = serial(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def get_row(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound()


def get_one(model, serial, pk):
    data = get_row(model, pk=pk)
    serialized_data = serial(data)
    return Response(serialized_data.data, status=status.HTTP_200_OK)


def delete_one(model, pk):
    data = get_row(model=model, pk=pk)
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def update_one(model, serial, request, pk):
    data = get_row(model=model, pk=pk)
    updated_data = serial(data, data=request.data)
    if updated_data.is_valid():
        updated_data.save()
        return Response(updated_data.data, status=status.HTTP_202_ACCEPTED)
    return Response(updated_data.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def favorite(model, serial, request, pk):
    permission_classes = IsAuthenticated
    if permission_classes:
        try:
            data = model.objects.get(pk=pk)
            if request.user in data.favorited_by.all():
                data.favorited_by.remove(request.user.id)
            else:
                data.favorited_by.add(request.user.id)
            data.save()
            serialized_data = serial(data)
            return Response(serialized_data.data, status=status.HTTP_202_ACCEPTED)
        except model.DoesNotExist:
            raise NotFound()
