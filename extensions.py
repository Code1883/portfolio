user_input = input("File name: ")
if user_input.endswith(".gif"):
    print("image/gif")
elif user_input.endswith(".jpeg") or user_input.endswith(".jpg"):
    print("image/jpeg")
elif user_input.endswith(".png"):
    print("image/png")
elif user_input.endswith(".pdf"):
    print("application/pdf")
elif user_input.endswith(".txt"):
    print(".txt")
elif user_input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")









