# Bank Account Management System

This Python program implements a simple bank account management system. It provides classes for basic bank account operations such as deposit, withdrawal, and transfer. Additionally, it includes features such as interest rewards and savings accounts.

## Classes

### BankAccount

The `BankAccount` class represents a basic bank account. It has the following methods:

- `__init__(self, initialAmount, acctName)`: Initializes a bank account with an initial balance and account name.
- `getBalance(self)`: Prints the current balance of the account.
- `deposit(self, amount)`: Deposits the specified amount into the account.
- `withdraw(self, amount)`: Withdraws the specified amount from the account.
- `transfer(self, amount, account)`: Transfers the specified amount to another account.

### InterestRewardsAcct

The `InterestRewardsAcct` class inherits from `BankAccount` and overrides the `deposit` method to apply a 5% interest reward on deposits.

### SavingsAcct

The `SavingsAcct` class inherits from `InterestRewardsAcct` and includes a $5 fee on withdrawals in addition to interest rewards.