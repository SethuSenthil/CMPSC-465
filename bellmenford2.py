class CurrencyGraph:
    def __init__(self, currencies, exchange_rates):
        # Initialize the CurrencyGraph object with currencies and exchange rates
        self.currencies = currencies  # O(1)
        self.exchange_rates = exchange_rates  # O(1)

    def bellman_ford_negative_cycle(self, start_currency):
        # Initialize distances dictionary with start_currency having distance 0 and all other currencies having distance infinity
        distances = {currency: 0 if currency == start_currency else float('inf') for currency in self.currencies}  # O(n)

        # Iterate for the number of currencies
        for _ in range(len(self.currencies)):  # O(n)
            # Iterate over each source currency
            for source_currency in self.currencies:  # O(n)
                # Iterate over each target currency
                for target_currency in self.currencies:  # O(n)
                    # Check if source_currency is not equal to target_currency
                    if source_currency != target_currency:  # O(1)
                        # Get the exchange rate from source_currency to target_currency
                        exchange_rate = self.exchange_rates[source_currency][target_currency]  # O(1)
                        # Check if the distance from source_currency + exchange_rate is less than the current distance of target_currency
                        if distances[source_currency] + exchange_rate < distances[target_currency]:  # O(1)
                            # Update the distance of target_currency
                            distances[target_currency] = distances[source_currency] + exchange_rate  # O(1)

                            # If we can relax a vertex in the last iteration, there is a negative cycle
                            if _ == len(self.currencies) - 1:  # O(1)
                                return True

        # If no negative cycle is found, return False
        return False  # O(1)