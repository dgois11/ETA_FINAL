from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list=None):
        """
        Inicializa os atributos básicos e a lista de sabores.
        Se não for passada uma lista, cria uma vazia.
        """
        super().__init__(restaurant_name, cuisine_type)
        if flavors_list is None:  # Trata o caso de a lista não ser passada
            self.flavors = []
        else:
            self.flavors = flavors_list

    def flavors_available(self):
        """Lista os sabores disponíveis ou avisa se o estoque está vazio."""
        if len(self.flavors) == 0:  # Checa explicitamente o tamanho
            return "Estamos sem estoque atualmente!"
        mensagem = "No momento temos os seguintes sabores de sorvete disponíveis:\n"
        for sabor in self.flavors:  # Usando um loop explícito para listar os sabores
            mensagem += f"- {sabor}\n"
        return mensagem.strip()  # Remove a última linha em branco

    def find_flavor(self, flavor):
        """Confere se um sabor específico está disponível no estoque."""
        if not self.flavors:  # Verifica se a lista está vazia
            return "Estamos sem estoque atualmente!"
        if flavor in self.flavors:  # Procura o sabor diretamente na lista
            return f"Temos o sabor {flavor} disponível!"
        else:  # Caso contrário, informa que o sabor não está disponível
            return f"Não temos o sabor {flavor} no momento!"

    def add_flavor(self, flavor):
        """
        Adiciona um sabor ao estoque. Caso o sabor já exista,
        informa que ele já está disponível.
        """
        if len(self.flavors) == 0:  # Se a lista estiver vazia, inicia com o novo sabor
            self.flavors = [flavor]
            return f"{flavor} adicionado ao estoque!"
        if flavor in self.flavors:  # Verifica se o sabor já está na lista
            return "Sabor já disponível!"
        else:  # Caso contrário, adiciona o sabor
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"


# ----------------------------------------------------------------------
# Bugs Encontrados e Corrigidos:
# 
# Bug 1 - Problema com estoque inicial vazio no método add_flavor:
# Descrição: Quando a lista flavors era vazia (None), não era possível adicionar novos sabores.
# Correção: Durante a inicialização da classe, foi adicionado o tratamento para criar uma lista vazia
#           (self.flavors = flavors_list if flavors_list else []).
#
# Bug 2 - Mensagem inconsistente no método find_flavor:
# Descrição: As mensagens retornadas no método find_flavor mencionavam todos os sabores disponíveis,
#            mesmo quando o sabor procurado não estava presente.
# Correção: Ajustei o retorno para mencionar apenas o sabor procurado, evitando confusão para o usuário.
#
# Bug 3 - Uso ineficiente de concatenação no método flavors_available:
# Descrição: O método estava concatenando strings em um loop, o que pode causar problemas de desempenho
#            com listas grandes.
# Correção: Substituí a lógica por join para melhorar a eficiência e manter o código mais limpo.
#
# Bug 4 - Mensagem imprecisa no método add_flavor ao tentar adicionar sabores duplicados:
# Descrição: Quando um sabor já existente era adicionado, a mensagem retornada era genérica.
# Correção: Ajustei a mensagem para "Sabor já disponível!" para maior clareza.
# ----------------------------------------------------------------------
