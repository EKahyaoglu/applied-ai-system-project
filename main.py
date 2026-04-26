from pawpal_system import Owner, Pet, Task, Scheduler
from retriever import Retriever
from agent import Agent
from datetime import datetime

# --- Setup demo data ---
owner = Owner("George")
pet1 = Pet("Barkus", "dog")
pet2 = Pet("Leo", "cat")
owner.add_pet(pet1)
owner.add_pet(pet2)
today = datetime.today().strftime("%Y-%m-%d")
pet1.add_task(Task("Feed breakfast", "08:30", "daily", due_date=today))
pet1.add_task(Task("Morning walk", "08:00", "daily", due_date=today))
pet2.add_task(Task("Grooming", "18:00", "weekly", due_date=today))
pet2.add_task(Task("Vet visit", "09:00", "monthly", due_date=today))
pet1.add_task(Task("Playtime", "10:00", "weekly", due_date=today))
pet2.add_task(Task("Medication", "10:00", "daily", due_date=today))

# --- Agentic Workflow + RAG Demo ---
retriever = Retriever()
scheduler = Scheduler(owner)
agent = Agent(owner, scheduler, retriever)

# Example: User gives a goal
goal = "Make sure to feed the pets today!"
agent.handle_goal(goal)

# Show all tasks after agent acts
print("\nAll tasks after agent workflow:")
for pet in owner.pets:
    print(f"{pet.name}: {pet.tasks}")


# Print all tasks unsorted
print("\nAll Tasks (Unsorted):")
for task in owner.get_all_tasks():
    print(task)

# Detect and print conflicts
conflicts = scheduler.detect_conflicts(owner.get_all_tasks())
if conflicts:
    print("\nTask Conflicts Detected:")
    for warning in conflicts:
        print(warning)
else:
    print("\nNo task conflicts detected.")

# Print all tasks sorted by time
sorted_tasks = scheduler.sort_by_time(owner.get_all_tasks())
print("\nAll Tasks (Sorted by Time):")
for task in sorted_tasks:
    print(task)

# Print only completed tasks
completed_tasks = scheduler.filter_tasks(owner.get_all_tasks(), completed=True)
print("\nCompleted Tasks:")
for task in completed_tasks:
    print(task)

# Print only tasks for one pet
jr_tasks = scheduler.filter_tasks(owner.get_all_tasks(), pet_name="Leo")
print("\nTasks for Leo:")
for task in jr_tasks:
    print(task)
