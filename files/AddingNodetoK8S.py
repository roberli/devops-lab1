import time
from selenium import webdriver
"""
The following three lines are default to execute dynamic the selenium withou 
think about the specific version of driver manager of each browser, that's necessary 
if you don't use the library webdriver-manager. That has the function to abstract manager the version
of interact module of project itself
"""
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://192.168.56.80/login")

"""
Because of the invalid certificate, it's  the  next to lines as necessary extra step 
to accept the warning of the browser
"""
navegador.find_element('xpath', '//*[@id="details-button"]').click()
navegador.find_element('xpath', '//*[@id="proceed-link"]').click()

"""
It has been necessary to put pause time wait because the full load of browser and answer unfortunily,
in this case don't answer quick enough
"""
time.sleep(5)

# Authentication on Rancher Server
navegador.find_element('xpath', '//*[@id="login-username-local"]').send_keys("admin")
navegador.find_element('xpath', '//*[@id="login-password-local"]').send_keys("123qwe!@#")

navegador.find_element('xpath', '//*[@id="ember11"]/form/p/button').click()

# Creating a new cluster k8s on Rancher Server
time.sleep(2)
navegador.find_element('xpath', '//*[@id="ember29"]').click()

time.sleep(2)
navegador.find_element('xpath', '//*[@id="ember85"]').click()

time.sleep(2)
navegador.find_element('xpath', '//*[@id="ember105-form-name"]').send_keys("ClusterNnameDesired")
navegador.find_element('xpath', '//*[@id="ember132"]/button[1]').click()

time.sleep(5)
# Check the box to seletc the role etcd of node k8s
navegador.find_element('xpath', '//*[@id="ember179"]').click()

# Check the box to select the role control plane of node k8s
navegador.find_element('xpath', '//*[@id="ember180"]').click()
"""
The role worker It's not necessary to check, because when you are creating a new cluster 
already checked
"""

# Copy the command that will be executed at server that will join the cluster k8s
command_to_join_cluster = navegador.find_element('xpath', '//*[@id="registration-command"]').text

# Finish the creating of Custom cluter on Rancher
navegador.find_element('xpath', '//*[@id="ember119"]/div[3]/button').click()

# Get the command to join a new member to the cluster Rancher
print(command_to_join_cluster)