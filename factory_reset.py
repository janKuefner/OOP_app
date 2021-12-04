import pickle #used to store elements (SQL for storage would be better, though)
from auth import * #import the auth.py module


USER_PICKLE = 'user_pickle.dat' #filename, where the user data is saved to
ACL_PICKLE = 'acl_pickle.dat' #filename, where the ACL is saved to


# ----------------------
# clear command line window
# ----------------------

screen_clear() #clear the screen


#-----------------------
# fill the user table
#-----------------------

users = []
users.append(User('tim',
'bdeb0bfcf34ad6f0e21816b60137f2118d1ec541f814eaff5bd58887ba7e1f50',
'889f299b74a5308ea38020995291efa69f3dcdaf61f655c2fa358eda99783d46',
['2021-04 | Covid vaccination','2020-12 | stomach ache','2019-04 | flu']))


users.append(User('steve',
'e20a27ba3d051a97974c9abf3acb4db2e2187f8fb9c1bae5fec9b3d5d363684b',
'8c9ab77460e0404d0a1d97e009b66155a6654df3022a1bb4e0f91e0f7f686b95',
[]))
users.append(User('Administrator',
'8ba211b871eb19efd4d303397609a8e318ad2519afb943c928badbc95ab2aa67',
'fc9e2e5d533867b48fc7844d904485928b1d04302c2eede0e97533aacc32a99a',
['2021-04 | Covid vaccination']))

with open(USER_PICKLE, 'wb') as f:
    pickle.dump(users, f)

#-----------------------
# fill the access control list (ACL)
#-----------------------
access_control_list = []
access_control_list.append(AccessControlListEntry('tim',[
        'read_own_medical_history'
        ]))
access_control_list.append(AccessControlListEntry('steve',[
        'read_other_patients_medical_history',
        'read_own_medical_history'
        ]))
access_control_list.append(AccessControlListEntry('Administrator',[
        'add_user',
        'add_new_global_permission',
        'change_user_permissions',
        'read_other_patients_medical_history',
        'read_own_medical_history',
        'is_logged_in',
        'print_user_permissions'
        ]))

with open(ACL_PICKLE, 'wb') as f:
    pickle.dump(access_control_list, f)

#-----------------------
# print out some information
#-----------------------

print()
print('Factory reset of ASMIS \'backend\' successfull')
print()
print('Here are some logins:')
print('Username: tim            | password: qwerty1234')
print('Username: steve          | password: yolo007')
print('Username: Administrator  | password: password')
print()
print('fyi: try \'read_out_backend.py\' to get other tables from the backend')
print()