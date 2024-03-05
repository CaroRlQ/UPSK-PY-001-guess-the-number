from function import random_number, play_start, number_player, input_number_player
from unittest import TestCase, mock
import pytest



class TestNumberPlayer(TestCase):
  @mock.patch("function.input_number_player")
  
  def test_input_number(self, mock_input):
   mock_input.return_value = '40'
 
   result = number_player()
  
   self.assertEqual(result, 40)
   
   
   
class TestGame:
    def test_play_start_correct_number(self):
        secret_number = 50
        number_player = 50
        assert play_start(number_player, secret_number) is True

    def test_play_start_number_too_low(self):
        secret_number = 50
        number_player = 40
        assert not play_start(number_player, secret_number)

    def test_play_start_number_too_high(self):
        secret_number = 50
        number_player = 60
        assert not play_start(number_player, secret_number)
        
        
        
def test_random_number_range():
  for _ in range(10):
    number = random_number()
    assert 0 <= number <= 100
