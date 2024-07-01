class CommonRepository:
    @classmethod
    def create(cls, serializer_class, data):
        serializer = serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @classmethod
    def update(cls, instance, serializer_class, data, partial=True):
        serializer = serializer_class(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @classmethod
    def delete(cls, instance):
        instance.delete()

    @classmethod
    def get_by_pk(cls, queryset, pk):
        return queryset.get(pk=pk)
