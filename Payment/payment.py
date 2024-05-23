from abc import ABC, abstractmethod

class Payment(ABC):
    """
    Abstract base class for payment methods.
    """
    
    @abstractmethod
    def process_payment(self):
        pass