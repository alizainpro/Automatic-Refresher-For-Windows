from os import system
from pyautogui import click,hotkey
from pystray import *
from PIL import Image
state = False
state2 = False
def create_image():
    image = Image.open("google icon.png")
    return image
def refresh_on_click(self,item):
    global state
    state = not item.checked
    click(1103,204)
    for i in range(15):
        hotkey('f5')
def exitonclick(self,items):
    global state2
    state2 = not items.checked
    # TODO : SOME UNUSUAL PROCESS RUNNING BEHIND!
    # Customize YOURSELF!
    system('taskkill /F /IM "Adobe CEF Helper.exe"')
    system('taskkill /F /IM "Creative Cloud.exe"')
    system('taskkill /F /IM "Adobe Desktop Service.exe"')
    system('taskkill /F /IM "CCXProcess.exe"')
    system('taskkill /F /IM "CoreSync.exe"')
    system('taskkill /F /IM "node.exe"')
    system('taskkill /F /IM "AdobeIPCBroker.exe"')
    system('taskkill /F /IM "WSHelper.exe"')
    system("taskkill /F /IM pythonw.exe")
    system("taskkill /F /IM python.exe")
def main():
    click(1103,2)
main()
for i in range(15):
    hotkey('f5')
icon = Icon('Refresher',
            icon=create_image(),title="Refresher",menu=Menu(
                MenuItem('Refresh Now!',refresh_on_click,
                    checked=lambda item: icon.notify(
'Developed by Ali Zain!\nTIP:Press Ctrl+Shift+` to refresh more quickly!','Refreshed Successfully!')),
                MenuItem('EXIT-->',exitonclick,checked=lambda items: icon.notify(
                        title="Good Bye!",
                        message="Thanks for using!\nTIP:Press Ctrl+Shift+` to Refresh!"))))
icon.notify('Developed by Ali Zain!\nTIP:Press Ctrl+Shift+` to refresh more quickly!','Refreshed Successfully!')
icon.run()