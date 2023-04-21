from django.shortcuts import render
from zeep import Client
import xml.etree.ElementTree as ET

def countryinfo(request):
    # Creamos un cliente SOAP para consumir el servicio web de Country Info
    client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')

    # Llamamos al método "FullCountryInfo" del servicio web para obtener información de un país específico
    result = client.service.FullCountryInfo('AR')

    # Creamos un diccionario con los datos que queremos mostrar en el template
    country_data = {
        'country_name': result.sName,
        'country_capital': result.sCapitalCity,
        'country_phone_code': result.sPhoneCode,
        'country_currency': result.sCurrencyISOCode
    }

    # Renderizamos el template y le pasamos los datos del país como contexto
    return render(request, 'countryinfo.html', country_data)



def continentlist(request) :

    # Creamos un cliente SOAP para consumir el servicio web de Country Info
    client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')

    # Llamamos al método "ListOfContinentsByName" del servicio web para obtener la lista de continentes
    response = client.service.ListOfContinentsByName()
    
    # Parsea la respuesta XML
    continent_list = []

    for continent in response :
        continent_list.append(continent)

    my_dict = {'my_list_key': continent_list}


    # Retorna los datos al usuario
    return render(request, 'continentlist.html', context=my_dict)
