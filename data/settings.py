"""
-----------------------------------------------------AMOUNT CONTROL-----------------------------------------------------
    Здесь вы определяете количество или % токенов для обменов, добавления ликвидности, депозитов и трансферов
    Софт берет % только для нативных токенов, остальные токены берутся на 100% от баланса

    Можно указать минимальную/максимальную сумму или минимальный/максимальный % от баланса

    Количество - (0.01, 0.02)
    Процент    - ("55", "60") ⚠️ Значения в скобках

"""

GLOBAL_LIMITER = {
    "Arbitrum": (0, 0),
    "Optimism": (0, 0),
    "Scroll": (0, 0),
    "Linea": (0, 0),
    "zkSync": (0, 0),
    "Ethereum": (0, 0),
}  # указывать в нативном токене каждой сети, не в баксах!

SWAP_AMOUNT = ('80', '90')  # Применяется для свапов, настройка работает для первого свапа, второй на 100%
DACKIESWAP_AMOUNT = ('3', '4')  # Применяется для свапов на DackieSwap, slippage выключен, будьте аккуратны
LANDINGS_AMOUNT = ('80', '90')  # Применяется для депозитов на лендинг, вывод на 100%
TRANSFER_AMOUNT = (0.00001, 0.00002)  # Применяется для трансферов эфира на свой или рандомный адрес
WRAPS_AMOUNT = (0.0001, 0.0002)  # Применяется для Wrap и Unwrap ETH
STAKE_AMOUNT = (0.0001, 0.0002)  # Применяется для Stake TIA в сети Celestia

ARBITRUM_TIA_SWAP_AMOUNT = ('100', '100')  # Применяется для cвапов ETH -> TIA на Jumper
MANTA_TIA_SWAP_AMOUNT = ('40', '40')  # Применяется для cвапов ETH -> TIA на OpenOcean
ONEINCH_SWAP_AMOUNT = ('85', '90')  # Применяется для cвапов BNB -> ZBC на 1inch. 0.001 BNB удерживается для комиссии. Минимум 0.004 BNB ~ 50 ZBC (1 бридж из Nautilus)
REFUEL_NAUTILUS_AMOUNT = ('100', '100')  # Применяется для рефьюла ZBC из BNB Chain -> Nautilus

ELIXIR_AMOUNT = (0.0285, 0.03)  # Применяется для стейкинга на лендинг https://www.elixir.xyz/
"""
-------------------------------------------------------CEX CONTROL------------------------------------------------------
    Выберите сети/суммы для вывода и ввода с CEX. Не забудьте вставить API ключи в general_settings.py.
    Депозиты и выводы работают только со спотовым балансом на бирже.

    1 - ETH-ERC20                  13 - METIS-Metis         25 - USDC-Arbitrum One             37 - USDV-BSC                        
    2 - ETH-Arbitrum One           14 - CORE-CORE           26 - USDC-Avalanche C-Chain        38 - ARB-Arbitrum One                        
    3 - ETH-Optimism               15 - CFX-CFX_EVM         27 - USDC-Optimism                 39 - MAV-Base                        
    4 - ETH-zkSync Era             16 - KLAY-Klaytn         28 - USDC-Polygon                  40 - MAV-zkSync Era                        
    5 - ETH-Linea                  17 - FTM-Fantom          29 - USDC-Optimism (Bridged)       41 - OP-Optimism
    6 - ETH-Base                   18 - MATIC-Polygon       30 - USDC-Polygon (Bridged)        42 - INJ-Injective
    7 - AVAX-Avalanche C-Chain     19 - USDT-Arbitrum One   31 - USDC-BSC                      43 - TIA-Celestia   
    8 - BNB-BSC                    20 - USDT-Avalanche      32 - USDC-ERC20                    44 - NTRN-Neutron   
    9 - BNB-OPBNB                  21 - USDT-Optimism       33 - STG-Arbitrum One              45 - ETH-Manta 
    10 - CELO-CELO                 22 - USDT-Polygon        34 - STG-BSC                       46 - ETH-BSC   
    11 - GLMR-Moonbeam             23 - USDT-BSC            35 - STG-Avalanche C-Chain         47 - SOL-Solana 
    12 - MOVR-Moonriver            24 - USDT-ERC20          36 - STG-Fantom                    48 - OKB-X Layer 

    ⚠️ Софт сам отнимает комиссию от суммы депозита, при работе с нативными токенами ⚠️

    Сумма в количестве  - (0.01, 0.02)
    Сумма в процентах   - ("10", "20") ⚠️ Значения в кавычках.

    OKX_WITHDRAW_DATA | Каждый список - один модуль для вывода из биржи. Примеры работы указаны ниже:
                        Для каждого вывода указывайте [сеть вывода, (мин и макс сумма)]

    OKX_DEPOSIT_DATA | Каждый список - один модуль для депозита на биржу. Примеры работы указаны ниже:
                       Для каждого вывода указывайте [сеть депозита, (мин и макс сумма), лимитерX, лимитерY]

                       Настройка лимитного вывода на биржу. Указывать в $USD
                       лимитерX - это минимальный баланс на аккаунте, чтобы софт начал процесс вывода
                       лимитерY - это мин. и макс. сумма, которая должна остаться на балансе после вывода.
                       Если сумма депозита будет оставлять баланс на аккаунте больше 2-го значения, софт не будет
                       пытать сделать сумму депозита больше или меньше указанной в DEPOSIT_DATA

    Примеры рандомизации вывода с биржи:

    [[17, (1, 1.011)], None] | Пример установки None, для случайного выбора (выполнение действия или его пропуск)
    [[2, (0.48, 0.5)], [3, (0.48, 0.5)]] | Пример установки двух сетей, софт выберет одну случайную.

    Дополнительно к верхним примерам, для депозита на биржу поддерживается режим поиска баланса:
        [(2, 3, 4), (0.001, 0.002), 0, (0, 0)] | Пример указания нескольких сетей, cофт выберет сеть с наибольшим
                                                 балансом.

    CEX_BALANCER_CONFIG = [
        [Х, Y, Z],
    ]

    «Х» - Софт проверит количество этого токена в этой сети, согласно списку в группе «CEX CONTROL»
    Если количество токена меньше значения «Y», то происходит вывод с биржи «Z» токена «Х» в сумме равной разнице
    между балансом и желаемом количестве токенов на балансе.
    «Z» значение - биржа для вывода. 1 - OKX, 2 - BingX, 3 - Binance, 4 - Bitget. Можно указать несколько в скобках,
    софт выберет одну биржу. Модуль (make_balance_to_average).

    Пример:
    CEX_BALANCER_CONFIG = [
        [20, 5, 1],
    ]

    Софт проверяет USDT в сети Avalanche. Если меньше 5, а на балансе 2.1 то софт докидывает с биржи 2.9 USDT
"""

WAIT_FOR_RECEIPT_CEX = True  # Если True, будет ждать получения средств во входящей сети после депозита/вывода
COLLECT_FROM_SUB_CEX = True  # Если True, будет собирать средства до/после депозита/вывода с субов на мейн аккаунт

'------------------------------------------------------Fee Support-----------------------------------------------------'

FEE_SUPPORT_DATA = {
    2: (0.0011, 0.0012),
    3: (0.0007, 0.0009),
    5: (0.0007, 0.0009)
}  # сети, где софт проверит балансы и выведет указанную сумму в сеть, с наибольшим балансом, если баланс там - меньше указанной суммы

FEE_SUPPORT_MIN_WITHDRAW = (3.6, 4)  # мин. разница между балансом аккаунта и суммой для вывода, чтобы софт сделал вывод
FEE_SUPPORT_CEXS = [1]  # биржи, участвующие в выводах. Если указать несколько, софт выберет случайную

