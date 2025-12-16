from random import*

class Animal:
    def __init__(self, name, gender, weigth, length, width, height):
        self.name = name
        self.gender = gender
        self.weigth = weigth
        self.length = length
        self.width = width
        self.height =  height
    
    def sound(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        pass
    
        

class Cat(Animal):
    def sound(self):
        soundNum = randint(1, 10)
        if soundNum == 1:
            print('Мяуууу')
        if soundNum == 2:
            print('Миааааааауууу')   
        if soundNum == 3:
            print('МЯЯЯЯЯЯЯУУУ')   
        if soundNum == 4:
            print('Мя')   
        if soundNum == 5:
            print('ня')   
        if soundNum == 6:
            print('ШШШШшшшшшш')   
        if soundNum == 7:
            print('мр мр мр мр мрмрмрмр мр мр')   
        if soundNum == 8:
            print('урррррррр')   
        if soundNum == 9:
            print('мя.......мя.......мя..мяу')   
        if soundNum == 10:
            print('МРЯР')   
    
    def eat(self):
        print("Что вы хотите дать вашей кошке?")
        print('1 - Мягкий корм')
        print('2 - Сухой корм')
        print('3 - Рыбов')
        print('4 - Сметану')
        print('5 - Молоко')
        print('6 - Мясо')
        print('7 - Кошачья мята')
        print('8 - Что-то другое')
        print('Выберете вариант из вышеперечисленного (число): ')
        meal = int(input())
        if meal == 1:
            print('Звуки поедания мягкого корма', '.',  '.', '.')
            print('Миска опустела, кошка довольно мурлыкает и обтирается об твою ногу')
        if meal == 2:
            print('Хрум ', 'хрум хрум ',  'хр хррум', 'хрум')

            print('Миска опустела, кошка довольно мурлыкает и обтирается об твою ногу')
        if meal == 3:
            print('Звуки поедания рыбов', '.',  '.', '.')
 
            print('На полу кости от рыбов и чешуя.')

            print('Кошка довольно мурлыкает и обтирается об твою ногу')
        if meal == 4:
            print('Звуки поедания сметаны', '.',  '.', '.')

            print('Миска опустела, кошка довольно мурлыкает и обтирается об твою ногу')
        if meal == 5:
            print('Звуки хлебания молока', '.',  '.', '.')

            print('Миска опустела, кошка довольно мурлыкает и обтирается об твою ногу')
        if meal == 6:
            print('Звуки поедания мяса', '.',  '.', '.')
 
            print('Миска опустела, кошка довольно мурлыкает и обтирается об твою ногу')
        if meal == 7:
            print('Кошка нюхает кошачью мяту', '.',  '.', '.')

            print('Кошка начинает неистово мяукать, валяться по полу')
  
            print('Кошка всеми частями тела пытается изнасиловать место где лежит кошачья мята')
        if meal == 8:
            print('Кошка нюхает то, что вы ей положили', '.',  '.', '.')

            print('Кошка уходит')
            
    def sleeping(self):
        print('Кошка идёт к своей лежанке', '.',  '.', '.')
        print('Сворачивается клубочком', '.',  '.', '.')
        print('Спит')
            
        
        
        
class Dog(Animal):
    pass

    



def main():
    murka = Cat('Murka', 'Female',  1, 1, 1, 1)
    murka.sound()
    murka.sound()
    murka.sound()
    murka.eat()
    murka.sleeping()
if __name__ == "__main__":
    main()
