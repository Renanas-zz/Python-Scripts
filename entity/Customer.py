class Customer:
    
    def __init__(self, id, cpf):
        self.__id = id
        self.__cpf = cpf

    @property
    def getId(self):
        return self.__id
    
    @property
    def getCpf(self):
        return self.__cpf
    
customer = Customer(1, "11111111111")

print(customer.getId)
print(customer.getCpf)
   

