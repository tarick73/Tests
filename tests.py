import unittest
from bank_account import BankAccount, InsufficientFunds


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.empty = BankAccount()
        self.rich = BankAccount(100)

    def test_initial_balance_default_is_zero(self):
        self.assertEqual(self.empty.get_balance(), 0)

    def test_initial_balance_custom(self):
        self.assertEqual(self.rich.get_balance(), 100)

    def test_deposit_positive(self):
        self.empty.deposit(50)
        self.assertEqual(self.empty.get_balance(), 50)

    def test_deposit_zero_raises(self):
        with self.assertRaises(ValueError):
            self.empty.deposit(0)

    def test_deposit_negative_raises(self):
        with self.assertRaises(ValueError):
            self.empty.deposit(-10)

    def test_withdraw_positive(self):
        self.rich.withdraw(30)
        self.assertEqual(self.rich.get_balance(), 70)

    def test_withdraw_exact_to_zero_allowed(self):
        self.rich.withdraw(100)
        self.assertEqual(self.rich.get_balance(), 0)

    def test_withdraw_zero_raises(self):
        with self.assertRaises(ValueError):
            self.rich.withdraw(0)

    def test_withdraw_negative_raises(self):
        with self.assertRaises(ValueError):
            self.rich.withdraw(-5)

    def test_withdraw_insufficient_funds_raises(self):
        with self.assertRaises(InsufficientFunds):
            self.empty.withdraw(1)
    def test_transfer_success(self):
        sender = BankAccount(80)
        receiver = BankAccount(20)
        sender.transfer(receiver, 30)
        self.assertEqual(sender.get_balance(), 50)
        self.assertEqual(receiver.get_balance(), 50)

    def test_transfer_non_bank_account_raises(self):
        with self.assertRaises(TypeError):
            self.rich.transfer("not-an-account", 10)

    def test_get_balance_reflects_operations(self):
        acc = BankAccount(10)
        acc.deposit(5)
        acc.withdraw(3)
        self.assertEqual(acc.get_balance(), 12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
