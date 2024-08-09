from rich.console import Console
from rich.text import Text
import random
from colorama import Fore, Back, Style, init
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from texttable import Texttable
import time
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

pathtochromedrive="" #add chrome driver path

init(autoreset=True) 

ascii=[
"""
 __  .__   __. .___________..______       __    __   _______   _______ .______      
|  | |  \ |  | |           ||   _  \     |  |  |  | |       \ |   ____||   _  \     
|  | |   \|  | `---|  |----`|  |_)  |    |  |  |  | |  .--.  ||  |__   |  |_)  |    
|  | |  . `  |     |  |     |      /     |  |  |  | |  |  |  ||   __|  |      /     
|  | |  |\   |     |  |     |  |\  \----.|  `--'  | |  '--'  ||  |____ |  |\  \----.
|__| |__| \__|     |__|     | _| `._____| \______/  |_______/ |_______|| _| `._____|
""",
'''
 ▄█  ███▄▄▄▄       ███        ▄████████ ███    █▄  ████████▄     ▄████████    ▄████████ 
███  ███▀▀▀██▄ ▀█████████▄   ███    ███ ███    ███ ███   ▀███   ███    ███   ███    ███ 
███▌ ███   ███    ▀███▀▀██   ███    ███ ███    ███ ███    ███   ███    █▀    ███    ███ 
███▌ ███   ███     ███   ▀  ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███▌ ███   ███     ███     ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███  ███   ███     ███     ▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████ 
███  ███   ███     ███       ███    ███ ███    ███ ███   ▄███   ███    ███   ███    ███ 
█▀    ▀█   █▀     ▄████▀     ███    ███ ████████▀  ████████▀    ██████████   ███    ███ 
                             ███    ███                                      ███    ███ 
''',
"""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
     ▐░▌     ▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
     ▐░▌     ▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▐░▌     ▐░▌   ▐░▌ ▐░▌     ▐░▌     ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
     ▐░▌     ▐░▌    ▐░▌▐░▌     ▐░▌     ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌     ▐░▌  
 ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌     ▐░▌     ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
▐░░░░░░░░░░░▌▐░▌      ▐░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀       ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
"""
]

def cgt(text, st, ec, steps):
    gradient_text = Text()
    for i in range(steps):
        ratio = i / (steps - 1)
        r = int(st[0] * (1 - ratio) + ec[0] * ratio)
        g = int(st[1] * (1 - ratio) + ec[1] * ratio)
        b = int(st[2] * (1 - ratio) + ec[2] * ratio)
        color = f"rgb({r},{g},{b})"
        gradient_text.append(text[i], style=color)
    return gradient_text

console = Console()
cyan = (0, 255, 255)
blue = (0, 0, 255)

def printbuttons(driver):
    table = Texttable()
    table.set_cols_align(["c", "c", "c", "c"])
    table.set_cols_valign(["m", "m", "m", "m"])
    table.set_cols_width([20, 20, 20, 30])
    table.header(["text", "class(es)", "id", "extra"])
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="submit"]')
    
    all_elements = buttons + inputs
    
    for element in all_elements:
        if element.tag_name == 'button':
            text = element.text or "no text"
        else:
            text = element.get_attribute('value') or "no text" 

        element_id = element.get_attribute('id') or "no id"
        element_class = element.get_attribute('class') or "no class"

        extra_attributes = []
        if element.tag_name == 'button':
            button_type = element.get_attribute('type')
            button_name = element.get_attribute('name')

            if button_type:
                extra_attributes.append(f"type; {button_type}")
            if button_name:
                extra_attributes.append(f"name; {button_name}")
        else: 
            input_name = element.get_attribute('name')
            extra_attributes.append("type; submit")
            if input_name:
                extra_attributes.append(f"name; {input_name}")
        extra_attributes_str = ', '.join(extra_attributes) if extra_attributes else "no extra"
        
        table.add_row([text, element_class, element_id, extra_attributes_str])
    
    console.print(cgt(table.draw(), cyan, blue, len(table.draw())))

def printentry(driver):
    table = Texttable()
    table.set_cols_align(["c", "c", "c", "c"])
    table.set_cols_valign(["m", "m", "m", "m"])
    table.set_cols_width([20, 20, 20, 30])
    table.header(["name", "class", "id", "extra"])
    
    entries = driver.find_elements(By.TAG_NAME, 'input')
    for entry in entries:
        entry_type = entry.get_attribute('type')
        if entry_type == 'submit':
            continue
        
        name = entry.get_attribute('name') or "no name"
        entry_class = entry.get_attribute('class') or "no class"
        entry_id = entry.get_attribute('id') or "no id"
        extra_attributes = []
        
        if entry_type:
            extra_attributes.append(f"type; {entry_type}")
        entry_placeholder = entry.get_attribute('placeholder')
        if entry_placeholder:
            extra_attributes.append(f"placeholder; {entry_placeholder}")
        extra_attributes_str = ', '.join(extra_attributes) if extra_attributes else "no extra"
        table.add_row([name, entry_class, entry_id, extra_attributes_str])
    table_output = table.draw()
    console.print(cgt(table_output, cyan, blue, len(table_output)))

def spinner(duration=3):
    spinner = ['-', '\\', '|', '/']
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in spinner:
            sys.stdout.write(f'\rLOADING {frame}')
            sys.stdout.flush()
            time.sleep(0.1)

