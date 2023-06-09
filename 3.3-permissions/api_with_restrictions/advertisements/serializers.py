from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        # print(validated_data)
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # Ограничение на десять открытых объявлений.
        # Статус клиенту отправлять не обязательно, поэтому есть доп. проверка
        # на наличие статуса в полученных данных, и если он "закрыть",
        # то такое изменение внести дозволено
        if (Advertisement.objects.filter(
                creator=self.context["request"].user,
                status=AdvertisementStatusChoices.OPEN)
        ).count() >= 10:
            if 'status' in data.keys():
                if data['status'] == 'OPEN':
                    raise serializers.ValidationError('Too many opened advertisements')
            else:
                raise serializers.ValidationError('Too many opened advertisements')

        return data
