import sys
import os
from gradient_descent import gradient_descent

# rem C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\deeplearning\start_stanford_cpy.py
#  C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\deeplearning\start_cpy.py
# C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\deeplearning\dltensor\dlip\Mean_Squared_Error.py
# C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\deeplearning\dltensor\kerasexamples\image_ocr.py
# C:\lkd\ht\apps_dl_keras_course\app\src\Easy-deep-learning-with-Keras\6. Examples\CNN for sentence classification\cnn-static.py
class LKD_MainExec:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_MainExec::__init__::in::")
                self.xx_dbg("LKD_MainExec::__init__::out:")

        def xx_dbg(self, tt):
                "" ""
                print ( tt )

        def exec_main(self, tt):
                dd = LKD_TensorCore("")
                dd.exec_main("")
                
                        
        
        def gradient(self, tt):
                dd = LKD_GradientDesc("")
                dd.exec_main("")

        def gradient_stanford(self, tt):
                gradient_descent.gradientDescent(
                        gradient_descent.F
                        , gradient_descent.dF
                        , gradient_descent.d
                        ,40)

        def stochastic_gradient_stanford(self, tt):
                gradient_descent.stochasticGradientDescent(
                        gradient_descent.sF
                        , gradient_descent.sdF
                        , gradient_descent.d
                        , len(gradient_descent.points)
                        , 40)
                ##stochasticGradientDescent(sF, sdF, d, len(points))

if __name__ == "__main__":

        ddh = LKD_MainExec("")
        #ddh.exec_main("")
        # ddh.gradient("")
        ddh.stochastic_gradient_stanford("")
        ddh.gradient_stanford("")
        