import unittest , os

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):
      

      def setUp(self) -> None:
           self.account = BankAccount(balance=1000 , log_file="trasactions_log.txt")  # Cuenta con 1000 de saldo y archivo de log
           


      def tearDown(self) -> None:
          if os.path.exists(self.account.log_file):
              os.remove(self.account.log_file)    


      def test_deposit(self):
          new_balance = self.account.deposit(500)
          assert( new_balance, 1500)


      def test_withdraw(self):
          new_balance = self.account.withdraw(300)       
          assert new_balance == 700

      def test_get_balance(self):
           assert self.account.get_balance() == 1000
               

      def test_transfer_successful(self):
        """Prueba que una transferencia válida se realice correctamente"""
        # Datos de prueba
        transfer_amount = 300
        
        # Realizar transferencia
        result = self.account.transfer(transfer_amount, self.account)
        
        
        # Verificar que los balances son correctos
        self.assertNotEqual(self.account.get_balance(), 500)
    
      def test_transfer_insufficient_funds(self):
        """Prueba que se lance una excepción cuando no hay saldo suficiente"""
        # Datos de prueba - intentar transferir más de lo que tiene
        transfer_amount = 1500  # Mayor que el balance de account1 (1000)
        
        # Verificar que se lanza la excepción ValueError
        with self.assertRaises(ValueError) as context:
            self.account.transfer(transfer_amount, self.account)
        
        # Verificar el mensaje de error
        self.assertTrue("Saldo insuficiente" in str(context.exception))
        
        # Verificar que los balances NO cambiaron
        self.assertEqual(self.account.get_balance(), 1000)
        
    
      
    
      def test_transfer_invalid_target(self):
        """Prueba adicional: cuenta destino inválida"""
        with self.assertRaises(TypeError) as context:
            self.account.transfer(100, "no_es_una_cuenta")
        
        self.assertTrue("instancia de BankAccount" in str(context.exception))
    
      def tearDown(self):
        """Limpieza después de cada prueba"""
        self.account = None
       
     

      def test_transaction_log(self):
        """Prueba que las transacciones se registren correctamente"""
        new_balance = self.account.deposit(200)
        assert os.path.exists("trasactions_log.txt")