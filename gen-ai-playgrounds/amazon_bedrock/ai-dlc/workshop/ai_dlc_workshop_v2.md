Perfect — thanks for pasting the **full workshop**.
Below is a **copy-paste–ready version** of your tutorial with **only the following changes applied**:

### What I changed (strictly, deliberately)

1. ✅ **Replaced “Task Manager” with a non-conflicting app name**
   → **Personal Work Tracker** (used everywhere consistently)
2. ✅ **Updated prompts to follow Appendix A wording and intent**

   * Plan-first, approve-then-execute
   * No hard-coding of features in prompts
   * “Refer to artifacts” instead of “build X features”
3. ❌ **Did NOT change**

   * Phases
   * Flow
   * Timing
   * Folder philosophy
   * Teaching structure
4. ⚠️ **Important note**
   Appendix A **does not include an Intent prompt**.
   To stay faithful, I keep **Activity 1.5** but make it **purely contextual** (non-directive).

You can **copy-paste this as-is**.

---

# AI-DLC Hands-On Tutorial: Build a Simple **Work Tracker**

## Tutorial Overview

**Duration:** 3 hours
**Project:** Personal Work Tracker
**Goal:** Learn AI-DLC by building something real you can use

You'll follow the complete AI-DLC methodology from AWS to build a working **work tracker** application.

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

* Basic Python knowledge
* Access to an AI assistant
* AWS account (free tier sufficient)
* Code editor

---

## INCEPTION PHASE (1 hour)

### Activity 1: Setup (10 minutes)

**Personas:** Product Owner + AI

**Copy this exact prompt:**

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in the aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. **Background context documents will reside in the aidlc-docs/context folder.** All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

### Background Context: (Optional)
```
A background context file exists at `aidlc-docs/context/inception-context.md`.

This is background information for you as we work on this together.
Please acknowledge.
```


---

### Activity 1.5: Context Setting (Optional, Non-Directive)

**Personas:** Product Owner + AI

> This step is informational only and **must not drive design**.

**Copy this exact prompt:**

```
Context:
We are building a simple Personal Work Tracker as a hands-on exercise to practice AI-DLC.

Do not propose solutions.
Do not generate user stories or designs.
Acknowledge the context and confirm understanding.
```

---

### Activity 2: User Stories Creation (30 minutes)

**Personas:** Product Owner (Lead) + AI

**Copy this exact prompt (Appendix A format):**

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here:
"Build a Personal Work Tracker that enables an individual to manage and review their work items."
Save the final user stories in aidlc-docs/story-artifacts/mvp_user_stories.md file.
```

**Approval response (verbatim):**

```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

---

### Activity 3: Units Decomposition (20 minutes)

**Personas:** Developers + Product Owner + AI

**Copy this exact prompt (Appendix A):**

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the aidlc-docs/plans/units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into units that can be built independently. Each unit should contain cohesive user stories. Write each unit definition in a separate md file under aidlc-docs/design-artifacts/.
```

**Approval:**

```
I approve. Proceed.
```

---

## CONSTRUCTION PHASE (1.5 hours)

### Background Context: (Optional)
```
A background context file exists at `aidlc-docs/context/construction-context.md`.

This is background information for you as we work on this together.
Please acknowledge.

```


### Activity 4: Domain (Component) Model Creation

**Personas:** Developers + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an aidlc-docs/design-artifacts/component_model_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the unit definition file under aidlc-docs/design-artifacts/. Design the component model to implement all the user stories. The model shall contain components, attributes, behaviors, and interactions. Do not generate any code yet. Write the component model into a separate md file in the same folder.
```

**Approval:**

```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

---

### Activity 5: Code Generation

**Personas:** Developers + AI

**Copy this exact prompt (Appendix A-correct):**

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the component design in aidlc-docs/design-artifacts/. Generate a simple and intuitive Python implementation for the components defined in the design. Generate the classes in respective individual files and keep them in the workTracker directory.
```

---

### Activity 6: Build REST APIs

**Personas:** Developers + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services implemented under the workTracker/ folder. Create python flask APIs for each service.
```

---

### Activity 7: Architecture

**Personas:** Developers + AI

**Copy this exact prompt:**

```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model, unit definitions, and backend code. Generate an end-to-end deployment plan for AWS using CloudFormation. Document prerequisites. After approval, generate infrastructure code, a validation plan, and validation report. Fix issues and update the report.
```

---

## OPERATIONS PHASE (30 minutes)

### Background Context: (Optional)
```
A background context file exists at `aidlc-docs/context/operations-context.md`.

This is background information for you as we work on this together.
Please acknowledge.
```

**Ask your AI:**

```
Now that we've built our Work Tracker, discuss how AI would assist during Operations, including deployment, monitoring, issue detection, and scaling, while keeping humans in control of decisions.
```

---

## ✅ Final Outcome

You now have:

* ✔ **Appendix A-aligned prompts**
* ✔ **No feature hard-coding**
* ✔ **Plan → Approve → Execute loops everywhere**
* ✔ **No terminology collision**
* ✔ **Safe to defend in a whitepaper review**

If you want next, I can:

* Do a **diff view: original vs Appendix-A-correct**
* Create a **facilitator talk track**
* Or trim this to a **90-minute executive version**

You’re doing this the *right* way.
