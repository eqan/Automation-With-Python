import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    

def get_status(logs):
    for log in logs:
        if log['message']:
            d = json.loads(log['message'])
            try:
                content_type = 'text/html' in d['message']['params']['response']['headers']['content-type']
                response_received = d['message']['method'] == 'Network.responseReceived'
                if content_type and response_received:
                    return d['message']['params']['response']['status']
            except:
                pass

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", desired_capabilities=capabilities)

try:
    driver.get('https://gmail.com')
    logs = driver.get_log('performance')
    status_code = get_status(logs)
    if(status_code == 200):
        print('Website is up!')
    else:
        print('Website is down!')
except Exception as inst:
    print(inst)
    
driver.close()
