import pytest
import constants
from get_cep import get_data, build_info, create_and_write_document, clean_data
from urllib.parse import urlencode
from urllib.request import Request, urlopen


url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCep.cfm'
fields = {"UF": 'SC', 'Localidade': '', 'qtdrow' : '100', 'pagini': '1', 'pagfim' : '101' }
request = Request(url, urlencode(fields).encode())
result = urlopen(request).read()
data = get_data(result)

##Tests if the type of cleaned data still a dictionary
def test_type_of_clean_data():
    address = clean_data(data)
    if type(address) == type(dict):
        assert True

##Tests if the cleaned data has more than one object
def test_return_of_clean_data():
     address = list(clean_data(data))
     assert len(address) >= 1

##Tests if the cleaned data was cleaned
def test_clean_data_duplicates():
    address_dup = list(build_info(data))
    address = list(clean_data(data))
    assert len(address) != len(address_dup)

##The return of data can't be None
def test_get_data_result():
    data = get_data(result)
    assert data != None