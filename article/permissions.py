from rest_framework import permissions


class IsSuperUserOrStuff(permissions.BasePermission):
    """
    其他用户仅可查看
    超级用户可查看、修改、删除
    工作人员只可以对自己的文章进行修改、删除
    """

    # def has_object_permission(self, request, view, obj):

    #     # 对所有人允许 GET, HEAD or OPTIONS 请求.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True

    #     return request.user.is_superuser or request.user == obj.author

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser
