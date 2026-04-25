

class WelcomePage:
    def __init__(self, page):
        print("\n### Welcome Page ###\n")
        self.page = page


    def swag_labs_website_set_login(self):

        # Set username

        user_name = self.page.locator('[name="user-name"]')
        user_name.click()
        user_name.fill("standard_user")

        # Set password

        password = self.page.locator('[name="password"]')
        password.click()
        password.fill("secret_sauce")

        # Click the login button

        login_btn = self.page.get_by_text("Login")
        login_btn.click()