if __name__ == "__main__":
    x = f"{Fore.BLUE} $ {Fore.CYAN}> {Style.RESET_ALL}"
    xssx = "[ XSS ] > "
    start = True
    onxss = False
    asci = random.choice(ascii)
    asciii = cgt(asci, cyan, blue, len(asci))
    console.print(asciii)
    joinstand = "add @xd4018 on discord for more information"
    console.print(cgt((joinstand), cyan, blue, len(joinstand)))
    print("\n")
    
    while start:
        command = input(x)
        if command.startswith("cd "):
            if command == "cd xss":
                start = False
                onxss = True
                while onxss:
                    command = input(f"{Fore.BLUE} XSS {Fore.CYAN}> {Style.RESET_ALL}")
                    if command.startswith("xss"):
                        if "-c" in command:
                            parts = command.split()
                            if "-cb" in parts:
                                index = parts.index("-cb") + 1
                                if index < len(parts):
                                    website = parts[index]
                                    chrome_options = Options()
                                    chrome_options.add_argument("--headless")
                                    chrome_options.add_argument("--no-sandbox")
                                    chrome_options.add_argument("--disable-dev-shm-usage")
                                    service = Service(pathtochromedrive)
                                    driver = webdriver.Chrome(service=service, options=chrome_options)
                                    
                                    spinner_thread = threading.Thread(target=spinner, args=(5,))
                                    spinner_thread.start()
                                    
                                    driver.get(website)
                                    driver.implicitly_wait(5)
                                    spinner_thread.join()  
                                    print("\n")
                                    printbuttons(driver)
                                else:
                                    i = "add an arg"
                                    console.print(cgt((i), cyan, blue, len(i)))
                            if "-ce" in parts:
                                index = parts.index("-ce") + 1
                                if index < len(parts):
                                    website = parts[index]
                                    chrome_options = Options()
                                    chrome_options.add_argument("--headless")
                                    chrome_options.add_argument("--no-sandbox")
                                    chrome_options.add_argument("--disable-dev-shm-usage")
                                    service = Service(pathtochromedrive)
                                    driver = webdriver.Chrome(service=service, options=chrome_options)
                                
                                    spinner_thread = threading.Thread(target=spinner, args=(5,))
                                    spinner_thread.start()
                                    
                                    driver.get(website)
                                    driver.implicitly_wait(5)
                                    spinner_thread.join() 
                                    print("\n")
                                    printentry(driver)
                                else:
                                    i = "add an arg"
                                    console.print(cgt((i), cyan, blue, len(i)))






                    if command.startswith('startxss'):
                        command = command.replace("type submit", "xpath //input[@type='submit']")
                        parts = command.split()

                        l11 = l12 = c11 = c12 = None
                        website = None

                        if "-l1" in command:
                            l11 = parts[parts.index("-l1") + 1]  
                            l12 = parts[parts.index("-l1") + 2]  
                        if "-c1" in command:
                            c11 = parts[parts.index("-c1") + 1]  
                            c12 = parts[parts.index("-c1") + 2] 
                        if "-s" in command:
                            website = parts[parts.index("-s") + 1]

                        chrome_options = Options()
                        chrome_options.add_argument("--headless")
                        chrome_options.add_argument("--no-sandbox")
                        chrome_options.add_argument("--disable-dev-shm-usage")
                        service = Service(pathtochromedrive)
                        driver = webdriver.Chrome(service=service, options=chrome_options)
                        
                        table = Texttable()
                        table.set_cols_align(["l", "c", "l"])
                        table.set_cols_valign(["m", "m", "m"])
                        table.add_row(["payload", "error", "notes"])

                        try:
                            driver.get(website)

                            harmless_payload = "a"
                            if l11 and l12:
                                input_field = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((getattr(By, l11.upper()), l12))
                                )
                                input_field.send_keys(harmless_payload)

                            if c11 and c12:
                                submit_button = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((getattr(By, c11.upper()), c12))
                                )
                                submit_button.click()

                            initial_page_source = driver.page_source
                            initial_alert_present = False
                            try:
                                alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                                initial_alert_present = True
                                alert.accept() 
                            except TimeoutException:
                                initial_alert_present = False

                            with open('xssi.txt', 'r') as file:
                                for line in file:
                                    payload = line.strip()
                                    if not payload:  
                                        continue
                                    if l11 and l12:
                                        input_field = WebDriverWait(driver, 30).until(
                                            EC.presence_of_element_located((getattr(By, l11.upper()), l12))
                                        )
                                        input_field.clear()  
                                        input_field.send_keys(payload)
                                    if c11 and c12:
                                        submit_button = WebDriverWait(driver, 30).until(
                                            EC.presence_of_element_located((getattr(By, c11.upper()), c12))
                                        )
                                        submit_button.click()

                                    alert_present = False
                                    try:
                                        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                                        alert_present = True
                                        alert_text = alert.text
                                        alert.accept() 
                                    except TimeoutException:
                                        alert_present = False

                                    error = "x"
                                    details = ""
                                    if alert_present:
                                        error = "✓"
                                        details = f"notes: {alert_text}; "
                                    elif initial_alert_present:
                                        error = "✓"
                                        details = "alert was present before but not now."
                                    if alert_present or (alert_present != initial_alert_present):
                                        details += f"page changed significantly"
                                    table.add_row([payload, error, details])
                                    driver.refresh()
                            #print(table.draw())
                            console.print(cgt((table.draw()), cyan, blue, len(table.draw())))

                        except Exception as e:
                            print(f"An error occurred: {str(e)}")
                        finally:
                            driver.quit()

                    elif command == "cd":
                        onxss = False
                        start = True
            else:
                print(f"cd: no such file or directory: {command[3:]}")
