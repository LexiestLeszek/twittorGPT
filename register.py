from playwright.sync_api import sync_playwright
import time, json, random, re, os, requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, HardwareType, OperatingSystem

# it works up until capcha

def random_user_agent():
    return UserAgent(software_names=[SoftwareName.CHROME.value,SoftwareName.EDGE.value,SoftwareName.OPERA.value], hardware_types=[HardwareType.COMPUTER.value,HardwareType.MOBILE.value], limit=100).get_random_user_agent()

def get_random_name():
    return json.loads(requests.get("https://api.namefake.com/").text)["name"]

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

def create_twitter_account(name, email, month, day, year, password, avatar, agent):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(user_agent=agent)
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
        
        
        # TODO: Click audio icon button
        # ---- ALREADY TRIED:
        
        # button = page.locator('//*[@id="root"]/div/div[2]/button/img')
        # button = page.locator('div.sc-99cwso-0.sc-1cbf51e-0.gMEQEa.fLfntv.navigation.box')
        # button = page.locator('//*[@id="root"]/div/div[2]/button/p')
        # button = page.locator('//*[@id="root"]/div/div[2]/button')
        # button = page.query_selector('button.sc-rqvnx3-0.kTxXTj.audio-button.icon-button')
        # button = page.locator('audio-button')
        
        button.click()
        
        # https://client-api.arkoselabs.com/cdn/fc/assets/style-manager/assets/e94ae91f-1774-408b-a8b3-1237915c996c.svg
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # wait to receive a verification code to the email
        time.sleep(300)
        code = get_code(email)
        time.sleep(300)
        
        page.fill('input[name="Verification code"]',code)
        
        # click Next
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click
        
        page.fill('input[name="password"]',password)
        
        # click Next
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click
        
        
        # >>>>>>>>>> upload photo XPATH
        ava_upload = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div/svg')
        ava_upload.input_files(avatar)
        
        
        # click "apply" button for image sizing XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span')
        button.click()
        
        # click Next XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click()
        
        # click Skip for Now XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
        button.click()
        
        # click Skip For Now XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/span/span')
        button.click()
        
        # 3 random topics choosing:
        button = page.locator('//*[@id="verticalGridItem-1-categoryrecommendations-1696878796621217792"]/div/div/div/div/div/div/div')
        button = page.locator('//*[@id="verticalGridItem-4-categoryrecommendations-1696878796621217792"]/div/div/div/div/div/div/div')
        button = page.locator('//*[@id="verticalGridItem-5-categoryrecommendations-1696878796621217792"]/div/div/div/div/div/div/div')
        
        # click Next XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/span')
        button.click()
        
        # click Next XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        button.click
        
        # follow one account XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/section/div/div/div/div/div[4]/div/div/div/div/div[2]/div[1]/div[2]/div/div/span/span')
        button.click()
        
        # click Next XPATH:
        button = page.locator('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/span/span')
        button.click()
        
        browser.close()

if __name__ == "__main__":
        
    num_accounts = 3
    
    for i in range(1,num_accounts): 
        agent = random_user_agent()
        name = get_random_name()
        email = get_email()
        month = random.choice(["January","April","May","June","December"])
        day = random.choice(["1","3","4","7","8","11","14","15","17","22","25"])
        year = random.choice(["1981","1983","1984","1987","1988","1989","1990","1992","1993","1994","1997"])
        password = "kQafrt#145LL"
        avatar = f"./avatars/{i}"
        print(name,email,avatar)
        create_twitter_account(name, email, month, day, year, password, avatar, agent)
        creds = f"Account #{i},name: {name},email: {email},password: {password}\n"
        print(creds)
        with open("accounts.txt", 'w') as file:
            file.write(creds)