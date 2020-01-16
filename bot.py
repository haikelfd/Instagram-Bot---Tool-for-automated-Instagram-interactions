from selenium import webdriver 
import os
import time


class InstagramBot:

    def __init__(self, username, password):
        """
        Initializes an instance of the instagramBot.

        Call the login method to authenticate a user with IG.

        Args:
         username:str: The instagram username .
         passowrd:str: the instagram password for a usewe .

        attributes:
         driver:selenium.webdriver.chrome: the chromedriver that is used to automate browser actions.
        """
        self.username = username 
        self.password = password
        self.base_url= 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')
       
        self.login()

        
       
 
    def login(self):
        time.sleep(3)
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(2)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

    def nav_user(self, user):
      self.driver.get('{}/{}/'.format(self.base_url, user))
    
    def follow_user(self, user):
        self.nav_user(user)

        follow_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
        follow_button.click()

    def unfollow_user(self, user):
        self.nav_user(user)

        unfollow_btns = self.find_buttons('Following')

        if unfollow_btns:
            for btn in unfollow_btns:
                btn.click()
                unfollow_confirmation = self.find_buttons('Unfollow')[0]
                unfollow_confirmation.click()
        else:
            print('No {} buttons were found.'.format('Following'))

    def like_latest_posts(self, user, n_posts, like=True):
        """
        Likes a number of a users latest posts, specified by n_posts.
        Args:
            user:str: User whose posts to like or unlike
            n_posts:int: Number of most recent posts to like or unlike
            like:bool: If True, likes recent posts, else if False, unlikes recent posts
          Currently maxes out around 15.
        """

        action = 'Like' if like else 'Unlike'

        self.nav_user(user)

        imgs = []
        imgs.extend(self.driver.find_elements_by_class_name('_9AhH0'))

        for img in imgs[:n_posts]:
            img.click() 
            time.sleep(1) 
            try:
                self.driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click()
            except Exception as e:
                print(e)

            #self.comment_post('beep boop testing bot')
            self.driver.find_elements_by_class_name('ckWGn')[0].click()


              
    def find_buttons(self, button_text):
        """
        Finds buttons for following and unfollowing users by filtering follow elements for buttons. Defaults to finding follow buttons.
        Args:
            button_text: Text that the desired button(s) has 
        """

        buttons = self.driver.find_elements_by_xpath("//*[text()='{}']".format(button_text))

        return buttons
if __name__ == '__main__':
    ig_bot = InstagramBot('email', 'password')
   # ig_bot.nav_user('pewdiepie')
    time.sleep(3)
    ig_bot.follow_user('pewdiepie')
    time.sleep(2)
    ig_bot.unfollow_user('pewdiepie')
    ig_bot.like_latest_posts('pewdiepie', 7, like=True)

    
    

    
