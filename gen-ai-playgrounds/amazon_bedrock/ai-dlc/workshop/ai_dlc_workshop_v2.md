# AI-DLC Hands-On Tutorial: Build a Simple Task Manager

## Tutorial Overview
**Duration:** 3 hours  
**Project:** Personal Task Manager  
**Goal:** Learn AI-DLC by building something real you can use

You'll follow the complete AI-DLC methodology from AWS to build a working task manager application.

AI-DLC intentionally mirrors a familiar SDLC flow (requirements → design → build → operate), but reassigns responsibility so AI accelerates planning and generation while humans govern decisions.


**AI-DLC Three Phases:**
- **INCEPTION PHASE** *(Human-led, AI-expanded)*
- **CONSTRUCTION PHASE** *(AI-led, Human-validated)*
- **OPERATIONS PHASE** *(AI-assisted, Human-governed)*

---

## Personas (How the Team Shows Up in Each Phase)

### INCEPTION (Product + Dev + AI)
- **Product Owner** *(lead)* — sets intent, approves plans, accepts stories
- **Developers** — validate feasibility, clarify constraints, confirm boundaries
- **AI Assistant** — proposes plans, drafts artifacts, generates code/tests,and enforces traceability across the lifecycle (after human approval)


### CONSTRUCTION (Dev + QA + AI)
- **Developers** *(lead)* — implement, review, integrate
- **QA / Test mindset** — validates acceptance criteria, edge cases, test coverage
- **AI Assistant** — generates plans/code/tests/docs after approvals

### OPERATIONS (DevOps + Dev + AI)
- **DevOps / Platform** *(lead)* — deployment, pipelines, observability, reliability
- **Developers** — validate changes, own correctness, evolve safely
- **AI Assistant** — correlates signals, recommends fixes, suggests improvements

---

## What is a “Bolt” in this Workshop?

A **Bolt** is a short, validation-driven execution loop inside **Construction** (and often **Operations**) that produces a concrete, reviewable increment (code + tests + docs + validation).  
Bolts are **not** time-boxed sprints — they are **scope-boxed** chunks with explicit acceptance and validation.

### Bolt Naming for This Tutorial
- **Bolt 0 — Inception Artifacts Bolt** *(intent + stories + unit boundary)*
- **Bolt 1 — Design Bolt** *(component model)*
- **Bolt 2 — Build Bolt** *(core code)*
- **Bolt 3 — API Bolt** *(service interface)*
- **Bolt 4 — Deployability Bolt** *(cloud plan + IaC + validation)*
- **Bolt 5 — Operability Bolt** *(monitor/respond/scale patterns & runbooks)*

> ✅ **Where Bolt execution “really starts”:** right after **Activity 3 (Units Decomposition)**, when the Unit boundary is agreed.  
> From that point onward, each Construction activity is a distinct Bolt.

---

