from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    # مسار تغيير اللغة
    path('i18n/', include('django.conf.urls.i18n')),
    # مسار التسجيل بدون كود اللغة (اختياري، لأجل سهولة الوصول المباشر)
    path('register/', include('core.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('register/', include('core.urls')),  # نفس المسار لكن يظهر تحت /ar/ أو /en/
    path('', include('core.urls')),           # بقية مسارات التطبيق
)