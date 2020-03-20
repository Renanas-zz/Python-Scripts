''''
Testando o que já vi em python com apenas um programa
'''


class NuBankNextWithLepra:
    fish = 100.00
    cashFish = 0
    tiger = 50.00
    cashTiger = 0
    monkey = 20.00
    cashMonkey = 0
    bird = 10.00
    cashBird = 0
    birdWithLongFeet = 5.00
    cashBirdWithLongFeet = 0
    turtle = 2.00
    cashTurtle = 0
    woman = 1.00
    cashWoman = 0
    cashBank = 1050.00
    noCash = 0.0
    takeMoney = 0.0
    options = ['Saque', 'Deposito']

    option = input(f'What you wanna do {options[0]} or {options[1]}')

    if option == options[0]:
        money = float(input('How much do you wanna take?'))

        if money > cashBank:
            print(f'You dont have soo much money, you have {cashBank}')
        else:
            cashBank = cashBank - money
            while money != noCash:
                while (money / fish) >= 1:
                    money = money - fish
                    takeMoney = takeMoney + money
                    cashFish = cashFish + 1

                while (money / tiger) >= 1:
                    money = money - tiger
                    takeMoney = takeMoney + money
                    cashTiger = cashTiger + 1

                while (money / monkey) >= 1:
                    money = money - monkey
                    takeMoney = takeMoney + money
                    cashMonkey = cashMonkey + 1

                while (money / bird) >= 1:
                    money = money - bird
                    takeMoney = takeMoney + money
                    cashBird = cashBird + 1

                while (money / birdWithLongFeet) >= 1:
                    money = money - birdWithLongFeet
                    takeMoney = takeMoney + money
                    cashBirdWithLongFeet = cashBirdWithLongFeet + 1

                while (money / turtle) >= 1:
                    money = money - turtle
                    takeMoney = takeMoney + money
                    cashTurtle = cashTurtle + 1

                while (money / woman) >= 1:
                    money = money - woman
                    takeMoney = takeMoney + money
                    cashWoman = cashWoman + 1

    print(f'Now you have {cashBank} in your account')

    print(f' R$:{cashFish*100}, R$:{cashTiger*50}, R$:{cashMonkey*20}, R$:{cashBird*10}, R$:{cashBirdWithLongFeet*5}, R$:{cashTurtle*2}, R$:{cashWoman*1}')
