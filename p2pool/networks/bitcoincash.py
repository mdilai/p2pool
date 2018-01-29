from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['bitcoincash']
SHARE_PERIOD = 60 # seconds -- one minute
CHAIN_LENGTH = 3*24*60 # shares -- three days
REAL_CHAIN_LENGTH = 3*24*60 # shares -- three days
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'b826c0a51ddc2d2b'.decode('hex')
PREFIX = 'ac9a8fda9a911bce'.decode('hex')
P2P_PORT = 9349
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True # Set to False for solo mining or starting a new chain
WORKER_PORT = 9348
BOOTSTRAP_ADDRS = 'ml.toom.im woff.toom.im crypto.office-on-the.net siberia.mine.nu'.split(' ') # fixme, need more seed nodes
ANNOUNCE_CHANNEL = '#p2pool'
VERSION_CHECK = lambda v: None if 100000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3301
BLOCK_MAX_SIZE = 8000000
BLOCK_MAX_WEIGHT = 32000000
