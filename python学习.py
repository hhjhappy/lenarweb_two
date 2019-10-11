# -*- coding: utf-8 -*-
#列表
def list_ex():
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles)
    #选择元素，开头大写
    print(bicycles[0].title())   
    #可以使用负数，从列表的最后往前
    print(bicycles[-1])
    message = "My first bicycle was a " + bicycles[0].title() + '.'

    print(message)


#修改元素
def change_list():
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles[0] = 'ducati'
    print(motorcycles)

#添加元素 append方法
def add_app():
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles.append('ducati')
    print(motorcycles)

#添加元素 insert方法
def add_insert():
    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles.insert(0,'ducati')
    print(motorcycles)

#列表元素删除
def del_som():
    print('----------------------------')
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    del motorcycles[2]
    print(motorcycles)

    motorcycles = ['honda', 'yamaha', 'suzuki']
    popped_motorcycles = motorcycles.pop()
    print(motorcycles)
    print(popped_motorcycles)

    motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
    print(motorcycles)
    motorcycles.remove('ducati')
    print(motorcycles)


def excemple_list():
    name_list = ['a','b','c','d','e']
    print(name_list)

    names = name_list.pop()
    print('%s is not join' %names)
    name_list.insert(-1,'f')
    print(name_list)

    name_list.insert(0,'g')
    print(name_list)

    print('Only Invite two guests')

    while True:
        # print(name_list)
        guests = name_list.pop()
        print('sorry %s can\'t join' %guests)
        if len(name_list) == 2:
            print('Invite two guests %s %s' %(name_list[0],name_list[1]) )
            del name_list[0]
            del name_list[0]
            print(name_list)
            break

def sort_list():
    #列表正向排序
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort()
    print(cars)
    #列表反向排序
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort(reverse = True)
    print(cars)

    #改变列表排序，同时改变原始列表
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    print('Here is the original list:')
    print(cars)

    #对列表临时排序，不改变原始文件
    print('\nHere is the sorted list:')
    print(sorted(cars,reverse = True))
    print(cars)

    #列表翻转，对调
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.reverse()
    print('\n')
    print(cars)


def excemple_sort_list():
    attractions = ['内蒙','大兴安岭','九寨沟','滇南','云南']
    print(attractions)
    print(sorted(attractions))
    print(attractions)
    print(sorted(attractions,reverse=True))
    print('\n')
    print(attractions)
    print('\n reverse')
    print(reversed(attractions))
    print('\n reverse')


# excemple_sort_list()


# motorcycles = ['honda', 'yamaha', 'suzuki']
# try:
#     print(motorcycles[3])
# except IndexError as err:
#     print(err)

def list_slice():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    frind_foods = my_foods
    print('myfood is :',my_foods)
    print('frind_foods :',frind_foods)
    print('\n')

    my_foods = ['pizza', 'falafel', 'carrot cake']
    frind_foods = my_foods[:]

    my_foods.append('cannoli')
    frind_foods.append('ice cream')

    print('My favorite foods are:', my_foods)
    print('My frind\'s favorite foods are:',frind_foods)

    print('\n')
    print('The first three items in the list are:',my_foods[:3])
    print('Three items from the middle of the list are:',my_foods[1:4])
    print('The last three items in the list are:',my_foods[-3:])

# list_slice()

def tuple_ex():
    dimensions = (200,50)
    print(dimensions[0])
    print(dimensions[1])

# tuple_ex()

def dict_excemple():
    alien_0 = {'color': 'green', 'points': 5}
    new_points = alien_0['points']
    print('You just earned ' + str(new_points) + ' ' + 'points!')

    alien_0 = {}
    alien_0['color'] = 'green'
    alien_0['points'] = 5
    print(alien_0)
    alien_0['color'] = 'green'
    print('The alien is' + ' ' + alien_0['color'] + '.')
    alien_0['color'] = 'yellow'
    print('The alien is now' + ' ' + alien_0['color'] + '.')
    print('\n')
    alien_0 = {'x_position' : 0,'y_position' : 25,'speed' : 'medium'}
    print(alien_0)
    del alien_0['x_position']
    print(alien_0)
    print('\n')

    mess = {'first_name':'hh','last_name':'j','age':'m','city':'Shanghai'}
    user_0 = { 
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi', 
    }

    for k,v in user_0.items():
        print('\nKey:' + k)
        print('Value:' + v)

    favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }

    print('\n')
    for name in favorite_languages.keys():
        print(name.title())

    print('\n')
    for name in sorted(favorite_languages.keys()):
        print(name)

    print('\n')
    print(list(favorite_languages.values()))
    for language in favorite_languages.values():
        print(language)

    print(set(favorite_languages.values()))

    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}

    aliens = [alien_0,alien_1,alien_2]
    print(aliens)
    for aline in aliens:
        print(aline)

    aliens = []
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)

    print(aliens[:5])
    print(len(aliens))




dict_excemple()







































