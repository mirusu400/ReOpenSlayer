from lib import CSNSocket
from lib import p8, p16, p32, p64, p8u, p16u, p32u, p64u, pf32, pf64, pstr

import random

# Supermode Packet
def opcode_26():
    csn = CSNSocket()
    payload = b"\x26"  # opcode 0x26

    payload += p16u(random.randint(0,255))  # ??
    return csn.inject_payload(payload)