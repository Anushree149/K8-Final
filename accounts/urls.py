from django.urls import path
from .import views
urlpatterns = [
    path("",views.main,name='main'),
    # path("my_home/",views.my_home,name='my_home'),
    path('add_emp/',views.add_emp,name='add_emp'),
    path("Bulk Register/",views.bulk_register,name='bulk_register'),
    path('Single Register/',views.single_reg,name='single_reg'),
    path('emp_list/',views.emp_list,name='emp_list'),
    path('emp_del/<int:pk>/',views.emp_delete,name='emp_del'),
    path('activate/<uid>/<token>/',views.activate,name="activate"),
    path('company_register/',views.company_register,name='company_register'),
    path('all_login/',views.all_login,name='all_login'),
    path('all_logout/',views.all_logout,name='all_logout'),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('resetpassword_validate>/<uid>/<token>/',views.resetpassword_validate,name="resetpassword_validate"),
    path('resetpassword/',views.resetpassword,name="resetpassword"),
    path('changepassword/',views.changepassword,name="changepassword"),

]
