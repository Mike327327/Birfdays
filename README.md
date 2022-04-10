# Birfdays

Aplikace slouží k připomínání narozenin pomocí sítě Telegram.

Použití:
1) Konfigurace sítě Telegram (https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)
- je nutné si založit bezplatný účet a "domluvit se" s botem
- ze zprávy je pro nás důležitý API kód, který využijeme při konfiguraci v terminálu (viz odkaz)
2) Soubor "narozeniny.txt" doplnit o narozeniny lidí (v příslušném formátu, který je třeba striktně dodržet).
3) Spuštění skriptu pomocí "python3 birfdays.py" a ověření, že zprávy chodí.
4) Pro automatizaci (spouštění skriptu denně v daný čas) se využije Cron (https://bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/)


# 2. fáze odevzdání projektu
---
## Komentáře k řešení
 - Řešení vychází ze struktury dané referenčním projektem CookBook. Oproti tomu však pro testování plníme databázi pro každý test, máme tedy plnou kontrolu nad tím, co v databázi je.
---
## Popis testování
### DbContext 
- Testy DbContextu vycházejí z entit deklarovaných (naplněných) v DbContextTestsEntities. 
- Testy by měly pokrývat základní CRUD operace včetně důkladnější otestování M:N vazeb (ověření správného chování při OnDelete.Cascade()).                             
### User-, Ride- a CarFacadeTests
- Testování fasády pro CRUD i komplexnější operace. 
- Nejprve se testují jednodušší operace (vkládání, získání, aktualizování), později jsou testy složitější. 
- Jsme si vědomi toho, že testy unit by měly testovat co nejmenší části, avšak pro důkladné ověření funkcionality jsou některé testy komplikovanější. 
- Pro ověření fungování využíváme nejnižší vrstvu (dbContext). 
- Repozitáře jsou vytažené z CookBooku a fungují obecně pro libovolnou entitu. 
- Do složky docs jsme přidali wireframy s popisem, kde je v plánu využít jaký model. 
- Zároveň jsme testovali jen složitější modely; ty jednodušší, kde ani není zpětné mapování, v testech hlouběji netestujeme (když jsme schopni vytáhnout více informací, určitě budeme schopni vytáhnout i méně informací stejným postupem). 
- V testech se nevyskytují entity z nižších vrstev, vše by mělo být přemapováno na modely (např. u RideDetailModel je entita auta jako CarListModel).
---
## Migrace
- Při migracích jsme měli problém s datovým typem DatyOnly, který je novinkou v EF. Soudě dle diskuze na Discordu jsme nebyli jediný. Pro účely migrace jsme datový typ změnili na takový, se kterým EF neměl problém a migraci provedli. 
- Migrace se nám jevila, že reflektuje náš ERD.
---
## Build a testy v Azure DevOps
- Vytvořena pipeline pro sestavení i otestování projektu. 
---
# Členové
- Jan Brudný (xbrudn02)
- Zdeněk Dobeš (xdobes21)
- Filip Jahn (xjahnf00)
- Michal Luner (xluner01)
- David Michalica (xmicha81)
---
