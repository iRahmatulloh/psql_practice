from os import system
from time import sleep

import psycopg2
from db_data import *

system('cls')

register_name = input("Tahallus kiriting -> ")
register_card = input("Bank card kiriting (8 talik va raqamlardan iborat bo'lgan)-> ")
register_sum = int(input("Ichidagi summani kiriting: "))


def adding_data(name=register_name, card_num=register_card, card_sum=register_sum):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS register (Username VARCHAR(20), card INT NOT NULL UNIQUE, sum BIGINT );")

    cur.execute(f"SELECT EXISTS (SELECT * FROM register WHERE card = '{register_card}');")

    x = cur.fetchall()[0][0]
    if x:
        print("Bu Bank cartasi Bazada mavjud!")
        exit()
    elif len(register_card) != 8:
        print("karta raqam mos emas!")
        exit()
    try:
        cur.execute("START TRANSACTION;")
        cur.execute(f"INSERT INTO register VALUES ('{name}', '{card_num}', '{card_sum}');")
        cur.execute("COMMIT TRANSACTION;")
    except psycopg2.Error as Error:
        print("Siz xatoga yo'l qo'ydingiz!!")
        exit()
    sleep(0.5)
    print("Ma'lumotlar kiritildi!\n  Dasturdan foydalanishingiz mumkin!")
    connection.commit()


adding_data()


def payment():
    print("""
    1. Kommunal to'lovlar 
    2. Mobil operatorlar
    3. Sug'urta
    4. Transport va Avtoturargoh
    
    0. Dasturdan chiqish!""")
    ask_pay = int(input("Qaysi biridan foydalanasiz: "))

    if ask_pay == 1:
        return 1
    elif ask_pay == 2:
        return 2
    elif ask_pay == 3:
        return 3
    elif ask_pay == 4:
        return 4
    print("Dasturdan foydalanganingiz uchun rahmat!")


def kommunal_payment():
    cur.execute("CREATE TABLE IF NOT EXISTS kommunal (Turi VARCHAR(16) UNIQUE, balance double precision, "
                "idCard INT UNIQUE, sum_pay SMALLINT, date_last TIME);")
    cur.execute("INSERT INTO kommunal (turi, balance) VALUES ('IchimlikSuvi', 10000), ('ElektrEnergiya', 10000),"
                "('TozaHudud', 10000), ('Gaz', 10000);")
    cur.execute("ALTER TABLE kommunal ALTER COLUMN date_last SET DEFAULT now();")
    print("""
    IchimlikSuvi
    ElektrEnergiya
    TozaHudud
    Gaz
    """)
    pay_kommunal = input("Qaysi biriga to'lov amalga oshiramiz(yozilishga etibor bering!): ")
    pay_kommunal_sum = int(input("qancha to'lov amalga oshiramiz(mablag'ingiz yetarli bo'lishi kerak)-> "))
    if register_sum > pay_kommunal_sum:
        try:
            cur.execute("START TRANSACTION;")
            cur.execute(f"UPDATE kommunal SET balance = balance + {pay_kommunal_sum} WHERE turi = '{pay_kommunal}'")
            cur.execute(f"UPDATE kommunal SET date_last = now() WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE kommunal SET sum_pay = {pay_kommunal_sum} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE kommunal SET idcard = {register_card} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE register SET sum = sum - {pay_kommunal_sum} WHERE card='{register_card}';")
            cur.execute("COMMIT TRANSACTION;")
            exit()
        except psycopg2.Error as Error:
            cur.execute("ROLLBACK TRANSACTION;")
            print(f"Siz qaerdadur xato qildingiz! {Error}")
            exit()


