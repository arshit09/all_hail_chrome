""""
Change default browser in Windows 11 to Chrome

----Constraint----
OS: Windows 11
Display resolution: 1920*1080
Windows theme: Dark mode
Scale and layout: 125%
"""

import pyautogui
import time


def click_image(image_name):
    click_image = pyautogui.locateOnScreen(
        'Images/' + image_name + '.png', confidence=0.9)
    while click_image == None:
        click_image = pyautogui.locateOnScreen(
            'Images/' + image_name + '.png', confidence=0.9)
    pyautogui.click(pyautogui.center(click_image), duration=0.5)
    time.sleep(0.25)


def chrome_ok_click():
    click_image('Chrome')
    click_image('OK')


def extension_click(extension):
    time.sleep(0.5)
    click_image(extension)
    pyautogui.moveRel(113, 55, duration=0.25)
    pyautogui.click()
    chrome_ok_click()


pyautogui.hotkey('win', 'i')
time.sleep(0.5)

click_image('AppsInNavbar')

time.sleep(0.5)
click_image('DefaultApps')
click_image('Search')

time.sleep(0.5)
pyautogui.write('chrome')
pyautogui.moveRel(0, 70)
time.sleep(0.25)
pyautogui.click()
time.sleep(0.25)

extension_click('htm')
# click html - bot is confused for HTM & HTML
pyautogui.click(542, 414)
chrome_ok_click()
# ---------------------------------------------
extension_click('pdf')
extension_click('shtml')
extension_click('svg')
pyautogui.scroll(-200)
extension_click('webp')
extension_click('xht')
extension_click('xhtml')
extension_click('ftp')
extension_click('http')
pyautogui.scroll(-200)
extension_click('https')
extension_click('mailto')
