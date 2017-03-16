#!/usr/bin/python
# -*- coding:utf-8 -*-
#pip3 install ipwhois

from ipwhois import IPWhois
from pprint import pprint
from urllib import request
from ipwhois import IPWhois
import requests
import json
import socket
import os
import sys

#Colors

cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'
ciano='\033[46m'
magenta='\033[45m'
normal = '\033[0;0m'

#Proxy
##################################################################
#os.system('clear')
#print('Example: 111.68.124.10:8080')
#print('')
#Mask = input('Digite um Proxy Valido: ')
#print('')
#handler = request.ProxyHandler({'http': 'http://'+Mask+'/'})
#opener = request.build_opener(handler)
#Proxy = IPWhois('74.125.225.229', proxy_opener = opener)
#res = Proxy.lookup_whois(inc_nir=True)
#pprint(res)

####################################################################
EXPECTUS = ''' 	         ☣         ☣          ☣         ☣       ☣        ☣
 ☣   ☣         ☣     .ed"""" """$$$$be.      ☣           
                   -"           ^""**$$$e. ☣      ☣     ☣ 
    ☣    ☣       ."                   '$$$c   ☣     ☣
                /                      "4$$b             ☣
 ☣        ☣    d  3                      $$$$ ☣  ☣            ☣                   ☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
    ☣          $  *                   .$$$$$$          ☣                          ☣                      ☣
              .$  ^c           $$$$$e$$$$$$$$.      ☣                             ☣  ▒█░▒█ █▀▀ █░░ █▀▀█  ☣
        ☣     d$L  4.         4$$$$$$$$$$$$$$b  ☣         ☣                       ☣  ▒█▀▀█ █▀▀ █░░ █░░█  ☣
 ☣            $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$                                    ☣  ▒█░▒█ ▀▀▀ ▀▀▀ █▀▀▀  ☣
  e$""=.   ☣  $$$$P d$$$$F $ $$$$$$$$$- $$$$$$       ☣         ☣                  ☣                      ☣
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c                        ☣ łαbørαŧøriø Fαηŧαsмα ☣
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$      ☣ .=  e$$$.   ☣                    ☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$              +===========================================+
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""               |             FooT3rFing3r.py               |
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"    ☣           +===========================================+
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"      ☣               | ♚ Coded: łuŧЋ1єr ルシアー                 |
    ☣        "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"   ☣                    | ♚ Contact: @Xcultevil (Telegram)          |
         ☣     "*$$$  *=%4.$ L L$ P3$$$F $$$P"             ☣             | ♚ Date: 16/03/2017                        |
  ☣               "$   "%*ebJLzb$e$$$$$b $P"       ☣                     | ♚ Chanell:telegram.me/Phantasm_Lab        |
           ☣    ☣   %..      4$$$$$$$$$$ "      ☣       ☣                | ♚ I take no responsibilities for the      |
     ☣               $$$e   z$$$$$$$$$$%                                 |   use of this program !                   |
                      "*$c  "$$$$$$$P"     ☣         ☣      ☣            +===========================================+
 ☣           ☣   ☣     ."""*$$$$$$$$bc                                   |             łαbørαŧøriø Fαηŧαsмα          |
      ☣             .-"    .$***$$$"""*e.       ☣                        +===========================================+
                 .-"    .e$"  ☣  "*$c  ^*b.               ☣
☣         .=*""""    .e$*"          "*bc  "*$e..      ☣
        .$"        .z*"  ☣   ☣    ☣   ^*$e.   "*****e.       ☣
   ☣    $$ee$c   .d"   ☣            ☣    "*$.        3.  ☣
        ^*$E")$..$"          ☣              *   .ee==d%
   ☣       $.d$$$*   łαbørαŧøriø Fαηŧαsмα    *  J$$$e*  ☣      ☣
☣       ☣   """""                              "$$$" ☣      ☣  '''
HELP='''
☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
☣                      ☣
☣  ▒█░▒█ █▀▀ █░░ █▀▀█  ☣
☣  ▒█▀▀█ █▀▀ █░░ █░░█  ☣
☣  ▒█░▒█ ▀▀▀ ▀▀▀ █▀▀▀  ☣
☣                      ☣
☣ łαbørαŧøriø Fαηŧαsмα ☣
☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
'''
ROBOT = """	
              .andAHHAbnn.
           .aAHHHAAUUAAHHHAn.
          dHP^~"        "~^THb.
    .   .AHF                YHA.   .
    |  .AHHb.              .dHHA.  |           +===========================================+
    |  HHAUAAHAbn      adAHAAUAHA  |           |             FooT3rFing3r.py               |
    I  HF~"_____        ____ ]HHH  I           +===========================================+
   HHI HAPK""~^YUHb  dAHHHHHHHHHH IHH          | ♚ Coded: łuŧЋ1єr ルシアー                 |
   HHI HHHD> .andHH  HHUUP^~YHHHH IHH          | ♚ Contact: @Xcultevil (Telegram)          |
   YUI ]HHP     "~Y  P~"     THH[ IUP          | ♚ Date: 16/03/2017                        |
    "  `HK                   ]HH'  "           | ♚ Chanell:telegram.me/Phantasm_Lab        |
        THAn.  .d.aAAn.b.  .dHHP               | ♚ I take no responsibilities for the      |
        ]HHHHAAUP" ~~ "YUAAHHHH[               |   use of this program !                   |
        `HHP^~"  .annn.  "~^YHH'               +===========================================+
         YHb    ~" "" "~    dHF                |             łαbørαŧøriø Fαηŧαsмα          |
          "YAb..abdHHbndbndAP"                 +===========================================+
           THHAAb.  .adAHHF 
            "UHHHHHHHHHHU"
              ]HHUUHHHHHH[
            .adHHb "HHHHHbn.
     ..andAAHHHHHHb.AHHHHHHHAAbnn..
.ndAAHHHHHHUUHHHHHHHHHHUP^~"~^YUHHHAAbn.
  "~^YUHHP"   "~^YUHHUP"        "^YUP^"
       ""         "~~"
"""
os.system('clear')
print(purpleClaro + ROBOT + normal)
def help():
   print(verde+'Modo de uso:')
   print(verde+'$ python3 Foot3rFing3r.py [opções] [url]\n')
   print(verde+'URL > http://www.osaka-u.ac.jp')
   print(verde+'URL > http://www.anatel.gov.br/institucional\n')
   print(vermelho+'URL >  https://www.tecmundo.com.br')
   print(vermelho+'URL >  https://www.uol.com.br\n')

