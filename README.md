# Data Pirates Challenge - Possible Solution

## Scenario:

This project aims to make a crawler to get information from all UF's ZIPCODE of the [Correios](http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCep.cfm) website and save it in a JSON file.

## Requirements:

The script runs on `Python 3.8`.

To install the requirements you need to execute:

    $ cd ./src
    $ pip install -r requirements.txt
## Run Project: 

To run this project, just execute the following command in your terminal:
 
    $ cd ./src
    $ python get_cep.py

## Results:

The results appear in a folder called docs, with all ZIPCODE separated in a JSON file according to their UF.
    
## Tests:

This project have unitary tests, to run them just use the following commands in your terminal:

    $ cd ./src
    $ pytest test_verify.py
 
