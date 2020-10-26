import e3db

# Initialized each config by uncommenting the desired config
# Used code from the Tozny e3db gh page and documentation
token = '329b50a92e88460fd90189d43d77604cc354678040aadc704772a5fa60a9dd90'
client_name = 'clarence_creds'


# token = '84fd618af5608a1f23bc1a2eecf894b046b22d74ee9fde7690efd5f03af35d95'
# client_name = 'alicia_creds'


# token = '508c5631c0567974f523013fb073614718f40531c44d91e6f509b86cdd3db02c'
# client_name = 'bruce_creds'

public_key, private_key = e3db.Client.generate_keypair()

# Register your client
client_info = e3db.Client.register(token, client_name, public_key)

config = e3db.Config(
    client_info.client_id,
    client_info.api_key_id,
    client_info.api_secret,
    public_key,
    private_key
)

# To save this Configuration to disk, do the following:
config.write()

# Instantiate your client to communicate with TozStore
# Test instantiation once created.
client = e3db.Client(config())