from PyQt5.QtCore.QByteArray import number


class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        result = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}."      #alteramos o and para e | Alteramos a variavel cuisine_type, o correto era restaurant_name
        result += f" Esse restaurante está servindo {self.number_served} consumidores desde está aberto."
        return result

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True                                            # Trocar o False pelo True
            #self.number_served = -2                                    # Retirado por não fazer sentido
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            #self.number_served = 0                                     # Retirado por não fazer sentido
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""

        '''
        Codigo Original, houve alteração por completo:
        if self.open:
            self.number_served = total_customers
        else:
            return f"{self.restaurant_name} está fechado!"
        '''

        if self.open and total_customers < 0:
            return "Número de clientes não pode ser negativo."

        elif(self.open and total_customers > 0):
            self.number_served = total_customers
            return total_customers

        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        '''
        #Codigo Original, houve alteração por completo:
        if self.open:
            self.number_served = more_customers
        else:
            return f"{self.restaurant_name} está fechado!"
        '''

        if self.open and more_customers > 0:
            self.number_served += more_customers
            return self.number_served

        elif(self.open and more_customers < 0):
            return "Numero nao pode ser negativo"

        else:
            return f"{self.restaurant_name} está fechado!"
