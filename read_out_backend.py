import pickle #used to store elements (SQL for storage would be better, though)
from auth import * #import the auth.py module

USER_PICKLE = 'user_pickle.dat' #filename, where the user data is saved to
ACL_PICKLE = 'acl_pickle.dat' #filename, where the ACL is saved to

# ----------------------
# clear command line window
# ----------------------

screen_clear() #clear the screen


#-----------------------
# read out 
#-----------------------

print()
print(' readout is as follows:')
print()

print('#-------------------#')
print('# \"backend\" readout #')
print('#-------------------#')

#-----------------------
# read out user table
#-----------------------

#load user data in memory from user pickle file
print('#------------#')
print('# User table #')
print('#------------#')
users = [] #flush users array
with open(USER_PICKLE, 'rb') as f:
    users = (pickle.load(f)) #fill users arra
for user in users:
    print ('Username: ', user.username)
    print ('Password: ', user.password)
    print ('Salt: ', user.salt)
    print ('Medical History: ', user.medical_history)
    print ()
print()


#-----------------------
# read out the access control list (ACL)
#-----------------------

#load user data in memory from user pickle file
print('#---------------------------------#')
print('# Access Control List (ACL) table #')
print('#---------------------------------#')
acl = [] #flush users array
with open(ACL_PICKLE, 'rb') as f:
    acl = (pickle.load(f)) #fill users arra
for acl_entry in acl:
    print ('Username: ', acl_entry.username)
    print ('Permissions: ', acl_entry.user_permissions)
    print()
print()