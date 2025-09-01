class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        masked_password = "*" * len(self.password)
        print(f"User {self.name} currently works as a {self.current_job_title}. "
              f"You can contact them at {self.email}. "
              f"Password: {masked_password}")
app_user_one = User("np@np.com", "Nana Janapashia", "pwd1", "DevOps Engineer")

app_user_one.get_user_info()
# Output: User Nana Janapashia currently works as a DevOps Engineer. 
# You can contact them at np@np.com. Password: ****
