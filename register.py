from playwright.sync_api import sync_playwright
import time, json, random, re, os, requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, HardwareType, OperatingSystem
from fp.fp import FreeProxy

# it works up until capcha, possible solution - audiocapcha with ML capabilities
# TODO: add logic to skip if capcha is unslved and start over (try-except stuff)

def get_proxy():
    proxy_url = FreeProxy().get()
    proxy_obj = {
        "server": proxy_url,
        "username": "",
        "password": ""
    }
    
    return proxy_obj

def random_user_agent():

    user_agent = UserAgent(software_names=[SoftwareName.CHROME.value], hardware_types={HardwareType.COMPUTER.value}, limit=100).get_random_user_agent()
    return user_agent

def get_random_name():
    person = json.loads(requests.get("https://api.namefake.com/").text)
    person_name = person["name"]
    person_psw = person["password"]
    return person_name

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
    
def get_phone():
    phone = ""
    return phone

def create_twitter_account(name, email, month, day, year, password, avatar, agent, proxy):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False,proxy=proxy)
        #context = browser.new_context()
        context = browser.new_context(user_agent=agent) # would make sense to add user agent later
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
        
        # ------- ALREADY TRIED -------- :
        # button = page.locator('//*[@id="root"]/div/div[2]/button/img')
        # button = page.locator('div.sc-99cwso-0.sc-1cbf51e-0.gMEQEa.fLfntv.navigation.box')
        # button = page.locator('//*[@id="root"]/div/div[2]/button/p')
        # button = page.locator('//*[@id="root"]/div/div[2]/button')
        # button = page.query_selector('button.sc-rqvnx3-0.kTxXTj.audio-button.icon-button')
        # button = page.locator('audio-button')
        # button = page.locator('.icon')
        # button = page.locator('img')
        # button = page.query_selector('[class*="audio"]')
        # button = page.locator('//*[@id="root"]/div/div[2]/button')
        # button.click(force=True)
        # <button class="sc-rqvnx3-0 kTxXTj audio-button icon-button" aria-label="Audio"><img src="https://client-api.arkoselabs.com/cdn/fc/assets/style-manager/assets/e94ae91f-1774-408b-a8b3-1237915c996c.svg" alt=""><p font-size="0.625r" class="sc-1io4bok-0 eIWPBf text">Audio</p></button>
        # button = page.query_selector('[class*="sc-rqvnx3-0.kTxXTj.audio-button.icon-button"]')
        # button = page.locator('sc-rqvnx3-0.kTxXTj.audio-button.icon-button')
        # button = page.locator('aria-label="Audio"')
        # button = page.locator('e94ae91f-1774-408b-a8b3-1237915c996c.svg')
        # button = page.locator('.img')
        
        #button = page.locator('button[href*="arkoselabs.com"]')
        #button = page.get_by_role("button")
        
        #button = page.get_by_title("Audio")
        #button.click()
        
        #button = page.get_by_label("Audio")
        # button.click()
        
        #button = page.get_by_placeholder("Audio")
        #button.click()
        
        #page.get_by_role("button", name=re.compile("audio", re.IGNORECASE)).click(force=True)
        
        # page.get_by_alt_text("").click()
        
        # page.get_by_text(re.compile("audio", re.IGNORECASE)).click()
        
        # page.get_by_label("Audio").click()
        
        time.sleep(100)
        "div.sc-99cwso-0.sc-1cbf51e-0.gMEQEa.fLfntv.navigation.box"
        
        
    
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
    
    proxy = get_proxy()
    print(proxy)
        
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
        creds = f"Account #{i},name: {name},email: {email},password: {password},\n"
        print("---STARTING REGISTRATION: ", creds)
        create_twitter_account(name, email, month, day, year, password, avatar, agent, proxy)
        print("---USER CREATED: ", creds)
        with open("tw_accounts.txt", 'w') as file:
            file.write(creds)
            print(f"USER {i} SAVED")