TRANSFER_COSMOS_CEXS = {
    'Neutron': [1],
    'Injective': [2],
    'Celestia': [1],
}  # 1 - Bitget, 2 - OKX. Текущая настройка трансферит на выбранную биржу, можно указать несколько

'----------------------------------------------------------OKX---------------------------------------------------------'

OKX_WITHDRAW_DATA = [
    [[2, (0.0011, 0.0012)], [3, (0.0007, 0.0009)], [5, (0.0007, 0.0009)]],
]

OKX_DEPOSIT_DATA = [
    [(2, 3, 5, 6, 42), ('100', '100'), 0, (0.4, 0.5)],
]

'---------------------------------------------------------BingX--------------------------------------------------------'

BINGX_WITHDRAW_DATA = [
    [8, (0.004, 0.00411)],
]

BINGX_DEPOSIT_DATA = [
    [37, ('100', '100'), 0, (0, 0)],
]

'--------------------------------------------------------Binance-------------------------------------------------------'

BINANCE_WITHDRAW_DATA = [
    [44, (0.4, 0.45)],
]

BINANCE_DEPOSIT_DATA = [
    [37, ('100', '100'), 0, (0, 0)],
]

'---------------------------------------------------------BitGet-------------------------------------------------------'

BITGET_WITHDRAW_DATA = [
    [43, ('80', '100')],
]

BITGET_DEPOSIT_DATA = [
    [(23, 43), ('100', '100'), 0, (0, 0)],
]

'--------------------------------------------------------Customs-------------------------------------------------------'

# OKX CUSTOM WITHDRAW

OKX_CUSTOM_WITHDRAW_1 = [
    [[2, ('80', '100')], [3, ('80', '100')], [6, ('80', '100')]],
]

OKX_CUSTOM_WITHDRAW_2 = [
    [42, ('80', '100')]
]

OKX_CUSTOM_WITHDRAW_3 = [
    [2, (0.0011, 0.0012)],
]

OKX_CUSTOM_WITHDRAW_4 = [
    [[2, ('80', '100')], [3, ('80', '100')], [5, ('80', '100')], [6, ('80', '100')]],
]

# BITGET CUSTOM WITHDRAW

BITGET_CUSTOM_WITHDRAW_1 = [
    [43, ('80', '100')],
]

BITGET_CUSTOM_WITHDRAW_2 = [
    [23, ('80', '100')],
    [8, (0.01, 0.011)]
]

BITGET_CUSTOM_WITHDRAW_3 = [
    [[2, ('80', '100')], [3, ('80', '100')], [6, ('80', '100')]],
]

BITGET_CUSTOM_WITHDRAW_4 = [
    [23, ('80', '100')],
]

# BINANCE CUSTOM WITHDRAW

BINANCE_CUSTOM_WITHDRAW_1 = [
    [44, (0.4, 0.45)],
]

BINANCE_CUSTOM_WITHDRAW_2 = [
    [23, ('80', '100')]
]

BINANCE_CUSTOM_WITHDRAW_3 = [
    [43, ('80', '100')],
]

BINANCE_CUSTOM_WITHDRAW_4 = [
    [8, (0.01, 0.011)]
]

'--------------------------------------------------------Control-------------------------------------------------------'

CEX_BALANCER_CONFIG = [
    [1, 0.005, 3]
]

"""
-----------------------------------------------------BRIDGE CONTROL-----------------------------------------------------
    Проверьте руками, работает ли сеть на сайте. (Софт сам проверит, но зачем его напрягать?)
    Не забудьте вставить API ключ для LayerSwap снизу. Для каждого моста поддерживается уникальная настройка
       
        Arbitrum = 1                    zkSync Era = 11     X Layer = 56     
        Arbitrum Nova = 2               Zora = 12           Taiko = 57
        Base = 3                        Ethereum = 13
        Linea = 4                       Avalanche = 14
        Manta = 5                       BNB Chain = 15
        Polygon = 6                     Metis = 26        
        Optimism = 7                    OpBNB = 28
        Scroll = 8                      Mantle = 29
        Starknet = 9                    ZKFair = 45
        Polygon zkEVM = 10              Blast = 49
                                           
    Сумма в количестве  - (0.01, 0.02)
    Сумма в процентах   - ("10", "20") ⚠️ Значения в кавычках
    
    ACROSS_TOKEN_NAME | Укажите токен для бриджа. Поддерживаются: ETH, BNB, MATIC, USDC, USDC.e (Bridged), USDT. 
                        Если у бриджа указано 2 токена в скобках см. BUNGEE_TOKEN_NAME, то бридж сможет делать бриджи
                        между разными токенами. Справа от параметра, для каждого бриджа указаны доступные токены.
                        
    ACROSS_AMOUNT_LIMITER | Настройка лимитных бриджей. Указывать в $USD
                            1 значение - это минимальный баланс на аккаунте, чтобы софт начал процесс бриджа
                            2 значение - это мин. и макс. сумма, которая должна остаться на балансе после бриджа
                            Если сумма для бриджа будет оставлять баланс на аккаунте больше второго значения,
                            софт не будет пытать сделать сумму бриджа больше или меньше указанной
                    
    BUNGEE_ROUTE_TYPE | Установка своего роута для совершения транзакции, по умолчанию (0) - самый лучший. 
                        1-Across   3-Celer     5-Stargate   7-Synapse      9-Hop
                        2-CCTP     4-Connext   6-Socket     8-Symbiosis    10-Hyphen   
    
    BRIDGE_SWITCH_CONTROL | Позволяет использовать один и тот же бридж два раза. По умолчанию каждая цифра закреплена за
                            за своим бриджем (см. значения снизу), чтобы поменять эту настройку
                            ориентируйтесь зависимостями снизу и указывайте для каждого моста свое значение настройки,
                            по которой он будет работать.
                            
                            1-ACROSS     3-LAYERSWAP    5-ORBITER     7-RELAY
                            2-BUNGEE     4-NITRO        6-OWLTO       8-RHINO
                               
"""

WAIT_FOR_RECEIPT_BRIDGE = True  # Если True, будет ждать получения средств во входящей сети после бриджа

'-----------------------------------------------------Native Bridge----------------------------------------------------'

NATIVE_CHAIN_ID_FROM = [3]                 # Исходящая сеть
NATIVE_CHAIN_ID_TO = [13]                  # Входящая сеть
NATIVE_BRIDGE_AMOUNT = (0.001, 0.001)      # (минимум, максимум) (% или кол-во)
NATIVE_TOKEN_NAME = 'ETH'
NATIVE_AMOUNT_LIMITER = 0, (0.3, 0.4)

'--------------------------------------------------------Across--------------------------------------------------------'

ACROSS_CHAIN_ID_FROM = [1, 3, 4, 7]         # Исходящая сеть
ACROSS_CHAIN_ID_TO = [1, 3, 4, 7]           # Входящая сеть
ACROSS_BRIDGE_AMOUNT = (0.01, 0.02)         # (минимум, максимум) (% или кол-во)
ACROSS_TOKEN_NAME = 'ETH'
ACROSS_AMOUNT_LIMITER = 0, (0.3, 0.4)

'--------------------------------------------------------Bungee--------------------------------------------------------'

BUNGEE_CHAIN_ID_FROM = [1, 3, 4, 7, 8]         # Исходящая сеть
BUNGEE_CHAIN_ID_TO = [13]                   # Входящая сеть
BUNGEE_BRIDGE_AMOUNT = ('100', '100')       # (минимум, максимум) (% или кол-во)
BUNGEE_TOKEN_NAME = ('ETH', 'ETH')          # ETH, BNB, MATIC, USDC, USDC.e, USDT
BUNGEE_ROUTE_TYPE = 0                       # см. BUNGEE_ROUTE_TYPE
BUNGEE_AMOUNT_LIMITER = 0, (0.3, 0.4)

