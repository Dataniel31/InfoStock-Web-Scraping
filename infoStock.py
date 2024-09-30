import requests
from bs4 import BeautifulSoup

# detalles del pedido
url = "https://es-us.finanzas.yahoo.com/quote/NVDA/"
encabezados = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
html = requests.get(url, headers=encabezados)

#Crear la sopa
sopa = BeautifulSoup(html.content, "lxml")

#Extraer informacion de la sopa
info_encabezado = sopa.find_all("div", id = "quote-header-info")[0]
titulo_simbolo = info_encabezado.find("h1").get_text()
precio_actual = info_encabezado.find("fin-streamer", class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()


print(precio_actual)