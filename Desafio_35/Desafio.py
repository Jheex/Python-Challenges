servidores = [
    {"nome": "SRV1", "ip": "192.168.0.6", "status": "ativo"},
    {"nome": "SRV2", "ip": "192.168.4.2", "status": "inativo"},
    {"nome": "SRV3", "ip": "192.168.9.3", "status": "ativo"}
]

print(servidores[1]["ip"])
print(servidores[2]["status"])

for i in range (0,3):
    print(f"{servidores[i]['nome']} - {servidores[i]['status']}")