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

def pause2Sec():
    time.sleep(random.uniform(1.65, 2.15))

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
    agui_tools.moveToImageCenter(hashAstromostro, random.uniform(0.3, 1.3))
    for i in range(30):
        agui.click()
        #  TTS.read("t")
        pause()
    TTS.read("tag finiti")
    pause()
    image_check(uploaded, seconds=180)
    TTS.read("caricato")
    pause()

    #cambia thumb
    if agui_tools.imagePresent(editCover):
        agui_tools.moveToImageCenter(editCover,random.uniform(0.3, .6))
        TTS.read("open edit cover")
        pause()
        agui.click()
        TTS.read("click")
        pause()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        pause2Sec()
        agui_tools.moveToImageCenter(blackFrame, random.uniform(0.3, .6))
        TTS.read("black")
        #agui.click()

        agui_tools.moveToImageCenter(blackFrame2, random.uniform(0.3, .6))
            # agui.click()
            #  TTS.read("black 2")
                 #  agui_tools.moveToImageCenter(blackFrame, random.uniform(0.3, .6))
            #  agui.click()
            #  TTS.read("black")
            #  pause2Sec()
             # check_and_click(blackFrame, 6)
             # drag_and_drop(UploadNow,blackFrame)

        check_and_click(bottoncino,6)
        TTS.read("bottoncino click")
         # agui.click()
        # agui_tools.moveToImageCenter(bottoncino, random.uniform(0.3, .6))
        #agui.click()
        #agui_tools.moveToImageCenter(SaveThumb, random.uniform(0.3, .6))
        #agui.click()
    while  agui_tools.imagePresent(SaveThumb):
        agui_tools.moveToImageCenter(UploadNow, random.uniform(0.3, .6))
        pause2Sec()
        agui_tools.moveToImageCenter(SaveThumb, random.uniform(0.3, .6))
        agui.click()
        #check_and_click(SaveThumb, 8)
        pause2Sec()
        pause2Sec()
        TTS.read("Save  click")

    while  not agui_tools.imagePresent(uploaded):
        pause2Sec()
        TTS.read("waiting")

    pause2Sec()
    agui_tools.moveToImageCenter(uploaded, random.uniform(0.3, .6))
    agui.click()
    pause()
    TTS.read("now scroll")
    agui.scroll(-1300)
    TTS.read("scrollato")

def detect_schedule_layout(seconds=20):
    """
    Rileva automaticamente se siamo di fronte al NUOVO layout (3 menu a tendina:
    Calendario | Orologio | Timezone) oppure al VECCHIO layout (2 menu a tendina:
    Orologio | Calendario).
    Restituisce (layout_type, active_calendar_icon, active_clock_icon).
    """
    for i in range(seconds):
        print(f"secondi rilevamento layout schedule {i + 1}")
        time.sleep(1)

        # 1. Controllo Nuovo Layout: presenza del 3° menu Timezone
        if agui_tools.imagePresent(timezone_new_icon):
            print("[Layout Schedule] Rilevato NUOVO layout (3 menu a tendina)")
            return "new", calendar_new_icon, clock_new_icon

        # 2. Controllo tramite posizione relativa tra Calendario e Orologio
        cal_new_loc = None
        cal_old_loc = None
        clk_loc = None
        try:
            cal_new_loc = agui.locateCenterOnScreen(calendar_new_icon, confidence=0.85)
        except Exception:
            pass
        try:
            cal_old_loc = agui.locateCenterOnScreen(calendar_icon, confidence=0.85)
        except Exception:
            pass
        try:
            clk_loc = agui.locateCenterOnScreen(clock_new_icon, confidence=0.85)
        except Exception:
            pass
        if clk_loc is None:
            try:
                clk_loc = agui.locateCenterOnScreen(clock, confidence=0.85)
            except Exception:
                pass

        if cal_new_loc is not None and clk_loc is not None and cal_new_loc.x < clk_loc.x:
            print("[Layout Schedule] Rilevato NUOVO layout da posizione (Calendario a sinistra di Orologio)")
            return "new", calendar_new_icon, clock_new_icon

        if cal_old_loc is not None and clk_loc is not None and clk_loc.x < cal_old_loc.x:
            print("[Layout Schedule] Rilevato VECCHIO layout (2 menu a tendina: Orologio a sinistra di Calendario)")
            return "old", calendar_icon, clock

        if cal_old_loc is not None:
            print("[Layout Schedule] Rilevato VECCHIO layout")
            return "old", calendar_icon, clock

        if cal_new_loc is not None:
            print("[Layout Schedule] Rilevato NUOVO layout")
            return "new", calendar_new_icon, clock_new_icon

    print("Impossibile rilevare il layout Schedule")
    TTS.read("Layout schedule missing")
    send_message_cele_telegram("Automazione BLOCCATA: layout schedule non riconosciuto")
    sys.exit()

