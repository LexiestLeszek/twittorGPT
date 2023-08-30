from playwright.sync_api import sync_playwright
import time, json, random, re, os, requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, HardwareType

def random_user_agent():
	return UserAgent(software_names=[SoftwareName.CHROME.value], hardware_types={HardwareType.COMPUTER.value}, limit=100).get_random_user_agent()

def get_random_name():
    return json.loads(requests.get("https://api.namefake.com/").text)["name"]

def get_avatar():
    photos_folder = "./avatars"
    photo_files = [f for f in os.listdir(photos_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random_photo = random.choice(photo_files)
    photo_path = os.path.join(photos_folder, random_photo)
    return photo_path

def get_email():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()        
        page = context.new_page()
        page.goto('https://email-fake.com/')
        email = page.locator('//*[@id="email_ch_text"]').inner_text()
        return email

def get_code(email):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        go = "https://email-fake.com/" + email
        page.goto(go)
        title = page.locator('//*[@id="email-table"]/div[1]/div[2]').inner_text()
        match = re.search(r'\b\d{6}\b', title)
        code = match.group()
        return code

def create_twitter_account(name, email, month, day, year, password, avatar):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://twitter.com/i/flow/signup')  # Twitter homepage URL

        # create account button
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div/span/span')
        button.click()
        
        page.fill('input[name="name"]',name)
        page.fill('input[name="email"]',email)
        
        # month / day / year selectors
        month_selector = '//*[@id="SELECTOR_1"]'
        day_selector = '//*[@id="SELECTOR_2"]'
        year_selector = '//*[@id="SELECTOR_3"]'
        
        # select month / day / year
        page.select_option(month_selector, month)
        page.select_option(day_selector, day)
        page.select_option(year_selector, year)
        
        # click Next
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')        
        button.click()
        
        # time.sleep(random.randint(2, 6))
        
        # click Next
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click()
        
        # time.sleep(random.randint(1, 11))
        
        # click Create Account / Submit
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div')
        button.click()
        
        # >>>>>>> NEXT STEPS: <<<<<<<<<<<<<<
        # click "authenticate"
        # solve capcha
        
        # wait to receive a verification code to the email
        time.sleep(300)
        code = get_code(email)
        
        page.fill('input[name="Verification code"]',code)
        
        # click Next
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click
        
        page.fill('input[name="password"]',password)
        
        # click Next
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click
        
        
        # >>>>>>>>>> upload photo XPATH
        # ava_upload = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div/svg')
        # ava_upload.input_files(avatar)
        
        
        # click "apply" button for image sizing XPATH:
        # //*[@id="layers"]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span
        
        # click Next XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span
        
        
        # click Skip for Now XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span
        
        # click Skip For Now XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/span/span
        
        # 3 random topics choosing:
        # //*[@id="verticalGridItem-1-categoryrecommendations-1696878796621217792"]/div/div/div/div/div/div/div
        # //*[@id="verticalGridItem-3-categoryrecommendations-1696878796621217792"]/div/div/div/div/div/div/div
        # //*[@id="verticalGridItem-7-categoryrecommendations-1696878796621217792"]/div/div/div/div/div/div/div
        
        # click Next XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/span
        
        
        # click Next XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div
        
        # follow one account XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/section/div/div/div/div/div[4]/div/div/div/div/div[2]/div[1]/div[2]/div/div/span/span
        
        # click Next XPATH:
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/span
        
        
        
        time.sleep(100)
        browser.close()

if __name__ == "__main__":
        
    num_accounts = 3
    
    for i in range(1,num_accounts): 
        name = get_random_name()
        email = get_email()
        month = random.choice("January","April","May","December")
        day = random.randint(1,24)
        year = random.randint(1981,1999)
        password = "kQafrt#145LL"
        avatar = get_avatar()
        create_twitter_account(name, email, month, day, year, password, avatar)
        creds = f"Account #{i} \n, name: {name} email: {email} password: {password}"
        print(creds)
        with open("accounts.txt", 'w') as file:
            file.write(creds + "\n")