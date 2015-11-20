# -*- coding: utf-8 -*-
__author__ = 'Joelmir'

from suds.client import Client
import sys, re, traceback

def find_address(cep):
    '''
        Função que busca o endereço com o numero do CEP
    '''
    web_service = Client('https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl')
    
    try:
        return web_service.service.consultaCEP(cep)
    except:
        return u'cep: {0} inválido!'.format(cep)


if __name__== "__main__":

    if len(sys.argv) < 2:
        print 'parametros invalidos!'
        print 'adicione o valor do cep sem espaços ou ifens '
    else:
        list_of_address = []
        for cep in sys.argv[1:]:
            list_of_address.append(find_address(u''.join(re.findall('\d+', cep))))

        #Exibe os endereços encontrados
        for a in list_of_address:
            print a
