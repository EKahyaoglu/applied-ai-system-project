import streamlit as st

from pawpal_system import Owner, Pet, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "owner" not in st.session_state:
    st.session_state["owner"] = Owner("Your Name")

    # Add Pet UI Action
    if st.button("Add pet"):
        new_pet = Pet(pet_name, species)
        st.session_state["owner"].add_pet(new_pet)
        st.success(f"Added {pet_name} the {species}!")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

    # Display current pets
    if st.session_state["owner"].pets:
        st.write("Current pets:")
        for pet in st.session_state["owner"].pets:
            st.write(f"- {pet}")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

from pawpal_system import Scheduler

if st.button("Generate schedule"):
    # Build the schedule using Scheduler
    scheduler = Scheduler(st.session_state["owner"])
    all_tasks = st.session_state["owner"].get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(all_tasks)
    conflicts = scheduler.detect_conflicts(sorted_tasks)

    if conflicts:
        for warning in conflicts:
            st.warning(warning)
    else:
        st.success("No conflicts detected. Your schedule is ready!")

    # Prepare data for display
    if sorted_tasks:
        st.markdown("### Today's Schedule (Sorted by Time)")
        schedule_data = [
            {
                "Time": t.time,
                "Task": t.description,
                "Pet": t.pet_name,
                "Frequency": t.frequency,
                "Completed": "Yes" if t.completed else "No",
                "Due Date": t.due_date or "-"
            }
            for t in sorted_tasks
        ]
        st.table(schedule_data)
    else:
        st.info("No tasks scheduled yet. Add tasks and pets above.")