def mobil_pay():
    cur.execute("CREATE TABLE IF NOT EXISTS mobil (Turi VARCHAR(16) UNIQUE, balance double precision, "
                "idCard INT UNIQUE, sum_pay SMALLINT, date_last TIME);")
    cur.execute("INSERT INTO mobil (turi, balance) VALUES ('Beeline', 10000), ('ucell', 10000),"
                "('uzmobile', 10000), ('mobiuz', 10000);")
    cur.execute("ALTER TABLE mobil ALTER COLUMN date_last SET DEFAULT now();")
    print("""
        beeline
        ucell
        uzmobile
        mobiuz
        """)
    pay_kommunal = input("Qaysi biriga to'lov amalga oshiramiz(yozilishga etibor bering!): ")
    pay_kommunal_sum = int(input("qancha to'lov amalga oshiramiz(mablag'ingiz yetarli bo'lishi kerak)-> "))
    if register_sum > pay_kommunal_sum:
        try:
            cur.execute("START TRANSACTION;")
            cur.execute(f"UPDATE mobil SET balance = balance + {pay_kommunal_sum} WHERE turi = '{pay_kommunal}'")
            cur.execute(f"UPDATE mobil SET date_last = now() WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE mobil SET sum_pay = {pay_kommunal_sum} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE mobil SET idcard = {register_card} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE register SET sum = sum - {pay_kommunal_sum} WHERE card='{register_card}';")
            cur.execute("COMMIT TRANSACTION;")
            exit()
        except psycopg2.Error as Error:
            cur.execute("ROLLBACK TRANSACTION;")
            print(f"Siz qaerdadur xato qildingiz! {Error}")
            exit()


def insurance():
    cur.execute("CREATE TABLE IF NOT EXISTS insurance (Turi VARCHAR(16) UNIQUE, balance double precision, "
                "idCard INT UNIQUE, sum_pay SMALLINT, date_last TIME);")
    cur.execute("INSERT INTO insurance (turi, balance) VALUES ('apex', 10000), ('gross', 10000),"
                "('inson', 10000), ('kapital', 10000);")
    cur.execute("ALTER TABLE insurance ALTER COLUMN date_last SET DEFAULT now();")
    print("""
        apex
        gross
        inson
        """)
    pay_kommunal = input("Qaysi biriga to'lov amalga oshiramiz(yozilishga etibor bering!): ")
    pay_kommunal_sum = int(input("qancha to'lov amalga oshiramiz(mablag'ingiz yetarli bo'lishi kerak)-> "))
    if register_sum > pay_kommunal_sum:
        try:
            cur.execute("START TRANSACTION;")
            cur.execute(f"UPDATE insurance SET balance = balance + {pay_kommunal_sum} WHERE turi = '{pay_kommunal}'")
            cur.execute(f"UPDATE insurance SET date_last = now() WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE insurance SET sum_pay = {pay_kommunal_sum} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE insurance SET idcard = {register_card} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE register SET sum = sum - {pay_kommunal_sum} WHERE card='{register_card}';")
            cur.execute("COMMIT TRANSACTION;")
            exit()
        except psycopg2.Error as Error:
            cur.execute("ROLLBACK TRANSACTION;")
            print(f"Siz qaerdadur xato qildingiz! {Error}")
            exit()



def for_car():
    cur.execute("CREATE TABLE IF NOT EXISTS car (Turi VARCHAR(16) UNIQUE, balance double precision, "
                "idCard INT UNIQUE, sum_pay SMALLINT, date_last TIME);")
    cur.execute("INSERT INTO car (turi, balance) VALUES ('ATTO', 10000), ('YOTO', 10000),"
                "('tashbus', 10000), ('parqour', 10000);")
    cur.execute("ALTER TABLE insurance ALTER COLUMN date_last SET DEFAULT now();")
    print("""
        ATTO
        YOTO
        tashbus
        parqour
        """)
    pay_kommunal = input("Qaysi biriga to'lov amalga oshiramiz(yozilishga etibor bering!): ")
    pay_kommunal_sum = int(input("qancha to'lov amalga oshiramiz(mablag'ingiz yetarli bo'lishi kerak)-> "))
    if register_sum > pay_kommunal_sum:
        try:
            cur.execute("START TRANSACTION;")
            cur.execute(f"UPDATE car SET balance = balance + {pay_kommunal_sum} WHERE turi = '{pay_kommunal}'")
            cur.execute(f"UPDATE car SET date_last = now() WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE car SET sum_pay = {pay_kommunal_sum} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE car SET idcard = {register_card} WHERE turi='{pay_kommunal}';")
            cur.execute(f"UPDATE register SET sum = sum - {pay_kommunal_sum} WHERE card='{register_card}';")
            cur.execute("COMMIT TRANSACTION;")
            exit()
        except psycopg2.Error as Error:
            cur.execute("ROLLBACK TRANSACTION;")
            print(f"Siz qaerdadur xato qildingiz! {Error}")
            exit()


save = payment()
if save == 1:
    kommunal_payment()
if save == 2:
    mobil_pay()
if save == 3:
    insurance()
if save == 4:
    for_car()
