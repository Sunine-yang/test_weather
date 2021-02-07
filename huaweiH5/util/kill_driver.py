import os


def kill_driver():
    os.system('taskkill /im chrome.exe /F')
    os.system('taskkill /im chromedriver.exe /F')


# kill_driver()
