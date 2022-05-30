import requests
import json
from pprint import pprint
apiKey = ''


# NOTE - much of these are paginated





# get balance
lookup_address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
balance_lookup_url = f'https://api.etherscan.io/api?module=account&action=balance&address={lookup_address}&tag=latest&apikey={apiKey}'
# fetch = requests.get(balance_lookup_url).json()
# pprint(fetch)
# exit()



# get transactions
# internal
lookup_address = '0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3'
internal_transactions_url = f'https://api.etherscan.io/api?module=account&action=txlistinternal&address={lookup_address}&startblock=0&endblock=2702578&sort=asc&apikey={apiKey}'
# fetch = requests.get(internal_transactions_url).json()
# pprint(fetch)
# exit()


# normal
lookup_address = '0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
normal_transactions_url = f'https://api.etherscan.io/api?module=account&action=txlist&address={lookup_address}&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey={apiKey}'
# fetch = requests.get(normal_transactions_url).json()
# pprint(fetch)
# exit()









# total ether supply
supply_url = f'https://api.etherscan.io/api?module=stats&action=ethsupply&apikey={apiKey}'

# Get ETHER Last Price
Current_Price_url = f'https://api.etherscan.io/api?module=stats&action=ethprice&apikey={apiKey}'









# pretty sure you can look up either ERC20 OR ERC721 BY LOOKING UP THE CONTRACT

# TOKEN TRANSFER by contract & address 
lookup_address = '0x4e83362442b8d1bec281594cea3050c8eb01311c'
lookup_contract = '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'
erc20_transfers_url = f'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={lookup_contract}&address={lookup_address}&page=1&offset=100&sort=asc&apikey={apiKey}'
# fetch = requests.get(erc20_transfers_url).json()
# pprint(fetch)
# exit()

# TOKEN TRANSFER by address (nft)
lookup_address = '0x4e83362442b8d1bec281594cea3050c8eb01311c'
erc20_transfers_url = f'https://api.etherscan.io/api?module=account&action=tokentx&address={lookup_address}&page=1&offset=100&sort=asc&apikey={apiKey}'
# fetch = requests.get(erc20_transfers_url).json()
# pprint(fetch)
# exit()

# TOKEN TRANSFER by contract (nft)     
lookup_contract = '0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2'
erc20_transfers_url = f'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={lookup_contract}&page=1&offset=100&sort=asc&apikey={apiKey}'
# fetch = requests.get(erc20_transfers_url).json()
# pprint(fetch)
# exit()





