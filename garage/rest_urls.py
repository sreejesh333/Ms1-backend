from django.urls import path
from .views import *


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="custom_login"),# login
    path("add_employee/", AddEmplpyee.as_view(), name="add_employee"),# add employee
    path("update_salary/<uuid:id>/", UpdatePayment.as_view(), name="update_salary"),#to create salary details of employees
    path("list_salary/<uuid:id>/", ListSalary.as_view(), name="list_salary"),#to list the salary details of the employee
    path("retrieve_employee/<uuid:id>/", RetrieveEmployee.as_view(), name="retrieve_employee"),#to get the details of a specify employee
    path("add_remarks/", AddRemark.as_view(), name="add_remark"),#to add remarks of an employee
    path("list_remarks/<uuid:id>/", ListRemark.as_view(), name="list-remarks"),#to list remarks of an employee
    path("add_jobcard/", AddJobcard.as_view(), name="add-jobcard"),#to add the jobcard

]