def _select_new_clock_column_item(col_x, slot0_y, target_idx, total_items):
    """
    Seleziona l'elemento target_idx (0..total_items-1) in una colonna del nuovo
    orologio di TikTok (che ha 7 slot visibili da -3 a +3, distanziati di 36 px,
    con 3 slot vuoti di padding in cima e in fondo).
    Scorre prima a inizio/fine corsa per avere un riferimento certo (0 oppure total_items-1
    nello slot centrale 0) e poi clicca a passi di max 3 slot fino a centrare target_idx.
    """
    slot_step_y = 36

    if target_idx <= total_items // 2:
        # Scorri tutto in alto: l'elemento 0 ('00') si posiziona nello slot centrale 0 (slot0_y)
        agui.moveTo(col_x, slot0_y, duration=0.1)
        time.sleep(random.uniform(0.08, 0.15))
        for _ in range(18):
            agui.scroll(900)
            time.sleep(random.uniform(0.03, 0.06))
        time.sleep(random.uniform(0.2, 0.3))

        if target_idx == 0:
            agui.click(col_x, slot0_y)
            time.sleep(random.uniform(0.25, 0.35))
            return

        cur = 0
        while cur < target_idx:
            step = min(3, target_idx - cur)
            click_y = slot0_y + step * slot_step_y
            agui.moveTo(col_x, click_y, duration=random.uniform(0.08, 0.15))
            time.sleep(random.uniform(0.05, 0.1))
            agui.click()
            time.sleep(random.uniform(0.32, 0.45))
            cur += step
    else:
        # Scorri tutto in basso: l'ultimo elemento (total_items - 1) si posiziona nello slot centrale 0 (slot0_y)
        agui.moveTo(col_x, slot0_y, duration=0.1)
        time.sleep(random.uniform(0.08, 0.15))
        for _ in range(18):
            agui.scroll(-900)
            time.sleep(random.uniform(0.03, 0.06))
        time.sleep(random.uniform(0.2, 0.3))

        last_idx = total_items - 1
        if target_idx == last_idx:
            agui.click(col_x, slot0_y)
            time.sleep(random.uniform(0.25, 0.35))
            return

        cur = last_idx
        while cur > target_idx:
            step = min(3, cur - target_idx)
            click_y = slot0_y - step * slot_step_y
            agui.moveTo(col_x, click_y, duration=random.uniform(0.08, 0.15))
            time.sleep(random.uniform(0.05, 0.1))
            agui.click()
            time.sleep(random.uniform(0.32, 0.45))
            cur -= step


def set_clock(clock_img=None, layout_type="old"):
    target_clock = clock_img or clock
    image_check(target_clock)
    time.sleep(random.uniform(0.05, 0.1))
    loc = None
    try:
        loc = agui.locateCenterOnScreen(target_clock, confidence=0.8)
    except Exception:
        pass
    agui_tools.moveToImageCenter(target_clock, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.05, 0.1))
    TTS.read("clocko")
    agui.click()
    time.sleep(random.uniform(0.15, 0.25))

    try:
        loc_after = agui.locateCenterOnScreen(target_clock, confidence=0.8)
        if loc_after is not None:
            loc = loc_after
    except Exception:
        pass

    if loc is not None:
        print(f"CLOCK ({layout_type}): {loc}")
        if layout_type == "new":
            slot0_y = loc.y - 153
            hours_x = loc.x + 34
            minutes_x = loc.x + 177
            _select_new_clock_column_item(hours_x, slot0_y, 23, 24)
            _select_new_clock_column_item(minutes_x, slot0_y, 11, 12)
            # Chiudi il popup dell'orologio cliccando sul bottone dell'orologio prima dello scroll pagina
            agui.moveTo(loc.x, loc.y, duration=0.1)
            time.sleep(random.uniform(0.05, 0.1))
            agui.click()
            time.sleep(random.uniform(0.1, 0.2))
            return loc

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

