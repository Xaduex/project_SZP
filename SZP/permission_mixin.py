from django.contrib.auth.mixins import UserPassesTestMixin

from SZP.models import Employee


class MyTestUserPassesTest(UserPassesTestMixin):

    def test_func(self):
        u = Employee.objects.get(operator='2')
        print(u.operator)
        print(Employee.operator)
        if self.request.user == u.operator:
            return True
        return False