if len(sys.argv) <= 3 and len(sys.argv) >= 2:
	opt = sys.argv[1]
	if opt == '-h' or opt == '--help':
		os.system('clear')
		print(vermelho + EXPECTUS)
		help()
	else:
		pass
else:
	pass	

GeoLocation = """
+===================================================+
|            [+] Geo Location Info [+]              |
+===================================================+
"""

def requisicao(IP):
	try:
		req = requests.get('http://ip-api.com/json/'+IP)
		Geo = json.loads(req.text)
		return Geo
	
	except:
		print('Error na Conexão')
		return None

def printar_detalhes(Geo):
	print('')
	print(verde+GeoLocation)
	print('')
	print(verde + 'IP: '+normal,Geo['query']+normal,'\n')
	print(verde + 'Country:'+normal,Geo['country']+normal,'\n')
	print(verde + 'Country code:'+normal,Geo['countryCode']+normal,'\n')
	print(verde + 'Region:'+normal,Geo['regionName']+normal,'\n')
	print(verde + 'Region code:'+normal,Geo['region']+normal,'\n')
	print(verde + 'City:'+normal,Geo['city']+normal,'\n')
	print(verde + 'Zip Code:'+normal,Geo['zip']+normal,'\n')
	print(verde + 'Latitude:',Geo['lat'])
	print(verde + 'Longitude:',Geo['lon'],'\n')
	print(verde + 'Timezone:'+normal,Geo['timezone']+normal,'\n')
	print(verde + 'ISP:'+normal,Geo['isp']+normal,'\n')
	print(verde + 'Organization:'+normal,Geo['org']+normal,'\n')
	print(verde + 'AS number/name:'+normal,Geo['as']+normal,'\n')
	print('')


url = input(verde + '☯ Digite uma url : ')

try:
	rep = url.replace('http://','')
	socket = socket.gethostbyname(rep)
	obj = IPWhois(socket)
	Geo = requisicao(socket)
	printar_detalhes(Geo)
	res = obj.lookup_whois(inc_nir=True)
	res1 = obj.lookup_rdap(depth=1, inc_nir=True)
except:
	rep = url.replace('https://','')
	socket = socket.gethostbyname(rep)
	Geo = requisicao(socket)
	printar_detalhes(Geo)
	obj = IPWhois(socket)
	res = obj.lookup_whois(inc_nir=True)
	res1 = obj.lookup_rdap(depth=1, inc_nir=True)

NETWORK = """
+===================================================+
|            [+] NETWORK INFORMATION [+]            |
+===================================================+
"""
ADMIN = """
+===================================================+
|            [+] Administration Info [+]            |
+===================================================+
"""

T3CH = """
+===================================================+
|               [+] Organization [+]                |
+===================================================+
"""
M0re_Information = """
+===================================================+
|              [+] More Information [+]             |
+===================================================+
"""


