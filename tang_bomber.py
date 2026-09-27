# tang_bomber.py - V13.0 DRAGON EDITION

import os
import sys
import time
import json
import random
import traceback
from datetime import datetime
import emoji

# Windows terminal Unicode desteği
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')

from colorama import init, Fore, Style, just_fix_windows_console

just_fix_windows_console()
init(autoreset=True, convert=True)

# Modül importları
try:
    from modules.sms_bomber import SendSms
    from modules.proxy_manager import ProxyManager
    from modules.email_bomber import SendEmail
except Exception as e:
    print(Fore.RED + f"[!] Modül hatası: {e}")
    traceback.print_exc()
    input("Enter'a bas...")
    sys.exit(1)

# Emoji yardımcısı
def em(text):
    return emoji.emojize(text, language='alias')

# ----- SABİTLER -----
VERSION = "13.0"
EDITION = "DRAGON EDITION"
AUTHOR = "Sulu Mandalina"
RELEASE_DATE = "06.09.2026"

# ----- RENKLER -----
C = Fore.CYAN
G = Fore.LIGHTGREEN_EX
R = Fore.LIGHTRED_EX
Y = Fore.LIGHTYELLOW_EX
M = Fore.LIGHTMAGENTA_EX
W = Fore.WHITE
S = Style.RESET_ALL

# ----- GLOBAL -----
USE_PROXY = True
USE_TOR = False
USE_FAKE_LOGS = True
MAX_THREADS = 30
HEDEF_SMS = 50000

# ----- LOG SİSTEMİ -----
LOG_FILE = "data/tang_bomber.log"

def log_yaz(mesaj, seviye="INFO"):
    """Detaylı log yaz"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{seviye}] {mesaj}"
    try:
        os.makedirs('data', exist_ok=True)
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry + "\n")
    except:
        pass
    return log_entry

# ----- FONKSİYONLAR -----

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.RED + """
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║    ████████╗ █████╗ ███╗   ██╗ ██████╗                              ║
    ║    ╚══██╔══╝██╔══██╗████╗  ██║██╔════╝                              ║
    ║       ██║   ███████║██╔██╗ ██║██║     ██████╗  ██████╗              ║
    ║       ██║   ██╔══██║██║╚██╗██║██║     ╚════██╗██╔═══██╗             ║
    ║       ██║   ██║  ██║██║ ╚████║╚██████╗██████╔╝╚██████╔╝             ║
    ║       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═════╝  ╚═════╝              ║
    ║                                                                      ║
    ║    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗              ║
    ║    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗             ║
    ║    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝             ║
    ║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗             ║
    ║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║             ║
    ║    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝             ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
    """ + Fore.RESET)

    print(Fore.CYAN + f"""
╔══════════════════════════════════════════════════════════════════════╗
║ {em(':bomb:')} TANG BOMBER v{VERSION} - {EDITION}                    ║
║ {em(':ghost:')} %99 Anonim • Tor • Elite Proxy • Fake Log              ║
║ {em(':flag-cn:')} 52 API (Çin Dahil) • Async • 30 Thread              ║
║ {em(':clipboard:')} Detaylı Log • Hızlı Test • Gelişmiş Menü             ║
║ Geliştirici: {AUTHOR}                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """ + Fore.RESET)

def menu():
    print(Fore.YELLOW + f"""