def set_clock_time(hours, minutes, clock_img=None, layout_type="old"):
    target_clock = clock_img or clock
    image_check(target_clock)
    time.sleep(random.uniform(0.05, 0.1))
    loc = None
    try:
        loc = agui.locateCenterOnScreen(target_clock, confidence=0.8)
    except Exception:
        pass
    agui_tools.moveToImageCenter(target_clock, random.uniform(0.1, 0.3))
    time.sleep(random.uniform(0.05, 0.1))
    TTS.read("clocko")
    agui.click()
    time.sleep(random.uniform(0.15, 0.25))

    try:
        loc_after = agui.locateCenterOnScreen(target_clock, confidence=0.8)
        if loc_after is not None:
            loc = loc_after
    except Exception:
        pass

    if loc is not None:
        print(f"CLOCK ({layout_type}): {loc} -> Target {hours:02d}:{minutes:02d}")
        if layout_type == "new":
            slot0_y = loc.y - 153
            hours_x = loc.x + 34
            minutes_x = loc.x + 177
            _select_new_clock_column_item(hours_x, slot0_y, int(hours), 24)
            _select_new_clock_column_item(minutes_x, slot0_y, int(minutes) // 5, 12)
            # Chiudi il popup dell'orologio cliccando sul bottone dell'orologio prima dello scroll pagina
            agui.moveTo(loc.x, loc.y, duration=0.1)
            time.sleep(random.uniform(0.05, 0.1))
            agui.click()
            time.sleep(random.uniform(0.1, 0.2))
            return loc

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
    layout_type, _, active_clock_icon = detect_schedule_layout()

    loc=set_clock(clock_img=active_clock_icon, layout_type=layout_type)

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

def get_calendar_day_coords(anchor_x, anchor_y, day, month, year, cal_layout="old"):
    """
    Calcola le coordinate (x, y) sullo schermo per un dato giorno (day, month, year)
    a partire dal centro dell'immagine anchor ('images/CambioMese.PNG' oppure 'images/CambioMese_new.PNG').
    Griglia TikTok: 7 colonne (0=Domenica .. 6=Sabato), fino a 6 righe (0..5).
    """
    from datetime import datetime
    # In Python weekday(): 0=Lun .. 6=Dom -> convertiamo in: 0=Dom, 1=Lun, ..., 6=Sab
    first_weekday_sun0 = (datetime(int(year), int(month), 1).weekday() + 1) % 7
    index = first_weekday_sun0 + (int(day) - 1)
    row = index // 7
    col = index % 7

    if cal_layout == "new":
        # Nuovo layout calendario (calibrato da 'nuovo layout calendario.PNG' + 'CambioMese_new.PNG'):
        # Cella (row=0, col=6 [Sabato]) -> dx = 0, dy = +53 dal centro di CambioMese_new.PNG
        # Passo tra colonne: 37.5 px | Passo tra righe: 36 px
        col6_x = anchor_x
        row0_y = anchor_y + 53
        col_step = 37.5
        row_step = 36.0
    else:
        # Vecchio layout calendario (calibrato da 'CambioMese.PNG'):
        # Cella (row=0, col=6 [Sabato]) -> dx = -11, dy = +94 dal centro di CambioMese.PNG
        # Passo tra colonne: 49.8 px | Passo tra righe: 36 px
        col6_x = anchor_x - 11
        row0_y = anchor_y + 94
        col_step = 49.8
        row_step = 36.0

    target_x = int(round(col6_x - (6 - col) * col_step))
    target_y = int(round(row0_y + row * row_step))
    return target_x, target_y, row, col


def parse_calendar_day_info(calendar_day_info, cambioMeseDecision=False):
    """
    Estrae (day, month, year) sia da un dizionario {'day', 'month', 'year'}
    sia da una stringa legacy tipo 'images/15ottobre.PNG'.
    """
    import re
    from datetime import datetime

    now = datetime.now()
    if isinstance(calendar_day_info, dict):
        day = calendar_day_info.get('day')
        month = calendar_day_info.get('month')
        year = calendar_day_info.get('year', now.year)
        if day and month:
            return int(day), int(month), int(year)
        calendar_day_info = calendar_day_info.get('image', '')

    if isinstance(calendar_day_info, str):
        months_map = {
            "gennaio": 1, "febbraio": 2, "febbrailo": 2, "marzo": 3, "aprile": 4, "april": 4,
            "maggio": 5, "naggio": 5, "giugno": 6, "luglio": 7, "agosto": 8,
            "settembre": 9, "settenbre": 9, "ottobre": 10, "novembre": 11, "dicembre": 12
        }
        m = re.search(r'(\d+)\s*([a-zA-Z]+)', calendar_day_info.lower())
        if m:
            day = int(m.group(1))
            month_name = m.group(2).replace('bis', '')
            month = months_map.get(month_name, now.month)
            year = now.year
            if cambioMeseDecision and month == 1 and now.month == 12:
                year += 1
            return day, month, year

    return None, None, None


def wait_for_calendar_anchor(preferred_layout="old", seconds=20):
    """
    Attende l'apertura del popup del calendario cercando sia CambioMese_new.PNG
    sia CambioMese.PNG, e restituisce (cal_layout, anchor_point).
    """
    order = [("new", cambioMese_new), ("old", cambioMese)] if preferred_layout == "new" else [("old", cambioMese), ("new", cambioMese_new)]
    for i in range(seconds):
        print(f"secondi apertura calendario {i + 1}")
        time.sleep(1)
        for lay, img_path in order:
            try:
                loc = agui.locateCenterOnScreen(img_path, confidence=0.8)
                if loc is not None:
                    print(f"[Calendario] Rilevato popup calendario ({lay}) su {img_path}: {loc}")
                    return lay, loc
            except Exception:
                pass

    missing_img = cambioMese_new if preferred_layout == "new" else cambioMese
    print(missing_img + " missing")
    TTS.read(missing_img + " missing")
    TTS.read("Programma terminato")
    send_message_cele_telegram("Automazione BLOCCATA su immagine " + missing_img)
    sys.exit()


def click_calendar_day(calendar_day_info, cambioMeseDecision=False, layout_type="old"):
    """
    Seleziona automaticamente il giorno sul calendario di TikTok calcolando
    la posizione nella griglia rispetto all'ancora CambioMese_new.PNG o CambioMese.PNG.
    """
    cal_layout, anchor = wait_for_calendar_anchor(preferred_layout=layout_type)
    time.sleep(random.uniform(0.08, 0.15))

    if cambioMeseDecision:
        # Nel nuovo layout la freccia '>' è a (anchor.x + 5, anchor.y - 14); nel vecchio è al centro
        arrow_x = anchor.x + 5 if cal_layout == "new" else anchor.x
        arrow_y = anchor.y - 14 if cal_layout == "new" else anchor.y
        agui.moveTo(arrow_x, arrow_y, duration=random.uniform(0.05, 0.11))
        time.sleep(random.uniform(0.05, 0.1))
        agui.click()
        time.sleep(random.uniform(0.25, 0.4))

    day, month, year = parse_calendar_day_info(calendar_day_info, cambioMeseDecision)
    if day is not None and month is not None:
        target_x, target_y, row, col = get_calendar_day_coords(anchor.x, anchor.y, day, month, year, cal_layout=cal_layout)
        print(f"[Calendario Auto ({cal_layout})] Data {day:02d}/{month:02d}/{year} -> Griglia (riga={row}, col={col}) -> Click ({target_x}, {target_y})")
        agui.moveTo(target_x, target_y, duration=random.uniform(0.1, 0.25))
        time.sleep(random.uniform(0.05, 0.12))
        agui.click()
    else:
        # Fallback legacy nel caso non sia possibile ricavare la data
        image_path = calendar_day_info.get('image') if isinstance(calendar_day_info, dict) else calendar_day_info
        check_and_click(image_path)


def publish_day(image_day, hours, minutes, cambioMeseDecision=False):
    TTS.read("automazione Day")
    load_video()

    if skipcontrol:
        check_and_click(cancel)

    check_and_click(schedule)
    check_and_click(schedule)

    layout_type, active_calendar_icon, active_clock_icon = detect_schedule_layout()
    check_and_click(active_calendar_icon)

    click_calendar_day(image_day, cambioMeseDecision, layout_type=layout_type)

    time.sleep(random.uniform(0.1, 0.2))
    #loc = set_clock()
    loc=set_clock_time(hours, minutes, clock_img=active_clock_icon, layout_type=layout_type)

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


def schedule_posts(start_hour, start_minute, minute_step, calendar_day, max_cycles=12, change_month_par=False):
    """
    Programma le pubblicazioni a intervalli regolari

    Args:
        start_hour (int): Ora di inizio (0-23)
        start_minute (int): Minuto di inizio (0-59)
        minute_step (int): Intervallo in minuti tra le pubblicazioni
        calendar_day (dict | str): Dati del giorno {'day', 'month', 'year'} o riferimento legacy
        max_cycles (int): Numero massimo di pubblicazioni (default: 12)
    """
    from datetime import datetime, timedelta

    current_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)

    for _ in range(max_cycles):
        print(f"Pubblicazione alle: {current_time.strftime('%H:%M')}")
        publish_day(calendar_day, current_time.hour, current_time.minute, change_month_par)

        # Aggiungi l'intervallo di tempo
        current_time += timedelta(minutes=minute_step)

