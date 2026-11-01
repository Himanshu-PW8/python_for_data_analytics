# Create a Python script demonstrating the lifetime of local and global variables using WhatsApp online/offline status.

app_status = "Offline"

def change_status():

    user_status = "Online"

    print("Inside Function:")
    print("User Status:", user_status)
    print("App Status:", app_status)

print("Before Function Call:")
print("App Status:", app_status)

change_status()

print("After Function Call:")
print("App Status:", app_status)