┌──────────────────────────────────────────────────────────────────────┐
│  {em(':iphone:')} [01] SMS Bomb Başlat (ULTRA Mode)                         │
│  {em(':e-mail:')} [02] Email Bomb Başlat                                    │
│  {em(':gear:')} [03] Ayarlar                                              │
│  {em(':bar_chart:')} [04] API Listesini Göster                                  │
│  {em(':arrows_counterclockwise:')} [05] Tor Kimlik Değiştir                                   │
│  {em(':arrows_counterclockwise:')} [06] Proxy Havuzunu Yenile                                 │
│  {em(':clipboard:')} [07] Log Dosyasını Göster                                    │
│  {em(':x:')} [99] Çıkış                                                 │
└──────────────────────────────────────────────────────────────────────┘
    """ + Fore.RESET)

def load_apis():
    try:
        with open('data/apis.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def sms_bomb():
    global USE_PROXY, USE_TOR, USE_FAKE_LOGS, MAX_THREADS, HEDEF_SMS
    try:
        temizle()
        banner()
        
        log_yaz("=== SMS BOMB BAŞLATILDI ===", "INFO")
        
        print(Fore.CYAN + f"\n┌──(TANG BOMBER DRAGON)──[{em(':iphone:')} SMS Bomb]")
        phone = input(Fore.WHITE + "└──$ 📱 Telefon (5xxxxxxxxx): " + Fore.RESET)
        
        if not phone or len(phone) != 10:
            print(Fore.RED + em(':x:') + " Geçersiz telefon!")
            log_yaz(f"Geçersiz telefon: {phone}", "ERROR")
            time.sleep(2)
            return
        
        try:
            target = int(input(Fore.WHITE + f"└──$ {em(':1234:')} Kaç SMS? (1-500): " + Fore.RESET) or HEDEF_SMS)
            target = max(1, min(50000, target))
        except:
            target = HEDEF_SMS
        
        log_yaz(f"Hedef: {phone} | SMS: {target} | Thread: {MAX_THREADS} | Proxy: {USE_PROXY}", "INFO")
        
        print(Fore.YELLOW + f"\n{em(':rocket:')} SMS Bomb başlatılıyor... Hedef: {phone}")
        print(Fore.CYAN + f"{em(':dart:')} Hedef SMS: {target}")
        print(Fore.CYAN + f"{em(':thread:')} Thread: {MAX_THREADS}")
        print(Fore.CYAN + f"{em(':globe_with_meridians:')} Tor: {'Açık' if USE_TOR else 'Kapalı'}")
        print(Fore.CYAN + f"{em(':globe_with_meridians:')} Proxy: {'Açık' if USE_PROXY else 'Kapalı'}")
        print(Fore.CYAN + f"{em(':pencil:')} Fake Log: {'Açık' if USE_FAKE_LOGS else 'Kapalı'}\n")
        
        # PROXY YÖNETİCİSİ
        print(Fore.CYAN + "[*] Anonim sistem başlatılıyor..." + Fore.RESET)
        log_yaz("ProxyManager başlatılıyor...", "INFO")
        pm = ProxyManager(use_proxy=USE_PROXY, use_tor=USE_TOR, use_fake_logs=USE_FAKE_LOGS)
        
        print(Fore.CYAN + "[*] SMS motoru başlatılıyor..." + Fore.RESET)
        log_yaz("SMS motoru başlatılıyor...", "INFO")
        sms = SendSms(phone, pm, USE_PROXY, MAX_THREADS)
        
        print(Fore.GREEN + "[*] Bombalama başlıyor..." + Fore.RESET)
        log_yaz("Bombalama başladı!", "INFO")
        start_time = time.time()
        success, fail, api_stats = sms.run(target)
        elapsed = time.time() - start_time
        
        # İstatistikleri göster
        if pm:
            stats = pm.get_stats()
            print(Fore.CYAN + f"\n{em(':bar_chart:')} Anonimlik İstatistikleri:")
            print(Fore.WHITE + f"   Proxy Havuzu: {stats['toplam']}")
            print(Fore.GREEN + f"   Elite Proxy: {stats['calisan']}")
            print(Fore.CYAN + f"   Hızlı Proxy: {stats.get('hizli', 0)}")
            print(Fore.RED + f"   Ölü Proxy: {stats['olu']}")
            print(Fore.YELLOW + f"   Başarı Oranı: {stats['oran']}")
            print(Fore.MAGENTA + f"   Tor Aktif: {'✅' if stats['tor_aktif'] else '❌'}")
            print(Fore.MAGENTA + f"   Fake Log: {stats['fake_logs']} adet")
            
            if USE_FAKE_LOGS:
                print(Fore.CYAN + f"\n{em(':pencil:')} Fake Log Örneği: {pm.get_fake_log()}")
        
        # API Bazlı İstatistikler
        if api_stats:
            print(Fore.CYAN + f"\n{em(':bar_chart:')} API Bazlı Başarı İstatistikleri:")
            for api_name, api_data in sorted(api_stats.items(), key=lambda x: x[1]['success'], reverse=True)[:10]:
                total = api_data['success'] + api_data['fail']
                rate = (api_data['success'] / total * 100) if total > 0 else 0
                status = Fore.GREEN if rate > 50 else Fore.RED
                print(f"   {api_name}: {status}{api_data['success']}/{total} ({rate:.1f}%){Style.RESET_ALL}")
        
        log_yaz(f"BOMBALAMA TAMAMLANDI: {success} başarılı, {fail} başarısız, {elapsed:.1f} sn", "INFO")
        
        print(Fore.GREEN + f"\n{em(':white_check_mark:')} {success} SMS başarıyla gönderildi! ({elapsed:.1f} sn)")
        print(Fore.RED + f"{em(':x:')} {fail} SMS başarısız!")
        print(Fore.YELLOW + f"{em(':chart_increasing:')} Başarı Oranı: {success/(success+fail+1)*100:.1f}%")
        
    except Exception as e:
        log_yaz(f"HATA: {e}", "ERROR")
        print(Fore.RED + f"\n{em(':x:')} HATA: {e}")
        traceback.print_exc()
    
    input(Fore.YELLOW + "\nDevam etmek için Enter'a bas..." + Fore.RESET)

def email_bomb():
    """Email Bomb başlat"""
    global USE_PROXY, USE_TOR, USE_FAKE_LOGS, MAX_THREADS
    try:
        temizle()
        banner()
        
        log_yaz("=== EMAIL BOMB BAŞLATILDI ===", "INFO")
        
        print(Fore.CYAN + f"\n┌──(TANG BOMBER DRAGON)──[{em(':e-mail:')} Email Bomb]")
        email = input(Fore.WHITE + "└──$ 📧 Email: " + Fore.RESET)
        
        if not email or '@' not in email:
            print(Fore.RED + em(':x:') + " Geçersiz email!")
            log_yaz(f"Geçersiz email: {email}", "ERROR")
            time.sleep(2)
            return
        
        try:
            target = int(input(Fore.WHITE + f"└──$ {em(':1234:')} Kaç email bomb? (1-50): " + Fore.RESET) or 10)
            target = max(1, min(50, target))
        except:
            target = 10
        
        log_yaz(f"Hedef: {email} | Email: {target} | Proxy: {USE_PROXY}", "INFO")
        
        print(Fore.YELLOW + f"\n{em(':rocket:')} Email Bomb başlatılıyor... Hedef: {email}")
        print(Fore.CYAN + f"{em(':dart:')} Hedef: {target} email")
        print(Fore.CYAN + f"{em(':globe_with_meridians:')} Proxy: {'Açık' if USE_PROXY else 'Kapalı'}")
        print(Fore.CYAN + f"{em(':lock:')} Tor: {'Açık' if USE_TOR else 'Kapalı'}\n")
        
        # Proxy Manager
        pm = ProxyManager(use_proxy=USE_PROXY, use_tor=USE_TOR, use_fake_logs=USE_FAKE_LOGS)
        
        # Email Bomber
        email_bomber = SendEmail(email, pm, USE_PROXY)
        
        print(Fore.GREEN + "[*] Email bomb başlıyor..." + Fore.RESET)
        log_yaz("Email bomb başladı!", "INFO")
        start_time = time.time()
        success, fail = email_bomber.run(target)
        elapsed = time.time() - start_time
        
        log_yaz(f"EMAIL BOMB TAMAMLANDI: {success} başarılı, {fail} başarısız", "INFO")
        
        print(Fore.GREEN + f"\n{em(':white_check_mark:')} {success} email başarıyla gönderildi! ({elapsed:.1f} sn)")
        print(Fore.RED + f"{em(':x:')} {fail} email başarısız!")
        print(Fore.YELLOW + f"{em(':chart_increasing:')} Başarı Oranı: {success/(success+1)*100:.1f}%")
        
    except Exception as e:
        log_yaz(f"HATA: {e}", "ERROR")
        print(Fore.RED + f"\n{em(':x:')} HATA: {e}")
        traceback.print_exc()
    
    input(Fore.YELLOW + "\nDevam etmek için Enter'a bas..." + Fore.RESET)

def ayarlar():
    global USE_PROXY, USE_TOR, USE_FAKE_LOGS, MAX_THREADS, HEDEF_SMS
    temizle()
    banner()
    
    print(Fore.CYAN + f"\n┌──(TANG BOMBER DRAGON)──[{em(':gear:')} Ayarlar]")
    print(Fore.WHITE + f"""