uploadPlus = "images/uploadBuzz.PNG"
uploadPlus = "images/plusUpload.PNG"
#videoUploadArea = "images/uploadAreaVps_old.PNG"
#videoUploadArea = "images/uploadAreaVps.PNG"
#..........................................
videoUploadArea = "images/uploadAreaVpsM.PNG"
#videoUploadArea = "images/uploadAreaVpsO.PNG"
#..........................................
iconAM = "images/am.png"
hashAstromostro = "images/astromostro_tag_vps.PNG"
uploaded = "images/uploaded_vps.PNG"
post = "images/Post_vps.PNG"
views = "images/views_vps_old.PNG"
successivo = "images/successivo_vps.PNG"
schedule = "images/schedule_vps.PNG"
clock = "images/clock_vps.PNG"
clock_new_icon = "images/clock_new_vps.PNG"
red_schedule = "images/red_schedule_vps.PNG"
calendar_icon = "images/calendar_vps.PNG"
calendar_new_icon = "images/calendar_new_vps.PNG"
timezone_new_icon = "images/timezone_new_vps.PNG"
cambioMese = "images/CambioMese.PNG"
cambioMese_new = "images/CambioMese_new.PNG"
editCover="images/editCover.PNG"
SaveThumb="images/SaveThumb.PNG"
UploadNow="images/UploadNow.PNG"
blackFrame="images/blackFrame.PNG"
blackFrame2="images/blackFrame2.PNG"
bottoncino="images/bottoncino.PNG"
day_on_calendar1 = "images/1maggio.PNG"




