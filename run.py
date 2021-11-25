from selenium import webdriver
import sys
import  time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import os
import json

chrm_options=Options()
chrm_caps = webdriver.DesiredCapabilities.CHROME.copy()
chrm_caps['goog:loggingPrefs'] = { 'performance':'ALL' }
driver = webdriver.Chrome(executable_path = 'chromedriver.exe', chrome_options=chrm_options,desired_capabilities=chrm_caps) #Windows
#driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options=chrm_options,desired_capabilities=chrm_caps) #Linux


def LoadWebDriver() :
    print("Web driver Init ")
    base_url = "https://pocketoption.com/en/cabinet/demo-quick-high-low/#td"  #Change the site
    print('Loading URL ....')
    driver.get(base_url )
    

def WebSocketLog():
    for wsData in driver.get_log('performance'):
        #print(wsData) 
        wsJson = json.loads((wsData['message']))
        print(wsData)
#         if wsJson["message"]["method"]== "Network.webSocketFrameReceived":
#             print ("Rx :"+ str(wsJson["message"]["params"]["timestamp"]) + wsJson["message"]["params"]["response"]["payloadData"])
#         if wsJson["message"]["method"] =="Network.webSocketFrameSent":
#             print ("Tx :"+ wsJson["message"]["params"]["response"]["payloadData"])


LoadWebDriver()
print("Waiting")
time.sleep(30) #Capt