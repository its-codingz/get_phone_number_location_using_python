import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = input("Enter Phone Number(With Country Code): ")

ch_number = phonenumbers.parse(number, "CH")
print("Country is:",geocoder.description_for_number(ch_number, "en"))

service_provider = phonenumbers.parse(number, "RO")
print("Service Provider:",carrier.name_for_number(service_provider, "en"))
