# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
- My initial UML design included Owner, Pet, Task, and Scheduler classes, each with clear responsibilities.

- Owner managed a list of pets, Pet managed its own tasks, Task stored details like time and frequency, and Scheduler handled sorting, filtering, and conflict detection.

- I wanted each class to have a single, focused responsibility to keep the design modular and easy to extend.

**b. Design changes**
- The design evolved as I implemented recurring tasks and conflict detection.

- I added a due_date attribute to Task to support scheduling future occurrences, which wasn't in my original plan.

- Some methods moved between classes as I realized where the logic fit best, especially for automating recurring tasks in the Scheduler.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**
- The scheduler considers time (HH:MM), frequency (daily, weekly, monthly), and completion status for each task.

- I focused on time and frequency because they are the most important for pet care routines and reminders.

- I decided to prioritize simplicity and reliability over adding complex preferences or priorities, since most users just need to know what to do and when.


**b. Tradeoffs**
- Our scheduler only checks for exact time matches (tasks scheduled at the same time and date), not for overlapping durations. This means if two tasks overlap but do not start at the exact same time, the conflict will not be detected.

- This tradeoff is reasonable because most pet care tasks are short and occur at specific times (e.g., feeding, walking), so exact time conflicts are the most common and relevant for users. Checking for overlapping durations would add complexity without significant benefit for the typical use case.

---

## 3. AI Collaboration

**a. How you used AI**
- I used AI for brainstorming class structure and method responsibilities, which helped me get started quickly.

- GitHub Copilot was especially useful for generating code snippets and suggesting ways to handle recurring tasks and conflict detection.

- The most helpful prompts were specific, like asking how to use Python's timedelta or how to simplify a particular algorithm.


**b. Judgment and verification**
- There were times when Copilot suggested a more "Pythonic" solution that was harder to read, so I chose to keep my original, more readable version.

- I always reviewed AI-generated code for clarity and tested it in the terminal to make sure it worked as expected.

- If a suggestion seemed too complex, I asked for a simpler or more explicit version and compared the results.

---

## 4. Testing and Verification

**a. What you tested**
- I tested adding tasks out of order, sorting them, and filtering by completion and pet name.

- I checked that recurring tasks were created automatically and that time conflicts were detected and reported.

- These tests were important to ensure the scheduler logic worked for real-world pet care scenarios.

**b. Confidence**
- I am confident the main features work, since I saw the expected output in the terminal for all test cases.

- If I had more time, I would test edge cases like missing or malformed times, overlapping durations, and tasks with no pet assigned.

- I would also add tests for monthly and one-off tasks to make sure they are handled correctly.

---

## 5. Reflection

**a. What went well**
- I'm most satisfied with how quickly I could iterate on the scheduler logic using AI suggestions.

- The conflict detection and recurring task automation features worked smoothly and felt robust.


**b. What you would improve**
- I would improve the UI/UX for adding and viewing tasks, maybe with a simple web or mobile interface.

- I'd also refine the conflict detection to handle overlapping durations, not just exact time matches.


**c. Key takeaway**
- I learned that AI is a great partner for rapid prototyping, but it's important to review and adapt its suggestions for clarity and maintainability.

- Clear, specific prompts lead to much better AI-generated code and explanations.
