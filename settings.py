"""
-------------------------------------------------OKX WITHDRAW-----------------------------------------------------------
    Choose withdrawal | deposit network. The software works only with ETH withdraw | deposit
    Don't forget to insert your API_KEYs
    
    1 - ETH-ERC20
    2 - ETH-Arbitrum One
    3 - ETH-zkSync Lite
    4 - ETH-Optimism
    5 - ETH-Starknet
    6 - ETH-zkSync Era
    7 - ETH-Linea
    
    OKX_WITHDRAW_NETWORK = 6
    OKX_AMOUNT_MIN = 0.009  ( ETH )
    OKX_AMOUNT_MAX = 0.012  ( ETH )
    OKX_DEPOSIT_NETWORK = 6
------------------------------------------------------------------------------------------------------------------------
"""
OKX_WITHDRAW_NETWORK = 6
OKX_AMOUNT_MIN = 0.004  # ETH
OKX_AMOUNT_MAX = 0.0045  # ETH
OKX_DEPOSIT_NETWORK = 6

"""
--------------------------------------------------SCROLL BRIDGE---------------------------------------------------------
    Official bridge on Scroll. Specify the minimum and maximum of deposit/withdraw in ETH
    
    SCROLL_DEP_MIN = 0.01 ( ETH )
    SCROLL_DEP_MAX = 0.02 ( ETH )
    SCROLL_WITHDRAW_MIN = 0.02 ( ETH )
    SCROLL_WITHDRAW_MAX = 0.02 ( ETH )
"""
SCROLL_DEP_MIN = 0.01  # ETH
SCROLL_DEP_MAX = 0.02  # ETH
SCROLL_WITHDRAW_MIN = 0.001  # ETH
SCROLL_WITHDRAW_MAX = 0.002  # ETH

"""
------------------------------------------------LayerSwap BRIDGE--------------------------------------------------------
    Check available tokens and networks for bridge before setting values. Works only with ETH
    Don't forget to insert your API_KEY
       
    Arbitrum = 1            Optimism = 7
    Arbitrum Nova = 2       Scroll = 8  
    Base = 3                Polygon ZKEVM = 9   
    Linea = 4               zkSync Era = 10      
    Manta = 5               Zora = 11  
    Polygon = 6             zkSync Lite = 12
    
    LAYERSWAP_CHAIN_ID_FROM(TO) = [2, 4, 16] | One network in list will be chosen
    LAYERSWAP_REFUEL means to add a little amount of native tokens to destination chain
"""
LAYERSWAP_CHAIN_ID_FROM = [2, 10]  # BRIDGE FROM
LAYERSWAP_CHAIN_ID_TO = [11]  # BRIDGE TO
LAYERSWAP_AMOUNT_MIN = 0.018  # ETH
LAYERSWAP_AMOUNT_MAX = 0.019  # ETH
LAYERSWAP_REFUEL = False  # True or False

"""
------------------------------------------------ORBITER BRIDGE----------------------------------------------------------
    Check available tokens and networks for bridge before setting values. Works only with ETH

    Arbitrum = 1            Optimism = 7
    Arbitrum Nova = 2       Scroll = 8  
    Base = 3                Polygon ZKEVM = 9   
    Linea = 4               zkSync Era = 10      
    Manta = 5               Zora = 11  
    Polygon = 6             zkSync Lite = 12

    ORBITER_CHAIN_ID_FROM(TO) = [2, 4, 11] | One network in list will be chosen
"""
ORBITER_CHAIN_ID_FROM = [2, 10, 11]  # BRIDGE FROM
ORBITER_CHAIN_ID_TO = [5]  # BRIDGE TO
ORBITER_AMOUNT_MIN = 0.009  # ETH
ORBITER_AMOUNT_MAX = 0.012  # ETH

"""
------------------------------------------------RHINO BRIDGE----------------------------------------------------------
    Check networks for bridge before setting values. Works only with ETH.

    Arbitrum = 1            Polygon = 6
    Arbitrum Nova = 2       Optimism = 7
    Base = 3                Scroll = 8  
    Linea = 4               Polygon ZKEVM = 9       
    Manta = 5               zkSync Era = 10            
                             
    RHINO_CHAIN_ID_FROM(TO) = [2, 3, 10] | One network in list will be chosen
"""
RHINO_CHAIN_ID_FROM = [2]  # BRIDGE FROM
RHINO_CHAIN_ID_TO = [10]  # BRIDGE TO
RHINO_AMOUNT_MIN = 0.001  # # ETH
RHINO_AMOUNT_MAX = 0.002  # # ETH


