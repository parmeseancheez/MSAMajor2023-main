#Ask for lowercase input
user_input = input("type below: \n").lower()

#Retrieve file type from input
file_type = user_input[user_input.find(".")+1:len(user_input)]

#cool funny fake loading thing
import time
print("\nloading file type.")
time.sleep(0.5)
print("loading file type..")
time.sleep(0.5)
print("loading file type...\n")
time.sleep(0.5)

#Determine what to print
if file_type == "gif":
    print("image/gif")
elif file_type == "jpg":
    print("image/jpg")
elif file_type == "jpeg":
    print("image/jpeg")
elif file_type == "png":
    print("image/png")
elif file_type == "pdf":
    print("document/pdf")
elif file_type == "txt":
    print("document/txt")
elif file_type == "zip":
    print("file/zip")
else:
    print("application/octet-stream")