'-------------------------------------------------------LayerSwap------------------------------------------------------'

LAYERSWAP_CHAIN_ID_FROM = [11]               # Исходящая сеть
LAYERSWAP_CHAIN_ID_TO = [3]                  # Входящая сеть
LAYERSWAP_BRIDGE_AMOUNT = ('95', '97')     # (минимум, максимум) (% или кол-во)
LAYERSWAP_TOKEN_NAME = ('ETH', 'ETH')     # ETH, USDC, USDC.e
LAYERSWAP_AMOUNT_LIMITER = 0, (0.3, 0.4)


'--------------------------------------------------------Nitro---------------------------------------------------------'

NITRO_CHAIN_ID_FROM = [1, 3, 4, 7]                   # Исходящая сеть
NITRO_CHAIN_ID_TO = [1, 3, 4, 7]                    # Входящая сеть
NITRO_BRIDGE_AMOUNT = (0.01, 0.02)         # (минимум, максимум) (% или кол-во)
NITRO_TOKEN_NAME = ('ETH', 'ETH')          # ETH, USDC, USDT
NITRO_AMOUNT_LIMITER = 0, (0, 0)

'-------------------------------------------------------Orbiter--------------------------------------------------------'

ORBITER_CHAIN_ID_FROM = [1, 3, 4, 7]           # Исходящая сеть
ORBITER_CHAIN_ID_TO = [8]                   # Входящая сеть
ORBITER_BRIDGE_AMOUNT = ('70', '80')              # (минимум, максимум) (% или кол-во)
ORBITER_TOKEN_NAME = 'ETH'
ORBITER_AMOUNT_LIMITER = 0, (0.3, 0.4)

'--------------------------------------------------------Owlto---------------------------------------------------------'

OWLTO_CHAIN_ID_FROM = [1, 3, 4, 7]                 # Исходящая сеть
OWLTO_CHAIN_ID_TO = [1, 3, 4, 7]                    # Входящая сеть
OWLTO_BRIDGE_AMOUNT = (0.01, 0.03)       # (минимум, максимум) (% или кол-во)
OWLTO_TOKEN_NAME = 'ETH'
OWLTO_AMOUNT_LIMITER = 0, (0.3, 0.4)

'--------------------------------------------------------Relay---------------------------------------------------------'

RELAY_CHAIN_ID_FROM = [1, 3, 4, 7]                # Исходящая сеть
RELAY_CHAIN_ID_TO = [8]                   # Входящая сеть
RELAY_BRIDGE_AMOUNT = (0.001, 0.001)      # (минимум, максимум) (% или кол-во)
RELAY_TOKEN_NAME = 'ETH'
RELAY_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Rhino---------------------------------------------------------'

RHINO_CHAIN_ID_FROM = [1, 3, 4, 7]                # Исходящая сеть
RHINO_CHAIN_ID_TO = [8]                 # Входящая сеть
RHINO_BRIDGE_AMOUNT = ('100', '100')           # (минимум, максимум) (% или кол-во)
RHINO_TOKEN_NAME = ('ETH', 'ETH')       # ETH, BNB, MATIC, USDC, USDT
RHINO_AMOUNT_LIMITER = 0, (0.3, 0.4)

'--------------------------------------------------------Rango---------------------------------------------------------'

RANGO_CHAIN_ID_FROM = [1, 3, 4, 7]          # Исходящая сеть
RANGO_CHAIN_ID_TO = [8]                     # Входящая сеть
RANGO_BRIDGE_AMOUNT = ('100', '100')        # (минимум, максимум) (% или кол-во)
RANGO_TOKEN_NAME = ('ETH', 'ETH')           # ETH, BNB, MATIC, USDC, USDT
RANGO_AMOUNT_LIMITER = 0, (0.3, 0.4)

'------------------------------------------------------XYfinance-------------------------------------------------------'

XYFINANCE_CHAIN_ID_FROM = [1, 3, 4, 7]      # Исходящая сеть
XYFINANCE_CHAIN_ID_TO = [8]                 # Входящая сеть
XYFINANCE_BRIDGE_AMOUNT = ('100', '100')    # (минимум, максимум) (% или кол-во)
XYFINANCE_TOKEN_NAME = ('ETH', 'ETH')       # ETH, BNB, MATIC, USDC, USDT
XYFINANCE_AMOUNT_LIMITER = 0, (0.3, 0.4)

BRIDGE_SWITCH_CONTROL = {
    1: 1,  # ACROSS
    2: 2,  # BUNGEE
    3: 3,  # LAYERSWAP
    4: 4,  # NITRO
    5: 5,  # ORBITER
    6: 6,  # OWLTO
    7: 7,  # RELAY
    8: 8,  # RHINO
    10: 10,  # RANGO
    11: 11,  # XYFINANCE
}

