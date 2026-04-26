from typing import List

class Task:
    def __init__(self, description: str, time: str, frequency: str, completed: bool = False, pet_name: str = None, due_date: str = None):
        """Initialize a Task with description, time, frequency, completion status, optional pet name, and due date (YYYY-MM-DD)."""
        self.description = description
        self.time = time  # e.g., '08:00', 'evening'
        self.frequency = frequency  # e.g., 'daily', 'weekly'
        self.completed = completed
        self.pet_name = pet_name
        self.due_date = due_date  # e.g., '2026-04-04'

    def mark_complete(self):
        """Mark the task as complete."""
        self.completed = True

    def __repr__(self):
        """Return a string representation of the task."""
        status = '✓' if self.completed else '✗'
        return f"{self.time} - {self.description} ({self.frequency}) [{status}]"

class Pet:
    def __init__(self, name: str, species: str):
        """Initialize a Pet with name and species."""
        self.name = name
        self.species = species
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the pet's task list. Sets the pet_name on the task for filtering."""
        task.pet_name = self.name
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return the list of tasks for the pet."""
        return self.tasks

    def __repr__(self):
        """Return a string representation of the pet."""
        return f"{self.name} the {self.species}"

class Owner:
    """
    Represents an owner with a name and a list of pets. Provides methods to
    add pets, retrieve all tasks from owned pets, and display a string
    representation of the owner.
    """
    def __init__(self, name: str):
        """Initialize an Owner with a name."""
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks from all pets owned by the owner."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.get_tasks())
        return tasks

    def __repr__(self):
        """Return a string representation of the owner."""
        return f"Owner: {self.name}"

class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize a Scheduler with an owner."""
        self.owner = owner

    def get_todays_schedule(self) -> List[Task]:
        """Return today's schedule of tasks sorted by time."""
        # For demo, just return all tasks (could filter by date/time/frequency)
        return sorted(self.owner.get_all_tasks(), key=lambda t: t.time)

    def mark_task_complete(self, task: Task):
        """Mark a given task as complete. If recurring, create next occurrence automatically."""
        from datetime import datetime, timedelta
        task.mark_complete()
        # Automate recurring tasks
        if task.frequency in ("daily", "weekly"):
            # Ask Copilot: How to use timedelta to add days/weeks to a date string?
            # Copilot: Use datetime.strptime to parse, then add timedelta(days=1) or timedelta(weeks=1), then strftime to format.
            if task.due_date:
                try:
                    current_date = datetime.strptime(task.due_date, "%Y-%m-%d")
                except ValueError:
                    current_date = datetime.today()
            else:
                current_date = datetime.today()
            if task.frequency == "daily":
                next_date = current_date + timedelta(days=1)
            elif task.frequency == "weekly":
                next_date = current_date + timedelta(weeks=1)
            # Create new task for next occurrence
            new_task = Task(
                description=task.description,
                time=task.time,
                frequency=task.frequency,
                pet_name=task.pet_name,
                due_date=next_date.strftime("%Y-%m-%d")
            )
            # Add to the correct pet
            for pet in self.owner.pets:
                if pet.name == task.pet_name:
                    pet.add_task(new_task)
                    break

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """
        Detect if two tasks for the same or different pets are scheduled at the same time and date.
        Returns a list of warning messages for conflicts found.
        Lightweight: uses a dict to group by (due_date, time), warns if more than one task at same slot.
        """
        # Ask Copilot: What's a lightweight way to detect time conflicts in a list of tasks?
        # Copilot: Use a dict to group by (date, time), warn if more than one task per slot.
        from collections import defaultdict
        slot_dict = defaultdict(list)
        for task in tasks:
            slot = (task.due_date, task.time)
            slot_dict[slot].append(task)
        warnings = []
        for slot, slot_tasks in slot_dict.items():
            if len(slot_tasks) > 1:
                pets = ', '.join([t.pet_name or 'Unknown' for t in slot_tasks])
                warnings.append(f"Conflict: {len(slot_tasks)} tasks scheduled at {slot[1]} on {slot[0]} for pets: {pets}")
        return warnings

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """
        Return a list of Task objects sorted by their time attribute (HH:MM format).
        Uses a lambda as the key for sorted().
        """
        # Inline Chat: How do I use a lambda as a key to sort strings in 'HH:MM' format?
        # Copilot: Use key=lambda t: t.time or key=lambda t: datetime.strptime(t.time, '%H:%M') if you want chronological order.
        from datetime import datetime
        def parse_time(t):
            try:
                return datetime.strptime(t.time, '%H:%M')
            except ValueError:
                return datetime.strptime('23:59', '%H:%M')  # fallback for non-HH:MM
        return sorted(tasks, key=parse_time)

    def filter_tasks(self, tasks: List[Task], completed: bool = None, pet_name: str = None) -> List[Task]:
        """
        Filter tasks by completion status and/or pet name.
        If completed is None, do not filter by completion.
        If pet_name is provided, only include tasks for that pet.
        """
        filtered = tasks
        if completed is not None:
            filtered = [t for t in filtered if t.completed == completed]
        if pet_name is not None:
            # Find tasks belonging to the specified pet
            filtered = [t for t in filtered if hasattr(t, 'pet_name') and t.pet_name == pet_name]
        return filtered
