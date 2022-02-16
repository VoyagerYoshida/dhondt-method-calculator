import configparser
import datetime

from selenium.webdriver import ChromeOptions, Remote
from selenium.webdriver.common.by import By


def collect():
    parser = configparser.ConfigParser()
    parser.read('./config.ini', encoding='utf-8')
    config = parser['COLLECT']

    base_url = config.get('BASE_URL')
    year = config.get('YEAR')
    num_parties = int(config.get('NUM_PARTIES'))
    remote_container = config.get('REMOTE_CONTAINER_NAME')

    options = ChromeOptions()
    driver = Remote(command_executor=remote_container+':4444/wd/hub', options=options)
    driver.get(base_url+"/"+year+"/00/hsm11.html")
    print("Access to ", driver.current_url)

    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    log_path = "./log/" + now.strftime('%Y%m%d%H%M%S') + ".txt"
    xpath_prefix = '//*[@id="senkyo-main"]/div[1]/div[2]/div/table/tbody/'
    with open(log_path, mode='w') as f:
        for i in range(num_parties):
            party_name = driver.find_element(by=By.XPATH, value=xpath_prefix+'tr[' + str(i+1) + ']/td[1]/a')
            num_searts = driver.find_element(by=By.XPATH, value=xpath_prefix+'tr[' + str(i+1) + ']/td[2]')
            vote = driver.find_element(by=By.XPATH, value=xpath_prefix+'tr[' + str(i+1) + ']/td[4]/div')
            line = party_name.text+'-'+num_searts.text+'-'+vote.text
            print(line)
            f.write(line+'\n')

    driver.quit()


if __name__ == '__main__':
    collect()
