import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from agent import Agent
from retriever import Retriever
from datetime import datetime

st.set_page_config(page_title="PawPal Scheduler", page_icon="🐾", layout="centered")
st.title("🐾 PawPal Scheduler")

# --- Session State Setup ---
if "owner" not in st.session_state:
    st.session_state.owner = None
if "pets" not in st.session_state:
    st.session_state.pets = []
if "selected_pet" not in st.session_state:
    st.session_state.selected_pet = None
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Owner Info ---
st.header("Owner Information")
owner_name = st.text_input("Enter your name:")
if st.button("Set Owner"):
    st.session_state.owner = Owner(owner_name)
    st.success(f"Welcome, {owner_name}! Now add your pets.")

# --- Pet Management ---
st.header("Pet Management")
with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name", key="pet_name")
    species = st.selectbox("Species", ["dog", "cat", "other"], key="species")
    add_pet = st.form_submit_button("Add Pet")
    if add_pet and st.session_state.owner:
        new_pet = Pet(pet_name, species)
        st.session_state.pets.append(new_pet)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"Added {pet_name} the {species}!")

if st.session_state.pets:
    st.write("Your pets:")
    for i, pet in enumerate(st.session_state.pets):
        st.write(f"{i+1}. {pet.name} the {pet.species}")

# --- Task Management ---
st.header("Add Tasks for Your Pets")
if st.session_state.pets:
    pet_options = [pet.name for pet in st.session_state.pets]
    selected_pet_name = st.selectbox("Select pet to add a task for:", pet_options)
    selected_pet = next(
        (p for p in st.session_state.pets if p.name == selected_pet_name), None
    )
    task_desc = st.text_input("Task description", key="task_desc")
    task_time = st.time_input("Time (HH:MM)", key="task_time")
    frequency = st.selectbox(
        "Frequency", ["daily", "weekly", "monthly"], key="frequency"
    )
    due_date = st.date_input("Due date", key="due_date", value=datetime.today())
    add_task = st.button("Add Task")
    if add_task and selected_pet:
        t = Task(
            description=task_desc,
            time=task_time.strftime("%H:%M"),
            frequency=frequency,
            due_date=due_date.strftime("%Y-%m-%d"),
        )
        selected_pet.add_task(t)
        st.session_state.tasks.append(t)
        st.success(f"Added task '{task_desc}' for {selected_pet.name}.")

    # Show current tasks for selected pet
    if selected_pet:
        st.markdown(f"### Tasks for {selected_pet.name}")
        if selected_pet.tasks:
            st.table(
                [
                    {
                        "Description": t.description,
                        "Time": t.time,
                        "Frequency": t.frequency,
                        "Due Date": t.due_date,
                        "Completed": t.completed,
                    }
                    for t in selected_pet.tasks
                ]
            )
        else:
            st.info("No tasks for this pet yet.")

# --- Schedule Generation ---
st.header("Generate Daily Plan & Explanation")
if st.session_state.owner and st.session_state.pets and st.session_state.tasks:
    retriever = Retriever()
    scheduler = Scheduler(st.session_state.owner)
    agent = Agent(st.session_state.owner, scheduler, retriever)
    user_goal = st.text_input(
        "Describe your goal for today (e.g., 'Make sure all pets are fed and walked!'):",
        key="goal",
    )
    if st.button("Generate Plan"):
        agent.handle_goal(user_goal)
        all_tasks = st.session_state.owner.get_all_tasks()
        sorted_tasks = scheduler.sort_by_time(all_tasks)
        conflicts = scheduler.detect_conflicts(sorted_tasks)
        if conflicts:
            for warning in conflicts:
                st.warning(warning)
        st.markdown("### Today's Schedule (Sorted by Time)")
        st.table(
            [
                {
                    "Time": t.time,
                    "Task": t.description,
                    "Pet": t.pet_name,
                    "Frequency": t.frequency,
                    "Completed": t.completed,
                    "Due Date": t.due_date,
                }
                for t in sorted_tasks
            ]
        )
        st.markdown("### Plan Explanation")
        st.info(
            "The agent planned tasks based on your goal and retrieved relevant care tips as needed."
        )
else:
    st.info(
        "Please add an owner, at least one pet, and at least one task to generate a plan."
    )