"""
---------------------------------------------OMNI-CHAIN CONTROL---------------------------------------------------------
    Проверьте руками, работают ли сети на сайте. (Софт сам проверит, но зачем его напрягать?)
       
        Arbitrum = 1                  Gnosis = 17                        Polygon = 33              
        Arbitrum Nova = 2             Harmony = 18                       Polygon zkEVM = 34
        Astar = 3                     Horizen = 19                       Scroll = 35
        Aurora = 4                    Kava = 20                          ShimmerEVM = 36
        Avalanche = 5                 Klaytn = 21                        Telos = 37
        BNB = 6                       Linea = 22                         TomoChain = 38 
        Base = 7                      Loot = 23                          Tenet = 39
        Canto = 8                     Manta = 24                         XPLA = 40
        Celo = 9                      Mantle = 25                        Zora = 41  
        Conflux = 10                  Meter = 26                         opBNB = 42
        CoreDAO = 11                  Metis = 27                         zkSync = 43
        DFK = 12                      Moonbeam = 28                      Beam = 44
        Ethereum = 13                 Moonriver = 29                     inEVM = 45
        Fantom = 14                   OKX = 30                           Rarible = 46
        Fuse = 15                     Optimism = 31                      Blast = 49
        Goerli = 16                   Orderly = 32                       Mode = 50
                                                                         
        Celestia = 51
        Neutron = 52
        Injective = 53
        Nautilus = 54
        Solana = 55
    
    Все настройки показаны на примерах, похожие по названию настройки - работают аналогично
    
    USENEXUS_AMOUNT | Определяет какую сумму нужно отправлять через мост. Поддерживается % и количественное указание
    USENEXUS_CHAINS | Выберите чейны, между которыми будут производиться бриджи
    USENEXUS_TOKENS | Выберите монеты, между которыми будут производиться свапы 
                      Доступны: ETH, TIA.n, WETH, INJ, USDT, USDC, ZBC

        Софт сам определит, где сейчас находиться баланс и сделает бридж по указанной логике в вышеуказанных настройках    
        
        Токены указывать в таком же порядке, как и чейны. Условно USENEXUS_CHAINS = [5, 6] и
        USENEXUS_TOKENS = ['USDC', 'USDT'] будет означать, что для чейна №5 будет USDC, а для №6 USDT
        Можно указывать любое количество сетей, софт будет делать бриджи в рандомную сеть из списка. 
        
        Варианты работы всех бриджей:
        
        1) Круговой бридж с заходом из сети. Указав USENEXUS_CHAINS = [1, (52, 53)], софт сделает бридж 
        из сети '1' в левую из внутреннего списка '7', далее будут бриджи между сетями из внутреннего списка, для 
        активации этого режима нужно запустить модуль один раз и указать нужное количество бриджей USENEXUS_BRIDGE_COUNT.
        Последний бридж будет в сеть '1'. Можно указать больше двух сетей внутри скобок, первый бридж будет также в
        левую сеть. Также можно указать несколько начальных сетей, пример: USENEXUS_CHAINS = [1, 2, (7, 22)],
        тогда софт начнет и завершит в случайной сети.
        
        2) Режим касания каждой сети. Указав USENEXUS_CHAINS = [1, 7, 22] и USENEXUS_BRIDGE_COUNT равное количеству
        указанных сетей в USENEXUS_CHAINS и запустив модуль 1 раз, софт попытается сделать бридж из каждой указанной
        сети. При указании USENEXUS_BRIDGE_COUNT > USENEXUS_CHAINS, после попыток бриджа из каждой сети, софт будет
        выбирать рандомную сеть
        
        3) Режим строгого маршрута. Указав USENEXUS_CHAINS = (1, 7, 22) и запустив модуль 1 раз, софт будет делать
        бриджи по очереди из каждой указанной сети (i) в следующую (i + 1). USENEXUS_BRIDGE_COUNT должно быть строго
        равно длине USENEXUS_CHAINS - 1 
        
        4) Режим случайных сетей. Указав USENEXUS_CHAINS = [1, 7, 22] и USENEXUS_BRIDGE_COUNT равное 1, запустив модуль
        1 раз, софт найдет где сейчас находиться баланс и сделает 1 бридж в другую случайную сеть из списка.
        
    USENEXUS_BRIDGE_COUNT | Количество бриджей для одного запуска bridge_usenexus или bridge_hyperlane_merkly.
    Если указать списком, то софт выберет случайное количество. Пример: USENEXUS_BRIDGE_COUNT = [4, 6, 8], 
    будет выбрано одно из этих значений, не случайное между, а именно одно из этих значений.
    
    HYPERLANE_SEARCH_CHAINS | Настройка для поиска балансов во время прогона объемов, для врапов, трансферов, апрувов
                              Укажите между какими чейнами софт будет искать балансы.
    
    JUMPER_ROUTE_TYPE | Установка своего роута для совершения транзакции, по умолчанию (0) - самый лучший. 
            1 - Across          3 - Circle CCTP     5 - CelerIM   7 - Stargate      9 - Hop
            2 - Allbridge       4 - Celer cBridge   6 - Connext   8 - Symbiosis     10 - Hyphen
         
    SRC_CHAIN_L2PASS = [27, 29] | Одна из сетей будет выбрана (REFUEL/BRIDGE NFT/TOKENS)        

    DST_CHAIN_L2PASS_REFUEL = {
        1: (0.0016, 0.002), # Chain ID: (минимум, максимум) в нативном токене входящей сети**
        2: (0.0002, 0.0005) 
    } 

    Сумму нужно указывать в нативном токене входящей сети. Указывайте на 10% меньше от лимита, указанного на сайте,
    во избежания ошибок работы технологии LayerZero. Смотреть лимиты можно здесь: 
            1) L2Pass    - https://l2pass.com/refuel  
            2) nogem.app - https://nogem.app
            3) Merkly    - https://minter.merkly.com/gas  
            4) Whale     - https://whale-app.com/refuel
            5) Zerius    - https://zerius.io/refuel
            
"""
WAIT_FOR_RECEIPT = True      # Если True, то софт будет ждать получения средств во входящей сети, перед след. модулем
WAIT_FOR_RECEIPT_L0 = False  # Если True, аналогично как WAIT_FOR_RECEIPT, но для LayerZero модулей
ALL_DST_CHAINS = False       # Если True, то модули refuel и bridge попытаются сделать транзакцию в каждую входящую сеть
SEARCH_CHAINS = [1, 6, 7, 22, 31, 45]  # Сети, в которых софт будет искать нативку для разбавляющих транз
POSSIBLE_TOKENS = ['USDT', 'ETH', 'INJ']

'-------------------------------------------------------BRIDGES--------------------------------------------------------'

'------------------------------------------------------Superform-------------------------------------------------------'

SUPERFORM_CHAIN_FROM = [1, 7, 31]
SUPERFORM_CHAIN_WITHDRAW = [1, 7, 31]
SUPERFORM_VAULTS_TO = {
    1: ['UNjRpwsi2GF-0zFRap7nt', '5SUdXKtvBYkCyCxnLfwlM', '0mwur7ruIQk03CvTgl1t5', 'dNZCSfoPwId9TRrPYsjol'],
    7: ['VYKkjy_0XXzgZqeqkZKFo', 'Azq9mj0OQXjxUEFnvljUM', '-Sur6c_8I5ujr6FunDxWJ'],
    31: ['FZuZKa74BkF7AlFM7_7lo', 'T-LK2lQOYDIgNbNOim0pd', 'yJyG7wP3VdGsrd5ADzevO', 'FebJZszw5zx0HBSHe6lqK']
}
SUPERFORM_TOKEN_NAME = ['ETH', 'WETH']
SUPERFORM_AMOUNT = (0.002, 0.003)
SUPERFROM_EXCLUDE_ROUTE = 1  # 1 - LayerZero, 2 - Hyperlane, 3 - Wormhole

'-------------------------------------------------------UseNexus-------------------------------------------------------'

USENEXUS_CHAINS = (51, 52, 1, 52, 51)
USENEXUS_TOKENS = ['TIA.n', 'TIA.n', 'TIA.n', 'TIA.n', 'TIA.n']
USENEXUS_AMOUNT = ('100', '100')
USENEXUS_BRIDGE_COUNT = 1
USENEXUS_RUN_TIMES = 1
USENEXUS_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Merkly--------------------------------------------------------'

MERKLY_CHAINS = [1, 7, 31]
MERKLY_TOKENS = ['ETH', 'ETH', 'ETH']  # для BNB Chain и Polygon - WETH
MERKLY_AMOUNT = ('100', '100')
MERKLY_BRIDGE_COUNT = 1
MERKLY_RUN_TIMES = 1
MERKLY_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------inEVM---------------------------------------------------------'

INEVM_CHAINS = [53, 45]
INEVM_TOKENS = ['INJ', 'INJ']
INEVM_AMOUNT = ('100', '100')
INEVM_BRIDGE_COUNT = 1
INEVM_RUN_TIMES = 1
INEVM_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Renzo---------------------------------------------------------'

RENZO_CHAINS = [1, 7]
RENZO_TOKENS = ['ezETH', 'ezETH']
RENZO_AMOUNT = ('100', '100')
RENZO_BRIDGE_COUNT = 1
RENZO_RUN_TIMES = 1
RENZO_AMOUNT_LIMITER = 0, (0, 0)

'-------------------------------------------------------Nautilus-------------------------------------------------------'

NAUTILUS_CHAINS = [54, 6]
NAUTILUS_TOKENS = ['USDT', 'USDT']
NAUTILUS_AMOUNT = ('100', '100')
NAUTILUS_BRIDGE_COUNT = 1
NAUTILUS_RUN_TIMES = 1
NAUTILUS_AMOUNT_LIMITER = 0, (0, 0)

'-------------------------------------------------------Stargate-------------------------------------------------------'

STARGATE_CHAINS = [1, 31, (6, 33)]
STARGATE_TOKENS = ['USDT', 'USDT']  # USDT, USDC, WETH, ZBC
STARGATE_AMOUNT = ('100', '100')
STARGATE_BRIDGE_COUNT = 4
STARGATE_RUN_TIMES = 4
STARGATE_AMOUNT_LIMITER = 0, (0, 0)

'-----------------------------------------------------SquidRouter------------------------------------------------------'

SQUIDROUTER_CHAINS = [1, 22, 31, 7]
SQUIDROUTER_TOKENS = ['ETH', 'ETH', 'ETH', 'ETH']
SQUIDROUTER_AMOUNT = ('100', '100')
SQUIDROUTER_BRIDGE_COUNT = 1
SQUIDROUTER_RUN_TIMES = 1
SQUIDROUTER_AMOUNT_LIMITER = 0, (0, 0)
SQUIDROUTER_SWAP_TOKENS = ['WETH', 'USDC']

