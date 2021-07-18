import telegram_send
import os
import datetime

#datum
date = datetime.date.today()
month = str(date.month).zfill(2)
day = str(date.day).zfill(2)
year = str(date.year)


#soubor
with open('narozeniny.txt', 'r') as file:
    birfdays = file.read()
birfdays = birfdays.split('\n')[:-1] #soubor vlozime do listu, oddelujeme na zaklade znaku noveho radku a odstranuje prebytecnou prazdnou (posledni) polozku

#spravny format data, aby odpovidal vstupnim datum v souboru (18. cervenec odpovida zapisu '18.07')
correctDate = day + "." + month

#hledani shody dnesniho data s narozeninami
for birfday in birfdays:
    birfdayDate = birfday.split('-')                                    #18.07-Lorenso Teplák(2009) rozdelime na 18.07 a Lorenso Teplák(2009)
    nameOnly = (str(birfdayDate[1]).split('('))[0]                      #vypreparujeme pouze jmeno pro finalni vypis
    if birfdayDate[0] == correctDate:                                   #shoduje-li se dnesni datum s necimi narozeninami
        birfdayYear = (str(birfday.split('(')[1])).split(')')[0]        #:-)
        try:
            age = int(year) - int(birfdayYear)                          #vypocet veku
            mess = nameOnly + " dnes má " + str(age) + ". narozeniny!"
            telegram_send.send(messages=[mess])
        except:
            mess = nameOnly + " dnes má narozeniny!"
            telegram_send.send(messages=[mess])

