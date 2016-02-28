from .base import FunctionalTest

TEST_USERNAME = 'bob'
TEST_PASSWORD = 'password'
TEST_EMAIL = 'test@example.com'

class SignUpTest(FunctionalTest):

    def look_for_message_with_text(self, text):
        messages = self.browser.find_elements_by_xpath('//div[contains(@class, "message")]')
        isConfirmationMessageSeen = False
        for message in messages:
            if text in message.text:
                isConfirmationMessageSeen = True
        self.assertTrue(isConfirmationMessageSeen)

    def test_signup_with_minimum_fields_filled(self):
        # Bob visits the site and notices a "Sign Up" link for the first time.
        self.browser.get(self.server_url)
        sign_up_links = self.browser.find_elements_by_xpath("//*[contains(text(), 'Sign Up')]")
        sign_up_links[0].click()

        # Bob is brought to a sign up form
        self.wait_for_element_with_id('signup_form')

        # Bob fills in his information in the fields
        self.browser.find_element_by_id('id_username').click()
        self.browser.find_element_by_id('id_username').send_keys(TEST_USERNAME)
        self.browser.find_element_by_id('id_password1').click()
        self.browser.find_element_by_id('id_password1').send_keys(TEST_PASSWORD)
        self.browser.find_element_by_id('id_password2').click()
        self.browser.find_element_by_id('id_password2').send_keys(TEST_PASSWORD)
        self.browser.find_element_by_tag_name('button').click()

        # Bob can see that he is logged in
        self.wait_to_be_logged_in()

        # Bob can see that a confirmation email has been sent to his email account
        self.look_for_message_with_text("Successfully signed in")

    def test_signup_with_all_fields_filled(self):
        # Bob visits the site and notices a "Sign Up" link for the first time.
        self.browser.get(self.server_url)
        sign_up_links = self.browser.find_elements_by_xpath("//*[contains(text(), 'Sign Up')]")
        sign_up_links[0].click()

        # Bob is brought to a sign up form
        self.wait_for_element_with_id('signup_form')

        # Bob fills in his information in the fields
        self.browser.find_element_by_id('id_username').click()
        self.browser.find_element_by_id('id_username').send_keys(TEST_USERNAME)
        self.browser.find_element_by_id('id_email').click()
        self.browser.find_element_by_id('id_email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_id('id_password1').click()
        self.browser.find_element_by_id('id_password1').send_keys(TEST_PASSWORD)
        self.browser.find_element_by_id('id_password2').click()
        self.browser.find_element_by_id('id_password2').send_keys(TEST_PASSWORD)
        self.browser.find_element_by_tag_name('button').click()

        # Bob can see that he is logged in
        self.wait_to_be_logged_in()

        # Bob can see that a confirmation email has been sent to his email account
        self.look_for_message_with_text(TEST_EMAIL)
