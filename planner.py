from typing import List, Dict

class Owner:
    def __init__(self, name: str, preferences: Dict, available_time: int):
        self.name = name
        self.preferences = preferences
        self.available_time = available_time

class Pet:
    def __init__(self, name: str, pet_type: str, needs: Dict):
        self.name = name
        self.type = pet_type
        self.needs = needs

class Task:
    def __init__(self, name: str, task_type: str, duration: int, priority: int, constraints: Dict):
        self.name = name
        self.type = task_type
        self.duration = duration
        self.priority = priority
        self.constraints = constraints

class Plan:
    def __init__(self, tasks: List[Task], explanation: str):
        self.tasks = tasks
        self.explanation = explanation

class Scheduler:
    def generate_plan(self, owner: Owner, pet: Pet, tasks: List[Task]) -> Plan:
        # TODO: Implement scheduling logic
        pass

    def explain_plan(self, plan: Plan) -> str:
        # TODO: Implement explanation logic
        pass
