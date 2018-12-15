from rest_framework import permissions
from message_system.models import MessageRecipient


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class CanUpdateMessage(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own profile
    """

    def has_permission(self, request, view):

        if request.user.is_staff or request.user.can_update_article:
            return True
        # print(view.kwargs)
        # print(request.user.id)
        # Look for the requested user in the database
        try:
            messageRecipient = MessageRecipient.objects.get(
                pk=view.kwargs['pk'])
        except:
            # If the user was not found then return false
            return False

        # Check that the requesting user id matches the authenticated user id
        # print(request.user)
        # print(messageRecipient.recipient)
        if request.user == messageRecipient.recipient:
            return True
        return False
