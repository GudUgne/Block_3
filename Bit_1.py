# `pc_transaction.py` example
from bitcoin.rpc import RawProxy

p = RawProxy()  #sujungimas

# Pavyzdinis ID: "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"
txid = input("Iveskite transakcijos ID\n")

# First, retrieve the raw transaction in hex - is pavyzdzio visa tranzakcijos info
raw_tx = p.getrawtransaction(txid)

# Decode the transaction hex into a JSON object - is pavyzdzio
decoded_tx = p.decoderawtransaction(raw_tx)

i_sum = [] #saugojimo kintamasis
what_got = 0
# Retrieve each of the outputs from the transaction
for output in decoded_tx['vout']:
    i_sum.append(output['value']) #issaugo verte

print("Ka tranzakcijos gavejas gavo: ")
for ou in i_sum:
    print(ou)
    what_got += ou #ka gavo issaugo

whole_sum = 0 #bendra suma

# Calculating whole sum

for input in decoded_tx['vin']:     #susumuojami visi pervedimai kuriuos atliko
    out_index = input['vout']
    call_tx = p.getrawtransaction(input['txid'])
    decoded_call_tx = p.decoderawtransaction(call_tx)
    whole_sum += decoded_call_tx['vout'][out_index]['value']
print("Visa suma: ")
print(whole_sum)

tran_fee = whole_sum - what_got

print("Trasakcijos mokestis, kuri gavo mineris ")
print(tran_fee)