'-------------------------------------------------------deBridge-------------------------------------------------------'

DEBRIDGE_CHAINS = [1, 22, 31, 7]
DEBRIDGE_TOKENS = ['ETH', 'ETH', 'ETH', 'ETH']
DEBRIDGE_AMOUNT = ('100', '100')
DEBRIDGE_BRIDGE_COUNT = 1
DEBRIDGE_RUN_TIMES = 1
DEBRIDGE_AMOUNT_LIMITER = 0, (0, 0)
DEBRIDGE_SWAP_TOKENS = ['WETH', 'USDC']

'--------------------------------------------------------Rango---------------------------------------------------------'

RANGO_CHAINS = [1, 22, 31, 7]
RANGO_TOKENS = ['ETH', 'ETH', 'ETH', 'ETH']
RANGO_AMOUNT = ('100', '100')
RANGO_BRIDGE_COUNT = 1
RANGO_RUN_TIMES = 1
RANGO_AMOUNT_LIMITER2 = 0, (0, 0)
RANGO_SWAP_TOKENS = ['WETH', 'USDC']

'--------------------------------------------------------Jumper--------------------------------------------------------'

JUMPER_CHAINS = [1, 22, 31, 7]
JUMPER_TOKENS = ['ETH', 'ETH', 'ETH', 'ETH']
JUMPER_AMOUNT = ('100', '100')
JUMPER_BRIDGE_COUNT = 1
JUMPER_RUN_TIMES = 1
JUMPER_ROUTE_TYPE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
JUMPER_AMOUNT_LIMITER = 0, (0, 0)
JUMPER_SWAP_TOKENS = ['WETH', 'USDC']

'--------------------------------------------------------L2Pass--------------------------------------------------------'

SRC_CHAIN_L2PASS = [1, 7, 22, 31]         # Исходящая сеть для L2Pass
DST_CHAIN_L2PASS_NFT = [9, 17, 28]        # Входящая сеть для L2Pass Mint NFT
DST_CHAIN_L2PASS_REFUEL = {
    9: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    17: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    28: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
}

'-------------------------------------------------------nogem.app------------------------------------------------------'

SRC_CHAIN_NOGEM = [1, 7, 22, 31]             # Исходящая сеть для nogem.app
DST_CHAIN_NOGEM_NFT = [9, 17, 28]       # Входящая сеть для nogem.app Mint NFT
DST_CHAIN_NOGEM_REFUEL = {
    9: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    17: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    28: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
}

'--------------------------------------------------------Merkly--------------------------------------------------------'

SRC_CHAIN_MERKLY = [1, 7, 22, 31]         # Исходящая сеть для Merkly
DST_CHAIN_MERKLY_NFT = [9, 17, 28]     # Входящая сеть для Merkly Mint NFT
DST_CHAIN_MERKLY_REFUEL = {
     9: (0.00001, 0.00002),        # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
     17: (0.00001, 0.00002),        # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
     28: (0.00001, 0.00002),        # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
}

'--------------------------------------------------------Whale---------------------------------------------------------'

SRC_CHAIN_WHALE = [1, 7, 22, 31]          # Исходящая сеть для Whale
DST_CHAIN_WHALE_NFT = [9, 17, 28]     # Входящая сеть для Whale Mint NFT
DST_CHAIN_WHALE_REFUEL = {
    9: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    17: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    28: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
}

'-------------------------------------------------------Zerius---------------------------------------------------------'

SRC_CHAIN_ZERIUS = [1, 7, 22, 31]          # Исходящая сеть для Zerius
DST_CHAIN_ZERIUS_NFT = [9, 17, 28]      # Входящая сеть для Zerius Mint NFT
DST_CHAIN_ZERIUS_REFUEL = {
    9: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    17: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    28: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
}

'-------------------------------------------------------Bungee---------------------------------------------------------'

SRC_CHAIN_BUNGEE = [1, 7, 22, 31]          # Исходящая сеть для Bungee
DST_CHAIN_BUNGEE_REFUEL = {
    9: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
    17: (0.00001, 0.00002),  # Chain ID: (минимум, максимум) в нативном токене входящей сети (кол-во)
}

'---------------------------------------------------Merkly Hyperlane---------------------------------------------------'

SRC_CHAIN_MERKLY_HYPERLANE = [1, 7, 31]   # Исходящая сеть для Merkly Hyperlane
DST_CHAIN_MERKLY_HYPERLANE = [9, 17]   # Входящая сеть для Merkly Hyperlane
MERKLY_HYP_TOKENS_AMOUNTS = ([2, 3], [1, 2])   # Кол-во токенов для минта и бриджа на Merkly через Hyperlane

'----------------------------------------------------Nogem Hyperlane---------------------------------------------------'

SRC_CHAIN_NOGEM_HYPERLANE = [1, 7, 31]   # Исходящая сеть для Nogem Hyperlane
DST_CHAIN_NOGEM_HYPERLANE = [9, 17]   # Входящая сеть для Nogem Hyperlane
NOGEM_HYP_TOKENS_AMOUNTS = ([2, 3], [1, 2])   # Кол-во токенов для минта и бриджа на Nogem через Hyperlane

'-------------------------------------------------------GetMint--------------------------------------------------------'

SRC_CHAIN_GETMINT_HYPERLANE = [1, 7, 31]   # Исходящая сеть для GetMint
DST_CHAIN_GETMINT_HYPERLANE = [9, 17, 33]   # Входящая сеть для GetMint

'--------------------------------------------------------Womex---------------------------------------------------------'

SRC_CHAIN_WOMEX_HYPERLANE = [1, 7, 31]   # Исходящая сеть для GetMint
DST_CHAIN_WOMEX_HYPERLANE = [9, 17, 33]   # Входящая сеть для GetMint

"""
------------------------------------------------------CUSTOM SWAP-------------------------------------------------------
    
    CUSTOM_SWAP_DATA | Указывается для каждой сети где вы планируете запускать свап. Работает по текущей RPC, 
                       которую необходимо указать в роуте. см. пример в настройке маршрута 
                       Имеет 4 значения:
                        1 - сумма для свапа,
                        2 - использование одного приложения при свапах,
                        3 - включить двойной свап,
                        4 - приложения, между которыми софт должен будет выбирать
    
        Ключи от приложения указаны в первом столбике, доступные к использованию во втором столбике
        
            1: swap_1inch                     Arbitrum = [1, 2, 5]
            2: swap_odos                      Base = [1, 2, 5, 6]
            3: swap_syncswap                  Linea = [2, 3, 4, 7]
            4: swap_izumi                     Scroll = [2, 3, 4, 9, 13, 14]
            5: swap_uniswap                   zkSync = [2, 3, 4, 6, 7, 8]
            6: swap_maverick                  Optimism = [1, 2, 8]
            7: swap_pancake                   Solana = [10]
            8: swap_woofi                     inEVM = [11]
            9: swap_ambient                   Polygon ZKEVM = [12]
            10: swap_jupiter                  BNB Chain = [1, 2]
            11: swap_dackieswap               Polygon = [1, 2]
            12: swap_quickswap                   
            13: swap_sushiswap                   
            14: swap_spacefi                     

"""

