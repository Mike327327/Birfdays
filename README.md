# Birfdays

Aplikace slouží k připomínání narozenin pomocí sítě Telegram.

Použití:
1) Konfigurace sítě Telegram (https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)
- je nutné si založit bezplatný účet a "domluvit se" s botem
- ze zprávy je pro nás důležitý API kód, který využijeme při konfiguraci v terminálu (viz odkaz)
2) Soubor "narozeniny.txt" doplnit o narozeniny lidí (v příslušném formátu, který je třeba striktně dodržet).
3) Spuštění skriptu pomocí "python3 birfdays.py" a ověření, že zprávy chodí.
4) Pro automatizaci (spouštění skriptu denně v daný čas) se využije Cron (https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/)