"""
----------------------------------------------AMOUNT CONTROL------------------------------------------------------------
    Exchange of all tokens(include LP tokens), except ETH, is 100% of the balance 
    You specify how much ETH in % will be exchanged for the tokens.
    OKX_DEPOSIT USE THIS AMOUNT.
    
    MIN_BALANCE set the amount of ETH on the account balance, enabling the software working.
    
    AMOUNT_MIN = 70 ( % ) of token balance 
    AMOUNT_MAX = 80 ( % ) of token balance 
    MIN_BALANCE = 0.001 ( ETH ) 
"""
AMOUNT_MIN = 50  # %
AMOUNT_MAX = 60  # %
MIN_BALANCE = 0.001  # ETH

"""
--------------------------------------------ADD LIQUIDITY TO DEX--------------------------------------------------------
    DEX include SyncSwap
    Liquidity is added only to interact with the new contract
    
    DEX_LP_MIN = 0.0005 ( ETH ) 
    DEX_LP_MAX = 0.0015 ( ETH )
    WITHDRAW_LP = Fasle # Perform withdrawal after deposit or not?
"""
DEX_LP_MIN = 0.0005  # ETH
DEX_LP_MAX = 0.001  # ETH
WITHDRAW_LP = False  # True or False

"""
---------------------------------------------LayerZero CONTROL----------------------------------------------------------
    Check website for working destination networks and min/max amount before setting values
    One network in list will be chosen
    
   *Arbitrum = 1         Kava = 15
    Astar = 2            Klaytn = 16
    Aurora = 3          *Linea = 17
    Avalanche = 4        Meter = 18
   *Base = 5             Metis = 19
    BNB chain = 6        Moonbeam = 20
    Canto = 7            Moonriver = 21
    Celo = 8            *Arbitrum Nova = 22
    Core = 9             OpBNB = 23
    Ethereum = 10       *Optimism = 24
    Fantom = 11         *Polygon = 25
    Fuse = 12           *Polygon ZKEVM = 26
    Gnosis = 13         *Scroll = 27
    Harmony = 14         Tenet = 28
                        *zkSync Era = 29
    
    SOURCE_CHAIN_ZERIUS = [27, 29] | One network in list will be chosen
    SOURCE_CHAIN_MERKLY = [27, 29] | One network in list will be chosen
    DESTINATION_MERKLY_AMOUNT = {
        1: (0.0016, 0.002), # Chain ID: (min amount, max amount) in destination native**
        2: (0.0002, 0.0005) # Chain ID: (min amount, max amount) in destination native**
    }
        
    *  - Сan be used as a source network 
    ** - Amount for merkly needs to be given in the native token of destination network. And also decrease the maximum
         amount by 5-10% to avoid errors. You can see maximum amount to refuel on https://minter.merkly.com/gas  
"""
SOURCE_CHAIN_ZERIUS = [27, 29]  # BRIDGE FROM
DESTINATION_ZERIUS = [1, 4, 8]

SOURCE_CHAIN_MERKLY = [27, 29]  # REFUEL FROM
DESTINATION_MERKLY_DATA = {
    2: (0.03, 0.05),  # Chain ID: (min amount , max amount) in destination native
    28: (0.04, 0.05)  # Chain ID: (min amount, max amount) in destination native
}

"""
------------------------------------------------TRANSFERS CONTROL-------------------------------------------------------
    Specify min/max ETH amount to send for random wallets
    
    TRANSFER_MIN = 0.00001 ( ETH ) 
    TRANSFER_MAX = 0.00005 ( ETH )
"""
TRANSFER_MIN = 0.00001  # ETH
TRANSFER_MAX = 0.00005  # ETH

"""
------------------------------------------------GENERAL SETTINGS--------------------------------------------------------

    TX_COUNT = [70, 80] | [min, max] number of transactions needed

    MAX_UNQ_CONTACT = False | enable/disable maximum number of unique contracts.
    (The software will run each module at least once, if the number of needed transactions allows it)

    SOFTWARE_MODE = 0 | this setting is used to set the mode of the software.
    1 - Parallel Mode (can`t deposit to OKX). A group of wallets works at the same time.
    0 - Consistently Mode (good with deposit and withdraw on OKX). Only 1 account work at the same time.
    
    WALLETS_TO_WORK = 0 | if the value differs from zero, the software works only with the specified wallets.
    0       = all wallets will work
    3       = only wallet #3 will work
    4, 20   = wallets #4 and #20 will work
    [5, 25] = wallets from 5 to 25 will work

    GAS_MULTIPLIER = 1.1 | multiply gas limit by this value
    UNLIMITED_APPROVE = False | unlimited approve for spender contract (2**256-1 of needed tokens)
"""
SOFTWARE_MODE = 0  # 0 / 1
WALLETS_TO_WORK = 0  # 0 / 4, 20 / [5, 25]
TX_COUNT = [70, 80]  # [min, max] will be chosen at random between
MAX_UNQ_CONTACTS = True  # True or False

