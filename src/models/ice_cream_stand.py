from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list=None):
        """
        Inicializa atributos da classe pai e configura a lista de sabores.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list if flavors_list else []                         # Correção: inicializa vazio se None.

    def flavors_available(self):
        """Percorre a lista de sabores disponíveis e retorna uma mensagem."""
        if self.flavors:
            result = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n"
            result += "\n".join(f"- {flavor}" for flavor in self.flavors)
            return result
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor.lower() in (f.lower() for f in self.flavors):                 # Correção: case-insensitive.
                return f"Temos o sabor {flavor.title()} no momento!"
            else:
                return f"Não temos o sabor {flavor.title()} no momento!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if flavor.lower() in (f.lower() for f in self.flavors):                     # Correção: Evitar duplicatas case-insensitive.
            return f"\nO sabor {flavor.title()} já está disponível!"
        else:
            self.flavors.append(flavor.title())                                     # Correção: Adiciona flavor formatado.
            return f"Sabor {flavor.title()} adicionado ao estoque com sucesso!"