import requests
import os
import platform
import colorama
import ccxt
import yfinance as yf
import warnings
import time
from datetime import datetime

colorama.init(autoreset=True)

warnings.filterwarnings("ignore", message="The 'unit' keyword in TimedeltaIndex construction is deprecated")

while True:
    if(platform.system().lower()=='windows'):
        command = "cls"
    else:
        command = "clear"
    os.system(command)
    date = datetime.now()
    print(f'                  {colorama.Fore.RED}{date.strftime(f"%H{colorama.Fore.WHITE}:{colorama.Fore.RED}%M{colorama.Fore.WHITE}:{colorama.Fore.RED}%S")}{colorama.Fore.WHITE}')
    
    def __init__(self):
        self.exchange = ccxt.binance()

    def gold():
        gold_ticker = "GC=F"
        gold = yf.Ticker(gold_ticker)
        gold_price = gold.history(period="1mo")["Close"].iloc[0]
        gold_price = float(gold_price)
        response_eur = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data_eur = response_eur.json()
        eur = data_eur['rates']['EUR']
        eur = float(eur)
        response_pln = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data_pln = response_pln.json()
        pln = data_pln['rates']['PLN']
        pln = float(pln)
        gold_price_eur = eur*gold_price
        gold_price_pln = pln*gold_price
        print(f"{colorama.Fore.YELLOW}GOLD")
        print(f"{colorama.Fore.YELLOW}----------------------------------------------\n")
        print(f"{colorama.Fore.YELLOW}USD: {colorama.Fore.WHITE}{round(gold_price, 2)}$")
        print(f"{colorama.Fore.YELLOW}EUR: {colorama.Fore.WHITE}{round(gold_price_eur, 2)}€")
        print(f"{colorama.Fore.YELLOW}PLN: {colorama.Fore.WHITE}{round(gold_price_pln, 2)}zł\n")
        print(f"{colorama.Fore.YELLOW}----------------------------------------------")
        
    def silver():
        silver_ticker = "SI=F"
        silver = yf.Ticker(silver_ticker)
        silver_price = silver.history(period="1mo")["Close"].iloc[0]
        silver_price = float(silver_price)
        response_eur = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data_eur = response_eur.json()
        eur = data_eur['rates']['EUR']
        eur = float(eur)
        response_pln = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data_pln = response_pln.json()
        pln = data_pln['rates']['PLN']
        pln = float(pln)
        silver_eur_price = eur*silver_price
        silver_pln_price = pln*silver_price
        print(f"{colorama.Fore.LIGHTBLACK_EX}SILVER")
        print(f"{colorama.Fore.LIGHTBLACK_EX}----------------------------------------------\n")
        print(f"{colorama.Fore.LIGHTBLACK_EX}USD: {colorama.Fore.WHITE}{round(silver_price, 2)}$")
        print(f"{colorama.Fore.LIGHTBLACK_EX}EUR: {colorama.Fore.WHITE}{round(silver_eur_price, 2)}€")
        print(f"{colorama.Fore.LIGHTBLACK_EX}PLN: {colorama.Fore.WHITE}{round(silver_pln_price, 2)}zł\n")
        print(f"{colorama.Fore.LIGHTBLACK_EX}----------------------------------------------")
    gold()
    silver()
    time.sleep(60)
    