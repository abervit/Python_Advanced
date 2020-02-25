#1)Cоздать список из Н элементов (от 0 до с шагом 1). В этом списке вывести все четные значения
a = [1,2,3,4,5,6,7,8,9] # list of random numbers with step 1
for i in a:
    # checking if it`s an even number, if yes we print it out
    if i%2==0:
        print(i)


#3)Напишите прогрмму которая выводит на экран числа от 1 до 100.
# При этом вместе числе кратных трем, программа должна выводить слово Fizz, а вместо числе кратных пяти - Buzz.
# Если число кратно 15, то программа должна выводить слово FizBuzz
#we can count the number of our matches. It`s not important but nice to know how many of each we`ve got:D
count_fizz=0
count_buzz=0
count_fizzbuzz = 0
for i in range(1,101):
    #Using if statement we have to check first, if our number is divided by 15, next by 5 and in the end by 3
    #In other case we will have mostly Fizz numbers and some Buzz,
    # because all numbers devided by 15 can be divided by 3 and 5 at the same time
    if i%15==0:
        print('FizBuzz')
        count_fizzbuzz+=1
    elif i%5==0:
        print('Buzz')
        count_buzz+=1
    elif i % 3 == 0:
        print('Fizz')
        count_fizz+=1
    else:
        print(i)
print('We have',count_fizz, 'fizz numbers,', count_buzz,
      'buzz numbers and',count_fizzbuzz,'fizzbuzz numbers overall')


#2)Cоздать словарь Страна:Столица. Создать список стран.
# Не все страны со списка должны сходится с названиями стран со словаряю
# С помощю оператора in проверить на вхождение элемента страны в словарь,
# и если такой ключ действительно существует вывести столицу
dict={                #our dictionary with states and their capitals
    'Norway': 'Oslo',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Portugal': 'Lisboa',
    'Wales': 'Cardif',
}
#random list of countries
countries=['Germany','France','Japan','Norway','Poland','Canada','Wales','Portugal','Belgium']
for i in countries:#choising one by one country from our list
    if i in dict:#cheking if chosen country is in our dictionary, if yes we print out its capital
        print(dict[i])


#4) Реализовать функцию bank, которая принимает следущие аргументы: сумма депозита, кол-лет, и процент
# Результатом выполнения должна быть сумма по истечению депозита
def bank(suma,let,proc):

    suma_final = suma+(suma*let*proc)
    print('По истечению депозита ваша сумма составит:', suma_final,
          'а сумма процентов к выплате будет -', (suma*let*proc))

bank(10000,15,0.04)
bank(25000,30,0.20)