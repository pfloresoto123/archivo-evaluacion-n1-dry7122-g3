def verificador_acl(acl):
	if acl >= 1 and acl <= 99:
		return "ACL Estandar"
	elif acl >= 100 and acl <= 199:
		return "ACL Extendida"
	else:
		return "El valor ingresado no corresponde a una lista de acceso"
def main():
	try:
		acl = int(input("Introduce el numero de ACL en IPV4"))
		acl_tipo = verificador_acl(acl)
		print("El tipo de ACL IPV4 es;", acl_tipo)
	except ValueError:
		print("Fallo; Introduce un numero valido, por favor")

if __name__ == "__main__":
	main()