import random

from modules import *
from utils.networks import *
from config import OKX_WRAPED_ID, LAYERZERO_WRAPED_NETWORKS
from settings import (LAYERSWAP_CHAIN_ID_FROM, ORBITER_CHAIN_ID_FROM, RHINO_CHAIN_ID_FROM,
                      OKX_DEPOSIT_NETWORK, SOURCE_CHAIN_MERKLY, SOURCE_CHAIN_ZERIUS)


async def get_client(account_number, private_key, network, proxy):
    client_instance = Client(account_number, private_key, network, proxy)
    return client_instance


def get_network_by_chain_id(chain_id):
    return {
        1: Arbitrum,
        2: Arbitrum_nova,
        3: Base,
        4: Linea,
        5: Manta,
        6: Polygon,
        7: Optimism,
        8: ScrollRPC,
        9: Polygon_ZKEVM,
        10: zkSyncEra,
        11: Zora,
        12: zkSyncEra
    }[chain_id]


async def swap_syncswap(account_number, private_key, network, proxy, **kwargs):
    worker = SyncSwap(await get_client(account_number, private_key, network, proxy))
    await worker.swap(**kwargs)


async def add_liquidity_syncswap(account_number, private_key, network, proxy):
    worker = SyncSwap(await get_client(account_number, private_key, network, proxy))
    await worker.add_liquidity()


async def withdraw_liquidity_syncswap(account_number, private_key, network, proxy):
    worker = SyncSwap(await get_client(account_number, private_key, network, proxy))
    await worker.withdraw_liquidity()


async def send_message_dmail(account_number, private_key, network, proxy):
    worker = Dmail(await get_client(account_number, private_key, network, proxy))
    await worker.send_message()


async def bridge_scroll(account_number, private_key, network, proxy):
    worker = Scroll(await get_client(account_number, private_key, network, proxy))
    await worker.deposit()


async def transfer_eth(account_number, private_key, network, proxy):
    worker = Scroll(await get_client(account_number, private_key, network, proxy))
    await worker.transfer_eth()


async def transfer_eth_to_myself(account_number, private_key, network, proxy):
    worker = Scroll(await get_client(account_number, private_key, network, proxy))
    await worker.transfer_eth_to_myself()


async def withdraw_scrool(account_number, private_key, network, proxy):
    worker = Scroll(await get_client(account_number, private_key, network, proxy))
    await worker.withdraw()


async def wrap_eth(account_number, private_key, network, proxy):
    worker = Scroll(await get_client(account_number, private_key, network, proxy))
    await worker.wrap_eth()


async def unwrap_eth(account_number, private_key, network, proxy):
    wrap = Scroll(await get_client(account_number, private_key, network, proxy))
    await wrap.unwrap_eth()


async def deploy_contract(account_number, private_key, network, proxy):
    wrap = Scroll(await get_client(account_number, private_key, network, proxy))
    await wrap.deploy_contract()


# async  def deploy_contract(account_number, private_key, network, proxy, *args, **kwargs):
#     wrap = ZkSync(account_number, private_key, network, proxy)
#     await wrap.deploy_contract(*args, **kwargs)


# async  def mint_deployed_token(account_number, private_key, network, proxy, *args, **kwargs):
#     mint = ZkSync(account_number, private_key, network, proxy)
#     await mint.mint_token()


async def deposit_layerbank(account_number, private_key, network, proxy):
    worker = LayerBank(await get_client(account_number, private_key, network, proxy))
    await worker.deposit()


async def withdraw_layerbank(account_number, private_key, network, proxy):
    worker = LayerBank(await get_client(account_number, private_key, network, proxy))
    await worker.withdraw()


async def enable_collateral_layerbank(account_number, private_key, network, proxy):
    worker = LayerBank(await get_client(account_number, private_key, network, proxy))
    await worker.enable_collateral()


async def disable_collateral_layerbank(account_number, private_key, network, proxy):
    worker = LayerBank(await get_client(account_number, private_key, network, proxy))
    await worker.disable_collateral()


async def swap_openocean(account_number, private_key, network, proxy, **kwargs):
    worker = OpenOcean(await get_client(account_number, private_key, network, proxy))
    await worker.swap(**kwargs)


async def swap_izumi(account_number, private_key, network, proxy):
    worker = Izumi(await get_client(account_number, private_key, network, proxy))
    await worker.swap()


async def swap_scrollswap(account_number, private_key, network, proxy):
    worker = ScrollSwap(await get_client(account_number, private_key, network, proxy))
    await worker.swap()


