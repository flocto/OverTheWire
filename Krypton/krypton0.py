# Basic base64 decoding
import base64

msg = "S1JZUFRPTklTR1JFQVQ="

print(base64.b64decode(msg).decode())