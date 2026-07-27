from django.contrib.auth.mixins import UserPassesTestMixin


class ProfessorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return (
            user.is_superuser or
            user.is_staff or
            user.groups.filter(name="Professor").exists()
        )
