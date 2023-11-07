from eth_account import Account
from modules import Blockchain
from utils.tools import gas_checker, repeater
from settings import (
    SCROLL_DEP_MAX,
    SCROLL_DEP_MIN,
    SCROLL_WITHDRAW_MAX,
    SCROLL_WITHDRAW_MIN,
    TRANSFER_MIN,
    TRANSFER_MAX
)
from config import (
    WETH_ABI,
    CONTRACT_DATA,
    SCROLL_TOKENS,
    SCROLL_CONTRACTS,
    SCROLL_DEPOSIT_ABI,
    SCROLL_WITHDRAW_ABI,
    SCROLL_ORACLE_ABI,
)


class Scroll(Blockchain):
    def __init__(self, client):
        self.client = client

        self.deposit_contract = self.client.get_contract(SCROLL_CONTRACTS['deposit'], SCROLL_DEPOSIT_ABI)
        self.oracle_contract = self.client.get_contract(SCROLL_CONTRACTS["oracle"], SCROLL_ORACLE_ABI)
        self.withdraw_contract = self.client.get_contract(SCROLL_CONTRACTS['withdraw'], SCROLL_WITHDRAW_ABI)
        self.token_contract = self.client.get_contract(SCROLL_TOKENS['WETH'], WETH_ABI)

    @repeater
    @gas_checker
    async def deposit(self):

        amount = self.client.round_amount(SCROLL_DEP_MIN, SCROLL_DEP_MAX)
        amount_in_wei = int(amount * 10 ** 18)

        self.client.logger.info(f'{self.client.info} Scroll | Bridge {amount} ETH | ERC20 -> Scroll')

        if await self.client.w3.eth.get_balance(self.client.address) > amount_in_wei:

            bridge_fee = await self.oracle_contract.functions.estimateCrossDomainMessageFee(168000).call()

            tx_data = await self.client.prepare_transaction(value=amount_in_wei + bridge_fee)

            transaction = await self.deposit_contract.functions.depositETH(
                amount_in_wei,
                168000,
            ).build_transaction(tx_data)

            tx_hash = await self.client.send_transaction(transaction)

            await self.client.verify_transaction(tx_hash)

        else:
            raise RuntimeError('Insufficient balance!')

    @repeater
    @gas_checker
    async def withdraw(self):

        amount = self.client.round_amount(SCROLL_WITHDRAW_MIN, SCROLL_WITHDRAW_MAX)
        amount_in_wei = int(amount * 10 ** 18)

        self.client.logger.info(
            f'{self.client.info} Scroll | Withdraw {amount} ETH Scroll -> ERC20')

        if await self.client.w3.eth.get_balance(self.client.address) > amount_in_wei:

            tx_params = await self.client.prepare_transaction(value=amount_in_wei)

            transaction = await self.withdraw_contract.functions.withdrawETH(
                amount_in_wei,
                0
            ).build_transaction(tx_params)

            tx_hash = await self.client.send_transaction(transaction)

            await self.client.verify_transaction(tx_hash)

        else:
            raise RuntimeError('Insufficient balance!')

    @repeater
    @gas_checker
    async def transfer_eth_to_myself(self):

        amount, amount_in_wei = await self.client.check_and_get_eth_for_deposit()

        self.client.logger.info(
            f"{self.client.info} Scroll | Transfer {amount} ETH to your own address: {self.client.address}")

        tx_params = await self.client.prepare_transaction(value=amount_in_wei) | {
            "to": self.client.address,
            "data": "0x"
        }

        tx_hash = await self.client.send_transaction(tx_params)

        await self.client.verify_transaction(tx_hash)

    @repeater
    @gas_checker
    async def transfer_eth(self):

        amount = self.client.round_amount(TRANSFER_MIN, TRANSFER_MAX)
        amount_in_wei = int(amount * 10 ** 18)
        random_address = Account.create().address

        self.client.logger.info(f'{self.client.info} Scroll | Transfer ETH to random zkSync address: {amount} ETH')

        if await self.client.w3.eth.get_balance(self.client.address) > amount_in_wei:

            tx_params = (await self.client.prepare_transaction()) | {
                'to': random_address,
                'value': amount_in_wei,
                'data': "0x"
            }

            tx_hash = await self.client.send_transaction(tx_params)

            await self.client.verify_transaction(tx_hash)

        else:
            raise RuntimeError('Insufficient balance!')

    @repeater
    @gas_checker
    async def deploy_contract(self):

        self.client.logger.info(f"{self.client.info} Scroll | Deploy contract")

        tx_data = await self.client.prepare_transaction()

        contract = self.client.w3.eth.contract(abi=CONTRACT_DATA['abi'], bytecode=CONTRACT_DATA['bytecode'])

        transaction = await contract.constructor().build_transaction(tx_data)

        tx_hash = await self.client.send_transaction(transaction)

        await self.client.verify_transaction(tx_hash)

    # @repeater
    # @gas_checker
    # async def transfer_erc20_tokens(self, token_to_sent_name: str, address_to_sent: str, amount: float):
    #
    #     self.logger.info(
#                       f'{self.info} Transfer {token_to_sent_name} to random address: {amount} {token_to_sent_name}')
    #
    #     amount_in_wei = await self.get_amount_in_wei(token_to_sent_name, amount)
    #
    #     if (await self.get_token_balance(ZKSYNC_TOKENS[token_to_sent_name]))['balance_in_wei'] >= amount_in_wei:
    #
    #         token_contract = self.get_contract(ZKSYNC_TOKENS[token_to_sent_name], ERC20_ABI)
    #
    #         tx_params = await self.prepare_transaction()
    #
    #         transaction = await token_contract.functions.transfer(
    #             address_to_sent,
    #             amount
    #         ).build_transaction(tx_params)
    #
    #         tx_hash = await self.send_transaction(transaction)
    #
    #         await self.verify_transaction(tx_hash)
    #
    #     else:
    #         self.logger.error(f'{self.info} Insufficient balance!')

    @repeater
    @gas_checker
    async def wrap_eth(self):

        amount, amount_in_wei = await self.client.check_and_get_eth_for_deposit()

        self.client.logger.info(f'{self.client.info} Scroll | Wrap {amount} ETH')

        if await self.client.w3.eth.get_balance(self.client.address) > amount_in_wei:

            tx_params = await self.client.prepare_transaction(value=amount_in_wei)
            transaction = await self.token_contract.functions.deposit().build_transaction(tx_params)

            tx_hash = await self.client.send_transaction(transaction)

            await self.client.verify_transaction(tx_hash)

        else:
            raise RuntimeError('Insufficient balance!')

    @repeater
    @gas_checker
    async def unwrap_eth(self):

        amount_in_wei, amount, _ = await self.client.get_token_balance('WETH', check_symbol=False)

        self.client.logger.info(f'{self.client.info} Scroll | Unwrap {amount:.6f} WETH')

        tx_params = await self.client.prepare_transaction()

        transaction = await self.token_contract.functions.withdraw(
            amount_in_wei
        ).build_transaction(tx_params)

        tx_hash = await self.client.send_transaction(transaction)

        await self.client.verify_transaction(tx_hash)
