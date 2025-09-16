# Basic Cybersecurity Check
def check_security(ip):
    if ip == "192.168.1.1":
        return "Threat Detected"
    return "Secure"
print(check_security("192.168.1.1"))
