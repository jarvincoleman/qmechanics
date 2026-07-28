## Quantum States 

### Superposition & Measurement
import numpy as np 
import matplotlib.pyplot as plt 



class System: 
    
    def __init__(self, spin: int , _appa: float, vector: list[float] ):
        self.spin = spin 
        self.appa = _appa
        self.vector = vector

    def normalization(self, _appa, vector: list[int]):
        ## set degree orientation of the apparatus
        ## _appa = np.degrees(90)
        ### convert into radians
        
        _appa = 0.5

        for v in vector:
            spin = 0
            if v in vector <= 0: 
                v = vector[v] * _appa
            else: 
                v = 0.5

            while v:
                if v == 1:
                    spin = np.radians(180) * _appa
            return spin 

        print(spin) 
                

    def measure(self, two_state, state_1, state_2, bias):

        H = [1,0] 
        T = [0,1]
        state_1 = H 
        state_2 = T

        two_state = (state_1, state_2)

        while two_state:
            #if _appa >= 0: 
                return np.matmul(two_state)
        return two_state

        


        ### How do I want to structure this function? This current code will be deleted below
        

    def expectation(self, x, y, spin):

        ## set coordinates for probalistic expectation value 
        zz = any 
        y = any 
        x = any 
        pass

    def outcomes(self, zz):
        ## pass in coordinates and compute... 
            ## histograms of theoretical probs.
        pass
















if __name__ == "__main__":
    System(spin = 1, _appa = 0.5, vector=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.1, 1.2])
    
    _appa = 0.5
    _appa.normalization(_appa=0.5)



     

