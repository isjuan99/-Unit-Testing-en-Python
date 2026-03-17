class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('cuenta creada')



    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as file:
                file.write(f'{message}\n')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'deposito: {amount}, New balance: {self.balance}')
            return self.balance
       

    def withdraw(self, amount):
        if amount> 0:
            self.balance -= amount
            self._log_transaction(f'retiro: {amount}, New balance: {self.balance}')
            return self.balance
        
    
    def get_balance(self):
        self._log_transaction(f'consulta de saldo, Balance actual: {self.balance}')
        return self.balance
    

    def transfer(self, amount, target_account):
        """
        Transfiere una cantidad de dinero a otra cuenta
        
        Args:
            amount: Cantidad a transferir
            target_account: Cuenta destino
            
        Returns:
            El nuevo balance de la cuenta origen
            
        Raises:
            ValueError: Si el monto es negativo o cero
            ValueError: Si no hay saldo suficiente
            TypeError: Si target_account no es una instancia de BankAccount
        """
        # Validaciones
        if not isinstance(target_account, BankAccount):
            raise TypeError("La cuenta destino debe ser una instancia de BankAccount")
        
        if amount <= 0:
            raise ValueError("El monto a transferir debe ser mayor a cero")
        
        if self.balance < amount:
            raise ValueError(f"Saldo insuficiente en su cuenta. Balance actual: {self.balance}, Monto a transferir: {amount}")
        
        # Realizar la transferencia
        self.balance -= amount
        target_account.balance += amount
        self._log_transaction(f'transferencia: {amount} a {target_account}, New balance: {self.balance}')
        target_account._log_transaction(f'recibido: {amount} de {self}, New balance: {target_account.balance}') 
        
        return self.balance