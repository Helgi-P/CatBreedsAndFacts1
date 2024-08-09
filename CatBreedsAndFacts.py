import requests

# Base URL for all requests
base_url = 'https://catfact.ninja'

print('1. BREED REQUESTS')

#Base endpoint for breed requests
breeds_endpoint = '/breeds'

# Request 1.1.: full list of cat breeds
full_breeds_params = {'limit': '98'}

full_breeds_response = requests.get(base_url + breeds_endpoint, params=full_breeds_params)

print('\nRequest 1.1.: full list of cat breeds')
print('Status: ', full_breeds_response.status_code)
print('Body: ', full_breeds_response.text)
print('Headers: ', full_breeds_response.headers)

#  Request 1.2.: 1 cat breed

one_breed_params = {'limit': '1'}

one_breed_response = requests.get(base_url + breeds_endpoint, params=one_breed_params)

print('\nRequest 1.2.: 1 cat breed')
print('Status: ', one_breed_response.status_code)
print('Body: ', one_breed_response.text)
print('Headers: ', one_breed_response.headers)


#  Request 1.3.: pagination current page number = last available page

pagination1_params = {
    'limit': '32',
    'page': '4'
}

pagination1_response = requests.get(base_url + breeds_endpoint, params=pagination1_params)

print('\nRequest 1.3.: pagination current page number = last available page')
print('Status: ', pagination1_response.status_code)
print('Body: ', pagination1_response.text)
print('Headers: ', pagination1_response.headers)


#  Request 1.4.: pagination current page number > last available page

pagination2_params = {
    'limit': '49',
    'page': '3'
}

pagination2_response = requests.get(base_url + breeds_endpoint, params=pagination2_params)

print('\nRequest 1.4.: pagination current page number > last available page')
print('Status: ', pagination2_response.status_code)
print('Body: ', pagination2_response.text)
print('Headers: ', pagination2_response.headers)


print('\n2. FACT & LIST OF FACTS REQUESTS')

#Base endpoints for fact requests

fact_endpoint = '/fact'

list_of_facts_endpoint = '/facts'

# Request 2.1.: default random fact about cats

default_fact_response = requests.get(base_url + fact_endpoint)

print('\nRequest 2.1.: default random fact about cats')
print('Status: ', default_fact_response.status_code)
print('Body: ', default_fact_response.text)
print('Headers: ', default_fact_response.headers)

# Request 2.2.: random fact with max length

fact_max_length_params = {
    'max_length': '30',
}

fact_max_length_response = requests.get(base_url + fact_endpoint, params=fact_max_length_params)

print('\nRequest 2.2.: random fact with max length')
print('Status: ', fact_max_length_response.status_code)
print('Body: ', fact_max_length_response.text)
print('Headers: ', fact_max_length_response.headers)

# Request 2.3.:  full list of cat facts

full_fact_list_params = {
    'limit': '332',
}

full_fact_list_response = requests.get(base_url + list_of_facts_endpoint, params=full_fact_list_params)

print('\nRequest 2.3.: full list of cat facts')
print('Status: ', full_fact_list_response.status_code)
print('Body: ', full_fact_list_response.text)
print('Headers: ', full_fact_list_response.headers)

# Request 2.4.:  list of 3 cat facts with max length 40

three_facts_max_lenght_40_params = {
    'max_limit': '332',
    'limit': '40'
}

three_facts_max_lenght_40_response = requests.get(base_url + list_of_facts_endpoint, params=three_facts_max_lenght_40_params)

print('\nRequest 2.4.: list of 3 cat facts with max length 40')
print('Status: ', three_facts_max_lenght_40_response.status_code)
print('Body: ', three_facts_max_lenght_40_response.text)
print('Headers: ', three_facts_max_lenght_40_response.headers)