cancel = "images/skipcheck.PNG"
skipcontrol = False

agui_tools = AguiTools()

def run_automation(schedule_data, start_hour_val=14):
    """
    Funzione per far partire l'automazione con i dati ricevuti dalla UI.
    schedule_data: lista di dizionari con { 'day': int, 'month': int, 'year': int, 'image': path, 'change_month': bool }
    """
    from datetime import datetime
    
    send_message_cele_telegram("Automazione Python ASTROMOSTRO Inizio")
    
    months_ita = {
        1: "gennaio", 2: "febbraio", 3: "marzo", 4: "aprile",
        5: "maggio", 6: "giugno", 7: "luglio", 8: "agosto",
        9: "settembre", 10: "ottobre", 11: "novembre", 12: "dicembre"
    }
    
    now = datetime.now()
    current_month_name = months_ita[now.month]
    
    for item in schedule_data:
        day_image = item.get('image')
        day = item.get('day')
        month = item.get('month')
        year = item.get('year', now.year)
        
        # Determina se il giorno appartiene al mese corrente
        if month is not None:
            change_month = (int(month) != now.month) or (int(year) != now.year)
        elif day_image and current_month_name in day_image.lower():
            change_month = False
        else:
            change_month = True
        
        print(f"Scheduling post per: {day}/{month}/{year} [{day_image}] (Cambio mese: {change_month})")
        
        schedule_posts(
            start_hour=int(start_hour_val),
            start_minute=get_random_minutes(),
            minute_step=get_random_steps(),
            calendar_day=item,
            max_cycles=1,
            change_month_par=change_month
        )

    send_message_cele_telegram("Python Automazione ASTROMOSTRO terminata tutto ok!")
    TTS.read("Attenzione Terminato tutto")

if __name__ == "__main__":
    # Il loop principale ora è gestito dalla UI
    pass
