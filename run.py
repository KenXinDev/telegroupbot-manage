import telebot
import json
import time
import threading

TOKEN = '' # Isi token bot kamu 
BLACKLIST_FILE = 'blacklist.json'

bot = telebot.TeleBot(TOKEN)
blacklist = []

# Muat blacklist dari file
try:
    with open(BLACKLIST_FILE, 'r') as f:
        blacklist = json.load(f)
except FileNotFoundError:
    blacklist = []

def save_blacklist():
    with open(BLACKLIST_FILE, 'w') as f:
        json.dump(blacklist, f)

def is_admin(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['administrator', 'creator']
    except Exception as e:
        print(f"Admin check error: {str(e)}")
        return False

def delete_message(chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)
    except Exception as e:
        print(f"Delete message error: {str(e)}")

def send_temp_message(chat_id, text, delete_delay=3):
    try:
        msg = bot.send_message(chat_id, text, parse_mode='Markdown')
        threading.Timer(delete_delay, delete_message, args=(chat_id, msg.message_id)).start()
    except Exception as e:
        print(f"Send message error: {str(e)}")

def get_target_user(message):
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    if len(message.text.split()) > 1:
        return message.text.split()[1]
    return None

# Handler untuk command admin
def admin_command_handler(command):
    def decorator(func):
        @bot.message_handler(commands=[command])
        def wrapper(message):
            if not is_admin(message.chat.id, message.from_user.id):
                return send_temp_message(message.chat.id, "⛔ Anda bukan admin!")
                
            target = get_target_user(message)
            if not target:
                return send_temp_message(message.chat.id, "⚠️ Balas pesan pengguna atau sertakan ID!")

            try:
                func(message, target)
            except Exception as e:
                send_temp_message(message.chat.id, f"🚨 Error: {str(e)}")
            
            delete_message(message.chat.id, message.message_id)
        return wrapper
    return decorator

@admin_command_handler('ban')
def handle_ban(message, target):
    bot.ban_chat_member(message.chat.id, target)
    send_temp_message(message.chat.id, "✅ Pengguna berhasil di-ban")

@admin_command_handler('unban')
def handle_unban(message, target):
    bot.unban_chat_member(message.chat.id, target)
    send_temp_message(message.chat.id, "✅ Pengguna berhasil di-unban")

@admin_command_handler('mute')
def handle_mute(message, target):
    permissions = telebot.types.ChatPermissions(can_send_messages=False)
    bot.restrict_chat_member(message.chat.id, target, permissions)
    send_temp_message(message.chat.id, "🔇 Pengguna di-mute")

@admin_command_handler('unmute')
def handle_unmute(message, target):
    permissions = telebot.types.ChatPermissions(can_send_messages=True)
    bot.restrict_chat_member(message.chat.id, target, permissions)
    send_temp_message(message.chat.id, "🔊 Pengguna di-unmute")

@admin_command_handler('kick')
def handle_kick(message, target):
    bot.ban_chat_member(message.chat.id, target, until_date=time.time()+30)
    bot.unban_chat_member(message.chat.id, target)
    send_temp_message(message.chat.id, "👢 Pengguna dikick")

@admin_command_handler('addblacklist')
def handle_add_blacklist(message, target):
    try:
        word = message.text.split(' ', 1)[1].lower()
        if word not in blacklist:
            blacklist.append(word)
            save_blacklist()
            send_temp_message(message.chat.id, f"➕ '{word}' ditambahkan ke blacklist")
    except IndexError:
        send_temp_message(message.chat.id, "⚠️ Format: /addblacklist [kata]")

@admin_command_handler('removeblacklist')
def handle_remove_blacklist(message, target):
    try:
        word = message.text.split(' ', 1)[1].lower()
        if word in blacklist:
            blacklist.remove(word)
            save_blacklist()
            send_temp_message(message.chat.id, f"➖ '{word}' dihapus dari blacklist")
    except IndexError:
        send_temp_message(message.chat.id, "⚠️ Format: /removeblacklist [kata]")

# Handler blacklist HARUS DITARUH DIBAWAH
@bot.message_handler(func=lambda m: True)
def check_blacklist(message):
    if message.text and any(word in message.text.lower() for word in blacklist):
        delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    try:
        print("Bot sedang berjalan...")
        bot.infinity_polling()
    except Exception as e:
        print(f"Error: {str(e)}")
        time.sleep(15)
