from pawpal_system import Owner, Pet, Task, Scheduler
from retriever import Retriever

class Agent:
    def __init__(self, owner: Owner, scheduler: Scheduler, retriever: Retriever):
        self.owner = owner
        self.scheduler = scheduler
        self.retriever = retriever

    def handle_goal(self, goal: str):
        """
        Agentic workflow:
        1. Plan: Break down the goal into steps (simple demo: parse keywords)
        2. Retrieve: Use retriever to get info if needed
        3. Act: Add tasks, schedule, etc.
        4. Check: Confirm if goal is achieved
        """
        print(f"Received goal: {goal}")
        # Step 1: Plan (very simple demo)
        if "feed" in goal.lower():
            # Step 2: Retrieve info
            info = self.retriever.retrieve("feed")
            print("Retrieved info:", info)
            # Step 3: Act (add a feeding task)
            pet = self.owner.pets[0]  # demo: pick first pet
            task = Task("Feed pet (agent)", "09:00", "daily")
            pet.add_task(task)
            print(f"Added task for {pet.name}: {task}")
        # Step 4: Check
        tasks = self.owner.get_all_tasks()
        print(f"Current tasks: {tasks}")
        return tasks
