from pawpal_system import Owner, Pet, Task, Scheduler

# Create an owner
owner = Owner("Alex")

# Create two pets
pet1 = Pet("Biscuits", "dog")
pet2 = Pet("Jolly Rancher", "cat")

# Add pets to owner
owner.add_pet(pet1)
owner.add_pet(pet2)



# Add tasks to pets out of order, with due_date (today)
from datetime import datetime
today = datetime.today().strftime("%Y-%m-%d")
pet1.add_task(Task("Feed breakfast", "08:30", "daily", due_date=today))
pet1.add_task(Task("Morning walk", "08:00", "daily", due_date=today))
pet2.add_task(Task("Grooming", "18:00", "weekly", due_date=today))
pet2.add_task(Task("Vet visit", "09:00", "monthly", due_date=today))

# Add two tasks at the same time for conflict detection
pet1.add_task(Task("Playtime", "10:00", "weekly", due_date=today))
pet2.add_task(Task("Medication", "10:00", "daily", due_date=today))



# Create scheduler
scheduler = Scheduler(owner)

# Mark one recurring task as complete using Scheduler (triggers recurrence)
scheduler.mark_task_complete(pet1.tasks[0])  # Mark 'Feed breakfast' as complete

# Create scheduler
scheduler = Scheduler(owner)



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

# Print only tasks for Jolly Rancher
jr_tasks = scheduler.filter_tasks(owner.get_all_tasks(), pet_name="Jolly Rancher")
print("\nTasks for Jolly Rancher:")
for task in jr_tasks:
    print(task)
