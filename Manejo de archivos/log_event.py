
def logging_event(route, hour,  description):
    with open(route,'a',encoding='utf-8') as file:
        file.write(f"[{hour}], EVENT: {description}\n")


logging_event('bitacora.txt',"10:01 AM", "Startint conection")
logging_event('bitacora.txt',"10:15 AM", "Main User start program")
logging_event('bitacora.txt',"10:45 AM", "Main User End program")