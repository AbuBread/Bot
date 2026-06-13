🍞AbuBread🍞
abu_bread
В сети

Milk — 14:01
Ну что
🍞AbuBread🍞 [RUNE],  — 14:01
пиздец
там просят карту
а у меня ее нет
Milk — 14:02
Всм
В гит хабе добавить?
🍞AbuBread🍞 [RUNE],  — 14:02
в рендере
Milk — 14:02
В гит хабе добавь это:
Название:
render.yaml
Внутри:
services:
  
type: worker
  name: discord-bot
  runtime: python
  buildCommand: pip install -r requirements.txt
  startCommand: python bot.py
🍞AbuBread🍞 [RUNE],  — 14:03
добавил
Milk — 14:05
Ок
Назови код с ботом
bot.py
Щас код отправлю
Обновленный
import discord
from discord import app_commands
import google.generativeai as genai
import json
import os
import random

bot-2.py
14 кб
Лови
И дисциплину делай
Хахаха
Скажи когда сделаешь
Название тоже поменяй
🍞AbuBread🍞 [RUNE],  — 14:10
сделал
название на бот 2.пи поменять?
Milk — 14:49
Обновил код
Щас отправлю
import discord
from discord import app_commands
import google.generativeai as genai
import json
import os
import random
from datetime import datetime, timedelta
import asyncio
import pytz
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model_flash = genai.GenerativeModel("gemini-1.5-flash")
model_think = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

BALANCE_FILE = "balance.json"
CASINO_CHANNELS = ["казик", "казино", "лучшие-по-казику", "чемпионат-по-казику"]

СТРАНЫ = [
    ("Россия", ["Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург", "Краснодар"]),
    ("Украина", ["Киев", "Харьков", "Одесса", "Днепр"]),
    ("Беларусь", ["Минск", "Гомель", "Брест"]),
    ("Казахстан", ["Алматы", "Астана", "Шымкент"]),
    ("Узбекистан", ["Ташкент", "Самарканд"]),
    ("Азербайджан", ["Баку", "Гянджа"]),
    ("Армения", ["Ереван", "Гюмри"]),
    ("Грузия", ["Тбилиси", "Батуми"]),
    ("Молдова", ["Кишинёв"]),
    ("Кыргызстан", ["Бишкек"]),
    ("Таджикистан", ["Душанбе"]),
    ("Туркменистан", ["Ашхабад"]),
    ("Израиль", ["Тель-Авив", "Иерусалим", "Хайфа"]),
    ("Палестина", ["Газа", "Рамалла"]),
    ("Афганистан", ["Кабул", "Кандагар"]),
    ("КНДР", ["Пхеньян", "Вонсан"]),
    ("Иран", ["Тегеран", "Исфахан"]),
    ("США", ["Нью-Йорк", "Лос-Анджелес", "Чикаго", "Хьюстон"]),
    ("Сирия", ["Дамаск", "Алеппо"]),
    ("Ирак", ["Багдад", "Басра"]),
    ("Остров Эпштейна", ["Остров Эпштейна"]),
]

УЛИЦЫ = ["ул. Ленина", "пр. Мира", "ул. Пушкина", "ул. Гагарина", "пр. Победы",
          "ул. Советская", "ул. Садовая", "пр. Независимости", "ул. Центральная"]

BAN_ROLES = ["Модератор", "Главный Модератор", "Создатель Сервера"]
SEND_ROLES = ["Главный Модератор", "Владелец Сервера"]

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_balance(data):
    with open(BALANCE_FILE, "w") as f:
        json.dump(data, f)

def get_balance(user_id):
    data = load_balance()
    return data.get(str(user_id), 100)

def set_balance(user_id, amount):
    data = load_balance()
    data[str(user_id)] = amount
    save_balance(data)

async def daily_bonus():
    await client.wait_until_ready()
    msk = pytz.timezone("Europe/Moscow")
    while True:
        now = datetime.now(msk)
        seconds_until_midnight = ((24 - now.hour - 1) * 3600 +
                                   (60 - now.minute - 1) * 60 +
                                   (60 - now.second))
        await asyncio.sleep(seconds_until_midnight)
        data = load_balance()
        for user_id in data:
            data[user_id] += 100
        save_balance(data)
        await asyncio.sleep(60)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")
    def log_message(self, format, *args):
        pass

