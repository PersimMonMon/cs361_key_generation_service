from nacl.signing import SigningKey, VerifyKey
from nacl.encoding import Base64Encoder

def generate_ed25519_keypair():

    # generate key
    signing_key = SigningKey.generate()
    verify_key = signing_key.verify_key

    # encode to Base64 strings for transport
    private_b64 = signing_key.encode(encoder=Base64Encoder).decode("utf-8")
    public_b64 = verify_key.encode(encoder=Base64Encoder).decode("utf-8")

    return public_b64, private_b64