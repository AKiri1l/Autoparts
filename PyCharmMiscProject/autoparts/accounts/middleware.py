class DynamicCSRFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Получаем текущий домен из запроса
        if request.META.get('HTTP_HOST'):
            host = request.META['HTTP_HOST']
            scheme = 'https' if request.is_secure() else 'http'
            current_origin = f"{scheme}://{host}"

            # Динамически добавляем в настройки
            from django.conf import settings
            if current_origin not in settings.CSRF_TRUSTED_ORIGINS:
                settings.CSRF_TRUSTED_ORIGINS.append(current_origin)

        response = self.get_response(request)
        return response