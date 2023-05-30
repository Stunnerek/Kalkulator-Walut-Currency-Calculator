import urllib.request, json 
import tkinter as tk
from datetime import date
from tkcalendar import *

waluta="EUR"
liczba=0
today = date.today()



root = tk.Tk()
root.title('Kalkulator Walutowy')
root.geometry("1100x500")
root.configure(bg="#C5E0B3")
Kalkulator = tk.Label(root, text='Kalkulator Walut',  fg= 'black', font=("bold", 30, "italic"))
Kalkulator.grid(row=1 )
Kalkulator.place(relx=0.5, rely=0.090, anchor=tk.CENTER)

Blok_autorstwa = tk.Label(root, text='Kamil Janowski 3TPA',  fg= 'black', font=("bold", 30, "italic"))
Blok_autorstwa.grid(row=1 )
Blok_autorstwa.place(relx=0.5, rely=0.890, anchor=tk.CENTER)

def wybrana_metoda():
     e_text=textbox1.get()
     message3.config(text= str(e_text)+"zł")
def ustaw_euro():
     data_wybrana = cal.get_date()
     waluta="EUR"
     with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
      e_text=textbox1.get()
      kurs=data['rates'] [0] ['mid']
      finalowa_liczba=float(e_text)
      print( float(kurs))
      final=(float(e_text) * float(kurs))
      message3.config(text= str(round(final,2))+"zł")

Kalendarz = tk.Label(root,bg="#C5E0B3")
Kalendarz.place(relx=0.200, rely=0.590, anchor=tk.CENTER)
def date_scanner ():
    print(data_wybrana)     
cal = Calendar(
    Kalendarz, 
    selectmode="day", 
    year=today.year, 
    month=today.month,
    day=today.day,
    date_pattern="y-mm-dd",
    command=date_scanner
    )
cal.pack()
data_wybrana = cal.get_date()
with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
     
      kurs=data['rates'] [0] ['mid']
    
      print( float(kurs))

     
def ustaw_USD():
     data_wybrana = cal.get_date()
     print(data_wybrana)
     waluta="USD"
     print("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(data_wybrana)+"/?format=json")
     with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
  
      
      e_text=textbox1.get()
    
      kurs=data['rates'] [0] ['mid']
      print(float(e_text) * float(kurs))
      final=(float(e_text) * float(kurs))
      message3.config(text= str(round(final,2))+"zł")
def ustaw_CHF():
     data_wybrana = cal.get_date()
     waluta="CHF"
     print("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(date.today())+"/?format=json")
     with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/"+str(waluta)+"/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
      e_text=textbox1.get()
    
      kurs=data['rates'] [0] ['mid']
      print(float(e_text) * float(kurs))
      final=(float(e_text) * float(kurs))
      message3.config(text= str(round(final,2))+"zł")
      data_wybrana = cal.get_date()

     
     
USD_BUTTON = tk.Button(root, text ="USD",command=ustaw_USD )
USD_BUTTON.place(relx=0.630, rely=0.390, anchor=tk.CENTER, width=86, height= 50)
EURO_BUTTON = tk.Button(root, text ="EURO",command=ustaw_euro )
EURO_BUTTON.place(relx=0.630, rely=0.520, anchor=tk.CENTER, width=86, height= 50)
CHF_BUTTON = tk.Button(root, text ="CHF",command=ustaw_CHF )
CHF_BUTTON.place(relx=0.630, rely=0.650, anchor=tk.CENTER, width=86, height= 50)
message3 = tk.Label(root,   fg= 'black', font=("bold", 30, "italic"))
message3.grid(row=1 )
message3.place(relx=0.8, rely=0.530, anchor=tk.CENTER)
TABLICA_KURS = tk.Label(root,borderwidth=1, text="Kurs Dnia",bg="#C5E0B3", fg="blue"  )

TABLICA_KURS.place(relx=0.550, rely=0.290, anchor=tk.CENTER, width=86, height= 50)
TABLICA_KWOTA = tk.Label(root,borderwidth=1, text="Kwota",bg="#C5E0B3", fg="blue"  )

TABLICA_KWOTA.place(relx=0.710, rely=0.290, anchor=tk.CENTER, width=86, height= 50)
USD_KURS = tk.Label(root,borderwidth=1, relief="solid", )
print(kurs)
USD_KURS.place(relx=0.550, rely=0.390, anchor=tk.CENTER, width=86, height= 50)
EURO_KURS = tk.Label(root,text="KURS",borderwidth=1, relief="solid")
EURO_KURS.place(relx=0.550, rely=0.520, anchor=tk.CENTER, width=86, height= 50)
CHF_KURS = tk.Label(root,text="KURS",borderwidth=1, relief="solid")
CHF_KURS.place(relx=0.550, rely=0.650, anchor=tk.CENTER, width=86, height= 50)
textbox1 = tk.Entry(root, textvariable=liczba,font=('Times', 24),borderwidth=1, relief="solid")
textbox1.place(relx=0.710, rely=0.390, anchor=tk.CENTER, width=89, height= 50)
EURO_BOX = tk.Entry(root, textvariable=liczba,font=('Times', 24),borderwidth=1, relief="solid")
EURO_BOX.place(relx=0.710, rely=0.520, anchor=tk.CENTER, width=89, height= 50)
CHF_BOX = tk.Entry(root, textvariable=liczba,font=('Times', 24),borderwidth=1, relief="solid")
CHF_BOX.place(relx=0.710, rely=0.650, anchor=tk.CENTER, width=89, height= 50)
cal.pack()
def date_scanner(self):
    
    data_wybrana = cal.get_date()
    with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/EUR/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
      kurs_euro=data['rates'] [0] ['mid']
      EURO_KURS.config(text= kurs_euro)
    with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/USD/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
      kurs_usd=data['rates'] [0] ['mid']
      USD_KURS.config(text= kurs_usd)
    with urllib.request.urlopen("https://api.nbp.pl/api/exchangerates/rates/a/CHF/"+str(data_wybrana)+"/?format=json") as url:
      data = json.load(url)
      kurs_chf=data['rates'] [0] ['mid']
      CHF_KURS.config(text= kurs_chf)
  
  


print('Przelicznik Walut')
cal.bind("<<CalendarSelected>>", date_scanner)

        



#http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{dzien}/?format=json"}
#https://api.nbp.pl/api/exchangerates/rates/a/usd/2023-05-09/?format=json


root.mainloop()