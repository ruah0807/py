### **문제: 은행 관리 프로그램**

# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요. 
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.


class Account :
    
    def __init__(self, name, balance, new_account):
        self.name = name
        self.balance = balance
        self.new_account = new_account
        
    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else :
            raise ValueError('입금금액이 음수이거나 없습니다.')
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else :
            raise ValueError('잔액이 부족하거나 잘못된 출금입니다.')
    
    def display_balance(self):
        print(f"""------------------------------------------------
{self.name}님의 현재 잔액은 {self.balance}원 입니다.
-------------------------------------------------""")
    
    
    
    
class Bank(Account) :
    
    def __init__(self, bank_name):
        self.bank_name = bank_name
        #계좌 목록 초기화
        self.accounts = []
        
    def create_account(self, name, balance, new_account):
        account = Account(name,balance,new_account)
        self.accounts.append(account)
        print(f"""-------------------------
환영합니다 {name}님!
계좌번호 : {new_account}
잔액 : {balance}원
------------------------""")
        
    
    def get_account(self, name):
        for account in self.accounts:
            if account.name == name :
                return account
        print(f"{name}님의 계좌를 찾을 수 없습니다.")
        
       
    def display_accounts(self):
        print(f"{self.bank_name}의 모든 고객 계좌 정보")
        for account in self.accounts:
            print(f"""----------------------------------------------------------------
소유주 : {account.name}, 계좌번호 : {account.new_account}, 잔액 :{account.balance}원
----------------------------------------------------------------""")
    
    
bank = Bank('하나은행')
    

    
def display_menu():
    print(f'{bank.bank_name}에 오신 것을 환영합니다.')
    print('1. 계좌 생성')
    print('2. 내 계좌 조회')
    print('3. 입금')
    print('4. 출금')
    print('5. 전체 계좌 조회')
    print('6. 종료')   
        
    
while True:
    display_menu()
    choice = int(input("선택하세요 : "))
    
    if choice == 1 :
        name = input('이름을 입력해주세요 :')
        balance = int(input('초기 잔액을 입력해주세요 : '))
        new_account = input('계좌번호 : ')
        bank.create_account(name, balance, new_account)
        
    elif choice == 2 :
        name = input("이름을 입력하세요 :")
        account = bank.get_account(name)
        if account :
            account.display_balance()
            
    elif choice == 3 :
        name = input('이름을 입력해주세요 :')
        account =bank.get_account(name)
        if account : 
            amount = int(input('입금할 금액을 입력하세요 : '))
            account.deposit(amount)
            
    elif choice == 4 :
        name = input('이름을 입력해주세요 :')
        account =bank.get_account(name)
        if account :
            amount = int(input('출금할 금액을 입력해주세요 : '))
            account.withdraw(amount)
        
    elif choice == 5 :
        bank.display_accounts()
        
    elif choice == 6 :
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 다시 시도하세요")
        

# my_account = Bank('김루아', 500000)

# print('내 계좌 잔액 : ', my_account._Account__balance)

# print('잔액 : ', my_account.get_balance())
# #입금
# my_account.deposit(100)
# print("입금 후 잔액 : ", my_account.get_balance())

# #출금
# my_account.withdraw(500000)
# print("출금 후 잔액 : ", my_account.get_balance())


