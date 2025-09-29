import sys
import random
from tts import TTS
from autoGui import AguiTools
from PySide6.QtWidgets import QApplication
import time
import pyautogui as agui
from windowAM import MainWindow
from messageTelegram import  send_message_cele_telegram


def drag_and_drop(imageToDrag, imageToDropOn):
    print("nuovo drag and drop 1")
    time.sleep(random.uniform(0.1, 1.8))

    locationToDrag = agui.locateCenterOnScreen(imageToDrag, confidence=0.8)
    print("AM locationToDrag"+str(locationToDrag))
    locationToDropOn = agui.locateCenterOnScreen(imageToDropOn, confidence=0.8)
    print("tiktok locationToDropOn"+str(locationToDropOn))
    agui.moveTo(locationToDrag)
    time.sleep(random.uniform(0.1, 2.1))
    TTS.read("Draggo")
    agui.mouseDown(button='left')
    agui.moveTo(locationToDropOn, duration=random.uniform(0.3, 2.1))  # Durata di 1 secondo per il movimento
    # Rilasciare il mouse per completare il drag and drop
    agui.mouseUp(button='left')
    TTS.read("drop")


# Funzione per gestire la finestra principale
def run_window(file_list):
    app = QApplication(sys.argv)
  #  app = QApplication([])
    window = MainWindow(file_list)
    window.show()
    app.exec_()

# Funzione per eseguire il controllo immagine
def run_image_check():
    image_check("images/am.png")

def pause():
    time.sleep(random.uniform(0.05, 0.15))


def check_and_click(image, seconds=20):
    image_check(image, seconds)
    time.sleep(random.uniform(0.05, 0.1))
    agui_tools.moveToImageCenter(image, random.uniform(0.05, 0.11))
    time.sleep(random.uniform(0.05, 0.1))
    agui.click()

def image_check(image, seconds=20):
    ok = False
    for i in range(seconds):
        print(f"secondi caricamento {i + 1}")
        time.sleep(1)
        if agui_tools.imagePresent(image):
            ok = True
            print(image + " present")
            break
    if not ok:
        print(image + " missing")
        TTS.read(image + " missing")
        TTS.read("Programma terminato")
        send_message_cele_telegram("Automazione BLOCCATA su immagine" + image )
        sys.exit()

def load_video():
    image_check(uploadPlus)
    agui_tools.imageClick(uploadPlus)
    time.sleep(random.uniform(0.1, 0.12))
    # agui_tools.imageClick(uploadPlus)
    image_check(videoUploadArea)
    image_check(iconAM)
    pause()
    drag_and_drop(iconAM, videoUploadArea)
    pause()
    image_check(hashAstromostro, seconds=120)
    TTS.read("tag")
    agui_tools.moveToImageCenter(hashAstromostro, random.uniform(0.3, 1.9))
    for i in range(15):
        agui.click()
        #  TTS.read("t")
        pause()
    TTS.read("tag finiti")
    pause()
    image_check(uploaded, seconds=180)
    TTS.read("caricato")
    pause()
    agui.scroll(-1300)
    TTS.read("scrollato")

def set_clock():
    image_check(clock)
    time.sleep(random.uniform(0.05, 0.1))
    agui_tools.moveToImageCenter(clock, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.05, 0.1))
    TTS.read("clocko")
    agui.click()
    time.sleep(random.uniform(0.1, 0.2))

    loc = agui.locateCenterOnScreen(clock, confidence=0.9)
    if loc is not None:
        print("CLOCK")
        print(loc)
        agui.moveTo(loc.x + 10, loc.y - 100, duration=0.1)
        time.sleep(random.uniform(0.1, 0.2))
        for i in range(24):
            agui.scroll(-900)
            time.sleep(random.uniform(0.05, 0.12))

        time.sleep(random.uniform(0.05, 0.15))
        agui.moveTo(loc.x + 120, loc.y - 100, duration=0.1)
        time.sleep(random.uniform(0.05, 0.15))
        for i in range(24):
            agui.scroll(-900)
            time.sleep(random.uniform(0.05, 0.14))
        time.sleep(random.uniform(0.05, 0.15))
        return loc

