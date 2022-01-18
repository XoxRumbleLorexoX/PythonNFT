# import the OpenseaAPI object from the opensea module
from opensea import OpenseaAPI

# create an object to interact with the Opensea API (need an api key)
api = OpenseaAPI(apikey="YOUR APIKEY")

# fetch a single asset
contract_address = "0x495f947276749Ce646f68AC8c248420045cb7b5e"
token_id = "66406747123743156841746366950152533278033835913591691491127082341586364792833"
result = api.asset(asset_contract_address=contract_address, token_id=token_id)

# fetch multiple assets
result = api.assets(owner="0xce90a7949bb78892f159f428d0dc23a8e3584d75", limit=3)

# fetch a single contract
result = api.contract(asset_contract_address="0x495f947276749Ce646f68AC8c248420045cb7b5e")

# fetch a single collection
result = api.collection(collection_slug="cryptopunks")

# fetch multiple collections
result = api.collections(asset_owner="0xce90a7949bb78892f159f428d0dc23a8e3584d75", limit=3)

# fetch collection stats
result = api.collection_stats(collection_slug="cryptopunks")

# fetch multiple events
from opensea import utils as opensea_utils

period_start = opensea_utils.datetime_utc(2021, 11, 6, 14, 25)
period_end = opensea_utils.datetime_utc(2021, 11, 6, 14, 30)
result = api.events(
    occurred_after=period_start,
    occurred_before=period_end,
    limit=10,
    export_file_name="events.json",
)

# fetch multiple bundles
result = api.bundles(limit=2)
