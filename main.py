import phonenumbers 
from  test import number  

from phonenumbers import geocoder 

ch_nmber = phonenumbers.parse(number,"Ch")
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier 

service_nmbr  = phonenumbers.parse(number,"ho")
print(carrier.name_for_number(service_nmbr, "en"))