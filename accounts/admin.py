from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth", "photo")
    list_filter = ("date_of_birth",)
    search_fields = ("user__username",)

    # class Meta:
    #     model = Profile
    #     fields = ("user", "date_of_birth", "photo")

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(user=request.user)