def run_web():
... (осталось: 179 строк)

bot-3.py
15 кб
Скажи когда сделаешь
Ну что
Сделал?
@🍞AbuBread🍞
If a global survey were held today, which country do you think would be considered the most influential ?
﻿
Историк би лайк
Milk
mmmalik0898_83466
 
import discord
from discord import app_commands
import google.generativeai as genai
import json
import os
import random
from datetime import datetime, timedelta
import asyncio
import pytz
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model_flash = genai.GenerativeModel("gemini-1.5-flash")
model_think = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

BALANCE_FILE = "balance.json"
CASINO_CHANNELS = ["казик", "казино", "лучшие-по-казику", "чемпионат-по-казику"]

СТРАНЫ = [
    ("Россия", ["Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург", "Краснодар"]),
    ("Украина", ["Киев", "Харьков", "Одесса", "Днепр"]),
    ("Беларусь", ["Минск", "Гомель", "Брест"]),
    ("Казахстан", ["Алматы", "Астана", "Шымкент"]),
    ("Узбекистан", ["Ташкент", "Самарканд"]),
    ("Азербайджан", ["Баку", "Гянджа"]),
    ("Армения", ["Ереван", "Гюмри"]),
    ("Грузия", ["Тбилиси", "Батуми"]),
    ("Молдова", ["Кишинёв"]),
    ("Кыргызстан", ["Бишкек"]),
    ("Таджикистан", ["Душанбе"]),
    ("Туркменистан", ["Ашхабад"]),
    ("Израиль", ["Тель-Авив", "Иерусалим", "Хайфа"]),
    ("Палестина", ["Газа", "Рамалла"]),
    ("Афганистан", ["Кабул", "Кандагар"]),
    ("КНДР", ["Пхеньян", "Вонсан"]),
    ("Иран", ["Тегеран", "Исфахан"]),
    ("США", ["Нью-Йорк", "Лос-Анджелес", "Чикаго", "Хьюстон"]),
    ("Сирия", ["Дамаск", "Алеппо"]),
    ("Ирак", ["Багдад", "Басра"]),
    ("Остров Эпштейна", ["Остров Эпштейна"]),
]

УЛИЦЫ = ["ул. Ленина", "пр. Мира", "ул. Пушкина", "ул. Гагарина", "пр. Победы",
          "ул. Советская", "ул. Садовая", "пр. Независимости", "ул. Центральная"]

BAN_ROLES = ["Модератор", "Главный Модератор", "Создатель Сервера"]
SEND_ROLES = ["Главный Модератор", "Владелец Сервера"]

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_balance(data):
    with open(BALANCE_FILE, "w") as f:
        json.dump(data, f)

def get_balance(user_id):
    data = load_balance()
    return data.get(str(user_id), 100)

def set_balance(user_id, amount):
    data = load_balance()
    data[str(user_id)] = amount
    save_balance(data)

async def daily_bonus():
    await client.wait_until_ready()
    msk = pytz.timezone("Europe/Moscow")
    while True:
        now = datetime.now(msk)
        seconds_until_midnight = ((24 - now.hour - 1) * 3600 +
                                   (60 - now.minute - 1) * 60 +
                                   (60 - now.second))
        await asyncio.sleep(seconds_until_midnight)
        data = load_balance()
        for user_id in data:
            data[user_id] += 100
        save_balance(data)
        await asyncio.sleep(60)

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")
    def log_message(self, format, *args):
        pass

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

@client.event
async def on_ready():
    await tree.sync()
    print(f"Бот запущен: {client.user}")
    client.loop.create_task(daily_bonus())

@tree.command(name="баланс", description="Посмотреть свой баланс")
async def баланс(interaction: discord.Interaction):
    bal = get_balance(interaction.user.id)
    await interaction.response.send_message(f"💰 {interaction.user.name}, твой баланс: **{bal} руб.**")

