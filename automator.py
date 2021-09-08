import os
import pyautogui
import pandas as pd
import time
from datetime import datetime


def signin(link, roll):

    command = "cmd /c "
    cmd = "start chrome "+link
    command = command + cmd
    os.system(command)

    time.sleep(60)

    meeting_recorded_got_it = pyautogui.locateCenterOnScreen('img/got_it.png')
    # print(meeting_recorded_got_it)
    pyautogui.moveTo(meeting_recorded_got_it)
    pyautogui.click()

    time.sleep(2)

    # meeting_id = pyautogui.locateCenterOnScreen('img/meeting_id.png')
    # pyautogui.moveTo(meeting_id)
    # pyautogui.click()
    # pyautogui.write(link)

    join_audio = pyautogui.locateCenterOnScreen('img/join_with_audio.png')
    # print(join_audio)
    pyautogui.moveTo(join_audio)
    pyautogui.click()

    time.sleep(2)

    pyautogui.hotkey('alt', 'u')

    time.sleep(2)

    name = pyautogui.locateCenterOnScreen('img/name.png')
    # print(name)
    pyautogui.moveTo(name)
    # pyautogui.click()

    time.sleep(10)

    more_btn = pyautogui.locateCenterOnScreen('img/more.png')
    pyautogui.moveTo(more_btn)
    pyautogui.click()

    time.sleep(5)

    rename = pyautogui.locateCenterOnScreen('img/rename.png')
    pyautogui.moveTo(rename)
    pyautogui.click()

    time.sleep(7)

    pyautogui.write(roll)
    pyautogui.press('enter')

    time.sleep(5)

    pyautogui.hotkey('alt', 'q')
    pyautogui.press('enter')


df = pd.read_csv("timetable.csv")

while(True):
    now = datetime.now().strftime("%H:%M")
    # now = "10:49"
    day = datetime.today().weekday()
    if now in str(df['time']):
        row = df.loc[(df["time"] == now) & (df["day"] == day)]
        link = str(row.iloc[0,3])
        roll = str(row.iloc[0, 4])

        signin(link, roll)
        