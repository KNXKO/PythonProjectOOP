from bank_accounts import *

Dave = BankAccount(1000,"Dave")
Sara = BankAccount(2000,"Sara")
Dave.getBalance()
Sara.getBalance()
Dave.deposit(500)
Sara.deposit(300)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(50, Sara)

Jim = InterestRewardsAcct(1000,"Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)
