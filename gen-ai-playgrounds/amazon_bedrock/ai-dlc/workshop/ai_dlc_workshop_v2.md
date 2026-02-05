# AI-DLC Hands-On Tutorial: Build a Simple Action Tracker

## Tutorial Overview

**Duration:** 3 hours
**Project:** Personal Action Tracker
**Goal:** Learn AI-DLC by building something real you can use

You'll follow the complete AI-DLC methodology from AWS to build a working action tracker application.

**AI-DLC Three Phases:**

* **INCEPTION PHASE** *(Human-led, AI-expanded)*
* **CONSTRUCTION PHASE** *(AI-led, Human-validated)*
* **OPERATIONS PHASE** *(AI-assisted, Human-governed)*

**AI-DLC Personas:**

* **Product Owner** (You - making business decisions)
* **Developers** (You - technical implementation)
* **AI Assistant** (Planning, generation, and recommendations)

---

## Prerequisites

* Basic Python knowledge (for this workshop)
* Access to an AI assistant ([Kiro](https://kiro.dev/), [Claude Code](https://code.claude.com/docs/en/amazon-bedrock), [Cursor](https://cursor.com) etc.
* AWS account (free tier sufficient) or credits from the provider
* Code editor

## Optional Activity: Steering Setup

There is an optional section below. This optional activity sets up steering files so the AI consistently behaves like a teammate who understands the product, engineering approach, and operational expectations throughout the lifecycle.

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

### Activity 1: Setup (10 minutes)

**Personas:** Product Owner + AI

**Copy this exact prompt to your AI assistant:**

```
We will work on building an application today. For every front end
and backend component we will create a project folder. All
documents will reside in the aidlc-docs folder. Throughout our
session I'll ask you to plan your work ahead and create an md file
for the plan. You may work only after I approve said plan. These
plans will always be stored in aidlc-docs/plans folder. You will
create many types of documents in the md format. Requirement,
features changes documents will reside in the aidlc-
docs/requirements folder. User stories must be stored in the
aidlc-docs/story-artifacts folder. Architecture and Design
documents must be stored in the aidlc-docs/design-artifacts
folder. All prompts in order must be stored in the aidlc-
docs/prompts.md file. Confirm your understanding of this
prompt. Create the necessary folders and files for storage, if they
do not exist already.
```

**Expected Result:** AI creates folder structure and confirms understanding.

---

### Activity 1.5: Intent Definition (5 minutes)

**Personas:** Product Owner + AI

**Copy this exact prompt to your AI assistant:**

```
Intent:
Build a simple personal action tracker to help users record actions and view their action list.

Do not propose solutions yet.
Acknowledge the intent and confirm understanding.
```

**Expected Result:**

* AI acknowledges intent
* No user stories, no design, no code

> 📌 Why this matters:
> AI-DLC always separates WHY (Intent) from WHAT (User Stories).

---

### Activity 2: User Stories Creation (30 minutes)

> In AI-DLC, user stories are created after intent and act as behavioral contracts, not backlog items.

**Personas:** Product Owner (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an expert product manager and are tasked
with creating well defined user stories that becomes the contract
for developing the system as mentioned in the Task section
below. Plan for the work ahead and write your steps in an md file
(user_stories_plan.md) with checkboxes for each step in the plan.
If any step needs my clarification, add a note in the step to get
my confirmation. Do not make critical decisions on your own.
Upon completing the plan, ask for my review and approval. After
my approval, you can go ahead to execute the same plan one step
at a time. Once you finish each step, mark the checkboxes as done
in the plan.

Your Task: Build user stories for the high-level requirement as described here:
"Build a simple action tracker that allows me to record a new action and view my action list."
Save the final user stories in aidlc-docs/story-artifacts/mvp_user_stories.md file.
```

**When AI shows you the plan, respond exactly:**

```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

**Expected Files Created:**

* `aidlc-docs/plans/user_stories_plan.md`
* `aidlc-docs/story-artifacts/mvp_user_stories.md`

---

### Activity 3: Units Decomposition (20 minutes)

> In AI-DLC, Units define architectural boundaries first, so domain models are designed inside a unit, not across the entire system.

**Note:** We intentionally use a single Unit for this workshop.

> In real systems, AI-DLC often produces multiple Units.

**Personas:** Developers (Lead) + Product Owner + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the aidlc-docs/plans/units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in aidlc-docs/story-artifacts/mvp_user_stories.md file. Group the user stories into a single cohesive unit called "Action Tracking Unit" that contains all the user stories. Save this as aidlc-docs/design-artifacts/action_tracking_unit.md.
```

**When AI shows you the plan, respond exactly:**

```
I approve. Proceed.
```

**Expected Files Created:**

* `aidlc-docs/plans/units_plan.md`
* `aidlc-docs/design-artifacts/action_tracking_unit.md`

> In AI-DLC, the following Construction activities will be executed as short, validation-driven Bolts rather than time-boxed sprints.

---

## CONSTRUCTION PHASE (1.5 hours)

### Activity 4: Domain Model Creation (25 minutes)

**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you
start the task as mentioned below, please do the planning and
write your steps in an design/component_model.md file with
checkboxes against each step in the plan. If any step needs my
clarification, please add it to the step to interact with me and get
my confirmation. Do not make critical decisions on your own.
Once you produce the plan, ask for my review and approval. After
my approval, you can go ahead to execute the same plan one step
at a time. Once you finish each step, mark the checkboxes as done
in the plan.

Your Task: Refer to the user stories in the
design/action_tracking_unit.md file. Design the component
model to implement all the user stories. This model shall contain
all the components, the attributes, the behaviours and how the
components interact to implement the user stories. Do not
generate any codes yet. Write the component model into a
separate md file in the /design folder.
```

**When AI shows you the plan, respond exactly:**

```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

**Expected Files Created:**

* `aidlc-docs/design-artifacts/component_model_plan.md`
* `aidlc-docs/design-artifacts/action_component_model.md`

---

### Activity 5: Code Generation (35 minutes)

**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you
start the task as mentioned below, please do the planning and
write your steps in an md file with checkboxes against each step
in the plan. If any step needs my clarification, please add it to the
step to interact with me and get my confirmation. Do not make
critical decisions on your own. Once you produce the plan, ask for
my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each
step, mark the checkboxes as done in the plan.

Task: Refer to component design in the
aidlc-docs/design-artifacts/action_component_model.md file. Generate a very
simple and intuitive Python implementation for the Action Tracker Component that is in the design.
Generate the classes in respective individual files but keep them in the actionTracker directory.
```

**Expected Files Created:**

* `aidlc-docs/plans/code_generation_plan.md`
* Code generated under `actionTracker/`

---

### Activity 6: Build APIs (15 minutes)

**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you
start the task as mentioned below, please do the planning and
write your steps in an md file with checkboxes against each step
in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the backend implementation under the actionTracker/ folder. Create python flask apis for each of the services defined there.
```

**Expected Files Created:**

* `api_build_plan.md`
* Flask API code and dependencies under `actionTracker/`

---

### Activity 7: Architecture Planning (15 minutes)

**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced Cloud Architect. Before you
start the task as mentioned below, please do the planning and
write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: aidlc-docs/design-artifacts/action_component_model.md, units in the aidlc-docs/design-artifacts/ folder, and backend code in the actionTracker/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder as cloudformation-template.yaml and deployment-guide.md.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

**Expected Files Created:**

* `deployment_plan.md`
* `DEPLOYMENT/cloudformation-template.yaml`
* `DEPLOYMENT/deployment-guide.md`

---

## OPERATIONS PHASE (30 minutes)

### Activity 8: Operations Phase Discussion

**Personas:** Developers + Product Owner + AI

In AI-DLC, Operations is not driven by static prompts but by continuous AI observation and recommendation loops, with humans approving corrective actions.

**Ask your AI:**

```
Now that we've built our action tracker, let's discuss the Operations Phase. Based on what we've created, how would AI help with:

1. Deploying our action tracker to production
2. Monitoring the application performance  
3. Detecting and responding to issues automatically
4. Scaling the application as usage grows

Please explain how this would work for our specific action tracker application.
```

**Key Operations Concepts to Learn:**

* AI packages our code into deployment units (Lambda functions, containers)
* AI monitors application metrics and logs
* AI detects patterns and predicts issues
* AI recommends scaling and optimization actions
* Developers validate and approve AI recommendations

---

## Test Your Application

### Run Locally (10 minutes)

1. **Navigate to your action tracker folder:**

```bash
cd actionTracker
pip install -r requirements.txt
python app.py
```

2. **Test the Simple Features:**

```bash
# Add a new action
curl -X POST http://localhost:5000/actions -H "Content-Type: application/json" -d '{"title": "Learn AI-DLC", "description": "Complete the tutorial"}'

# Get all actions
curl http://localhost:5000/actions
```

### Deploy to AWS (Optional)

Use the CloudFormation template generated in `DEPLOYMENT/cloudformation-template.yaml` to deploy to AWS following the deployment guide.

---

## What You've Learned

**AI-DLC Methodology:**

* How AI initiates conversations and generates plans
* The importance of human validation at each step
* How artifacts build context for AI across the lifecycle
* The three-phase structure: Inception → Construction → Operations

**Practical Skills:**

* Using official AI-DLC prompts from AWS
* Building with AI while maintaining quality control
* Creating simple, working applications with AI assistance
* Understanding AI-human collaboration patterns

**Key Takeaway:** AI-DLC isn't about AI doing everything automatically - it's about AI and humans collaborating effectively, with AI handling planning and generation while humans provide oversight and validation.

---

## Files You Should Have

```
project-root/
├── aidlc-docs/
│   ├── plans/
│   │   ├── user_stories_plan.md
│   │   └── units_plan.md
│   ├── story-artifacts/
│   │   └── mvp_user_stories.md
│   ├── design-artifacts/
│   │   ├── action_tracking_unit.md
│   │   └── action_component_model.md
│   └── prompts.md
├── actionTracker/
├── DEPLOYMENT/
│   ├── cloudformation-template.yaml
│   └── deployment-guide.md
├── deployment_plan.md
└── api_build_plan.md
```

**Congratulations!** You've successfully completed an end-to-end AI-DLC project and built a simple but working action tracker using the official AWS methodology.

## Optional Activity: Steering Setup

**Providing persistent product, build, and operations context for AI-DLC**

This optional activity sets up steering files so the AI consistently behaves like a teammate who understands the product, engineering approach, and operational expectations throughout the lifecycle.

All steering files in this workshop use `inclusion: always`.

---

### Step 1: Create the Steering Directory

From the **root of your project**, run:

```bash
mkdir -p .kiro/steering
```

---

### Step 2: Create All Steering Files

```bash
touch .kiro/steering/product.md
touch .kiro/steering/construction.md
touch .kiro/steering/python.md
touch .kiro/steering/operations.md
```

---

### Step 3: Add Product Steering (Inception Context)

Open the file:

```bash
nano .kiro/steering/product.md
```

Paste and save:

```md
---
inclusion: always
---

# Product Steering – Action Tracker

## Product Intent
Build a simple personal action tracker for recording actions and viewing them later.

## Scope Constraints
- The MVP must support only:
  - Recording a new action
  - Viewing the list of recorded actions
- No authentication or user management
- No action status, priority, deadlines, or reminders

## Product Principles
- Keep the solution simple and easy to understand
- Prefer clarity over extensibility
- Avoid adding features not explicitly required

## Language & Terminology
- Use the term "action" consistently across user stories, design, and code
- Do not introduce alternative terms such as "task", "item", or "record"
```

---

### Step 4: Add Construction Steering (Build Context)

Open the file:

```bash
nano .kiro/steering/construction.md
```

Paste and save:

```md
---
inclusion: always
---

# Construction Steering – Action Tracker

## Implementation Expectations
- Keep implementations simple and readable
- Avoid over-engineering or premature abstractions
- Prefer straightforward logic over complex patterns

## Data Handling
- Store actions in memory for the MVP
- Do not introduce databases, files, or external storage

## API Design
- Use clear, predictable REST-style endpoints
- Keep request and response payloads minimal

## Out-of-Scope
- No background jobs or async processing
- No authentication or authorization
- No metrics, tracing, or advanced logging
```

---

### Step 5: Add Python Steering (Language Context)

Open the file:

```bash
nano .kiro/steering/python.md
```

Paste and save:

```md
---
inclusion: always
---

# Python Coding Standards – Action Tracker

## General Style
- Follow PEP 8 conventions
- Use snake_case for functions and variables
- Use CamelCase for class names

## Functions and Classes
- Keep functions small and focused
- Prefer explicit parameters
- Avoid deep nesting

## Data Structures
- Use built-in types (list, dict)
- Keep models simple and flat

## Error Handling
- Use basic validation and simple exceptions
- Fail fast on invalid input

## Out-of-Scope
- No advanced Python patterns
- No async code unless explicitly required
```

---

### Step 6: Add Operations Steering (Operations Context)

Open the file:

```bash
nano .kiro/steering/operations.md
```

Paste and save:

```md
---
inclusion: always
---

# Operations Steering – Action Tracker

## Deployment Expectations
- Deploy as a simple backend service
- Prefer managed AWS services
- Keep architecture minimal and explainable

## Environments
- Assume a single environment for the workshop
- No environment promotion workflows

## Monitoring
- Basic availability and error monitoring only
- Avoid advanced observability tooling

## Reliability
- Best-effort availability is sufficient
- Prefer restart-based recovery
- No multi-region or failover setups

## Scaling
- Expect low to moderate traffic
- Favor simple horizontal scaling
- Avoid autoscaling complexity

## Operational Constraints
- No runbooks required for the MVP
- No load testing or performance tuning
- No cost optimization beyond basic awareness
```

---

### Step 7: Verify Steering Files

Run:

```bash
ls .kiro/steering
```

You should see:

```text
product.md
construction.md
python.md
operations.md
```

---

### What Happens Next

Once these files exist:

* They are **automatically loaded** into AI context
* No changes are required to any AI-DLC prompts
* Inception, Construction, and Operations activities will follow this guidance
* The AI behaves like a teammate with shared product, engineering, and ops context