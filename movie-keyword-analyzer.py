url = "https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt"

import requests

ratings_data = requests.get(url)

from kiwipiepy import Kiwi

kiwi = Kiwi()

data_list = []
for data in ratings_data.text.split("\n")[1:1001]:
    data_list.append(data.split("\t")[1])

nng_list = []
for data in data_list:
    for token1,token2,_,_ in kiwi.tokenize(data):
        if token2 == "NNG":
            nng_list.append(token1)

print(nng_list.count("영화"))

result_dict = {}
for nng in set(nng_list):
    result_dict[nng] = nng_list.count(nng)

print(sorted(result_dict.items(), key=lambda x : x[1], reverse=False))