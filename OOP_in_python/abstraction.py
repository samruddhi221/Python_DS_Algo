from abc import ABC, abstractmethod
import math

class ActivationBase(ABC):
    # forward method
    @abstractmethod
    def forward(self, input_var: float) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Sigmoid(ActivationBase):
    def __init__(self):
        super().__init__()

    def forward(self, input_var: float) -> float:
        return 1 / (1 + math.exp(-input_var))

    def __str__(self):
        return "Sigmoid"


class TanH(ActivationBase):
    def __init__(self):
        super().__init__()

    def forward(self, input_var: float) -> float:
        return (math.exp(input_var) - math.exp(-input_var))/(math.exp(input_var) + math.exp(-input_var))

    def __str__(self):
        return "Tanh"

class LayerBase(ABC):

    @abstractmethod
    def forward(self, input: float) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Dense(LayerBase):
    def __init__(self):
        self.__weight = 1.0
        self.__bias = 1.0
        super().__init__()

    def forward(self, input: float) -> float:
        return (self.__weight * input + self.__bias)

    def __str__(self):
        return "Dense"

class Sequential:
    def __init__(self, activations: list):
        self.__network_elements = activations

    def forward(self, input_var: float) -> float:
        for network_element in self.__network_elements:
            input_var = network_element.forward(input_var)
        return input_var

    def summary(self):
        # layer_str = []
        for index, network_element in enumerate(self.__network_elements):
            if index < len(self.__network_elements)-1:
                print(network_element, end=" -> ")
            else:
                print(network_element)


if __name__ == '__main__':
    sig = Sigmoid()
    print(sig.forward(0.))
    tanh = TanH()
    print(tanh.forward(1.0))

    seq = Sequential([Sigmoid(), TanH()])
    print(seq.forward(0.))

    network = Sequential([Dense(), Sigmoid(), Dense(), TanH()])
    print(network.forward(0.))
    network.summary()