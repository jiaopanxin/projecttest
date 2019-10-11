from users.models import UsersProfile
from cmdb.models import Server, Memory, Disk, Asset, SysUsers

from rest_framework import serializers


class UserSerialize(serializers.Serializer):
    username = serializers.CharField(
        required=True,  max_length=150)
    email = serializers.EmailField(
        required=False, allow_null=True)
    password = serializers.CharField(
        required=True, max_length=128)

    last_login = serializers.DateTimeField(
        required=False, allow_null=True)

    avatar = serializers.ImageField(default='users/2019/09/26/iterable.png',
                                    max_length=128)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UsersProfile.objects.create(**validated_data)

# 多对一  正向查询


class ServerSerialize(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"


class MemorySerialize(serializers.ModelSerializer):
    server = ServerSerialize()

    class Meta:
        model = Memory
        fields = "__all__"


class DiskSerialize(serializers.ModelSerializer):
    server = ServerSerialize()

    class Meta:
        model = Disk
        fields = "__all__"


# 多对一  反向查询
# class MemorySerialize(serializers.ModelSerializer):

#     class Meta:
#         model = Memory
#         fields = "__all__"


# class DiskSerialize(serializers.ModelSerializer):

#     class Meta:
#         model = Disk
#         fields = "__all__"


# class ServerSerialize(serializers.ModelSerializer):
#     disk = DiskSerialize(many=True)

#     class Meta:
#         model = Server
#         fields = "__all__"


# 多对多
class SysuserSerializeMany(serializers.ModelSerializer):

    class Meta:
        model = SysUsers
        fields = "__all__"


class ServerSerializeMany(serializers.ModelSerializer):
    sysusers = SysuserSerializeMany(many=True)

    class Meta:
        model = Server
        fields = "__all__"
