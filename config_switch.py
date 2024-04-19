def generar_configuracion_switch():
    switch_config = {}
    preguntas = [
        "Nombre del equipo",
        "VLAN principal",
        "Interface asociada a la VLAN principal",
        "Interfaces de acceso (separadas por coma)",
        "Interfaces troncales VLAN de administración (separadas por coma)",
        "IP de administración",
        "IP default Gateway",
        "Usuario SSH",
        "Contraseña SSH",
        "Banner",
        "Contraseña enable secret",
        "¿Habilitar servicio de encriptación? (si/no)"
    ]

    for pregunta in preguntas:
        respuesta = input(f"{pregunta}: ")
        switch_config[pregunta] = respuesta if pregunta != "¿Habilitar servicio de encriptación? (si/no)" else respuesta.lower() == "si"

    configuracion_switch = [
        f"hostname {switch_config['Nombre del equipo']}",
        f"vlan {switch_config['VLAN principal']}",
        f"interface {switch_config['Interface asociada a la VLAN principal']}",
        "no shutdown",
        f"ip address {switch_config['IP de administración']} {switch_config['VLAN principal']}",
        f"ip default-gateway {switch_config['IP default Gateway']}",
        f"banner motd {switch_config['Banner']}",
        f"enable secret {switch_config['Contraseña enable secret']}",
        f"username {switch_config['Usuario SSH']} password {switch_config['Contraseña SSH']}",
        "service password-encryption" if switch_config['¿Habilitar servicio de encriptación? (si/no)'] else ""
    ]

    for interface in switch_config["Interfaces de acceso (separadas por coma)"].split(','):
        configuracion_switch.extend([
            f"interface {interface}",
            "switchport mode access",
            f"switchport access vlan {switch_config['VLAN principal']}",
            "no shutdown"
        ])

    for interface in switch_config["Interfaces troncales VLAN de administración (separadas por coma)"].split(','):
        configuracion_switch.extend([
            f"interface {interface}",
            "switchport mode trunk",
            f"switchport trunk allowed vlan {switch_config['VLAN principal']}",
            "no shutdown"
        ])

    return switch_config, configuracion_switch

def main():
    switch_config, configuracion_switch = generar_configuracion_switch()

    print("\nDatos ingresados:")
    for key, value in switch_config.items():
        print(f"{key}: {value}")

    print("\nConfiguración generada:")
    for comando in configuracion_switch:
        print(comando)

if __name__ == "__main__":
    main()