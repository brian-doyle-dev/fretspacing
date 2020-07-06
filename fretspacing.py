'''
Created on 22 Mar 2020

@author: briandoyle
'''


class Frets():
    
    def __init__(self, scale_length, num_frets):
        
        self.scale_length = scale_length
        self.num_frets = num_frets
        print(f'Scale Length: {scale_length}')
        print(f'Number of Frets: {num_frets}')
        
    def calc(self, fret_number):
        d = self.scale_length - (self.scale_length / (self.twelfth_root(2**fret_number)))
        d = round(d, 2)
        return d
     
    def twelfth_root(self, x):
        root = x**(1/12)
        return root

if __name__ == "__main__":
    
    frets = Frets(550, 22)
    index = 0
    last = 0
    for x in range(22):
        space = frets.calc(x)
        print(f'{index}\t{space}\t{round(space - last, 2)}')
        if index > 0:
            last = space
        index = index + 1
        
    