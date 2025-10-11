from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    #Custom permission to allow owners of an object to edit it.
    def has_object_permission(self,request, view, obj):
        #Read permissions allowed to any req. Always allow GET, HEAD or OPTIONS req.
        if request.method in permissions.SAFE_METHODS:
            return True

        #Write permissions are only allowed to the owner of the post/comment.
        return obj.author == request.user

