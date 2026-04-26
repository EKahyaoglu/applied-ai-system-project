# Portfolio Artifact

**GitHub Repository:**
https://github.com/EKahyaoglu/applied-ai-system-project

**Video Link:**
https://www.youtube.com/watch?v=zY8fmFipCf8&feature=youtu.be

# PawPal Scheduler

## Title & Summary

**PawPal Scheduler** is a smart assistant for pet owners, designed to automate and optimize daily pet care routines. It helps users track, schedule, and manage all pet-related tasks—feeding, walks, medication, grooming, and more—while leveraging advanced AI to plan, retrieve relevant information, and adapt to changing needs. This project matters because it brings together agentic AI workflows and retrieval-augmented generation (RAG) to make pet care reliable, explainable, and stress-free.

---

## Architecture Overview

PawPal Scheduler is built around a modular, object-oriented core:
- **Owner, Pet, Task, Scheduler:** Represent the real-world entities and handle scheduling, recurrence, and conflict detection.
- **Retriever (RAG):** Searches a knowledge base (assets) for relevant care tips or instructions.
- **Agent (Agentic Workflow):** Accepts user goals, plans steps, retrieves information as needed, acts (adds/schedules tasks), and checks its own work.
- **Streamlit UI (optional):** For user-friendly interaction (not required to run core logic).

**System Diagram:**
- Owner → Pet(s) → Task(s)
- Scheduler manages all tasks for an owner
- Agent orchestrates planning and retrieval
- Retriever provides context-aware information

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/applied-ai-system-final.git
   cd applied-ai-system-final
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate   # On Windows
   # Or: source .venv/bin/activate   # On Mac/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main demo:**
   ```bash
   python main.py
   ```

5. *(Optional)* To run tests:
   ```bash
   python -m pytest
   ```

---

## Example Interactions

**Example 1: Agentic Workflow + RAG**

_Input:_
```
goal = "Make sure to feed the pets today!"
agent.handle_goal(goal)
```

_Output:_
```
Received goal: Make sure to feed the pets today!
Retrieved info: ['Feeding pets should be done in the morning and evening. Make sure to provide fresh water.', ...]
Added task for Biscuits: 09:00 - Feed pet (agent) (daily) [✗]
Current tasks: [08:30 - Feed breakfast (daily) [✗], ..., 09:00 - Feed pet (agent) (daily) [✗], ...]
```

**Example 2: Conflict Detection**

_Input:_
```
pet1.add_task(Task("Playtime", "10:00", "weekly", due_date=today))
pet2.add_task(Task("Medication", "10:00", "daily", due_date=today))
conflicts = scheduler.detect_conflicts(owner.get_all_tasks())
print(conflicts)
```

_Output:_
```
['Conflict: 2 tasks scheduled at 10:00 on 2026-04-26 for pets: Biscuits, Jolly Rancher']
```

**Example 3: Recurring Task Completion**

_Input:_
```
scheduler.mark_task_complete(pet1.tasks[0])  # Mark 'Feed breakfast' as complete
```

_Output:_
```
# New 'Feed breakfast' task scheduled for the next day
```

---

## Design Decisions

- **Agentic Workflow:** Enables the system to plan, act, and self-check, making it robust and extensible.
- **Retrieval-Augmented Generation:** Allows the agent to provide context-aware advice and explanations, improving user trust and experience.
- **Modular OOP Design:** Owner, Pet, Task, and Scheduler are decoupled for maintainability and future expansion.
- **Simplicity vs. Complexity:** Focused on time-based conflicts and recurrence for clarity; avoided over-complicating with duration overlaps or deep preference modeling.

---

## Testing Summary

- **What worked:** Core scheduling, recurrence, and conflict detection logic are reliable and covered by tests. The agent and retriever modules integrate smoothly.
- **What didn’t:** More advanced planning (e.g., multi-step reasoning, deep preference learning) was out of scope for this version.
- **What I learned:** Iterative development and modular design made it easy to add AI features without breaking core logic. Testing early and often caught edge cases in recurrence and conflict detection.

---

## Reflection

Building PawPal Scheduler taught me how to combine classic software engineering with modern AI techniques. With this project, I learned to:
- Design for extensibility (so new AI features can be added easily)
- Use agentic workflows to automate complex, multi-step tasks
- Integrate retrieval systems for explainable, context-aware AI
- Balance user needs, technical feasibility, and clarity in both code and UI