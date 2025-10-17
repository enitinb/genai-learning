# AI-DLC Hands-On Tutorial: Build a Simple Task Manager

## Tutorial Overview
**Duration:** 3 hours  
**Project:** Personal Task Manager  
**Goal:** Learn AI-DLC by building something real you can use

You'll follow the complete AI-DLC methodology from AWS to build a working task manager application.

**AI-DLC Three Phases:**
- **INCEPTION PHASE** (Mob Elaboration)
- **CONSTRUCTION PHASE** (Mob Programming)  
- **OPERATIONS PHASE** (AI-Driven Operations)

**AI-DLC Personas:**
- **Product Owner** (You - making business decisions)
- **Developers** (You - technical implementation)
- **AI Assistant** (Planning, generation, and recommendations)

---

## Prerequisites
- Basic Python knowledge
- Access to an AI assistant (Claude, ChatGPT, etc.)
- AWS account (free tier sufficient)
- Code editor

---

## INCEPTION PHASE (1 hour)

### Activity 1: Setup (10 minutes)
**Personas:** Product Owner + AI

**Copy this exact prompt to your AI assistant:**

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

**Expected Result:** AI creates folder structure and confirms understanding.

### Activity 2: User Stories Creation (30 minutes)
**Personas:** Product Owner (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a personal task manager that helps me organize daily tasks, set priorities, track completion, and view my productivity."
```

**When AI shows you the plan, respond exactly:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

**Expected Files Created:** 
- `aidlc-docs/plans/user_stories_plan.md`
- `aidlc-docs/story-artifacts/mvp_user_stories.md`

### Activity 3: Units Decomposition (20 minutes)
**Personas:** Developers (Lead) + Product Owner + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the aidlc-docs/design-artifacts/ folder.
```

**When AI shows you the plan, respond exactly:**
```
I approve. Proceed.
```

**Expected Files Created:**
- `aidlc-docs/plans/units_plan.md`
- `aidlc-docs/design-artifacts/task_management_unit.md`
- `aidlc-docs/design-artifacts/productivity_tracking_unit.md`

---

## CONSTRUCTION PHASE (1.5 hours)

### Activity 4: Domain Model Creation (25 minutes)
**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an aidlc-docs/design-artifacts/component_model_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the aidlc-docs/design-artifacts/task_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the aidlc-docs/design-artifacts folder.
```

**When AI shows you the plan, respond exactly:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

**Expected Files Created:**
- `aidlc-docs/design-artifacts/component_model_plan.md`
- `aidlc-docs/design-artifacts/task_component_model.md`

### Activity 5: Code Generation (35 minutes)
**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an aidlc-docs/plans/code_generation_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the aidlc-docs/design-artifacts/task_component_model.md file. Generate a very simple and intuitive Python implementation for the Task Management Component that is in the design. For the prioritizeTask() method, use basic rule-based logic to assign priority scores. Generate the classes in respective individual files but keep them in `taskManager` directory.
```

**Expected Files Created:**
- `aidlc-docs/plans/code_generation_plan.md`
- `taskManager/task.py`
- `taskManager/task_service.py`
- `taskManager/priority_calculator.py`

### Activity 6: Architecture Planning (15 minutes)
**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: aidlc-docs/design-artifacts/task_component_model.md, units in the aidlc-docs/design-artifacts/ folder, and backend code in the taskManager/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

**Expected Files Created:**
- `deployment_plan.md`
- `DEPLOYMENT/cloudformation-template.yaml`
- `DEPLOYMENT/deployment-guide.md`

### Activity 7: Build APIs (15 minutes)
**Personas:** Developers (Lead) + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the taskManager/ folder. Create python flask apis for each of the service there.
```

**Expected Files Created:**
- `api_build_plan.md`
- `taskManager/app.py` (Flask application)
- `taskManager/requirements.txt`

---

## OPERATIONS PHASE (30 minutes)

### Activity 8: Operations Phase Discussion
**Personas:** Developers + Product Owner + AI

Since the Operations Phase doesn't have specific prompts in Appendix A, have this discussion with your AI:

**Ask your AI:**
```
Now that we've built our task manager following AI-DLC methodology, let's discuss the Operations Phase. Based on what we've created, how would AI help with:

1. Deploying our task manager to production
2. Monitoring the application performance
3. Detecting and responding to issues automatically
4. Scaling the application as usage grows

Please explain how AI-DLC Operations Phase would work for our specific task manager application.
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
```

2. **Test the API:**
```bash
# Create a task
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Learn AI-DLC", "description": "Complete the tutorial"}'

# Get all tasks
curl http://localhost:5000/tasks

# Update task priority
curl -X PUT http://localhost:5000/tasks/1/priority
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
- Creating production-ready applications with AI assistance
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
│   │   ├── productivity_tracking_unit.md
│   │   └── task_component_model.md
│   └── prompts.md
├── taskManager/
│   ├── task.py
│   ├── task_service.py
│   ├── priority_calculator.py
│   ├── app.py
│   └── requirements.txt
├── DEPLOYMENT/
│   ├── cloudformation-template.yaml
│   └── deployment-guide.md
├── deployment_plan.md
└── api_build_plan.md
```

**Congratulations!** You've successfully completed an end-to-end AI-DLC project and built a working application using the official AWS methodology.