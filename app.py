from main import *
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import smtplib
from email.message import EmailMessage
from os import environ
import re


suma1 = 0
palukanos1 = 0
terminas1 = 0
visos_uzklausos = ""
listas_pickle = []

try:
    with open('filename.pickle', 'rb') as handle:
        b = pickle.load(handle)
        for x in b:
            listas_pickle.append(x)
        suma1 = listas_pickle[0]
        palukanos1 = listas_pickle[1]
        terminas1 = listas_pickle[2]
        visos_uzklausos = listas_pickle[3]
        print(f"Suma: {suma1}\r\nPalukanos: {palukanos1}\r\nTerminas: {terminas1}")

except FileNotFoundError:
    pass
while True:
    print("--------------")
    menu = (input("1.Įvesti paskolos duomenis\r\n2.Parodyti paskolos informaciją\r\n3.Parodyti paskolos mokėjimo "
                  "grafiką\r\n4.Visų įvestų užklausų istorija\r\n5.Išsiusti duomenis emailu\r\n6.Baigti\r\n"))
    if menu == "1":
        try:
            suma1 = int(input("Iveskite norima suma: "))
            palukanos1 = int(input("Iveskite palukanas: "))
            terminas1 = int(input("Iveskite paskolos termina(menesiais): "))
            visos_uzklausos += f"suma: {suma1}, palūkanos: {palukanos1} , terminas: {terminas1}\r\n"
        except ValueError:
            print("--------------")
            print("Blogai įvesti duomenys!")
        with open('filename.pickle', 'wb') as handle:
            pickle.dump((suma1, palukanos1, terminas1, visos_uzklausos), handle, protocol=pickle.HIGHEST_PROTOCOL)
    if menu == "2":
        try:
            vartotojas = Paskola(suma1, palukanos1, terminas1).paskolos_info()
            print(vartotojas)
        except ZeroDivisionError:
            print("--------------")
            print("Nėra duomenų!")
    if menu == "3":
        if suma1 == 0 or palukanos1 == 0 or terminas1 == 0:
            print("--------------")
            print("Nėra duomenų!")
            continue
        else:
            try:
                vartotojas = Paskola(suma1, palukanos1, terminas1).mokejimo_grafikas()
                print(vartotojas)
                vartotojas.to_csv("paskola.csv", encoding='utf-8-sig')
                vartotojas.drop(["Total"], inplace=True)
                sns.pairplot(vartotojas)
                plt.show()
            except ValueError:
                print("Neteisingi duomenys!")
    if menu == "4":
        print(visos_uzklausos)
    if menu == "5":
        pswd = environ.get('slaptazodis')
        emailas_kam = input("Įveskite emailą, kam norit išsiusti duomenis: ")
        regex = r"^\S+@\S+\.\S+$"
        test_str = emailas_kam
        matches = re.search(regex, test_str)
        if matches:
            email = EmailMessage()
            email['from'] = 'Rokas Prabusas'
            email['to'] = emailas_kam
            email['subject'] = 'Paskolos duomenys'

            email.set_content(f"Suma: {suma1}\r\nPalūkanos: {palukanos1}\r\nTerminas: {terminas1}")

            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login('rokas.prabusas058@gmail.com', pswd)
                smtp.send_message(email)
            print("--------------")
            print("Laiškas išsiutas!")
        else:
            print("--------------")
            print("Blogai įvestas emailas")
    if menu == "6":
        break
