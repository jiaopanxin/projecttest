import xadmin
from .models import Server, Memory, IDC, Cabinet, Asset, SysUsers
from xadmin import views


class ServerAdmin():
    list_display = ("id", "os_name", "machine",
                    "host_name", "os_version",
                    "kernel", "model_name",
                    "cpu_type", "physical_count",
                    "cpu_cores")
    search_fields = ("id", "os_name", "machine",
                     "host_name", "os_version",
                     "kernel", "model_name",
                     "cpu_type", "physical_count",
                     "cpu_cores")
    list_filter = ("id", "os_name", "machine",
                   "host_name", "os_version",
                   "kernel", "model_name",
                   "cpu_type", "physical_count",
                   "cpu_cores")


class MemoryAdmin():
    list_display = ("id", "capacity", "slot",
                    "model", "speed",
                    "manufacturer", "sn",
                    "server",)
    search_fields = ("id", "capacity", "slot",
                     "model", "speed",
                     "manufacturer", "sn",
                     "server",)
    list_filter = ("id", "capacity", "slot",
                   "model", "speed",
                   "manufacturer", "sn",
                   "server",)


class IDCAdmin():
    list_display = ("id", "name",
                    "city",
                    "address")
    search_fields = ("id", "name",
                     "city",
                     "address")
    list_filter = ("id", "name",
                   "city",
                   "address")


class AssetAdmin():
    list_display = ("id", "device_type_id",
                    "device_status_id", "cabinet", "cabinet_order", "latest_date", "create_at")
    search_fields = ("id", "device_type_id",
                     "device_status_id", "cabinet", "cabinet_order", "latest_date", "create_at")
    list_filter = ("id", "device_type_id",
                   "device_status_id", "cabinet", "cabinet_order", "latest_date", "create_at")


class CabinetAdmin():
    list_display = ("id", "name",
                    "cab_lever",
                    "idc")
    search_fields = ("id", "name",
                     "cab_lever",
                     "idc")
    list_filter = ("id", "name",
                   "cab_lever",
                   "idc")


class SysUsersAdmin():
    list_display = ("id", "name",
                    "user_type")
    search_fields = ("id", "name",
                     "user_type")
    list_filter = ("id", "name",
                   "user_type")



xadmin.site.register(Server, ServerAdmin)
xadmin.site.register(Memory, MemoryAdmin)
xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Cabinet, CabinetAdmin)
xadmin.site.register(Asset, AssetAdmin)
xadmin.site.register(SysUsers, SysUsersAdmin)


# 使用主题
class BaseSetting():
    enable_thems = True  # 授权使用主题
    use_bootswatch = True  # 使用bootstrap的主题


xadmin.site.register(views.BaseAdminView, BaseSetting)
