from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import datetime

def test_task_completion():
    t = Task("Feed", "08:00", "daily")
    assert not t.completed
    t.mark_complete()
    assert t.completed

def test_add_task_to_pet():
    pet = Pet("Barkus", "dog")
    t = Task("Walk", "09:00", "daily")
    pet.add_task(t)
    assert t in pet.tasks

def test_owner_add_pet():
    owner = Owner("Alex")
    pet = Pet("Leo", "cat")
    owner.add_pet(pet)
    assert pet in owner.pets

def test_scheduler_sort_by_time():
    owner = Owner("Alex")
    pet = Pet("Leo", "cat")
    t1 = Task("Feed", "09:00", "daily")
    t2 = Task("Walk", "08:00", "daily")
    pet.add_task(t1)
    pet.add_task(t2)
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time(owner.get_all_tasks())
    assert sorted_tasks[0].description == "Walk"
    assert sorted_tasks[1].description == "Feed"

def test_scheduler_conflict_detection():
    owner = Owner("Alex")
    pet1 = Pet("Barkus", "dog")
    pet2 = Pet("Leo", "cat")
    today = datetime.today().strftime("%Y-%m-%d")
    t1 = Task("Feed", "10:00", "daily", due_date=today)
    t2 = Task("Medication", "10:00", "daily", due_date=today)
    pet1.add_task(t1)
    pet2.add_task(t2)
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())
    assert conflicts, "Should detect a conflict when two tasks are at the same time."
