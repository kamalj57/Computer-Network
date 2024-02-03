import ipaddress

def decimal_to_binary_ip(decimal_ip):
    try:
        ip_address = ipaddress.IPv4Address(decimal_ip)
    except ipaddress.AddressValueError as e:
        print(f"Error: {e}")
        print("Enter valid Decimal IP address")
        return
    binary_values = [bin(int(octet))[2:].zfill(8) for octet in str(ip_address).split('.')]
    for octet, binary in zip(str(ip_address).split('.'), binary_values):
        print(f"Decimal value : {octet}  Binary value : {binary}")
    print(f"\nBinary notation Ip address: {'.'.join(binary_values)}")
    return '.'.join(binary_values)

def binary_to_decimal_ip(binary_ip):
    binary_octets = binary_ip.split('.')   
    decimal_values = [str(int(octet, 2)) for octet in binary_octets]
    for octet, decimal in zip(binary_octets, decimal_values):
        print(f"Binary value: {octet}  Decimal value : {decimal}")
    print(f"\nDecimal IP address: {'.'.join(decimal_values)}")


decimal_ip = input("Enter the decimal dot notation of an IP address: ")
binary_ip = decimal_to_binary_ip(decimal_ip)

if binary_ip:
    print("\nConverting Binary to Decimal Ip address:")
    binary_to_decimal_ip(binary_ip)