CUSTOM_SWAP_DATA = {  # cумма свапа, использовать туже cвапалку, двойной свап, какие свапалки использовать
    'Ethereum'              : (('55', '60'), True, False, [1, 2]),
    'Arbitrum'              : (('55', '60'), True, False, [1, 2, 5]),
    'Base'                  : (('55', '60'), True, False, [1, 2, 5, 6]),
    'Linea'                 : (('55', '60'), True, False, [2, 3, 4, 7]),
    'Scroll'                : (('55', '60'), True, False, [2, 3, 4, 9, 13, 14]),
    'zkSync'                : (('55', '60'), True, False, [2, 3, 4, 6, 7, 8]),
    'Optimism'              : (('55', '60'), True, False, [1, 2, 8]),
    'Solana'                : (('55', '60'), True, False, [10]),
    'inEVM'                 : (('55', '60'), True, False, [11]),
    'Polygon ZKEVM'         : (('55', '60'), True, False, [12]),
    'BNB Chain'             : (('55', '60'), True, False, [1, 2]),
    'Polygon'               : (('55', '60'), True, False, [1, 2]),
}

'------------------------------------------------------Сollector-------------------------------------------------------'

COLLECTOR_MIN_AMOUNTS = {
    'WETH': 0.001,
    'USDT': 1,
    'USDC': 1,
}  # минимальная сумма токена для запуска свапа, если токен не указан, по умолчанию стоит - 1 единица токена, не баксов

COLLECTOR_DATA = {
    'Arbitrum': {
        "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        'USDC': '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        'USDT': '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9',
        'fUSDC': '0x4CFA50B7Ce747e2D61724fcAc57f24B748FF2b2A',
        'TIA.n': '0xD56734d7f9979dD94FAE3d67C7e928234e71cD4C',
        'STG': '0x6694340fc020c5E6B96567843da2df01b2CE1eb6',
        'USDV': '0x323665443CEf804A3b5206103304BD4872EA4253',
    },
    "Optimism": {
        "WETH": "0x4200000000000000000000000000000000000006",
        "OP": "0x4200000000000000000000000000000000000042",
        "USDC": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
        "USDT": "0x94b008aA00579c1307B0EF2c499aD98a8ce58e58",
        "USDC.e": "0x7F5c764cBc14f9669B88837ca1490cCa17c31607",
        "DAI": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        'STG': '0x296F55F8Fb28E498B858d0BcDA06D955B2Cb3f97',
        'USDV': '0x323665443CEf804A3b5206103304BD4872EA4253',
    },
    "zkSync": {
        "WETH": "0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91",
        'MAV': '0x787c09494Ec8Bcb24DcAf8659E7d5D69979eE508',
        "USDC": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4",
        "USDC.e": "0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4",
        "USDT": "0x493257fD37EDB34451f62EDf8D2a0C418852bA4C",
    },
    "Base": {
        "WETH": "0x4200000000000000000000000000000000000006",
        'USDC': '0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA',
        'USDC.e': '0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA',
        'STG': '0xE3B53AF74a4BF62Ae5511055290838050bf764Df',
        'MAV': '0x64b88c73A5DfA78D1713fE1b4c69a22d7E0faAa7',
    },
    "Linea": {
        "WETH": "0xe5D7C2a44FfDDf6b295A15c148167daaAf5Cf34f",
        "USDT": "0xA219439258ca9da29E9Cc4cE5596924745e12B93",
        "USDC": "0x176211869cA2b568f2A7D4EE941E073a821EE1ff",
        'STG': '0x808d7c71ad2ba3FA531b068a2417C63106BC0949'
    },
    "Scroll": {
        "WETH": "0x5300000000000000000000000000000000000004",
    },
}

"""
-----------------------------------------------------OTHER SETTINGS-----------------------------------------------------
    
    FULL_CUSTOM_SWAP_DATA | ([исх. токен, вх. токен для обмена], (сумма от и до), сеть запуска, (лимитерХ, лимитерY)),
                        будет выбрана сеть с наибольшим балансом токена для обмена, второй запуск будет производить
                        обратный свап. Если будете свапать из/в нативку, то вместо адреса указывайте название нативной
                        монеты. Пример: ['ETH', '0x123']

    MINTFUN_CONTRACTS | Список контрактов для минта в выбранной сети (GLOBAL NETWORK)
    MINTFUN_MINT_COUNT | Количество минтов для MINTFUN_CONTRACTS, софт выберет случайное число внутри указанного списка 


"""

DBK_BRIDGE_AMOUNT = (0.00005, 0.0001)

MINTFUN_CONTRACTS = {
    'Optimism': [
        '0xEb3805E0776180A783aD7f637e08172D40240311',
    ],
    'Zora': [
        '0x'
    ],
    'Base': [
        '0x'
    ],
}

MINTFUN_MINT_COUNT = [1, 1]  # от и до

CUSTOM_SLEEP_1 = (10, 20)  # (от, до) секунд сна для модуля custom_sleep1
CUSTOM_SLEEP_2 = (10, 20)  # (от, до) секунд сна для модуля custom_sleep2
CUSTOM_SLEEP_3 = (10, 20)  # (от, до) секунд сна для модуля custom_sleep3

FULL_CUSTOM_SWAP_DATA1 = (['ETH', '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9'], (0.001, 0.001), 1)
FULL_CUSTOM_SWAP_DATA2 = (['0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9', 'ETH'], ('100', '100'), 1)
FULL_CUSTOM_SWAP_DATA3 = (['0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9', '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'], ('100', '100'), 1)