СТОРОНА_ВЫБОР = [
    app_commands.Choice(name="Орёл", value="орёл"),
    app_commands.Choice(name="Решка", value="решка"),
]

@tree.command(name="оир", description="Орёл или решка")
@app_commands.describe(сторона="Выбери сторону", ставка="Сумма ставки")
@app_commands.choices(сторона=СТОРОНА_ВЫБОР)
async def оир(interaction: discord.Interaction, сторона: app_commands.Choice[str], ставка: int):
    if interaction.channel.name not in CASINO_CHANNELS:
        await interaction.response.send_message("❌ Используй только в **#казик**!", ephemeral=True)
        return
    if ставка <= 0:
        await interaction.response.send_message("❌ Ставка должна быть больше 0!", ephemeral=True)
        return
    bal = get_balance(interaction.user.id)
    if ставка > bal:
        await interaction.response.send_message(f"❌ Недостаточно денег! Твой баланс: **{bal} руб.**", ephemeral=True)
        return
    результат = random.choice(["орёл", "решка"])
    if сторона.value == результат:
        новый_баланс = bal + ставка
        set_balance(interaction.user.id, новый_баланс)
        await interaction.response.send_message(
            f"🪙 Монета подброшена...\nВыпало **{результат}**!\n\n"
            f"🎉 Удача на твоей стороне!\n"
            f"✅ Ты выиграл **{ставка} руб.**\n"
            f"💰 Твой баланс: **{новый_баланс} руб.**")
    else:
        новый_баланс = bal - ставка
        set_balance(interaction.user.id, новый_баланс)
        await interaction.response.send_message(
            f"🪙 Монета подброшена...\nВыпало **{результат}**!\n\n"
            f"😢 Не повезло!\n"
            f"❌ Ты проиграл **{ставка} руб.**\n"
            f"💰 Твой баланс: **{новый_баланс} руб.**")

@tree.command(name="рул", description="Рулетка")
@app_commands.describe(ставка="Сумма ставки")
async def рул(interaction: discord.Interaction, ставка: int):
    if interaction.channel.name not in CASINO_CHANNELS:
        await interaction.response.send_message("❌ Используй только в **#казик**!", ephemeral=True)
        return
    if ставка <= 0:
        await interaction.response.send_message("❌ Ставка должна быть больше 0!", ephemeral=True)
        return
    bal = get_balance(interaction.user.id)
    if ставка > bal:
        await interaction.response.send_message(f"❌ Недостаточно денег! Твой баланс: **{bal} руб.**", ephemeral=True)
        return
    победа = random.choice([True, False])
    if победа:
        новый_баланс = bal + ставка
        set_balance(interaction.user.id, новый_баланс)
        await interaction.response.send_message(
            f"🎰 Рулетка крутится...\n\n"
            f"🎉 ДЖЕКПОТ! Ты сорвал куш!\n"
            f"✅ Ты выиграл **{ставка} руб.**\n"
            f"💰 Твой баланс: **{новый_баланс} руб.**")
    else:
        новый_баланс = bal - ставка
        set_balance(interaction.user.id, новый_баланс)
        await interaction.response.send_message(
            f"🎰 Рулетка крутится...\n\n"
            f"💸 Рулетка не твоя сегодня...\n"
            f"❌ Ты проиграл **{ставка} руб.**\n"
            f"💰 Твой баланс: **{новый_баланс} руб.**")

@tree.command(name="нак", description="Накрутить баланс участнику")
@app_commands.describe(участник="Участник", сумма="Сумма")
async def нак(interaction: discord.Interaction, участник: discord.Member, сумма: int):
    роли = [r.name for r in interaction.user.roles]
    if "Владелец Сервера" not in роли:
        await interaction.response.send_message("❌ У тебя нет прав!", ephemeral=True)
        return
    bal = get_balance(участник.id)
    новый_баланс = bal + сумма
    set_balance(участник.id, новый_баланс)
    await interaction.response.send_message(
        f"✅ Готово! {участник.name} получил **{сумма} руб.**\n"
        f"💰 Новый баланс: **{новый_баланс} руб.**")

