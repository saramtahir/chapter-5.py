usernames = ['admin', 'john', 'alice', 'mary', 'peter']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