async def bridge_layerswap(account_number, private_key, _, proxy, **kwargs):
    chain_id_from = random.choice(LAYERSWAP_CHAIN_ID_FROM)

    if kwargs.get('help_okx'):
        network = get_network_by_chain_id(15)
    else:
        network = get_network_by_chain_id(chain_id_from)

    worker = LayerSwap(await get_client(account_number, private_key, network, proxy))
    await worker.bridge(chain_id_from,  **kwargs)


async def bridge_orbiter(account_number, private_key, _, proxy):
    chain_id_from = random.choice(ORBITER_CHAIN_ID_FROM)
    network = get_network_by_chain_id(chain_id_from)

    worker = Orbiter(await get_client(account_number, private_key, network, proxy))
    await worker.bridge(chain_id_from)


async def bridge_rhino(account_number, private_key, _, proxy):
    chain_id_from = random.choice(RHINO_CHAIN_ID_FROM)
    network = get_network_by_chain_id(chain_id_from)

    worker = Rhino(await get_client(account_number, private_key, network, proxy))
    await worker.bridge()


async def refuel_merkly(account_number, private_key, _, proxy):

    network = get_network_by_chain_id(LAYERZERO_WRAPED_NETWORKS[random.choice(SOURCE_CHAIN_MERKLY)])

    worker = Merkly(await get_client(account_number, private_key, network, proxy))
    await worker.refuel()


# async def send_message_l2telegraph(account_number, private_key, network, proxy):
#     worker = L2Telegraph(await get_client(account_number, private_key, network, proxy))
#     await worker.send_message()
#
#
# async def mint_and_bridge_l2telegraph(account_number, private_key, network, proxy):
#     worker = L2Telegraph(await get_client(account_number, private_key, network, proxy))
#     await worker.mint_and_bridge()


async def mint_zerius(account_number, private_key, network, proxy):
    worker = Zerius(await get_client(account_number, private_key, network, proxy))
    await worker.mint()


async def bridge_zerius(account_number, private_key, _, proxy):
    network = get_network_by_chain_id(LAYERZERO_WRAPED_NETWORKS[random.choice(SOURCE_CHAIN_ZERIUS)])

    worker = Zerius(await get_client(account_number, private_key, network, proxy))
    await worker.bridge()


async def create_omnisea(account_number, private_key, network, proxy):
    worker = Omnisea(await get_client(account_number, private_key, network, proxy))
    await worker.create()


async def create_safe(account_number, private_key, network, proxy):
    worker = GnosisSafe(await get_client(account_number, private_key, network, proxy))
    await worker.create()


async def okx_withdraw(account_number, private_key, network, proxy):
    worker = OKX(await get_client(account_number, private_key, network, proxy))
    await worker.withdraw()


async def okx_deposit(account_number, private_key, _, proxy):
    network = get_network_by_chain_id(OKX_WRAPED_ID[OKX_DEPOSIT_NETWORK])

    worker = OKX(await get_client(account_number, private_key, network, proxy))
    await worker.deposit()


async def okx_collect_from_sub(account_number, private_key, network, proxy):
    worker = OKX(await get_client(account_number, private_key, network, proxy))
    await worker.collect_from_sub()


MODULES = {
    "okx_withdraw": okx_withdraw,
    "bridge_layerswap": bridge_layerswap,
    "bridge_orbiter": bridge_orbiter,
    "bridge_rhino": bridge_rhino,
    "bridge_scroll": bridge_scroll,
    "add_liquidity_syncswap": add_liquidity_syncswap,
    "swap_izumi": swap_izumi,
    "swap_openocean": swap_openocean,
    "swap_syncswap": swap_syncswap,
    "swap_scrollswap": swap_scrollswap,
    "deposit_layerbank": deposit_layerbank,
    "enable_collateral_layerbank": enable_collateral_layerbank,
    "disable_collateral_layerbank": disable_collateral_layerbank,
    "withdraw_layerbank": withdraw_layerbank,
    "wrap_eth": wrap_eth,
    "create_omnisea": create_omnisea,
    # "mint_and_bridge_l2telegraph": mint_and_bridge_l2telegraph,
    "create_safe": create_safe,
    "refuel_merkly": refuel_merkly,
    "send_message_dmail": send_message_dmail,
    # "send_message_l2telegraph": send_message_l2telegraph,
    "transfer_eth": transfer_eth,
    "transfer_eth_to_myself": transfer_eth_to_myself,
    "mint_zerius": mint_zerius,
    "bridge_zerius": bridge_zerius,
    "unwrap_eth": unwrap_eth,
    "deploy_contract": deploy_contract,
    "withdraw_scroll": withdraw_scrool,
    "withdraw_liquidity_syncswap": withdraw_liquidity_syncswap,
    "okx_collect_from_sub": okx_collect_from_sub,
    "okx_deposit": okx_deposit,
}