╔══════════════════════════════════════════════════════════════════════╗
║  [1] Tor Kullanımı: {'✅ AÇIK' if USE_TOR else '❌ KAPALI'}                     ║
║  [2] Proxy Kullanımı: {'✅ AÇIK' if USE_PROXY else '❌ KAPALI'}                 ║
║  [3] Fake Log: {'✅ AÇIK' if USE_FAKE_LOGS else '❌ KAPALI'}                   ║
║  [4] Thread Sayısı: {MAX_THREADS}                                         ║
║  [5] Hedef SMS Sayısı: {HEDEF_SMS}                                         ║
║  [6] Geri Dön                                                   ║
╚══════════════════════════════════════════════════════════════════════╝
""")
    secim = input(Fore.WHITE + "└──$ Seçiminiz: " + Fore.RESET)
    
    if secim == "1":
        USE_TOR = not USE_TOR
        log_yaz(f"Tor: {'Açık' if USE_TOR else 'Kapalı'}", "INFO")
        print(Fore.GREEN + f"✅ Tor: {'Açık' if USE_TOR else 'Kapalı'}")
        time.sleep(1)
    elif secim == "2":
        USE_PROXY = not USE_PROXY
        log_yaz(f"Proxy: {'Açık' if USE_PROXY else 'Kapalı'}", "INFO")
        print(Fore.GREEN + f"✅ Proxy: {'Açık' if USE_PROXY else 'Kapalı'}")
        time.sleep(1)
    elif secim == "3":
        USE_FAKE_LOGS = not USE_FAKE_LOGS
        log_yaz(f"Fake Log: {'Açık' if USE_FAKE_LOGS else 'Kapalı'}", "INFO")
        print(Fore.GREEN + f"✅ Fake Log: {'Açık' if USE_FAKE_LOGS else 'Kapalı'}")
        time.sleep(1)
    elif secim == "4":
        try:
            MAX_THREADS = int(input(Fore.WHITE + "Yeni Thread Sayısı (1-50): " + Fore.RESET))
            MAX_THREADS = max(1, min(50, MAX_THREADS))
            log_yaz(f"Thread sayısı: {MAX_THREADS}", "INFO")
        except:
            pass
    elif secim == "5":
        try:
            HEDEF_SMS = int(input(Fore.WHITE + "Yeni Hedef SMS Sayısı (1-500): " + Fore.RESET))
            HEDEF_SMS = max(1, min(500, HEDEF_SMS))
            log_yaz(f"Hedef SMS: {HEDEF_SMS}", "INFO")
        except:
            pass

def tor_identity():
    """Tor kimliğini değiştir"""
    global USE_TOR
    if not USE_TOR:
        print(Fore.RED + em(':x:') + " Tor kapalı! Önce Tor'u aç.")
        time.sleep(2)
        return
    
    print(Fore.YELLOW + "\n[!] Tor kimliği değiştiriliyor...")
    log_yaz("Tor kimlik değiştirme başlatıldı", "INFO")
    pm = ProxyManager(use_proxy=False, use_tor=True, use_fake_logs=False)
    if pm.rotate_tor_identity():
        log_yaz("Tor kimlik değiştirildi", "INFO")
        print(Fore.GREEN + em(':white_check_mark:') + " Yeni IP aktif!")
    else:
        log_yaz("Tor kimlik değiştirme başarısız", "ERROR")
        print(Fore.RED + em(':x:') + " Kimlik değiştirilemedi!")
    time.sleep(2)

def proxy_yenile():
    """Proxy havuzunu yenile"""
    global USE_PROXY
    if not USE_PROXY:
        print(Fore.RED + em(':x:') + " Proxy kapalı! Önce Proxy'yi aç.")
        time.sleep(2)
        return
    
    print(Fore.YELLOW + "\n[!] Proxy havuzu yenileniyor...")
    log_yaz("Proxy havuzu yenileniyor", "INFO")
    pm = ProxyManager(use_proxy=True, use_tor=USE_TOR, use_fake_logs=False)
    log_yaz(f"Proxy havuzu yenilendi: {pm.count()} proxy", "INFO")
    print(Fore.GREEN + f"{em(':white_check_mark:')} {pm.count()} proxy hazır!")
    time.sleep(2)

def log_goster():
    """Log dosyasını göster"""
    temizle()
    banner()
    print(Fore.CYAN + f"\n┌──(TANG BOMBER DRAGON)──[{em(':clipboard:')} Log Dosyası]")
    
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Son 30 satırı göster
                for line in lines[-30:]:
                    print(Fore.WHITE + line.strip())
                print(Fore.YELLOW + f"\n... ve {len(lines)} satır log var (son 30 gösteriliyor)")
        else:
            print(Fore.RED + "Log dosyası bulunamadı!")
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")
    
    input(Fore.YELLOW + "\nDevam etmek için Enter'a bas...")

def apileri_goster():
    temizle()
    banner()
    apis = load_apis()
    print(Fore.CYAN + f"\n┌──(TANG BOMBER DRAGON)──[{em(':bar_chart:')} API Listesi - {len(apis)} API]")
    
    # Türk ve Çin API'lerini ayır
    turk_apis = []
    cin_apis = []
    for api in apis:
        name = api.get('name', 'Unknown')
        # Çin API'lerini tespit et (Çince karakter veya belirli isimler)
        if any('\u4e00' <= c <= '\u9fff' for c in name) or name in ['caiyun', 'pgyer', '12321', '0101ssd', 'guokr', 'ztestin', 'dehua', 'daojia', 'huajue', 'feeclouds', 'csdhe', 'gpa_gd']:
            cin_apis.append(api)
        else:
            turk_apis.append(api)
    
    print(Fore.GREEN + f"\n🇹🇷 Türkiye API'leri ({len(turk_apis)}):")
    for i, api in enumerate(turk_apis, 1):
        print(Fore.WHITE + f"  {i}. {api.get('name', 'Unknown')} ({api.get('method', 'POST')})")
    
    print(Fore.RED + f"\n🇨🇳 Çin API'leri ({len(cin_apis)}):")
    for i, api in enumerate(cin_apis, 1):
        print(Fore.WHITE + f"  {i}. {api.get('name', 'Unknown')} ({api.get('method', 'POST')})")
    
    input(Fore.YELLOW + "\nDevam etmek için Enter'a bas...")

def main():
    try:
        os.makedirs('data', exist_ok=True)
        log_yaz("=== TANG BOMBER BAŞLATILDI ===", "INFO")
        log_yaz(f"Sürüm: v{VERSION} {EDITION}", "INFO")
        
        while True:
            temizle()
            banner()
            menu()
            secim = input(Fore.WHITE + "└──$ Seçiminiz: " + Fore.RESET)
            
            if secim in ["01", "1"]:
                sms_bomb()
            elif secim in ["02", "2"]:
                email_bomb()
            elif secim in ["03", "3"]:
                ayarlar()
            elif secim in ["04", "4"]:
                apileri_goster()
            elif secim in ["05", "5"]:
                tor_identity()
            elif secim in ["06", "6"]:
                proxy_yenile()
            elif secim in ["07", "7"]:
                log_goster()
            elif secim == "99":
                log_yaz("=== TANG BOMBER KAPATILDI ===", "INFO")
                print(Fore.RED + f"\n{em(':wave:')} Çıkış yapılıyor...")
                break
            else:
                print(Fore.RED + em(':x:') + " Geçersiz seçim!")
                time.sleep(1)
    except KeyboardInterrupt:
        log_yaz("Program CTRL+C ile durduruldu", "WARNING")
        print(Fore.YELLOW + f"\n{em(':warning:')} Program durduruldu.")
    except Exception as e:
        log_yaz(f"KRİTİK HATA: {e}", "ERROR")
        print(Fore.RED + f"\n{em(':x:')} KRİTİK HATA: {e}")
        traceback.print_exc()
        input("Enter'a bas...")

if __name__ == "__main__":
    main()