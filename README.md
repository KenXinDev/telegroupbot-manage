# 📢 TelegroupBot Manage

Bot Telegram untuk mengelola grup secara otomatis — mendukung fitur **ban**, **mute**, **kick**, dan **filter kata terlarang (blacklist)** secara real-time. Bot ini sangat cocok untuk admin grup yang ingin menjaga keamanan dan kenyamanan komunitasnya dengan mudah.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![TeleBot](https://img.shields.io/badge/telebot-v0.0.4-blue)

## ✨ Fitur

- 🔨 Command admin (`/ban`, `/unban`, `/mute`, `/unmute`, `/kick`)
- 🚫 Filter otomatis berdasarkan kata terlarang
- 📂 Simpan blacklist ke file JSON
- ⏱️ Auto-delete pesan bot setelah beberapa detik
- 🔒 Hanya admin yang bisa menggunakan perintah
- 🧠 Smart command (bisa reply pesan atau pakai ID)

## ⚙️ Instalasi

1. **Clone repositori ini**
   ```bash
   git clone https://github.com/KenXinDev/telegroupbot-manage.git
   cd telegroupbot-manage
   ````

2. **Pasang dependensi**

   ```bash
   pip install pyTelegramBotAPI
   ```

3. **Edit token bot**
   Buka file `run.py` dan isi `TOKEN` dengan token dari BotFather:

   ```python
   TOKEN = 'ISI_TOKEN_BOT_KAMU'
   ```

4. **Jalankan bot**

   ```bash
   python run.py
   ```

---

## 📘 Penggunaan

Perintah hanya bisa dijalankan oleh admin grup:

| Perintah                | Deskripsi                                    |
| ----------------------- | -------------------------------------------- |
| `/ban`                  | Memblokir pengguna dari grup                 |
| `/unban`                | Mengizinkan pengguna yang diblokir kembali   |
| `/mute`                 | Membungkam pengguna (tidak bisa kirim pesan) |
| `/unmute`               | Mengembalikan hak kirim pesan pengguna       |
| `/kick`                 | Mengeluarkan pengguna dari grup (sementara)  |
| `/addblacklist kata`    | Menambahkan kata ke daftar blacklist         |
| `/removeblacklist kata` | Menghapus kata dari blacklist                |

> 💡 Gunakan *reply pesan* atau sertakan ID pengguna untuk semua perintah yang melibatkan pengguna.

---

## 🧠 Contoh

* Ban user dengan reply:

  ```
  /ban
  ```

* Tambahkan blacklist:

  ```
  /addblacklist kata_terlarang
  ```

---

## 📁 Struktur Proyek

```
.
├── blacklist.json       # File blacklist (otomatis dibuat)
├── run.py              # Kode utama bot
└── README.md            # Dokumentasi ini
```

---

## 🛡️ Lisensi

Kode ini dirilis di bawah lisensi MIT. Silakan digunakan dan dikembangkan dengan bebas.

---

## 👤 Kontribusi

Pull request dan issue sangat dipersilakan!

* ✨ Fork proyek ini
* 💡 Buat branch dengan fitur baru
* ✅ Commit perubahan
* 📩 Ajukan pull request

---

## 🌐 Kredit

Dikembangkan oleh [KenXinDev](https://github.com/KenXinDev)
Dengan ❤️ menggunakan [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

> 🚀 Buat komunitas Telegram kamu makin aman & tertib dengan *TelegroupBot Manage*!
