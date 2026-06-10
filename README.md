# 🧠 Task Scheduler (CSP)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI](https://img.shields.io/badge/AI-CSP-orange)
![Status](https://img.shields.io/badge/Status-Ongoing-yellow)
# 📅 Task Scheduler CSP

A Python task scheduling application inspired by **Harvard CS50AI Constraint Satisfaction Problems (CSP)**.

The project models tasks and available time slots, applies scheduling constraints, prioritizes important work, and automatically creates events in **Google Calendar** using the Google Calendar API.

The long-term vision is to evolve this project into an AI-powered personal planning assistant capable of transforming natural language requests into an optimized daily schedule.

---

# ✨ Features

* 📌 Object-Oriented task and scheduling model
* 🧠 Constraint Satisfaction Problem (CSP) inspired design
* ⚡ Priority-based task scheduling
* 🚫 Prevents overlapping tasks
* ⏱️ Ensures task duration fits available time slots
* 🌙 Prevents study-related tasks from being scheduled at night
* 📅 Automatic Google Calendar event creation
* 🔐 Secure OAuth2 authentication with Google APIs
* 🔄 Real-time synchronization between the scheduler and Google Calendar
- Convert natural language plans into structured tasks using Ollama
- Prioritize tasks automatically
- Runs locally using Ollama (no OpenAI API required)

---

# 🏗️ System Workflow

Brain dump
↓
Local Ollama
↓
Task extraction
↓
JSON validation
↓
Priority scheduling
↓
Google Calendar events
↓
Events appear on your actual phone

---

# 🧩 AI & Computer Science Concepts Used

## Constraint Satisfaction Problems (CSP)

The scheduler is designed around the idea of Constraint Satisfaction Problems, a classical Artificial Intelligence technique where variables must be assigned values while satisfying a set of rules.

### Variables

* Tasks

### Domains

* Available time slots

### Constraints

* Only one task can occupy a time slot.
* Task duration must fit the available slot.
* Study-related tasks cannot be scheduled at night.
* Higher priority tasks are scheduled first.

---

## Object-Oriented Programming (OOP)

The project models real-world entities as objects:

* Tasks
* Time Slots

This design makes the system modular and easy to extend with additional scheduling rules.

---

## Greedy Scheduling

The current implementation uses a simple greedy assignment strategy:

1. Sort tasks by priority.
2. Assign the next available valid time slot.

This serves as the foundation for future CSP backtracking algorithms.

---

## API Integration

The application integrates directly with the Google Calendar API using OAuth2 authentication.

After scheduling, tasks are automatically converted into real Google Calendar events.

---

# ⚙️ Technologies Used

* Python
* Google Calendar API
* OAuth2 Authentication
* Object-Oriented Programming
* Constraint Satisfaction Problems (CSP)
* Scheduling Algorithms

---

# 🚀 Example

Input:
"I need to cook, study machine learning for 2 hours, and go to the gym."

Output:
09:00–11:00 Study machine learning
11:00–12:00 Cook
12:00–13:00 Go to the gym

→ Events are added directly to Google Calendar.
---

# 🔮 Future Roadmap

## Version 2 — Enhanced CSP Engine

* Full constraint checking during scheduling
* Dynamic slot validation
* Constraint propagation
* Backtracking search algorithm

---

## Version 3 — AI Integration

Natural language task extraction using a local Large Language Model (LLM).

Example:

```
"I need to study SQL, go to the gym, and finish my Coursera lecture tomorrow."
```

↓

AI extracts structured tasks.

↓

Scheduler generates an optimized schedule.

↓

Google Calendar is automatically updated.

---

## Version 4 — Smart Personal Planner

* Automatic task prioritization
* Daily schedule optimization
* Automatic rescheduling
* Google Tasks integration
* Recurring tasks
* Deadline awareness
* Work-life balance constraints

---

# 🎓 Inspiration

This project was developed while studying:

* Harvard CS50AI
* Machine Learning Specialization
* Advanced Learning Algorithms

The objective is to combine classical Artificial Intelligence techniques with practical automation tools to build intelligent productivity systems.

---

# 📈 Project Vision

The current implementation demonstrates how classical AI concepts such as Constraint Satisfaction Problems can be applied to real-world scheduling.

The long-term goal is to evolve this project into a fully autonomous AI scheduling assistant capable of understanding user intentions, optimizing daily plans, and interacting directly with productivity tools.
