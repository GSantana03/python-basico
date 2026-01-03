
import datetime

def hora_atual():
    agora = datetime.datetime.now()
    return int(agora.strftime("%H"))

hora = hora_atual()
print("Hora atual:", hora)

if hora < 12:
    print("Bom dia!")
elif hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")