def set_clock_time(hours, minutes):
    image_check(clock)
    time.sleep(random.uniform(0.05, 0.1))
    agui_tools.moveToImageCenter(clock, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.05, 0.1))
    TTS.read("clocko")
    agui.click()
    time.sleep(random.uniform(0.1, 0.2))

    loc = agui.locateCenterOnScreen(clock, confidence=0.9)
    if loc is not None:
        print("CLOCK")
        print(loc)
        agui.moveTo(loc.x + 10, loc.y - 100, duration=0.1)
        time.sleep(random.uniform(0.1, 0.2))
        for i in range(24):
            agui.scroll(-900)
            time.sleep(random.uniform(0.05, 0.12))
        for i in range(23-hours):
            agui.scroll(900)
            time.sleep(random.uniform(0.05, 0.12))

        time.sleep(random.uniform(0.05, 0.15))
        agui.moveTo(loc.x + 120, loc.y - 100, duration=0.1)
        time.sleep(random.uniform(0.05, 0.15))
        for i in range(24):
            agui.scroll(-900)
            time.sleep(random.uniform(0.05, 0.14))
        for i in range(12 - (minutes // 5)):
            agui.scroll(900)
            time.sleep(random.uniform(0.05, 0.14))
        time.sleep(random.uniform(0.05, 0.15))
        return loc


def publish_now():
    TTS.read("automazione Post Now")
    load_video()

    if skipcontrol:
        check_and_click(cancel)

    check_and_click(post)

    check_and_click(post)
    TTS.read("posto")
    image_check(successivo)
    agui_tools.imageClick(successivo)
    time.sleep(random.uniform(2, 3.1))

def publish_before_midnight():
    TTS.read("automazione Sul tardi oggi")
    load_video()

    check_and_click(schedule)

    time.sleep(random.uniform(0.1, 0.2))

    loc=set_clock()

    agui.moveTo(loc.x, loc.y , duration=0.1)
    pause()
    agui.scroll(-1300)
    pause()
    image_check(red_schedule)
    pause()
    agui_tools.moveToImageCenter(red_schedule, random.uniform(0.3, 0.5))
    pause()
    agui.click()
    TTS.read("schedullo")


    time.sleep(random.uniform(1, 2.1))
    TTS.read("emozione!!! ")
    image_check(views)
    image_check(successivo)
    agui_tools.imageClick(successivo)
    time.sleep(random.uniform(2, 3.1))

def publish_day(image_day, hours, minutes):
    TTS.read("automazione Day")
    load_video()

    if skipcontrol:
        check_and_click(cancel)

    check_and_click(schedule)
    check_and_click(calendar_icon)
    #comment this if in not change mouth
    #check_and_click(cambioMese)

    check_and_click(image_day)

    time.sleep(random.uniform(0.1, 0.2))
    #loc = set_clock()
    loc=set_clock_time(hours, minutes)

    agui.moveTo(loc.x, loc.y , duration=0.1)
    pause()
    agui.scroll(-1300)
    pause()
    image_check(red_schedule)
    pause()
    agui_tools.moveToImageCenter(red_schedule, random.uniform(0.1, 0.3))
    pause()
    agui.click()
    TTS.read("schedullo")

    time.sleep(random.uniform(1, 2.1))
    TTS.read("emozione!!! ")
    image_check(views)
    image_check(successivo)
    agui_tools.imageClick(successivo)
    time.sleep(random.uniform(2, 3.1))

def get_random_minutes():
    values = [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    return random.choice(values)

def get_random_steps():
    values = [  20, 25]
    return random.choice(values)

def get_random_steps_short():
    values = [  5, 10,15]
    return random.choice(values)


def schedule_posts(start_hour, start_minute, minute_step, calendar_day, max_cycles=12):
    """
    Programma le pubblicazioni a intervalli regolari

    Args:
        start_hour (int): Ora di inizio (0-23)
        start_minute (int): Minuto di inizio (0-59)
        minute_step (int): Intervallo in minuti tra le pubblicazioni
        calendar_day (str): Riferimento al giorno del calendario
        max_cycles (int): Numero massimo di pubblicazioni (default: 12)
    """
    from datetime import datetime, timedelta

    current_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)

    for _ in range(max_cycles):
        print(f"Pubblicazione alle: {current_time.strftime('%H:%M')}")
        publish_day(calendar_day, current_time.hour, current_time.minute)

        # Aggiungi l'intervallo di tempo
        current_time += timedelta(minutes=minute_step)

#uploadPlus = "images/uploadBuzz.png"
uploadPlus = "images/plusUpload.png"
videoUploadArea = "images/uploadAreaVps.PNG"
iconAM = "images/am.png"
hashAstromostro = "images/astromostro_tag_vps.PNG"
uploaded = "images/uploaded_vps.PNG"
post = "images/Post_vps.PNG"
views = "images/views_vps_old.PNG"
successivo = "images/successivo_vps.PNG"
schedule = "images/schedule_vps.PNG"
clock = "images/clock_vps.PNG"
red_schedule = "images/red_schedule_vps.PNG"
calendar_icon = "images/calendar_vps.PNG"
cambioMese="images/CambioMese.PNG"
day_on_calendar1 = "images/30settembre.PNG"
day_on_calendar2 = "images/1ottobre.PNG"
day_on_calendar3 = "images/2ottobre.PNG"
day_on_calendar4 = "images/3ottobre.PNG"
cancel = "images/skipcheck.PNG"
skipcontrol = False

agui_tools = AguiTools()

send_message_cele_telegram("Automazione ASTROMOSTRO Inizio" )
for i in range(12):
    print (i)
    #publish_now()
    #publish_before_midnight()
    #publish_day(day_on_calendar1)

schedule_posts(
    start_hour=18,
    start_minute=get_random_minutes(),
    minute_step=get_random_steps(),
    calendar_day=day_on_calendar1,
    max_cycles=12
)

schedule_posts(
    start_hour=18,
    start_minute=get_random_minutes(),
    minute_step=get_random_steps(),
    calendar_day=day_on_calendar2,
    max_cycles=12
)

schedule_posts(
    start_hour=18,
    start_minute=get_random_minutes(),
    minute_step=get_random_steps(),
    calendar_day=day_on_calendar3,
    max_cycles=12
)

schedule_posts(
    start_hour=15,
    start_minute=get_random_minutes(),
    minute_step=get_random_steps_short(),
    calendar_day=day_on_calendar4,
    max_cycles=12
)


send_message_cele_telegram("Automazione ASTROMOSTRO terminata tutto ok!")
TTS.read("Attenzione Terminato tutto")
sys.exit(0)












