from fastapi import Request


class DatabaseMiddleware:
    def __call__(self, request: Request) -> None:
        self.request = request