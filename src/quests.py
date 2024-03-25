class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward
        self.completed = False

    def check_completion(self):
        return self.completed

    def complete(self):
        self.completed = True
        print(f"Quest '{self.name}' completed! You received {self.reward} gold.")


class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def complete_quest(self, quest_name):
        for quest in self.quests:
            if quest.name == quest_name:
                if not quest.completed:
                    quest.complete()
                else:
                    print("Quest already completed.")
                return
        print("Quest not found.")

# Example usage:
# quest1 = Quest("Defeat the Goblin", "Defeat the Goblin terrorizing the village.", 50)
# quest2 = Quest("Retrieve the Artifact", "Retrieve the ancient artifact hidden in the cave.", 100)
# quest_manager = QuestManager()
# quest_manager.add_quest(quest1)
# quest_manager.add_quest(quest2)
# quest_manager.complete_quest("Defeat the Goblin")