## Prerequisites
- Basic Python knowledge (for this workshop)
- Access to an AI assistant ([Kiro](https://kiro.dev/), [Claude Code](https://code.claude.com/docs/en/amazon-bedrock), [Cursor](https://cursor.com) etc. 
- AWS account (free tier sufficient) or credits from the provider
- Code editor

### 📌 Language Note

This workshop uses **Python** to keep the focus on AI-DLC concepts rather than
language-specific complexity.

The same AI-DLC flow, prompts, and artifacts apply equally well to **any
programming language or framework** (for example: Java, JavaScript/TypeScript,
Go, C#, etc.).

You can substitute Python with the language of your choice without changing the
methodology.

---

## INCEPTION PHASE (1 hour)

> **Story framing:** You’re in an inception meeting with Product + Dev + AI.  
> The goal is to lock intent, translate it into behavioral contracts (user stories),and define the Unit boundary — before design or code begins.


### Activity 1: Setup (10 minutes)
**Personas:** Product Owner + AI  
**What this prompt does:** Creates a consistent workspace and artifact structure so every step is traceable and repeatable.

**Copy this exact prompt to your AI assistant:**


```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```


**Expected Result:** AI creates folder structure and confirms understanding.

---

### Activity 1.5: Intent Definition (5 minutes)
**Personas:** Product Owner + AI  
**What this prompt does:** Locks the **WHY** without letting the AI jump into solutions. This is the “no design, no code, just intent” checkpoint.

**Copy this exact prompt to your AI assistant:**


```
Intent:
Build a simple personal task manager to help users add tasks and view their task list.

Do not propose solutions yet.
Acknowledge the intent and confirm understanding.
```

**Expected Result:**
- AI acknowledges intent
- No user stories, no design, no code

> 📌 Why this matters:  
> AI-DLC always separates WHY (Intent) from WHAT (User Stories).

---

### Activity 2: User Stories Creation (30 minutes)
**Personas:** Product Owner (Lead) + AI  
**What this prompt does:** Produces **user stories as contracts** and enforces the AI-DLC ritual: **plan → human approval → execute step-by-step → mark checkboxes**.

**Copy this exact prompt:**

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a simple task manager that allows me to add new tasks and view my task list. Keep it simple with just these two core features." Save the final user stories in aidlc-docs/story-artifacts/mvp_user_stories.md file.
```


**When AI shows you the plan, respond exactly:**

```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```


**Expected Files Created:** 
- `aidlc-docs/plans/user_stories_plan.md`
- `aidlc-docs/story-artifacts/mvp_user_stories.md`

---

### Activity 3: Units Decomposition (20 minutes)
**Personas:** Developers (Lead) + Product Owner + AI  
**What this prompt does:** Defines the **architectural boundary** (Unit) that will contain the stories. This is the “what belongs together” decision before design or code.

**Note:** We intentionally use a single Unit for this workshop.  
> In real systems, AI-DLC often produces multiple Units.

**Copy this exact prompt:**


```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the aidlc-docs/plans/units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in aidlc-docs/story-artifacts/mvp_user_stories.md file. Group the user stories into a single cohesive unit called "Task Management Unit" that contains all the user stories. Save this as aidlc-docs/design-artifacts/task_management_unit.md.
```


**When AI shows you the plan, respond exactly:**

```
I approve. Proceed.
```



**Expected Files Created:**
- `aidlc-docs/plans/units_plan.md`
- `aidlc-docs/design-artifacts/task_management_unit.md`

---

## ✅ BOLT STARTS HERE

> After **Unit boundary** is established, the team begins executing short, validation-driven Bolts.

---

## CONSTRUCTION PHASE (1.5 hours)

### ⚡ Bolt 1 — Design Bolt: Component Model (25 minutes)
**Maps to:** Activity 4  
**Personas:** Developers (Lead) + QA mindset + AI  
**Goal:** Create a component model so the AI can generate code *with guardrails*.

### Activity 4: Domain Model Creation (25 minutes)
**Personas:** Developers (Lead) + AI  
**What this prompt does:** Creates a component model (components, attributes, behaviors, interactions) **before** code is generated.

**Copy this exact prompt:**



```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an aidlc-docs/design-artifacts/component_model_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the aidlc-docs/design-artifacts/task_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviors and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into aidlc-docs/design-artifacts/task_component_model.md file.
```


**When AI shows you the plan, respond exactly:**


```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```



**Expected Files Created:**
- `aidlc-docs/design-artifacts/component_model_plan.md`
- `aidlc-docs/design-artifacts/task_component_model.md`

---

### ⚡ Bolt 2 — Build Bolt: Core Code (35 minutes)
**Maps to:** Activity 5  
**Personas:** Developers (Lead) + QA mindset + AI  
**Goal:** Generate core domain code from the model, then review/validate.

### Activity 5: Code Generation (35 minutes)
**Personas:** Developers (Lead) + AI  
**What this prompt does:** Generates the core implementation (Task + TaskService) directly from the approved component model.

**Copy this exact prompt:**



```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an aidlc-docs/plans/code_generation_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the aidlc-docs/design-artifacts/task_component_model.md file. Generate a very simple Python implementation for the Task Management Component with just two features: add new tasks and list all tasks. Keep it simple - no complex priority logic needed. Generate the classes in respective individual files and save them in the taskManager directory: task.py (Task class), and task_service.py (TaskService class).
```



**Expected Files Created:**
- `aidlc-docs/plans/code_generation_plan.md`
- `taskManager/task.py`
- `taskManager/task_service.py`

---

### ⚡ Bolt 3 — API Bolt: Make it Usable (15 minutes)
**Maps to:** Activity 6  
**Personas:** Developers (Lead) + QA mindset + AI  
**Goal:** Expose functionality via Flask APIs so it can be tested end-to-end.

### Activity 6: Build APIs (15 minutes)
**Personas:** Developers (Lead) + AI  
**What this prompt does:** Wraps the service into API endpoints and creates minimal dependencies for local execution.

**Copy this exact prompt:**



```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the task_service.py under the taskManager/ folder. Create python flask apis for each of the service there.
```



**Expected Files Created:**
- `api_build_plan.md`
- `taskManager/app.py` (Flask application)
- `taskManager/requirements.txt`

---

### ⚡ Bolt 4 — Deployability Bolt: Make it Cloud-Ready (15 minutes)
**Maps to:** Activity 7  
**Personas:** Developers + DevOps mindset + QA mindset + AI  
**Goal:** Produce a deployment plan + CloudFormation + validation artifacts.

### Activity 7: Architecture Planning (15 minutes)
**Personas:** Developers (Lead) + AI  
**What this prompt does:** Creates deployment plan + IaC + validation artifacts so the Bolt is production-oriented.

**Copy this exact prompt:**



```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: aidlc-docs/design-artifacts/task_component_model.md, units in the aidlc-docs/design-artifacts/ folder, and backend code in the taskManager/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder as cloudformation-template.yaml and deployment-guide.md.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```


**Expected Files Created:**
- `deployment_plan.md`
- `DEPLOYMENT/cloudformation-template.yaml`
- `DEPLOYMENT/deployment-guide.md`

---

## OPERATIONS PHASE (30 minutes)

### ⚡ Bolt 5 — Operability Bolt: Run It Like It’s Real (30 minutes)
**Maps to:** Activity 8  
**Personas:** DevOps / Platform + Developers + AI  
**Goal:** Define how AI assists deploy/monitor/respond/scale and how humans govern decisions.

### Activity 8: Operations Phase Discussion
**Personas:** DevOps / Platform + Developers + AI  
**What this prompt does:** Walks through AI-assisted operations loops with human approval gates.

In AI-DLC, Operations is not driven by static prompts but by continuous AI observation and recommendation loops, with humans approving corrective actions.

**Ask your AI:**


```
Now that we've built our task manager, let's discuss the Operations Phase. Based on what we've created, how would AI help with:

1. Deploying our task manager to production
2. Monitoring the application performance  
3. Detecting and responding to issues automatically
4. Scaling the application as usage grows

Please explain how this would work for our specific task manager application.
```


**Key Operations Concepts to Learn:**
- AI packages our code into deployment units (Lambda functions, containers)
- AI monitors application metrics and logs
- AI detects patterns and predicts issues
- AI recommends scaling and optimization actions
- Developers validate and approve AI recommendations

---

## Test Your Application

### Run Locally (10 minutes)

1. **Navigate to your task manager folder:**
```bash
cd taskManager
pip install -r requirements.txt
python app.py


2. **Test the Simple Features:**
```bash
# Add a new task
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Learn AI-DLC", "description": "Complete the tutorial"}'

# Get all tasks
curl http://localhost:5000/tasks
```

### Deploy to AWS (Optional)

Use the CloudFormation template generated in `DEPLOYMENT/cloudformation-template.yaml` to deploy to AWS following the deployment guide.

---

## What You've Learned

**AI-DLC Methodology:**
- How AI initiates conversations and generates plans
- The importance of human validation at each step
- How artifacts build context for AI across the lifecycle
- The three-phase structure: Inception → Construction → Operations

**Practical Skills:**
- Using official AI-DLC prompts from AWS
- Building with AI while maintaining quality control
- Creating simple, working applications with AI assistance
- Understanding AI-human collaboration patterns

**Key Takeaway:** AI-DLC isn't about AI doing everything automatically - it's about AI and humans collaborating effectively, with AI handling planning and generation while humans provide oversight and validation.

---

## Files You Should Have

```
project-root/
├── aidlc-docs/
│   ├── plans/
│   │   ├── user_stories_plan.md
│   │   ├── units_plan.md
│   │   └── code_generation_plan.md
│   ├── story-artifacts/
│   │   └── mvp_user_stories.md
│   ├── design-artifacts/
│   │   ├── component_model_plan.md
│   │   ├── task_management_unit.md
│   │   └── task_component_model.md
│   └── prompts.md
├── taskManager/
│   ├── task.py
│   ├── task_service.py
│   ├── app.py
│   └── requirements.txt
├── DEPLOYMENT/
│   ├── cloudformation-template.yaml
│   └── deployment-guide.md
├── deployment_plan.md
└── api_build_plan.md
```

**Congratulations!** You've successfully completed an end-to-end AI-DLC project and built a simple but working task manager using the official AWS methodology. You can now add tasks and view your task list - a perfect foundation for learning how AI-DLC works in practice!