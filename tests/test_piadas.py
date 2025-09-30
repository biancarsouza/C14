import unittest
from unittest.mock import patch, Mock
import sys
import os
import requests

# Adiciona o diretório src ao path para importar o módulo
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Importa a função main do módulo correto
from src.piadas.__main__ import main

class TestPiadas(unittest.TestCase):
    
    # Casos positivos (10 testes)
    
    @patch('piadas.__main__.requests.get')
    def test_main_successful_response(self, mock_get):
        """Testa resposta bem-sucedida da API"""
        # Mock da resposta
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Por que o programador foi à praia?",
            "punchline": "Para surfar na web!"
        }
        mock_get.return_value = mock_response
        
        # Captura a saída do print
        with patch('builtins.print') as mock_print:
            main()
            
            # Verifica se os prints foram chamados corretamente
            expected_calls = [
                unittest.mock.call("Piada do dia:"),
                unittest.mock.call("Por que o programador foi à praia?"),
                unittest.mock.call("Para surfar na web!")
            ]
            mock_print.assert_has_calls(expected_calls)
    
    @patch('piadas.__main__.requests.get')
    def test_main_different_joke(self, mock_get):
        """Testa piada diferente"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Qual é o café mais perigoso do mundo?",
            "punchline": "O ex-presso!"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Qual é o café mais perigoso do mundo?")
            mock_print.assert_any_call("O ex-presso!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_special_characters(self, mock_get):
        """Testa piada com caracteres especiais"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Piada com acentuação: café",
            "punchline": "Funciona com ç e á!"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Piada com acentuação: café")
    
    @patch('piadas.__main__.requests.get')
    def test_main_empty_strings(self, mock_get):
        """Testa strings vazias (ainda deve imprimir)"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "",
            "punchline": ""
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            # Deve imprimir as strings vazias
            mock_print.assert_any_call("")
    
    @patch('piadas.__main__.requests.get')
    def test_main_long_joke(self, mock_get):
        """Testa piada longa"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Por que os desenvolvedores preferem o modo escuro?",
            "punchline": "Porque a luz atrai bugs!"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Por que os desenvolvedores preferem o modo escuro?")
    
    @patch('piadas.__main__.requests.get')
    def test_main_multiple_calls(self, mock_get):
        """Testa múltiplas chamadas"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Teste",
            "punchline": "Funciona"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print'):
            for _ in range(3):
                main()
            self.assertEqual(mock_get.call_count, 3)
    
    @patch('piadas.__main__.requests.get')
    def test_main_extra_fields(self, mock_get):
        """Testa campos extras no JSON"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Teste",
            "punchline": "Funciona",
            "extra": "campo"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Teste")
            mock_print.assert_any_call("Funciona")
    
    @patch('piadas.__main__.requests.get')
    def test_main_numeric_values(self, mock_get):
        """Testa valores numéricos"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "123",
            "punchline": "456"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("123")
            mock_print.assert_any_call("456")
    
    @patch('piadas.__main__.requests.get')
    def test_main_no_exception(self, mock_get):
        """Testa que não levanta exceção"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Teste",
            "punchline": "OK"
        }
        mock_get.return_value = mock_response
        
        try:
            with patch('builtins.print'):
                main()
            success = True
        except:
            success = False
        
        self.assertTrue(success)
    
    @patch('piadas.__main__.requests.get')
    def test_main_normal_operation(self, mock_get):
        """Testa operação normal"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Normal",
            "punchline": "Operation"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Piada do dia:")
    
    # Casos negativos (10 testes)
    
    @patch('piadas.__main__.requests.get')
    def test_main_404_error(self, mock_get):
        """Testa erro 404"""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_500_error(self, mock_get):
        """Testa erro 500"""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_timeout(self, mock_get):
        """Testa timeout"""
        mock_get.side_effect = requests.exceptions.Timeout()
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_connection_error(self, mock_get):
        """Testa erro de conexão"""
        mock_get.side_effect = requests.exceptions.ConnectionError()
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_json_error(self, mock_get):
        """Testa erro de JSON"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("JSON error")
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_missing_setup(self, mock_get):
        """Testa campo setup faltando"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "punchline": "Só punchline"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_missing_punchline(self, mock_get):
        """Testa campo punchline faltando"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": "Só setup"
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_empty_json(self, mock_get):
        """Testa JSON vazio"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_null_values(self, mock_get):
        """Testa valores null"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "setup": None,
            "punchline": None
        }
        mock_get.return_value = mock_response
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")
    
    @patch('piadas.__main__.requests.get')
    def test_main_general_exception(self, mock_get):
        """Testa exceção geral"""
        mock_get.side_effect = Exception("General error")
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Não encontrei nenhuma piada!")

if __name__ == '__main__':
    unittest.main()