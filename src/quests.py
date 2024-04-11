class Quest:
    def __init__(self, name, description, reward, difficulty=1, dependencies=None, completion_conditions=None):
        self.name = name
        self.description = description
        self.reward = reward
        self.completed = False
        self.difficulty = difficulty
        self.dependencies = dependencies if dependencies else []
        self.completion_conditions = completion_conditions if completion_conditions else []

    def check_completion(self):
        return self.completed

    def complete(self):
        self.completed = True
        print(f"Quest '{self.name}' completed! You received {self.reward} gold.")

    def get_difficulty(self):
        return self.difficulty

    def get_dependencies(self):
        return self.dependencies

    def get_completion_conditions(self):
        return self.completion_conditions


class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def complete_quest(self, quest_name):
        for quest in self.quests:
            if quest.name == quest_name:
                if not quest.completed:
                    # Check if dependencies are met
                    dependencies_met = all(dep.check_completion() for dep in quest.get_dependencies())
                    if dependencies_met:
                        # Check if completion conditions are met
                        conditions_met = all(cond() for cond in quest.get_completion_conditions())
                        if conditions_met:
                            quest.complete()
                        else:
                            print("Completion conditions not met.")
                    else:
                        print("Quest dependencies not met.")
                else:
                    print("Quest already completed.")
                return
        print("Quest not found.")


# Example usage:
quest1 = Quest("Defeat the Goblin", "Defeat the Goblin terrorizing the village.", 50, difficulty=2)
quest2 = Quest("Retrieve the Artifact", "Retrieve the ancient artifact hidden in the cave.", 100, difficulty=3)
quest3 = Quest("Explore the Forest", "Explore the mysterious forest.", 80, dependencies=[quest1])
quest4 = Quest("Craft a Potion", "Craft a powerful potion.", 120, completion_conditions=[lambda: player.level >= 5])
quest_manager = QuestManager()
quest_manager.add_quest(quest1)
quest_manager.add_quest(quest2)
quest_manager.add_quest(quest3)
quest_manager.add_quest(quest4)

# Player class (for quest condition example)
class Player:
    def __init__(self):
        self.level = 1

player = Player()
player.level = 5  # Simulating player reaching level 5

quest_manager.complete_quest("Craft a Potion")
