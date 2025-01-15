# A = {"kitap":"book",
#     "bilim":"knowledge",
#     "kompyuter":"computer"}
# A['talyp'] = 'student'
# print(A)

A = {"kitap":"book",
    "bilim":"knowledge",
    "kompyuter":"computer"}
A.setdefault('talyp','student')
print(A)