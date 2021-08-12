import phonenumbers
trackable = input("eneter the number to be tracked:> ")

from phonenumbers import geocoder
parsed_coutry = phonenumbers.parse(trackable, "CH")
print("the tracked number country is " + geocoder.description_for_number(parsed_coutry, "en"))

from phonenumbers import carrier
parsed_service = phonenumbers.parse(trackable, "RO")
print("the tracked service privider name is" + carrier.name_for_number(parsed_service, "en"))

print('''
HAPPY
TRACKING:)''')