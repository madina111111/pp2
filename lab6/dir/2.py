import os
#"C:\Users\ASUS\Desktop\PP2"
path = input()
#path exists
print(os.access(path, os.F_OK))
#is Readable
print(os.access(path, os.R_OK))
#is Wriable
print(os.access(path, os.W_OK))
#is Execuatble

print(os.access(path, os.X_OK))