from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available_with_flavors(self):
        """Testa se a lista de sabores disponíveis é exibida corretamente."""
        stand = IceCreamStand("Gelateria", "Sorveteria", ["Morango", "Chocolate"])
        result = stand.flavors_available()

        assert "Morango" in result and "Chocolate" in result

    def test_flavors_available_no_stock(self):
        """Testa o retorno quando não há sabores disponíveis."""
        stand = IceCreamStand("Gelateria", "Sorveteria")
        result = stand.flavors_available()

        assert result == "Estamos sem estoque atualmente!"

    def test_find_flavor_available(self):
        """Testa se encontra um sabor disponível."""
        stand = IceCreamStand("Gelateria", "Sorveteria", ["Morango", "Chocolate"])
        result = stand.find_flavor("Morango")

        assert result == "Temos o sabor Morango no momento!"

    def test_find_flavor_not_available(self):
        """Testa se não encontra um sabor indisponível."""
        stand = IceCreamStand("Gelateria", "Sorveteria", ["Morango", "Chocolate"])
        result = stand.find_flavor("Baunilha")

        assert result == "Não temos o sabor Baunilha no momento!"

    def test_find_flavor_case_insensitive(self):
        """Testa se a busca por sabores é case-insensitive."""
        stand = IceCreamStand("Gelateria", "Sorveteria", ["Morango", "Chocolate"])
        result = stand.find_flavor("morango")

        assert result == "Temos o sabor Morango no momento!"

    def test_add_flavor_new(self):
        """Testa a adição de um novo sabor."""
        stand = IceCreamStand("Gelateria", "Sorveteria", ["Morango"])
        result = stand.add_flavor("Chocolate")

        assert "Chocolate adicionado" in result
        assert "Chocolate" in stand.flavors

    def test_add_flavor_existing(self):
        """Testa a tentativa de adicionar um sabor já existente."""
        stand = IceCreamStand("Gelateria", "Sorveteria", ["Morango"])
        result = stand.add_flavor("Morango")

        assert result == "\nO sabor Morango já está disponível!"