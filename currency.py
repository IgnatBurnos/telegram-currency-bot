import aiohttp

class CurrencyConventer:
    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url 
    
    async def get_all_rates(self, base_currency: str = "USD") -> dict | None:
        url = f"{self.api_base_url}/latest?from={base_currency}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return None
                data = await response.json()
                return data.get("rates")


    async def convert(self, amount: float, from_currency: str, to_currency: str) -> float | None:
        url = f"{self.api_base_url}/latest?amount={amount}&from={from_currency}&to={to_currency}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return None

                data = await response.json()

                try:
                    return data["rates"][to_currency.upper()]
                except KeyError:
                    return None
