#Clients should not be forced to depend upon methods that they do not use. 
# Interfaces belong to clients, not to hierarchies.
#In this case, clients are classes and subclasses, and interfaces consist of methods and attributes. 
# In other words, if a class doesn’t use particular methods or attributes, 
# then those methods and attributes should be segregated into more specific classes.


# printers_isp.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

#In this example, the base class, Printer, provides the interface that its subclasses must implement. 
# OldPrinter inherits from Printer and must implement the same interface. 
# However, OldPrinter doesn’t use the .fax() and .scan() methods because this type of printer doesn’t support these functionalities        

# printers_isp.py

# Implementação em conformidade:

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

#Now Printer, Fax, and Scanner are base classes that provide specific interfaces with a single responsibility each. 
# To create OldPrinter, you only inherit the Printer interface. 
# This way, the class won’t have unused methods. 
# To create the ModernPrinter class, you need to inherit from all the interfaces. In short, you’ve segregated the Printer interface.        