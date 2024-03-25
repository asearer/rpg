import unittest
from quests import Quest, QuestManager

class TestQuests(unittest.TestCase):
    def test_quest_completion(self):
        quest = Quest("Test Quest", "Test quest description", 50)
        self.assertFalse(quest.completed)
        quest.complete()
        self.assertTrue(quest.completed)

    def test_quest_manager(self):
        quest1 = Quest("Test Quest 1", "Test quest description", 50)
        quest2 = Quest("Test Quest 2", "Test quest description", 100)
        quest_manager = QuestManager()
        quest_manager.add_quest(quest1)
        quest_manager.add_quest(quest2)
        quest_manager.complete_quest("Test Quest 1")
        self.assertTrue(quest1.completed)
        self.assertFalse(quest2.completed)

if __name__ == '__main__':
    unittest.main()
