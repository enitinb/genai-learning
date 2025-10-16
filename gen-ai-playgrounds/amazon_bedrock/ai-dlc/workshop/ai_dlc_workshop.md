# AI-DLC Tiered Workshop Series: Standard Methodology Across All Levels

## Workshop Series Overview

This three-tier workshop series teaches AI-Driven Development Lifecycle (AI-DLC) using the **exact same methodology sequence** across all levels. Each tier follows the identical AI-DLC process from Appendix A, with only the **project complexity and scope** varying by skill level.

**Consistent AI-DLC Sequence for All Tiers:**
1. Setup Prompt
2. Inception - User Stories  
3. Units Decomposition
4. Construction - Domain Model Creation
5. Code Generation
6. Architecture
7. Build IaC/Rest APIs

---

# TIER 1: BEGINNER WORKSHOP
## "Personal Task Manager using AI-DLC"

### Target Audience
- Developers new to AI-assisted development
- Traditional methodology practitioners exploring AI-DLC
- Anyone wanting to learn AI-DLC fundamentals

### Duration: 4 hours
### Project Scope: Simple personal productivity application

---

## Phase 1: AI-DLC Setup (20 minutes)

### **Step 1: Setup Prompt**
```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

## Phase 2: Inception - User Stories (45 minutes)

### **Step 2: User Stories Prompt**
```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a personal task manager that helps freelancers organize their daily tasks, set priorities, and track completion across multiple client projects."
```

**After reviewing the plan:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

## Phase 3: Units Decomposition (30 minutes)

### **Step 3: Units Prompt**
```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**After reviewing the plan:**
```
I approve. Proceed.
```

## Phase 4: Construction - Domain Model Creation (40 minutes)

### **Step 4: Domain Model Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/task_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**After reviewing the plan:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

## Phase 5: Code Generation (40 minutes)

### **Step 5: Code Generation Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/task_component_model.md file. Generate a very simple and intuitive Python implementation for the Task Management Component that is in the design. For the prioritizeTask() method, use basic rule-based logic to assign priority scores. Generate the classes in respective individual files but keep them in `taskManager` directory.
```

## Phase 6: Architecture (35 minutes)

### **Step 6: Architecture Prompt**
```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: design/task_component_model.md, units in the design/ folder, and backend code in the taskManager/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

## Phase 7: Build IaC/Rest APIs (30 minutes)

### **Step 7: Build APIs Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the taskManager/ folder. Create python flask apis for each of the service there.
```

---

# TIER 2: INTERMEDIATE WORKSHOP
## "Smart Customer Feedback System using AI-DLC"

### Target Audience
- Developers comfortable with basic AI assistance
- Teams wanting to adopt AI-DLC methodology
- Those who completed Beginner workshop

### Duration: 5 hours
### Project Scope: Business application with AI integration

---

## Phase 1: AI-DLC Setup (20 minutes)

### **Step 1: Setup Prompt**
```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

## Phase 2: Inception - User Stories (50 minutes)

### **Step 2: User Stories Prompt**
```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a smart customer feedback system that collects feedback from multiple channels (email, chat, surveys), automatically categorizes and prioritizes feedback using AI, generates insights and trends for product managers, alerts teams about critical issues, and tracks resolution and follow-up."
```

**After reviewing the plan:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

## Phase 3: Units Decomposition (40 minutes)

### **Step 3: Units Prompt**
```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**After reviewing the plan:**
```
I approve. Proceed.
```

## Phase 4: Construction - Domain Model Creation (60 minutes)

### **Step 4: Domain Model Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/feedback_analysis_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**After reviewing the plan:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

## Phase 5: Code Generation (60 minutes)

### **Step 5: Code Generation Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/feedback_analysis_component.md file. Generate a very simple and intuitive Python implementation for the Feedback Analysis Component that is in the design. For the analyzeSentiment() method, use amazon bedrock APIs to extract sentiment and entities from the feedback text. Generate the classes in respective individual files but keep them in `feedbackAnalyzer` directory.

Refer to the generated codes in feedbackAnalyzer directory. I want the SentimentAnalyzer component to make a call to GenAI. The current implementation uses basic sentiment rules. Can you analyse and give me a plan on how I can leverage GenAI for both Sentiment Analysis and Category Classification.
```

## Phase 6: Architecture (50 minutes)

