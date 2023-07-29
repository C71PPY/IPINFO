import requests 

def get_ip_details(ip_address):
    api_url = f"http://ip-api.com/json/{ip_address}"
    reponse = requests.get(api_url)
    if reponse.status_code == 200:
        return reponse.json()
    else:
        return None

ip_address = input("Enter an IP address: ")
ip_details = get_ip_details(ip_address)

if ip_details:
    print("Ip: ", ip_details)
   

    input("Correct?: ")    