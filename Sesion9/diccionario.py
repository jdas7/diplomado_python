import os
os.system("clear")

equipo = [
    "cisco",
    "cisco catalyst",
    "cisco catalyst2",
    "conexion"
]

modelo = {
    "819": "Router",
    "888": "Router",
    "2960": "Switch",
    "7700": "Switch",
    "conexion": [
        "Gateway : 192.168.0.1",
        "IP: 192.168.0.2",
        "Mask: 255.255.255.0"
    ]
}
print(equipo)
print(modelo)
print(modelo["conexion"][0])