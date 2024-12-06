from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:

    def test_flavors_available(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", ["Chocolate", "Baunilha", "Morango"])
        result = ice_cream_stand.flavors_available()
        expected = (
            "No momento temos os seguintes sabores de sorvete disponíveis:\n"
            "- Chocolate\n- Baunilha\n- Morango"
        )
        assert result == expected, "A lista de sabores disponíveis está incorreta."

    def test_flavors_available_no_stock(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", [])
        result = ice_cream_stand.flavors_available()
        expected = "Estamos sem estoque atualmente!"
        assert result == expected, "A mensagem para estoque vazio está incorreta."

    def test_find_flavor_available(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", ["Chocolate", "Baunilha", "Morango"])
        result = ice_cream_stand.find_flavor("Chocolate")
        expected = "Temos o sabor Chocolate disponível!"
        assert result == expected, "O método não identificou o sabor disponível corretamente."

    def test_find_flavor_unavailable(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", ["Chocolate", "Baunilha", "Morango"])
        result = ice_cream_stand.find_flavor("Pistache")
        expected = "Não temos o sabor Pistache no momento!"
        assert result == expected, "O método não identificou corretamente que o sabor está indisponível."

    def test_find_flavor_no_stock(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", [])
        result = ice_cream_stand.find_flavor("Chocolate")
        expected = "Estamos sem estoque atualmente!"
        assert result == expected, "A mensagem para busca em estoque vazio está incorreta."

    def test_add_flavor_new(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", ["Chocolate", "Baunilha"])
        result = ice_cream_stand.add_flavor("Morango")
        expected = "Morango adicionado ao estoque!"
        assert result == expected, "O sabor não foi adicionado corretamente."
        assert "Morango" in ice_cream_stand.flavors, "O sabor não foi registrado na lista."

    def test_add_flavor_existing(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", ["Chocolate", "Baunilha"])
        result = ice_cream_stand.add_flavor("Chocolate")
        expected = "Sabor já disponível!"
        assert result == expected, "O método não reconheceu que o sabor já estava disponível."

    def test_add_flavor_no_stock(self):
        ice_cream_stand = IceCreamStand("Sorveteria do Bairro", "Sorveteria", [])
        result = ice_cream_stand.add_flavor("Pistache")
        expected = "Pistache adicionado ao estoque!"
        assert result == expected, "O sabor não foi adicionado corretamente em estoque vazio."
        assert "Pistache" in ice_cream_stand.flavors, "O sabor não foi registrado corretamente em estoque vazio."
