from unittest import TestCase
from game_scene import game_start

class Test(TestCase):
    def test_game_start(self):
        name=["test_game_start_1","test_game_start_0"]
        is_AI=[1,0]
        for each_name in name:
            for each_AI in is_AI:
                game_start(each_name,each_AI)