"""
-------------------------------------------------CLASSIC-ROUTES CONTROL-------------------------------------------------

--------------------------------------------------------HELPERS---------------------------------------------------------        

    okx_withdraw                     # смотри CEX CONTROL
    bingx_withdraw                   # смотри CEX CONTROL
    binance_withdraw                 # смотри CEX CONTROL
    bitget_withdraw                  # смотри CEX CONTROL
    
    okx_custom_withdraw_1            # кастомный вывод для работы c большим количеством модулей в маршруте.
    okx_custom_withdraw_2               см. CEX CONTROL(Custom)
    okx_custom_withdraw_3               
    okx_custom_withdraw_4               
    bitget_custom_withdraw_1            
    bitget_custom_withdraw_2            
    bitget_custom_withdraw_3            
    bitget_custom_withdraw_4            
    binance_custom_withdraw_1           
    binance_custom_withdraw_2           
    binance_custom_withdraw_3           
    binance_custom_withdraw_4           
    
    bridge_native                    # смотри BRIDGE CONTROL
    bridge_across                    # смотри BRIDGE CONTROL
    bridge_bungee                    # смотри BRIDGE CONTROL
    bridge_layerswap                 # смотри BRIDGE CONTROL
    bridge_nitro                     # смотри BRIDGE CONTROL
    bridge_owlto                     # смотри BRIDGE CONTROL
    bridge_orbiter                   # смотри BRIDGE CONTROL
    bridge_relay                     # смотри BRIDGE CONTROL
    bridge_rhino                     # смотри BRIDGE CONTROL    
    bridge_rango_simple              # смотри BRIDGE CONTROL
    bridge_xyfinance                 # смотри BRIDGE CONTROL

    okx_deposit                      # ввод средств на биржу + сбор средств на субАккаунтов на основной счет
    bingx_deposit                    # ввод средств на биржу + сбор средств на субАккаунтов на основной счет
    binance_deposit                  # ввод средств на биржу + сбор средств на субАккаунтов на основной счет
    bitget_deposit                   # ввод средств на биржу + сбор средств на субАккаунтов на основной счет
        
    make_balance_to_average          # уравнивает ваши балансы на аккаунтах (см. CEX_BALANCER_CONFIG) 
    rhino_recovery_funds             # вывод средств из Rhino.fi, работает по вашим по настройкам из BRIDGE CONTROL
    
-------------------------------------------------------HYPERLANE--------------------------------------------------------            
    
    swap_eth_to_tia_arb      # свап ETH -> TIA.n в сети Arbitrum на https://jumper.exchange/
    swap_tia_to_eth_arb      # свап TIA.n -> ETH в сети Arbitrum. см. ARBITRUM_TIA_SWAP_AMOUNT
    
    swap_eth_to_tia_manta    # свап ETH -> TIA.n в сети Manta на https://app.openocean.finance/swap/manta/USDT/TIA
    swap_tia_to_eth_manta    # свап TIA.n -> ETH в сети Manta. см. MANTA_TIA_SWAP_AMOUNT
        
    swap_bnb_to_zbc_bsc      # свап BNB -> ZBC в сети BNB Chain на https://app.1inch.io/#/56/simple/swap/BNB/ZBC
    swap_zbc_to_bnb_bsc      # свап ZBC -> BNB в сети BNB Chain. см. ONEINCH_SWAP_AMOUNT
    
    smart_swap_in_for_bridging  # свап ETH/BNB на TIA/ZBC для совершения бриджей, с поиском баланса в ARB, MANTA, BSC
    smart_swap_out_for_bridging # свап TIA/ZBC на ETH/BNB для пополения на биржу, с поиском баланса в ARB, MANTA, BSC
    
    bridge_getmint           # минт и бридж NFT через Hyperlane на https://getmint.io/
    bridge_womex             # минт и бридж NFT через Hyperlane на https://womex.io/
    bridge_usenexus          # бриджи на https://www.usenexus.org/. См. OMNI-CHAIN CONTROLE
    bridge_inevm             # бриджи на https://bridge.inevm.com/. См. OMNI-CHAIN CONTROLE
    bridge_renzo             # бриджи на https://bridge.inevm.com/. См. OMNI-CHAIN CONTROLE
    bridge_stargate          # бриджи на https://stargate.finance/. См. OMNI-CHAIN CONTROLE
    bridge_superform         # депозиты в лендинги через Hyperlane на https://app.superform.xyz/
    withdraw_superform       # вывод из случайного пула на https://app.superform.xyz/. см. SUPERFORM_CHAIN_WITHDRAW
    
    bridge_nautilus          # бриджи на https://www.nautilusbridge.com/. См. OMNI-CHAIN CONTROLE
    refuel_nautilus          # бридж ZBC из BNB Chain в Nautilus, для пополнения нативкой. см. REFUEL_NAUTILUS_AMOUNT
    
    bridge_nogem_hnft        # минт и бридж NFT на nogem.app через Hyperlane 
    bridge_nogem_htoken      # минт и бридж токенов на nogem.app через Hyperlane 
    bridge_hyperlane_nft     # минт и бридж NFT на Merkly через Hyperlane 
    bridge_hyperlane_token   # минт и бридж токенов на Merkly через Hyperlane 
    bridge_hyperlane_merkly  # бридж токенов (большие объемы) внутри EVM сетей на Merkly через Hyperlane

--------------------------------------------------------JUMPER----------------------------------------------------------            
    
    bridge_jumper                    # бриджи на https://jumper.exchange/. См. OMNI-CHAIN CONTROLE
    swap_jumper                      # свапы на https://jumper.exchange/. См. OMNI-CHAIN CONTROLE 
    mint_jumper                      # минт NFT on https://app.mercle.xyz/jumperpfp/events
    claim_task1_jumper               # клейм первого квеста на https://app.mercle.xyz/jumperpfp/events    
    claim_task2_jumper               # клейм второго квеста на https://app.mercle.xyz/jumperpfp/events    

-------------------------------------------------------DEBRIDGE---------------------------------------------------------            
    
    bridge_debridge                  # бриджи на https://app.debridge.finance/. См. OMNI-CHAIN CONTROLE
    swap_debridge                    # свапы на https://app.debridge.finance/. См. OMNI-CHAIN CONTROLE 
    
------------------------------------------------------SQUIDROUTER-------------------------------------------------------            
    
    bridge_squidrouter               # бриджи на https://app.squidrouter.com/. См. OMNI-CHAIN CONTROLE
    swap_squidrouter                 # свапы на https://app.squidrouter.com/. См. OMNI-CHAIN CONTROLE
    mint_squid_scholar_nft           # минт NFT на https://squidschool.squidrouter.com/.
---------------------------------------------------------RANGO----------------------------------------------------------            
    
    bridge_rango                     # бриджи на https://rango.exchange/. См. OMNI-CHAIN CONTROLE
    swap_rango                       # свапы на https://rango.exchange/. См. OMNI-CHAIN CONTROLE
    
-------------------------------------------------------LAYERZERO--------------------------------------------------------            
    
    bridge_l2pass                    # bridge последней NFT on L2Pass
    bridge_nogem                     # bridge последней NFT on nogem.app
    bridge_merkly                    # bridge последней NFT on Merkly
    bridge_whale                     # bridge последней NFT on Whale
    bridge_zerius                    # bridge последней NFT on Zerius
        
    refuel_l2pass                    # смотри OMNI-CHAIN CONTROL
    refuel_nogem                     # смотри OMNI-CHAIN CONTROL
    refuel_merkly                    # смотри OMNI-CHAIN CONTROL
    refuel_whale                     # смотри OMNI-CHAIN CONTROL
    refuel_zerius                    # смотри OMNI-CHAIN CONTROL
    refuel_bungee                    # смотри OMNI-CHAIN CONTROL

--------------------------------------------------------LANDINGS--------------------------------------------------------            

    deposit_aave_simple              # депозит в AAVE по номеру RPC. Доступны: Arbitrum, Base, Optimism, Scroll, BNB 
    withdraw_aave_simple             # вывод из AAVE по номеру RPC
    deposit_basilisk_simple          # депозит в Basilisk по номеру RPC. Доступны: zkSync   
    withdraw_basilisk_simple         # вывод из Basilisk по номеру RPC   
    deposit_eralend_simple           # депозит в Eralend по номеру RPC. Доступны: zkSync                                                 
    withdraw_eralend_simple          # вывод из Eralend по номеру RPC               
    deposit_keom_simple              # депозит в Keom по номеру RPC. Доступны: Polygon zkEVM               
    withdraw_keom_simple             # вывод из Keom по номеру RPC               
    deposit_layerbank_simple         # депозит в Layerbank по номеру RPC. Доступны: Linea                   
    withdraw_layerbank_simple        # вывод из Layerbank по номеру RPC                  
    deposit_moonwell_simple          # депозит в Moonwell по номеру RPC. Доступны: Base                
    withdraw_moonwell_simple         # вывод из Moonwell по номеру RPC                   
    deposit_seamless_simple          # депозит в Seamless по номеру RPC. Доступны: Base                     
    withdraw_seamless_simple         # вывод из Seamless по номеру RPC                   
    deposit_zerolend_simple          # депозит в Zerolend по номеру RPC. Доступны: zkSync                    
    withdraw_zerolend_simple         # вывод из Zerolend по номеру RPC                   

---------------------------------------------------------OTHER----------------------------------------------------------            
    
    Для каждого их этих модулей софт делает проверку баланса в чейнах из SEARCH_CHAINS, а для свапов также использует
    POSSIBLE_TOKENS, чтобы понимать какие токены искать. После того как софт проверит балансы, он запустит этот
    модуль в сети где найдет баланс нужного для транзакции токена.
    
    custom_sleep1                    # кастомный сон во время маршрута, см. CUSTOM_SLEEP_1
    custom_sleep2                    # кастомный сон во время маршрута, см. CUSTOM_SLEEP_2
    custom_sleep3                    # кастомный сон во время маршрута, см. CUSTOM_SLEEP_3
    
    custom_swap                      # свап в разных сетях, привязанных по RPCs. см. CUSTOM_SWAP_DATA
    full_custom_swap1                # кастомный свап. см. FULL_CUSTOM_SWAP_DATA1                    
    full_custom_swap2                # кастомный свап. см. FULL_CUSTOM_SWAP_DATA2                    
    full_custom_swap3                # кастомный свап. см. FULL_CUSTOM_SWAP_DATA3                    
    
    collector_eth                    # giga коллектор всех сетей по настройке COLLECTOR_DATA
    deposit_elixir                   # стейкинг на https://www.elixir.xyz/apothecary. см. ELIXIR_AMOUNT
    mint_dbk                         # бридж и минт NFT в DBK чейне. Бридж будет сделан, если в DBK нехватает средств. 
    smart_organic_swaps              # двойные свапы на дексах
    smart_organic_landings           # депозит и вывод на лендингах
    smart_check_in                   # checkIn на сайте https://owlto.finance/confirm
    smart_wrap_eth                   # wrap ETH (WRAP_AMOUNT)
    smart_unwrap_eth                 # unwrap ETH на 100% от баланса
    smart_rubyscore                  # голосование на RubyScore
    smart_mintfun                    # mint NFT на Mint.Fun. см. MINTFUN_CONTRACTS и MINTFUN_MINT_COUNT
    smart_dmail                      # отправка сообщения через Dmail на рандомный Web2 адрес
    smart_transfer_eth               # переводит (TRANSFER_AMOUNT) ETH на случайный адрес
    smart_transfer_cosmos            # переводит (TRANSFER_AMOUNT) нативки на случайный адрес в Cosmos сети
    smart_transfer_eth_to_myself     # переводит (TRANSFER_AMOUNT) ETH на ваш адрес
    smart_transfer_cosmos_to_cex     # переводит (TRANSFER_AMOUNT) нативки на ваш CEX адрес
    smart_stake_tia                  # стейкинг TIA случайному валидатору на https://wallet.keplr.app/chains/celestia
    smart_random_approve             # рандомный approve в EVM сети с большим балансом из SEARCH_CHAINS

    Выберите необходимые модули для взаимодействия
    Вы можете создать любой маршрут, софт отработает строго по нему. Для каждого списка будет выбран один модуль в
    маршрут, если софт выберет None, то он пропустит данный список модулей. 
    Список модулей сверху.
    
    CLASSIC_ROUTES_MODULES_USING = [
        ['okx_withdraw'],
        ['binance_withdraw'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token'],
        ['bridge_hyperlane_merkly'],
        ['swap_eth_to_tia_arb'],
        ['bridge_usenexus'],
        ...
    ]
    
    
    Сети для работы с разными проектами, позволят сделать вам маршрут сразу во всех активных сетях под ретро.
    Пример заполнения (сети указаны снизу):
    
    CLASSIC_ROUTES_MODULES_USING = [
        ['full_custom_swap:3'], # после знака ':' номер сети для работы
    ]
    
    Arbitrum = 1            Polygon zkEVM = 10
    Arbitrum Nova = 2       zkSync Era = 11
    Base = 3                Zora = 12
    Linea = 4               Ethereum = 13
    Manta = 5               inEVM = 47
    Polygon = 6             Solana = 55
    Optimism = 7            Taiko = 57
    Scroll = 8
    
"""

