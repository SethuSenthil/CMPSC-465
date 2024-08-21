class CurrencyGraph:
    def __init__(self, currencies, exchange_rates):
        # Initialize the CurrencyGraph object with a list of currencies and a dictionary of exchange rates
        # ! The exchange_rates dictionary should have the format {source_currency: {target_currency: exchange_rate}}
        self.currencies = currencies
        self.exchange_rates = exchange_rates

    def bellman_ford(self, start_currency):
        # Initialize distances to all currencies as infinity
        distances = {currency: float('inf') for currency in self.currencies}  # O(n)

        distances[start_currency] = 0  # O(1)

        # Relax edges repeatedly
        for _ in range(len(self.currencies) - 1):  # O(n)
            for source_currency in self.currencies:  # O(n)
                for target_currency in self.currencies:  # O(n)
                    if source_currency != target_currency:  # O(1)
                        # Get the exchange rate between source_currency and target_currency
                        exchange_rate = self.exchange_rates[source_currency][target_currency]  # O(1)
                        if distances[source_currency] + exchange_rate < distances[target_currency]:  # O(1)
                            # If the new distance is shorter, update the distance
                            distances[target_currency] = distances[source_currency] + exchange_rate  # O(1)

        # Check for negative cycles
        for source_currency in self.currencies:  # O(n)
            for target_currency in self.currencies:  # O(n)
                if source_currency != target_currency:  # O(1)
                    # Get the exchange rate between source_currency and target_currency
                    exchange_rate = self.exchange_rates[source_currency][target_currency]  # O(1)
                    if distances[source_currency] + exchange_rate < distances[target_currency]:  # O(1)
                        # If a negative cycle is detected, return the appropriate message
                        return "Negative cycle detected"  # O(1)

        # Return the distances dictionary
        return distances  # O(1)