@tree.command(name="ip", description="Узнать 'IP' участника")
@app_commands.describe(участник="Участник")
async def ip(interaction: discord.Interaction, участник: discord.Member):
    await interaction.response.defer()
    страна, города = random.choice(СТРАНЫ)
    город = random.choice(города)
    айпи = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
    улица = random.choice(УЛИЦЫ)
    дом = f"{random.randint(1,99)}{random.choice(['', 'а', 'б', 'в'])}"
    подъезд = random.randint(1, 10)
    квартира = random.randint(1, 99)
    await interaction.followup.send(
        f"🔍 **Пробив {участник.name}**\n\n"
        f"🌐 **IP:** `{айпи}`\n"
        f"🌍 **Страна:** {страна}\n"
        f"🏙️ **Город:** {город}\n"
        f"📍 **Адрес:** {улица}, д. {дом}\n"
        f"🚪 **Подъезд:** {подъезд}\n"
        f"🏠 **Квартира:** {квартира}")

@tree.command(name="fake_ban", description="Забанить участника на 67 секунд")
@app_commands.describe(участник="Участник")
async def fake_ban(interaction: discord.Interaction, участник: discord.Member):
    роли = [r.name for r in interaction.user.roles]
    if not any(r in роли for r in BAN_ROLES):
        await interaction.response.send_message("❌ У тебя нет прав!", ephemeral=True)
        return
    await interaction.response.send_message(
        f"🔨 {участник.mention} **вас забанили на 67 секунд во всех чатах!**")
    try:
        await участник.timeout(discord.utils.utcnow() + timedelta(seconds=67))
    except:
        pass
    await asyncio.sleep(67)
    await interaction.channel.send(f"✅ {участник.mention} бан снят!")

@tree.command(name="отправить", description="Отправить участника в страну")
@app_commands.describe(участник="Участник", страна="Страна на русском")
async def отправить(interaction: discord.Interaction, участник: discord.Member, страна: str):
    роли = [r.name for r in interaction.user.roles]
    if not any(r in роли for r in SEND_ROLES):
        await interaction.response.send_message("❌ У тебя нет прав!", ephemeral=True)
        return
    страна_норм = страна.strip().capitalize()
    await interaction.response.send_message(
        f"✈️ {участник.mention} **отправлен в {страна_норм}!**\n"
        f"🧳 Счастливого пути!")

@tree.command(name="gemini", description="Задай вопрос Gemini")
@app_commands.describe(вопрос="Твой вопрос")
async def gemini(interaction: discord.Interaction, вопрос: str):
    await interaction.response.defer()
    response = model_flash.generate_content(вопрос)
    ответ = response.text
    if len(ответ) > 1900:
        ответ = ответ[:1900] + "...(обрезано)"
    await interaction.followup.send(f"**Вопрос:** {вопрос}\n\n**Gemini:** {ответ}")

@tree.command(name="gemini_code", description="Gemini пишет качественный код")
@app_commands.describe(задача="Что нужно написать")
async def gemini_code(interaction: discord.Interaction, задача: str):
    await interaction.response.defer()
    промпт = f"Ты опытный программист. Напиши качественный чистый код с комментариями. Задача: {задача}"
    response = model_flash.generate_content(промпт)
    ответ = response.text
    if len(ответ) > 1900:
        ответ = ответ[:1900] + "...(обрезано)"
    await interaction.followup.send(f"**Код для:** {задача}\n\n{ответ}")

@tree.command(name="gemini_think", description="Думающий Gemini")
@app_commands.describe(вопрос="Твой вопрос")
async def gemini_think(interaction: discord.Interaction, вопрос: str):
    await interaction.response.defer()
    response = model_think.generate_content(вопрос)
    ответ = response.text
    if len(ответ) > 1900:
        ответ = ответ[:1900] + "...(обрезано)"
    await interaction.followup.send(f"**Вопрос:** {вопрос}\n\n**Gemini Think:** {ответ}")

threading.Thread(target=run_web, daemon=True).start()
client.run(DISCORD_TOKEN)
