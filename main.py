import requests
import random
import datetime
import os

os.system('cls' if os.name == 'nt' else 'clear')
def fail_basic():
    names = ["Fail Basic project new", "Fail Script", "Feito por Igor", "Clear = Linux", "Cls = Windows"]
    nome = random.choice(names)
    date = datetime.datetime.now()
    print(f"""
_____       ___   _   _            _____       ___   _____   _   _____  
|  ___|    /   | | | | |          |  _  \     /   | /  ___/ | | /  ___| 
| |__     / /| | | | | |          | |_| |    / /| | | |___  | | | |     
|  __|   / / | | | | | |          |  _  |   / / | | \___  \ | | | | {nome}    
| |     / /  | | | | | |___       | |_| |  / /  | |  ___| | | | | |___  
|_|    /_/   |_| |_| |_____|      |_____/ /_/   |_| /_____/ |_| \_____| 

Data: {date.strftime("%d/%m/%y %H:%M")} 
""")
    def consulta_ip():
        ip = input("Digite o ip: ")
        req = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719&lang=pt-BR")
        resp = req.json()
        if "message" not in resp:
            print(f"""
Ip: {resp["query"]}
Status: {resp["status"]}
Continente: {resp["continent"]} - {resp["continentCode"]}
País: {resp["country"]} - {resp["countryCode"]}
Moeda: {resp["currency"]}
Fuso horário: {resp["timezone"]}
Estado: {resp["regionName"]} - {resp["region"]}
Cidade: {resp["city"]}
Distrito: {resp["district"]}
Cep: {resp["zip"]}
Latitude: {resp["lat"]}
Longitude: {resp["lon"]}
Deslocamento: {resp["offset"]}
Fornecedor de acesso à Internet: {resp["isp"]}
Provedor de Internet: {resp["org"]}
Sistema Autônomo: {resp["as"]}
Nome Sistema Autônomo: {resp["asname"]}
Ip reverso: {resp["reverse"]}
Smartphone: {resp["mobile"]}
Proxy: {resp["proxy"]}
Hospedagem: {resp["hosting"]}

By: Igor
          """)
        else:
            print("\nIp inválido")
        def novacon():
            nova_consulta = input("Deseja fazer uma nova consulta? \n1 = Nova Consulta; \n0 = Sair; \nEscolha: ")
            if nova_consulta == "1" or nova_consulta == "01":
                os.system('cls' if os.name == 'nt' else 'clear')
                fail_basic()
            elif nova_consulta == "0" or nova_consulta == "00":
                os.system('cls' if os.name == 'nt' else 'clear')
                exit(0)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                fail_basic()
        novacon()
    print(consulta_ip())
if __name__ == "__main__":
    fail_basic()
