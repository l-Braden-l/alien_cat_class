#
#
#

# -- Cat Class -- # 
class Alien_cat: 

    '''Class to describe a alien cat'''

    def __init__(self, age, fur_color, dangerous, name, planet): 
        self.age = age 
        self.fur_color = fur_color 
        self.dangerous = dangerous
        self.name = name
        self.planet = planet

    
    def fly(self): 
        '''Method for the cat flying'''
        print(f'{self.name} is from the planet {self.planet}, they started flying!')

    
    def lazer_eyes(self):
        '''Method for the cats ability to shoot lazers out it's eyes'''
        print(f'{self.name} starts shooting lazers out its eyes!, it is {self.dangerous}!')


alien_cat1 = Alien_cat( 400, 'Black and White', 'Dangerous', 'Pilzbow', 'Lutheria')
alien_cat2 = Alien_cat( 4120, 'Green and Blue', 'Dangerous', 'Jaztoed', 'fulars')


print(f'\nThe first aliens name is {alien_cat1.name}, there fur color is {alien_cat1.fur_color}.')
alien_cat1.fly()


print(f'\nThe second aliens name is {alien_cat2.name}, there fur color is {alien_cat2.fur_color}.')
alien_cat1.lazer_eyes()
