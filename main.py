import requests
import time
import os
from win10toast import ToastNotifier
from colorama import Fore, Back, Style, init
init()
cooldown = int(input("Kaç saniyede bir yenilensin: "))
url = 'https://www.paribu.com/ticker'
header = {'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)')}
os.system('cls' if os.name == 'nt' else 'clear')
ToastNotifier().show_toast("Borsa","Borsa verileri çekiliyor...",duration=2)
while True:
        r = requests.get(url=url,headers=header)
        if r.status_code != 200:
            print("Lütfen daha sonra tekrar deneyin.")
            break
        else:
            data = r.json()
            print()
            print(Fore.CYAN + 'Dolar:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['USDT_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['USDT_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['USDT_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['USDT_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['USDT_TL']['low24hr']} TL")
            print()
            print(Fore.CYAN + 'Bitcoin:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['BTC_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['BTC_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['BTC_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['BTC_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['BTC_TL']['low24hr']} TL")
            print()
            print(Fore.CYAN + 'Etherium:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['ETH_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['ETH_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['ETH_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['ETH_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['ETH_TL']['low24hr']} TL") 
            print()
            print(Fore.CYAN + 'Ripple:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['XRP_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['XRP_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['XRP_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['XRP_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['XRP_TL']['low24hr']} TL") 
            print()
            print(Fore.CYAN + 'Litecoin:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['LTC_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['LTC_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['LTC_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['LTC_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['LTC_TL']['low24hr']} TL")
            print()
            print(Fore.CYAN + 'Bitcoin Cash:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['BCH_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['BCH_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['BCH_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['BCH_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['BCH_TL']['low24hr']} TL")
            print()
            print(Fore.CYAN + 'Dogecoin:')
            print(f"{Fore.WHITE}Güncel Değer: {Fore.GREEN}{data['DOGE_TL']['last']} TL")
            print(f"{Fore.WHITE}Değer Değişme Yüzdesi: {Fore.GREEN}{data['DOGE_TL']['percentChange']}%") 
            print(f"{Fore.WHITE}Günlük Ortalama Değer: {Fore.GREEN}{data['DOGE_TL']['avg24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Yüksek Değer: {Fore.GREEN}{data['DOGE_TL']['high24hr']} TL") 
            print(f"{Fore.WHITE}Günlük En Düşük Değer: {Fore.GREEN}{data['DOGE_TL']['low24hr']} TL") 
            print()
            time.sleep(cooldown)
            os.system('cls' if os.name == 'nt' else 'clear')
            ToastNotifier().show_toast("Borsa","Borsa verileri güncellendi.",duration=2)
