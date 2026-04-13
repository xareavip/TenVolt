import numpy as np
class ReluActivator(object):
    def forward(self,weighted_input):
        return max(0,weighted_input)
    def backward(self,output):
        return 1 if output > 0 else 0
class IdentityActivator(object):
    # f(x)=1
    def forward(self,weighted_input):
        return weighted_input
    def backward(self,output):
        return 1
class SigmoidActivator(object):
    def forward(self, weighted_input):
        return 1 / (1 + np.exp(-weighted_input))
    def backward(self, output):
        return output * (1 - output)


