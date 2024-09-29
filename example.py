import json
import time
import threading
from playwright.sync_api import sync_playwright



def logout(browser):
    if input() == "0":
        browser.close()

def login(web,num,pw):
    web.goto('https://cp.allcpp.cn/#/login/main')
    web.get_by_role("tab", name="密码登录").click()
    web.get_by_placeholder("请输入手机号码或邮箱").fill(num)
    web.get_by_placeholder("请输入密码").fill(pw)
    web.get_by_role("button", name="登录").click()


def bookticket(web,event,ticket):
    while True:
        while True:
            web.goto(event)
            web.get_by_text("票种：").wait_for()
            if web.get_by_text('立即购票').is_visible() == True:
                print("ticket exist!")
                break
            print("ticket absence!")
        web.get_by_text(ticket).click()
        if web.locator('.buy-ticket-number').is_visible() == True:
            web.locator('.buy-ticket-number').fill('2')
            print("two ticket!")
        else:
            print("one ticket")
        web.get_by_role("button", name="立即购票").click()
        if web.url != event:
            print("booking success!")
            print(web.url)
            break
def mainbooking(browser,number,password):
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)
    page = browser.new_page()
    page.set_default_timeout(3000000)
    login(page,number,password)
    bookticket(page,data['event_url'],data['ticket_type'])
    logout(browser)

def get_data():
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)
        number = data['number']
        password = data['password']
        event_url = data['event_url']
        ticket_type = data['ticket_type']
    return number, password, event_url, ticket_type


def process_one():
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)
    number = data['number1']
    password = data['password1']
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        mainbooking(browser,number,password)

def process_two():
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)
    number = data['number2']
    password = data['password2']
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        mainbooking(browser,number,password)

def process_three():
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)
    number = data['number3']
    password = data['password3']
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        mainbooking(browser,number,password)

if __name__ == "__main__":
    thread1 = threading.Thread(target=process_one)
    thread2 = threading.Thread(target=process_two)
    thread3 = threading.Thread(target=process_three)
    
    thread1.start()
    thread2.start()
    thread3.start()
    
    thread1.join()
    thread2.join()
    thread3.join()


    
    