def Printar_Nets():
	try:
		print('')
		print(azul + NETWORK)
		print('')
		print(azul + 'IP: ',res["query"],'\n')
		print(azul + 'Endereço: ',res["nets"][0]['address'],'\n')
		print(azul + 'Created:',res["nets"][0]['created'],'\n')
		print(azul + 'bloqueio de roteamento de rede: ',res["nets"][0]['cidr'],'\n')
		print(azul + 'City:',res["nets"][0]['city'],'\n')
		print(azul + 'Country:',res["nets"][0]['country'],'\n')
		print(azul + 'Description: ',res["nets"][0]['description'],'\n')
		print(azul + 'Emails:',res["nets"][0]['emails'][0])
		print(azul + 'Emails:',res["nets"][0]['emails'][1])
		print(azul + 'Emails:',res["nets"][0]['emails'][2],'\n')
		print(azul + 'Identificador exclusivo para um objeto registrado:',res["nets"][0]['handle'],'\n')
		print(azul + 'ID - registro de rede para um endereço IP: ',res["nets"][0]['name'],'\n')
		print(azul + 'Codigo Postal: ',res["nets"][0]['postal_code'],'\n')
		print(azul + 'Intervalo de rede: ',res["nets"][0]['range'],'\n')
		print(azul + 'Estado para uma rede registada: ',res["nets"][0]['state'],'\n')
		print(azul + 'Data atualizada do registro da rede no formato ISO 8601: ',res["nets"][0]['updated'],'\n')
		print(azul + 'Nomes de Servidores listados para uma rede registrada.: ',res["nir"]['nets'][0]['nameservers'],'\n')
		print(azul + 'Identificador exclusivo para uma rede registrada: ',res["nir"]['nets'][0]['handle'],'\n')
	except:
		print(vermelho + '[!] Error Information Not Found!')
		pass	
def Printar_Admin():
	try:
		print('')
		print(verde + ADMIN)
		print ('')
		print(verde + 'Nome do Administrador: ',res["nir"]['nets'][0]['contacts']['admin']['name'],'\n')
		print(verde + 'Endereço de e-mail: ',res["nir"]['nets'][0]['contacts']['admin']['email'],'\n')
		print(verde + 'Endereço de e-mail de resposta do contato:',res["nir"]['nets'][0]['contacts']['admin']['reply_email'],'\n')
		print(verde + 'Endereço de FAX: ',res["nir"]['nets'][0]['contacts']['admin']['fax'],'\n')
		print(verde + 'Organização: ',res["nir"]['nets'][0]['contacts']['admin']['organization'],'\n')
		print(verde + 'Cargo ou Posição: ',res["nir"]['nets'][0]['contacts']['admin']['title'],'\n')
		print(verde + 'Telefone: ',res["nir"]['nets'][0]['contacts']['admin']['phone'],'\n')
		print(verde + 'Divisão do contato da organização.: ', res["nir"]['nets'][0]['contacts']['admin']['division'],'\n')
	except:
		print(vermelho + '[!] Error Information Not Found!')
		pass

def Tech():
	try:
		print('')
		print(purpleClaro + T3CH)
		print('')
		print(purpleClaro +'Divisão do contato da organização.: ',res["nir"]['nets'][0]['contacts']['tech']['division'],'\n')
		print(purpleClaro +'Endereço de e-mail: ',res["nir"]['nets'][0]['contacts']['tech']['email'],'\n')
		print(purpleClaro +'Endereço de FAX: ',res["nir"]['nets'][0]['contacts']['tech']['fax'],'\n')
		print(purpleClaro +'Nome: ',res["nir"]['nets'][0]['contacts']['tech']['name'],'\n')
		print(purpleClaro +'Organização: ',res["nir"]['nets'][0]['contacts']['tech']['organization'],'\n')
		print(purpleClaro +'Telefone: ',res["nir"]['nets'][0]['contacts']['tech']['phone'],'\n')
		print(purpleClaro +'Endereço de e-mail de resposta do contato: ',res["nir"]['nets'][0]['contacts']['tech']['reply_email'],'\n')
		print(purpleClaro +'Cargo ou Posição: ',res["nir"]['nets'][0]['contacts']['tech']['title'],'\n')
		print(purpleClaro +'Data atualizada do registro da rede no formato ISO 8601: ',res["nir"]['nets'][0]['contacts']['tech']['updated'],'\n')
		print('')
	except:
		print(vermelho + '[!] Error Information Not Found!')
		print('')
		pass		

 
