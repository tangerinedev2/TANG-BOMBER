# 💣 TANG BOMBER

<p align="center">
  <img src="https://img.shields.io/badge/Version-13.0-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-lightgrey?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-Educational-yellow?style=for-the-badge">
</p>

<p align="center">
  <b>🚀 %99 Anonim • Tor • Elite Proxy • 52 API</b>
</p>

---

## ⚠️ YASAL UYARI

> **Bu araç SADECE eğitim ve test amaçlıdır.**
>
> - İzinsiz SMS göndermek **Türkiye'de suçtur** (5651 Sayılı Kanun)
> - Kullanıcı, tüm yasal sorumluluğu kabul eder
> - Geliştirici, kötüye kullanımdan sorumlu değildir
> - **Sadece kendi numaranızda test edin**

---

## 📌 ÖZELLİKLER

| Özellik | Açıklama |
|---------|----------|
| 💣 **SMS Bomber** | 52 API ile toplu SMS gönderimi |
| 📧 **Email Bomb** | 12 servis ile email spam |
| 🛡️ **Anonimlik** | Webshare proxy + Tor desteği |
| ⚡ **Hız** | 30 thread ile saniyede 3-5 SMS |
| 📊 **Log Sistemi** | Detaylı log kaydı |
| 🇹🇷 **Türk API'ler** | Trendyol, Migros, Bim, Sakasu... |
| 🇨🇳 **Çin API'ler** | Caiyun, Pgyer, 12321... |

---

## 📦 KURULUM

### 1. Repoyu Klonla

```bash
git clone https://github.com/SuluMandalina/TANG-BOMBER.git
cd TANG-BOMBER
```

### 2. Gerekli Kütüphaneleri Kur

```bash
pip install -r requirements.txt
```

### 3. Çalıştır

```bash
python tang_bomber.py
```

---

## 📱 TERMUX (ANDROID)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt
python tang_bomber.py
```

---

## 📱 iSH (iOS)

```sh
apk update && apk upgrade
apk add python3 py3-pip git
git clone https://github.com/SuluMandalina/TANG-BOMBER.git
cd TANG-BOMBER
pip3 install requests colorama fake-useragent pysocks stem emoji
python3 tang_bomber.py
```

---

## 🚀 KULLANIM

```bash
python tang_bomber.py
```

### Menü

```
[01] SMS Bomb Başlat (ULTRA Mode)
[02] Email Bomb Başlat
[03] Ayarlar
[04] API Listesini Göster
[05] Tor Kimlik Değiştir
[06] Proxy Havuzunu Yenile
[07] Log Dosyasını Göster
[99] Çıkış
```

---

## 📂 DOSYA YAPISI

```
TANG_BOMBER/
├── tang_bomber.py          # Ana program
├── requirements.txt        # Python kütüphaneleri
├── README.md              # Bu dosya
├── modules/
│   ├── sms_bomber.py      # SMS motoru
│   ├── proxy_manager.py   # Proxy + Tor
│   ├── email_bomber.py    # Email bomb
│   └── thread_manager.py  # Thread yönetimi
└── data/
    ├── apis.json          # API listesi
    └── proxies.txt        # Proxy listesi
```

---

## 🔧 AYARLAR

`tang_bomber.py` içinde değiştirebilirsin:

```python
USE_PROXY = True       # Proxy aç/kapat
USE_TOR = False        # Tor aç/kapat
USE_FAKE_LOGS = True   # Fake log aç/kapat
MAX_THREADS = 30       # Thread sayısı
HEDEF_SMS = 2000       # Varsayılan hedef
```

---

## 📊 ÇALIŞAN API'LER

### 🇹🇷 Türkiye API'leri

| API | Durum |
|-----|-------|
| kahvedunyasi | ✅ |
| suiste | ✅ |
| hayatsu | ✅ |
| porty | ✅ |
| yapp | ✅ |
| englishhome | ✅ |
| filemarket | ✅ |
| wmf | ✅ |
| bim | ✅ |

### 🇨🇳 Çin API'leri

| API | Durum |
|-----|-------|
| caiyun | ⚠️ |
| pgyer | ⚠️ |
| 12321 | ⚠️ |
| guokr | ⚠️ |
| ztestin | ⚠️ |

---

## 🛡️ GÜVENLİK

- ✅ **Webshare Proxy** ile anonim
- ✅ **Tor** desteği
- ✅ **Fake Log** sistemi
- ✅ **Rate Limit** koruması

## 📈 PERFORMANS

| Metrik | Değer |
|--------|-------|
| Ortalama Hız | 3-5 SMS/saniye |
| Başarı Oranı | %60-70 |
| 500 SMS Süresi | ~1.8 dakika |
| 2000 SMS Süresi | ~7-10 dakika |

---

## 📋 GEREKLİ KÜTÜPHANELER

```txt
requests
colorama
fake-useragent
pysocks
stem
emoji
```

---

## 🐛 SORUN GİDERME

| Hata | Çözüm |
|------|-------|
| `PermissionError: data` | Yönetici olarak çalıştır veya klasör izni ver |
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `Proxy çalışmıyor` | Menüden 6 → Proxy yenile |
| `API çalışmıyor` | API güncellenmiş olabilir, yeni API ekle |

---

## ⭐ YILDIZ VER

Projeyi beğendiysen yıldız vermeyi unutma! ⭐

---

<p align="center">
  <b>👻 TANG BOMBER v13.0 - DRAGON EDITION</b><br>
  <i>Ne mutlu Türk'üm diyene! 🇹🇷</i>
</p>