### **Step 6: Architecture Prompt**
```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: design/feedback_analysis_component.md, units in the design/ folder, cloud architecture in the ARCHITECTURE/ folder, and backend code in the feedbackAnalyzer/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

## Phase 7: Build IaC/Rest APIs (40 minutes)

### **Step 7: Build APIs Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the feedbackAnalyzer/ folder. Create python flask apis for each of the service there.
```

---

# TIER 3: ADVANCED WORKSHOP
## "Enterprise Digital Asset Management Platform using AI-DLC"

### Target Audience
- Experienced developers and architects
- Team leads implementing AI-DLC organizationally
- Those who completed Intermediate workshop

### Duration: 6 hours
### Project Scope: Enterprise-scale platform with compliance requirements

---

## Phase 1: AI-DLC Setup (25 minutes)

### **Step 1: Setup Prompt**
```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

## Phase 2: Inception - User Stories (65 minutes)

### **Step 2: User Stories Prompt**
```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build an enterprise digital asset management platform for a large financial services company that manages regulatory documents across 15 business units, ensures compliance with multiple jurisdictions, provides AI-powered document classification and search, supports audit trails and version control, integrates with existing enterprise systems, and scales to handle 100K+ documents with 500+ concurrent users."
```

**After reviewing the plan:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

## Phase 3: Units Decomposition (55 minutes)

### **Step 3: Units Prompt**
```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**After reviewing the plan:**
```
I approve. Proceed.
```

## Phase 4: Construction - Domain Model Creation (75 minutes)

### **Step 4: Domain Model Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/document_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**After reviewing the plan:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

## Phase 5: Code Generation (80 minutes)

### **Step 5: Code Generation Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/document_classifier_component.md file. Generate a very simple and intuitive Python implementation for the Document Classification Component that is in the design. For the classifyDocument() method, use amazon bedrock APIs to extract document type and compliance metadata from document content. Generate the classes in respective individual files but keep them in `documentClassifier` directory.

Refer to the generated codes in documentClassifier directory. I want the DocumentAnalyzer component to make a call to GenAI. The current implementation uses basic pattern matching. Can you analyse and give me a plan on how I can leverage GenAI for both Document Classification and Compliance Validation.
```

## Phase 6: Architecture (65 minutes)

### **Step 6: Architecture Prompt**
```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: design/document_management_component.md, units in the UNITS/ folder, cloud architecture in the ARCHITECTURE/ folder, and backend code in the documentClassifier/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CDK.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

## Phase 7: Build IaC/Rest APIs (55 minutes)

### **Step 7: Build APIs Prompt**
```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the documentClassifier/ folder. Create python flask apis for each of the service there.
```

---

## Workshop Series Summary

### **Consistent AI-DLC Methodology**
All three workshop tiers follow the identical 7-step AI-DLC sequence from Appendix A:

1. **Setup Prompt** - Establishes AI-DLC project structure
2. **User Stories** - Expert product manager role with plan-approve-execute
3. **Units** - Software architect role with independent unit decomposition  
4. **Domain Model** - Software engineer role with DDD component design
5. **Code Generation** - Python implementation with AI service integration
6. **Architecture** - Cloud architect role with AWS deployment planning
7. **APIs** - Flask REST API implementation

### **Tier Differentiation Through Scope Only**

| Aspect | Beginner | Intermediate | Advanced |
|--------|----------|--------------|----------|
| **Project** | Personal Task Manager | Customer Feedback System | Enterprise Asset Management |
| **Complexity** | Simple CRUD operations | AI-powered analysis | Enterprise compliance & scale |
| **Duration** | 4 hours | 5 hours | 6 hours |
| **AI Integration** | Basic rule-based logic | AWS Comprehend/Bedrock | Advanced ML pipelines |
| **Architecture** | Single service | Multi-service | Enterprise patterns |
| **Users** | Individual | Business teams | 500+ concurrent users |
| **Data Scale** | Personal tasks | Moderate feedback volume | 100K+ documents |

### **Key Learning Outcomes**

**All Participants Learn:**
- Authentic AI-DLC methodology from AWS
- Plan-approve-execute workflow patterns
- AI-human collaboration techniques
- Domain-driven design principles
- Progressive artifact refinement

**Skill-Appropriate Application:**
- Beginners focus on understanding the process
- Intermediate practitioners apply to business problems  
- Advanced teams tackle enterprise complexity

This approach ensures all participants learn the same proven AI-DLC methodology while working at their appropriate complexity level, enabling seamless progression through the workshop tiers.