def NETS():
	try:
		print('')
		print(amarelo + M0re_Information)
		print('')
		print(amarelo + 'Country: ',res["nir"]['nets'][0]['country'],'\n')
		print(amarelo + 'Data de Criação: ',res["nir"]['nets'][0]['created'],'\n')
		print(amarelo + 'Identificador exclusivo para um objeto registrado: ',res["nir"]['nets'][0]['handle'],'\n')
		print(amarelo + 'ID - registro de rede para um endereço IP: ',res["nir"]['nets'][0]['name'],'\n')
		print(amarelo + 'Nomes de Servidores listados para uma rede registrada.: ',res["nir"]['nets'][0]['nameservers'],'\n')
		print(amarelo + 'Código Postal: ',res["nir"]['nets'][0]['postal_code'],'\n')
		print(amarelo + 'IP: ',res["nir"]['query'],'\n')
	except:
		print(vermelho + '[!] Error Information Not Found!')
		pass	

def PirateRobert():
	try:
		print('')
		print(cyanClaro + M0re_Information)
		print('')
		print(cyanClaro +'Endereço: ',res1["objects"]['JNIC1-AP']['contact']['address'][0]['value'],'\n')
		print(cyanClaro +'Email: ',res1["objects"]['JNIC1-AP']['contact']['email'][0]['value'],'\n')
		print(cyanClaro +'O tipo de informação de contato (individual, grupo, org):',res1["objects"]['JNIC1-AP']['contact']['kind'],'\n')
		print(cyanClaro +'Registro De Rede:',res1["objects"]['JNIC1-AP']['contact']['name'],'\n')
		print('')
		print(cyanClaro +'[+] Lista De Contatos:\n')
		print(verde+"Phone:",res1["objects"]['JNIC1-AP']['contact']['phone'][0]['value'],cyanClaro + 'Tipo: ',res1["objects"]['JNIC1-AP']['contact']['phone'][0]['type'] )
		print(verde+"Phone:",res1["objects"]['JNIC1-AP']['contact']['phone'][1]['value'],cyanClaro + 'Tipo: ',res1["objects"]['JNIC1-AP']['contact']['phone'][1]['type'],'\n')
		print(cyanClaro +'Links HTTP / HTTPS fornecidos para um objeto RIR: ',res1["objects"]['JNIC1-AP']['links'][0],'\n')
		print(cyanClaro +'Notices: ',res1["objects"]['JNIC1-AP']['notices'],'\n')
		print(cyanClaro +'Lista de funções atribuídas a um objeto registrado: ',res1["objects"]['JNIC1-AP']['roles'][0],',',res1["objects"]['JNIC1-AP']['roles'][1],'\n')
	except:
		print(vermelho + '[!] Error Information Not Found!')
		pass

def Lab666():
	try:
		print('')
		print(cyanClaro + M0re_Information)
		print('')
		print(cyanClaro +'Endereço: ',res1["objects"]['ABUSE5250-ARIN']['contact']['address'][0]['value'],'\n')
		print(cyanClaro +'Email: ',res1["objects"]['ABUSE5250-ARIN']['contact']['email'][0]['value'],'\n')
		print(cyanClaro +'O tipo de informação de contato (individual, grupo, org):',res1["ABUSE5250-ARIN"]['JNIC1-AP']['contact']['kind'],'\n')
		print(cyanClaro +'Registro De Rede:',res1["objects"]['ABUSE5250-ARIN']['contact']['name'],'\n')
		print('')
		print(cyanClaro +'[+] Lista De Contatos:\n')
		print(verde+"Phone:",res1["objects"]['ABUSE5250-ARIN']['contact']['phone'][0]['value'],cyanClaro + 'Tipo: ',res1["objects"]['JNIC1-AP']['contact']['phone'][0]['type'] )
		print(verde+"Phone:",res1["objects"]['ABUSE5250-ARIN']['contact']['phone'][1]['value'],cyanClaro + 'Tipo: ',res1["objects"]['JNIC1-AP']['contact']['phone'][1]['type'],'\n')
		print(cyanClaro +'Links HTTP / HTTPS fornecidos para um objeto RIR: ',res1["objects"]['ABUSE5250-ARIN']['links'][0],'\n')
		print(cyanClaro +'Notices: ',res1["objects"]['ABUSE5250-ARIN']['notices'],'\n')
		print(cyanClaro +'Lista de funções atribuídas a um objeto registrado: ',res1["objects"]['ABUSE5250-ARIN']['roles'][0],',',res1["objects"]['JNIC1-AP']['roles'][1],'\n')
		print('')
	except:
		print(vermelho + '[!] Error Information Not Found!')
		pass
try:
	try:
		Printar_Nets()
		NETS()
		Printar_Admin()
		Tech()
		PirateRobert()
		Lab666()
	except:
		pass
except KeyboardInterrupt:
	print("[404] Error Not Found!")
