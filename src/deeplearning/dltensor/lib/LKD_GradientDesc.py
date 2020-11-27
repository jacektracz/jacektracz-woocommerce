"""
"""

import tensorflow as tf
from sklearn.metrics import mean_squared_error

from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

class LKD_GradientDesc:

        def __init__(self, tt):
                self.m_print_dbg = 0


        def class_name( self ):
                return "LKD_TensorCore::"

        def xx_dbg(self, tt ):
                s_fun = self.class_name() + "::xx_dbg::"
                print ( tt )

        def exec_main(self, tt):
            weights = np.array([0, 2, 1])
            input_data = np.array([1, 2, 3])
            target = 0
            learning_rate = 2
            n_updates = 20
            mse_hist = []
            for i in range(n_updates):
                slope = self.get_slope(input_data, target, weights)
                weights = weights + (learning_rate * slope)
                mse = self.get_mse(input_data, target, weights)
                mse_hist.append(mse)
                
            plt.plot(mse_hist)
            plt.xlabel('Iterations')
            plt.ylabel('Mean Squared Error')
            plt.show()


        def pred(self,input_data, target, weights):
            return ((input_data * weights).sum())

        def get_slope(self,input_data, target, weights):
            preds = self.pred(input_data, target, weights)
            error = target - preds
            slope = 2 * input_data * error
            return slope

        def get_mse(self,input_data, target, weights):
            preds = self.pred(input_data, target, weights)
            return mean_squared_error([preds], [target])

