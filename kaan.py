# Fill in this file with the code from parsing JSON exercise
import json
dosya=open("kaan.json","r")
json_dosya=json.load(dosya)
print("Adım    :",json_dosya["ad"])
print("Soyadım :",json_dosya["soyad"])
print("Hocam ben ödevden kaç aldım. Mezun olur muyum?")
print("Kimlik anahtar değeri : ",json_dosya["kimlik"])
