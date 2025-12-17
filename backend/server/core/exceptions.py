from fastapi import HTTPException


# Base exceptions
class NotFoundError(HTTPException):
    """Resource not found."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(status_code=404, detail=message)


class ForbiddenError(HTTPException):
    """Access forbidden."""

    def __init__(self, message: str = "Access forbidden"):
        super().__init__(status_code=403, detail=message)


class BadRequestError(HTTPException):
    """Bad request."""

    def __init__(self, message: str = "Bad request"):
        super().__init__(status_code=400, detail=message)


class UnauthorizedError(HTTPException):
    """Unauthorized access."""

    def __init__(self, message: str = "Unauthorized"):
        super().__init__(status_code=401, detail=message)


class ConflictError(HTTPException):
    """Resource conflict."""

    def __init__(self, message: str = "Resource conflict"):
        super().__init__(status_code=409, detail=message)


# User exceptions
class UserNotFoundException(NotFoundError):
    """User not found."""

    def __init__(self, message: str = "User not found"):
        super().__init__(message)

    @classmethod
    def from_id(cls, user_id: str) -> "UserNotFoundException":
        return cls(f"User with id '{user_id}' not found")


class UserAlreadyExistsException(ConflictError):
    """User already exists."""

    def __init__(self, message: str = "User already exists"):
        super().__init__(message)


# Forum exceptions
class ForumNotFoundException(NotFoundError):
    """Forum not found."""

    def __init__(self, message: str = "Forum not found"):
        super().__init__(message)

    @classmethod
    def from_id(cls, forum_id: str) -> "ForumNotFoundException":
        return cls(f"Forum with id '{forum_id}' not found")


# Post exceptions
class PostNotFoundException(NotFoundError):
    """Post not found."""

    def __init__(self, message: str = "Post not found"):
        super().__init__(message)

    @classmethod
    def from_id(cls, post_id: str) -> "PostNotFoundException":
        return cls(f"Post with id '{post_id}' not found")


# Room exceptions
class RoomNotFoundException(NotFoundError):
    """Room not found."""

    def __init__(self, message: str = "Room not found"):
        super().__init__(message)

    @classmethod
    def from_id(cls, room_id: str) -> "RoomNotFoundException":
        return cls(f"Room with id '{room_id}' not found")


class RoomFullException(BadRequestError):
    """Room is full."""

    def __init__(self, message: str = "Room is full"):
        super().__init__(message)


# Webhook exceptions
class WebhookException(HTTPException):
    """Base webhook exception."""

    def __init__(self, message: str = "Webhook error"):
        super().__init__(status_code=400, detail=message)


class WebhookVerificationException(WebhookException):
    """Webhook verification failed."""

    def __init__(self, message: str = "Webhook verification failed"):
        super().__init__(message)


class WebhookHandlerException(WebhookException):
    """Webhook handler error."""

    def __init__(self, message: str = "Webhook handler error"):
        super().__init__(message)
