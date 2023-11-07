from config import LAYERBANK_CONTRACT, LAYERSWAP_ABI
from utils.tools import gas_checker, repeater
from modules import Landing


class LayerBank(Landing):
    def __init__(self, client):
        self.client = client

        self.landing_contract = self.client.get_contract(LAYERBANK_CONTRACT['landing'], LAYERSWAP_ABI)
        self.collateral_contract = self.client.get_contract(LAYERBANK_CONTRACT['pool'], LAYERSWAP_ABI)

    @repeater
    @gas_checker
    async def deposit(self):

        amount, amount_in_wei = await self.client.check_and_get_eth_for_deposit()

        self.client.logger.info(f'{self.client.info} LayerBank | Deposit to LayerBank: {amount} ETH')

        tx_params = await self.client.prepare_transaction(value=amount_in_wei)

        transaction = await self.landing_contract.functions.supply(
            LAYERBANK_CONTRACT['pool'],
            amount_in_wei
        ).build_transaction(tx_params)

        tx_hash = await self.client.send_transaction(transaction)

        await self.client.verify_transaction(tx_hash)

    @repeater
    @gas_checker
    async def withdraw(self):
        self.client.logger.info(f'{self.client.info} LayerBank | Withdraw from LayerBank')

        liquidity_balance = await self.landing_contract.functions.balanceOf(self.client.address).call()

        if liquidity_balance != 0:

            tx_params = await self.client.prepare_transaction()

            transaction = await self.landing_contract.functions.redeemUnderlying(
                LAYERBANK_CONTRACT['pool'],
                liquidity_balance,
            ).build_transaction(tx_params)

            tx_hash = await self.client.send_transaction(transaction)

            await self.client.verify_transaction(tx_hash)
        else:
            raise RuntimeError("Insufficient balance on LayerBank!")

    @repeater
    @gas_checker
    async def enable_collateral(self):
        self.client.logger.info(f'{self.client.info} LayerBank | Enable collateral on LayerBank')

        tx_params = await self.client.prepare_transaction()

        transaction = await self.landing_contract.functions.enterMarkets(
            [LAYERBANK_CONTRACT['pool']]
        ).build_transaction(tx_params)

        tx_hash = await self.client.send_transaction(transaction)

        await self.client.verify_transaction(tx_hash)

    @repeater
    @gas_checker
    async def disable_collateral(self):
        self.client.logger.info(f'{self.client.info} LayerBank | Disable collateral on LayerBank')

        tx_params = await self.client.prepare_transaction()

        transaction = await self.collateral_contract.functions.exitMarket(
            LAYERBANK_CONTRACT['pool']
        ).build_transaction(tx_params)

        tx_hash = await self.client.send_transaction(transaction)

        await self.client.verify_transaction(tx_hash)
