current_users = ['admin', 'John', 'alice', 'Bob', 'Eve']
new_users = ['john', 'eve', 'Mike', 'sara', 'bob']


current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please choose another.")
    else:
        print(f"Username '{new_user}' is available.")
