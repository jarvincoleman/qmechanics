## Quantum States 

### Superposition & Measurement

import numpy as np 
import matplotlib.pyplot as plt 



class System: 
    
    def __init__(self, spin, _appa, vector):
        self.spin = spin 
        self.appa = _appa
        self.vector = vector

    def normalization(self):
        ## set degree orientation of the apparatus
        ## _appa = np.degrees(90)
        ### convert into radians
        pass

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
    State(any)

    pass