'-------------------------------------------------GAS CONTROL----------------------------------------------------------'
GAS_CONTROL = False  # True or False
MAXIMUM_GWEI = 100  # Gwei
SLEEP_TIME_GAS = 120  # Second
GAS_MULTIPLIER = 1.1  # Coefficient

'------------------------------------------------RETRY CONTROL---------------------------------------------------------'
MAXIMUM_RETRY = 1  # Times
SLEEP_TIME_RETRY = 5  # Second

'------------------------------------------------PROXY CONTROL---------------------------------------------------------'
USE_PROXY = True  # True or False

'-----------------------------------------------APPROVE CONTROL--------------------------------------------------------'
UNLIMITED_APPROVE = False  # True or False

'-----------------------------------------------SLIPPAGE CONTROL-------------------------------------------------------'
SLIPPAGE_PERCENT = 0.987  # 0.5 = 0.5%, 1 = 1%, 2 = 2%

'------------------------------------------------SLEEP CONTROL---------------------------------------------------------'
SLEEP_MODE = False  # True or False
MIN_SLEEP = 60  # Second
MAX_SLEEP = 120  # Second

'--------------------------------------------------API KEYS------------------------------------------------------------'
# OKX API KEYS https://www.okx.com/ru/account/my-api
OKX_API_KEY = ""
OKX_API_SECRET = ""
OKX_API_PASSPHRAS = ""

# LAYERSWAP API KEY https://www.layerswap.io/dashboard
LAYERSWAP_API_KEY = ""

"""
----------------------------------------------AUTO-ROUTES CONTROL-------------------------------------------------------
    Select the required modules to interact with
    These settings will be used to generate a random auto-route if you enabled it  

    AUTO_ROUTES_MODULES_USING = {
        okx_withdraw                            : 1, | ( module name ) : ( 1 - enable, 0 - disable )
        bridge_layerswap                        : 0, | ( module name ) : ( 1 - enable, 0 - disable )
        bridge_rhino                            : 1, | ( module name ) : ( 1 - enable, 0 - disable )
        etc...
        
"""

AUTO_ROUTES_MODULES_USING = {
    'okx_withdraw'                        : 1,  # check OKX settings
    'bridge_layerswap'                    : 1,  # check LayerSwap settings
    'bridge_rhino'                        : 1,  # check Rhino settings
    'bridge_scroll'                       : 1,  # check Scroll settings
    'bridge_orbiter'                      : 1,  # check Orbiter settings
    'add_liquidity_syncswap'              : 1,  # USDC/WETH LP
    'deposit_layerbank'                   : 1,  # including withdraw
    'enable_collateral_layerbank'         : 1,  # including disable
    'swap_izumi'                          : 1,
    'swap_openocean'                      : 1,
    'swap_spacefi'                        : 1,
    'swap_syncswap'                       : 1,
    'swap_scrollswap'                     : 1,
    'deploy_contract'                     : 1,  # deploy your own contract
    'wrap_eth'                            : 1,  # including unwrap
    'create_omnisea'                      : 1,  # create new NFT collection
    'create_safe'                         : 1,  # create safe on chain
    'mint_zerius'                         : 1,  # mint non-free NFT
    'bridge_zerius'                       : 1,  # bridge last NFT
    'refuel_merkly'                       : 1,  # see LayerZero settings
    'send_message_dmail'                  : 1,
    'transfer_eth'                        : 1,  # transfer ETH to random address
    'transfer_eth_to_myself'              : 1,
    'withdraw_scroll'                     : 1,  # check Scroll settings
    'okx_deposit'                         : 1,  # check OKX settings
    'okx_collect_from_sub'                : 1   # collect your funds from subAccounts to main
}

"""
--------------------------------------------CLASSIC-ROUTES CONTROL------------------------------------------------------
    Select the required modules to interact with
    Here you can create your own route. For each step the software will select one module from the list.
    You can set None to skip a module during the route.
    See the AUTO-ROUTES settings for list of current modules.
    
    CLASSIC_ROUTES_MODULES_USING = [
        ['okx_withdraw'],
        ['bridge_layerswap', 'bridge_scroll', None],
        ['swap_scrollswap', 'swap_izumi'],
        ...
    ]
"""
CLASSIC_ROUTES_MODULES_USING = [
    ['okx_withdraw'],
    ['bridge_layerswap', 'bridge_scroll', 'bridge_orbiter'],
    ['enable_collateral_layerbank', 'deposit_layerbank', None],
    ['swap_izumi', 'swap_openocean'],
    ['refuel_merkly', 'swap_syncswap'],
    ['wrap_eth', 'swap_izumi'],
    ['swap_scrollswap'],
    ['withdraw_scroll'],
    ['okx_deposit']
]


