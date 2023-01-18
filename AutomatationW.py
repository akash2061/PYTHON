import pywhatkit

phone_number = "+91 xxxxxxxxxx"
print("Initialisiere Notfallprotokoll...")

pywhatkit.sendwhatmsg(phone_number, "hello using python!", 19, 31)