CLASSIC_ROUTES_BLOCKS_COUNT = [7, 7]  # Количество блоков к работе для одного аккаунта. Указывайте от 1 до 7 блоков

ADD_FEE_SUPPORT_FOR_TXS = True  # софт добавит в маршрут первым модулем fee_support_withdraw. см. FEE_SUPPORT_DATA

CLASSIC_ROUTES_MODULES_USING = [
    # при наличии блоков (круглые скобки для маршрута), софт будет их мешать для каждого аккаунта
    ['okx_custom_withdraw_4'],  # см. OKX_CUSTOM_WITHDRAW_4
    (  # блок работы с Jumper (4 случайных бриджа ETH между Arbitrum, Optimism, Base, Linea
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_jumper'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['fee_support_withdraw_for_base'],
        ['mint_jumper'],
        ['claim_task1_jumper'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_jumper'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_jumper'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_jumper'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_getmint', 'bridge_womex', 'bridge_hyperlane_nft', 'bridge_hyperlane_token', None],
    ),
    (  # блок работы с SquidRouter (4 случайных бриджа ETH между Arbitrum, Optimism, Base, Linea
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['bridge_l2pass', 'bridge_nogem', 'bridge_merkly', 'bridge_zerius', None, None],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_squidrouter'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_squidrouter'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_squidrouter'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_squidrouter'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_getmint', 'bridge_womex', 'bridge_hyperlane_nft', 'bridge_hyperlane_token', None],
    ),
    (  # блок работы с deBridge (4 случайных бриджа ETH между Arbitrum, Optimism, Base, Linea
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['bridge_l2pass', 'bridge_nogem', 'bridge_merkly', 'bridge_zerius', None, None],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_debridge'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_debridge'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_debridge'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_debridge'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_getmint', 'bridge_womex', 'bridge_hyperlane_nft', 'bridge_hyperlane_token', None],
    ),
    (  # блок работы с Merkly (4 случайных бриджа ETH между Arbitrum, Optimism, Base
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['bridge_l2pass', 'bridge_nogem', 'bridge_merkly', 'bridge_zerius', None, None],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_hyperlane_merkly'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_hyperlane_merkly', 'bridge_superform'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_hyperlane_merkly'],
        ['smart_organic_swaps', 'smart_organic_landings', None],
        ['bridge_hyperlane_merkly', None],
        ['bridge_getmint', 'bridge_womex', 'bridge_hyperlane_nft', 'bridge_hyperlane_token', None],
    ),
    (  # блок работы с inEVM (4 бриджа INJ между Injective и inEVM
        ['okx_custom_withdraw_2'],  # см. OKX_CUSTOM_WITHDRAW_2
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['smart_transfer_cosmos', 'smart_transfer_cosmos_to_cex', None],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_inevm'],
        ['smart_organic_swaps', None],
        ['bridge_inevm'],
        ['smart_transfer_cosmos', 'smart_transfer_cosmos_to_cex', None],
        ['bridge_inevm'],
        ['smart_organic_swaps', None],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_inevm'],
        ['smart_transfer_cosmos', 'smart_transfer_cosmos_to_cex', None],
        ['okx_deposit'],
    ),
    (  # блок работы с UseNexus (5 бриджей TIA.n по строгому маршруту (Celestia->Neutron->ARB->Neutron->Celestia))
        ['bitget_custom_withdraw_1'],  # см. BITGET_CUSTOM_WITHDRAW_1
        ['binance_custom_withdraw_1'],  # см. BINANCE_CUSTOM_WITHDRAW_1
        ['fee_support_withdraw_for_arb'],  # см. OKX_CUSTOM_WITHDRAW_3
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['smart_stake_tia', 'smart_transfer_cosmos', 'smart_transfer_cosmos_to_cex', None],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_usenexus'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_usenexus'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_usenexus'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_usenexus'],
        ['smart_stake_tia', 'smart_transfer_cosmos', 'smart_transfer_cosmos_to_cex', None],
        ['bitget_deposit'],
    ),
    (  # блок работы с Nautilus (4 бриджа USDT между BNB Chain и Nautilus)
        ['bitget_custom_withdraw_2'],  # см. BITGET_CUSTOM_WITHDRAW_2
        ['smart_wrap_eth', 'smart_transfer_eth', 'smart_random_approve', None],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['swap_bnb_to_zbc_bsc'],
        ['refuel_nautilus'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_nautilus'],
        ['bridge_l2pass', 'bridge_nogem', 'bridge_merkly', 'bridge_zerius', None, None],
        ['bridge_nautilus'],
        ['smart_organic_swaps', None],
        ['bridge_nautilus'],
        ['bridge_hyperlane_nft', 'bridge_hyperlane_token', 'bridge_getmint', 'bridge_womex', 'bridge_nogem_hnft', None],
        ['bridge_nautilus'],
        ['smart_organic_swaps', None],
        ['bitget_deposit'],
    ),
    ['okx_deposit'],
]
