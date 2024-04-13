import socket


def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None


website = input("Enter Website [example.com]:\t")
ip_address = get_ip_address(website)

if ip_address:
    print(f"The IP address of {website} is: {ip_address}")
else:
    print(f"Could not resolve the IP address for {website}")
