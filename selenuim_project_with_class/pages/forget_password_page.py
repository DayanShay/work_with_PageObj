from selenuim_project_with_class.pages.Base_Page import BaseObj


class ForgetPasswordPage(BaseObj):
    def __init__(self, driver):
        super().__init__(driver)
        self._title = 'Forgot your password - My Store'