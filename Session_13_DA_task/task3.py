# Identify whether count is local or global and explain the output.

count = 10
def update_count():
    count = 5
    print("Inside:", count)

update_count()
print("Outside:", count)