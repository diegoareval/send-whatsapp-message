import pywhatkit

def send_whatsapp_message():
	pywhatkit.sendwhatmsg("whatsap_number_with_code_area","your_message",11,6) # en el ultimo parametro se debe pasar hora y minutos


send_whatsapp_message()
