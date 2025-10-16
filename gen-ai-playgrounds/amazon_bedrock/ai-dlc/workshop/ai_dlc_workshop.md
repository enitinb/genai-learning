# AI-DLC Complete End-to-End Workshop Series

## Workshop Series Overview

This three-tier workshop series teaches AI-Driven Development Lifecycle (AI-DLC) through complete end-to-end implementations following Appendix A exactly. Each tier executes all AI-DLC **Phases** and **Activities** with proper **AI-DLC Personas**.

**Complete AI-DLC Three-Phase Structure:**
- **INCEPTION PHASE** (Mob Elaboration)
- **CONSTRUCTION PHASE** (Mob Programming) 
- **OPERATIONS PHASE** (AI-Driven Operations)

**Key AI-DLC Personas:**
- **Product Owner** (Business validation and strategic decisions)
- **Developers** (Technical implementation and oversight)
- **AI** (Planning, decomposition, and generation)

---

# TIER 1: BEGINNER - COMPLETE END-TO-END
## "Personal Task Manager using Full AI-DLC Methodology"

### Duration: 5 hours
### Project: Simple personal productivity application for freelancers

---

## INCEPTION PHASE (1.5 hours)

### **Activity 1: Setup Prompt** (15 minutes)
**AI-DLC Personas:** Product Owner + AI

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

### **Activity 2: User Stories Creation** (45 minutes)
**AI-DLC Personas:** Product Owner (Lead) + AI

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a personal task manager that helps freelancers organize their daily tasks, set priorities based on client importance and deadlines, track completion status, and generate simple productivity reports."
```

**Product Owner Approval Response:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

### **Activity 3: Units Decomposition** (30 minutes)
**AI-DLC Personas:** Developers (Lead) + Product Owner + AI

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**Developer Approval Response:**
```
I approve. Proceed.
```

## CONSTRUCTION PHASE (2.5 hours)

### **Activity 4: Domain Model Creation** (45 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/task_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**Developer Approval Response:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

### **Activity 5: Code Generation** (50 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/task_component_model.md file. Generate a very simple and intuitive Python implementation for the Task Management Component that is in the design. For the prioritizeTask() method, use basic rule-based logic to assign priority scores based on deadline and client importance. Generate the classes in respective individual files but keep them in `taskManager` directory.
```

### **Activity 6: Architecture Planning** (35 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

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

### **Activity 7: Build IaC/Rest APIs** (30 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the taskManager/ folder. Create python flask apis for each of the service there.
```

## OPERATIONS PHASE (30 minutes)

### **Operations Phase Learning Discussion** (30 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Learning Focus:** Understanding AI-DLC Operations Phase Concepts

Since the Operations Phase doesn't have specific prompts in Appendix A, this is a guided discussion about Operations Phase principles from the AI-DLC whitepaper:

**Key Operations Phase Concepts:**
- **Deployment Units:** AI packages modules into operational artifacts (container images, serverless functions)
- **AI-Driven Testing:** AI executes functional, security, and performance tests and analyzes results
- **Observability:** AI analyzes metrics, logs, and traces to detect patterns and anomalies
- **Proactive Operations:** AI predicts potential SLA violations and proposes mitigation actions
- **Human Oversight:** Developers validate AI recommendations and approve operational changes

**Discussion Questions:**
1. How would AI help deploy our task manager to production?
2. What kinds of monitoring would be most valuable for this application?
3. How could AI help us detect and respond to issues proactively?
4. What operational decisions should humans validate vs. what could AI handle autonomously?

**Practical Exercise:** Review the generated deployment plan from Activity 6 and discuss how AI could enhance the operational monitoring and incident response for the task manager.

---

# TIER 2: INTERMEDIATE - COMPLETE END-TO-END
## "Smart Customer Feedback System using Full AI-DLC Methodology"

### Duration: 5 hours
### Project: AI-powered business application with multi-channel feedback processing

---

## INCEPTION PHASE (1.5 hours)

### **Activity 1: Setup Prompt** (15 minutes)
**AI-DLC Personas:** Product Owner + AI

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

### **Activity 2: User Stories Creation** (50 minutes)
**AI-DLC Personas:** Product Owner (Lead) + AI

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a smart customer feedback system that collects feedback from multiple channels (email, chat, surveys), automatically categorizes and prioritizes feedback using AI sentiment analysis, generates insights and trends for product managers, alerts teams about critical issues, and tracks resolution and follow-up activities."
```

**Product Owner Approval Response:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

### **Activity 3: Units Decomposition** (35 minutes)
**AI-DLC Personas:** Developers (Lead) + Product Owner + AI

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**Developer Approval Response:**
```
I approve. Proceed.
```

## CONSTRUCTION PHASE (3 hours)

### **Activity 4: Domain Model Creation** (60 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/feedback_analysis_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**Developer Approval Response:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

### **Activity 5: Code Generation** (70 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/feedback_analysis_component.md file. Generate a very simple and intuitive Python implementation for the Feedback Analysis Component that is in the design. For the analyzeSentiment() method, use amazon bedrock APIs to extract sentiment and entities from the feedback text. Generate the classes in respective individual files but keep them in `feedbackAnalyzer` directory.

Refer to the generated codes in feedbackAnalyzer directory. I want the SentimentAnalyzer component to make a call to GenAI. The current implementation uses basic sentiment rules. Can you analyse and give me a plan on how I can leverage GenAI for both Sentiment Analysis and Category Classification.
```

### **Activity 6: Architecture Planning** (30 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: design/feedback_analysis_component.md, units in the UNITS/ folder, cloud architecture in the ARCHITECTURE/ folder, and backend code in the feedbackAnalyzer/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

### **Activity 7: Build IaC/Rest APIs** (20 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the feedbackAnalyzer/ folder. Create python flask apis for each of the service there.
```

## OPERATIONS PHASE (30 minutes)

### **Operations Phase Learning Discussion** (30 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Learning Focus:** Advanced AI-DLC Operations for Business Applications

**Key Operations Phase Concepts for Business Systems:**
- **Multi-Service Deployment:** AI packages feedback system into multiple deployment units (Lambda functions, SQS queues, DynamoDB tables)
- **AI-Driven Testing:** AI generates and executes functional, security, and performance tests for sentiment analysis workflows
- **Business Metrics Monitoring:** AI analyzes feedback processing accuracy, sentiment classification precision, and user engagement metrics
- **Proactive Issue Detection:** AI detects patterns like sentiment analysis accuracy degradation or processing latency spikes
- **Intelligent Scaling:** AI recommends scaling actions based on feedback volume patterns and processing requirements

**Discussion Questions:**
1. How would AI help monitor the accuracy of sentiment analysis over time?
2. What operational alerts would be most critical for a customer feedback system?
3. How could AI help optimize costs while maintaining performance during varying feedback volumes?
4. What compliance or data privacy considerations would AI need to monitor in Operations?

**Practical Exercise:** Review the deployment and monitoring requirements for the feedback system and discuss how AI-driven operations would enhance reliability and performance.

---

# TIER 3: ADVANCED - COMPLETE END-TO-END
## "Enterprise Digital Asset Management Platform using Full AI-DLC Methodology"

### Duration: 6 hours
### Project: Enterprise-scale platform with compliance, security, and multi-tenant requirements

---

## INCEPTION PHASE (2 hours)

### **Activity 1: Setup Prompt** (20 minutes)
**AI-DLC Personas:** Product Owner + AI

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

### **Activity 2: Enterprise User Stories Creation** (70 minutes)
**AI-DLC Personas:** Product Owner (Lead) + Multiple Stakeholders + AI

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build an enterprise digital asset management platform for a large financial services company that manages regulatory documents across 15 business units, ensures compliance with multiple jurisdictions (SEC, FINRA, GDPR), provides AI-powered document classification and intelligent search, supports comprehensive audit trails and version control, integrates with existing enterprise systems (Active Directory, SharePoint, Salesforce), and scales to handle 100K+ documents with 500+ concurrent users while maintaining sub-second search response times."
```

**Product Owner Approval Response:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

### **Activity 3: Enterprise Units Decomposition** (50 minutes)
**AI-DLC Personas:** Developers (Lead) + Product Owner + AI

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**Developer Approval Response:**
```
I approve. Proceed.
```

## CONSTRUCTION PHASE (3.5 hours)

### **Activity 4: Enterprise Domain Model Creation** (80 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/document_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**Developer Approval Response:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

### **Activity 5: Enterprise Code Generation** (90 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/document_classifier_component.md file. Generate a very simple and intuitive Python implementation for the Document Classification Component that is in the design. For the classifyDocument() method, use amazon bedrock APIs to extract document type, compliance metadata, and regulatory classification from document content. Generate the classes in respective individual files but keep them in `documentClassifier` directory.

Refer to the generated codes in documentClassifier directory. I want the DocumentAnalyzer component to make a call to GenAI. The current implementation uses basic pattern matching. Can you analyse and give me a plan on how I can leverage GenAI for both Document Classification and Compliance Validation.
```

### **Activity 6: Enterprise Architecture** (40 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

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

### **Activity 7: Enterprise APIs** (20 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the documentClassifier/ folder. Create python flask apis for each of the service there.
```

## OPERATIONS PHASE (30 minutes)

### **Operations Phase Learning Discussion** (30 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Learning Focus:** Enterprise AI-DLC Operations at Scale

**Key Enterprise Operations Phase Concepts:**
- **Complex Deployment Units:** AI packages enterprise platform into container images, serverless functions, and infrastructure stacks with multi-tenant configurations
- **Comprehensive Testing:** AI generates enterprise-grade test suites including functional acceptance, security compliance, performance at scale (500+ users, 100K+ documents), and integration tests with enterprise systems
- **Enterprise Observability:** AI analyzes business metrics (document classification accuracy, search relevance), technical metrics (API latency, database performance), and compliance metrics (audit trail completeness, retention compliance)
- **Predictive Operations:** AI detects patterns and predicts SLA violations, compliance risks, and performance degradation before they impact users
- **Automated Remediation:** AI integrates with enterprise runbooks to propose scaling, optimization, and compliance remediation actions

**Discussion Questions:**
1. How would AI help ensure compliance with multiple regulatory frameworks (SEC, FINRA, GDPR) in production?
2. What operational challenges arise when managing 500+ concurrent users and 100K+ documents?
3. How could AI help with enterprise integration monitoring and troubleshooting?
4. What governance and approval processes would be needed for AI-driven operational changes in a financial services environment?

**Practical Exercise:** Review the enterprise deployment plan and discuss how AI-driven operations would handle the complexity, compliance, and scale requirements of the digital asset management platform.

---

## Workshop Series Summary

### **Authentic AI-DLC Implementation**

All workshop tiers follow the **exact 7-step sequence from Appendix A**:

| **Phase** | **Activities** | **Duration by Tier** |
|-----------|---------------|---------------------|
| **INCEPTION** | Setup, User Stories, Units | 1.5h / 1.5h / 2h |
| **CONSTRUCTION** | Domain Model, Code Generation, Architecture, APIs | 2.5h / 3h / 3.5h |
| **OPERATIONS** | Learning Discussion | 30min / 30min / 30min |

### **Operations Phase as Learning Experience**
Since Appendix A doesn't provide specific Operations Phase prompts, each tier includes a guided discussion covering:
- AI-DLC Operations Phase concepts from the whitepaper
- Tier-appropriate complexity (basic → business → enterprise)
- Practical application to the workshop project
- Understanding of AI-human collaboration in operations

This approach ensures participants learn the complete AI-DLC methodology while maintaining authenticity to the official framework.

---

# TIER 2: INTERMEDIATE - COMPLETE END-TO-END
## "Smart Customer Feedback System using Full AI-DLC Methodology"

### Duration: 6 hours
### Project: AI-powered business application with multi-channel feedback processing

---

## INCEPTION PHASE (1.5 hours)

### **Activity 1: Setup Prompt** (15 minutes)
**AI-DLC Personas:** Product Owner + AI

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

### **Activity 2: User Stories Creation** (50 minutes)
**AI-DLC Personas:** Product Owner (Lead) + AI

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build a smart customer feedback system that collects feedback from multiple channels (email, chat, surveys), automatically categorizes and prioritizes feedback using AI sentiment analysis, generates insights and trends for product managers, alerts teams about critical issues, and tracks resolution and follow-up activities."
```

**Product Owner Approval Response:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

### **Activity 3: Units Decomposition** (35 minutes)
**AI-DLC Personas:** Developers (Lead) + Product Owner + AI

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**Developer Approval Response:**
```
I approve. Proceed.
```

## CONSTRUCTION PHASE (3 hours)

### **Activity 4: Domain Model Creation** (60 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/feedback_analysis_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**Developer Approval Response:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

### **Activity 5: Code Generation** (70 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/feedback_analysis_component.md file. Generate a very simple and intuitive Python implementation for the Feedback Analysis Component that is in the design. For the analyzeSentiment() method, use amazon bedrock APIs to extract sentiment and entities from the feedback text. Generate the classes in respective individual files but keep them in `feedbackAnalyzer` directory.

Refer to the generated codes in feedbackAnalyzer directory. I want the SentimentAnalyzer component to make a call to GenAI. The current implementation uses basic sentiment rules. Can you analyse and give me a plan on how I can leverage GenAI for both Sentiment Analysis and Category Classification.
```

### **Activity 6: Architecture Planning** (30 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced Cloud Architect. Before you start the task as mentioned below, please do the planning and write your steps in a deployment_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer component design model: design/feedback_analysis_component.md, units in the UNITS/ folder, cloud architecture in the ARCHITECTURE/ folder, and backend code in the feedbackAnalyzer/ folder. Complete the following:
- Generate a end-to-end plan for deployment of the backend on AWS cloud using CloudFormation.
- Document all the pre-requisites for the deployment, if any.

Once I approve the plan:
- Follow the best practice of clean, simple, explainable coding.
- All output code goes in the DEPLOYMENT/ folder.
- Validate that the generated code works as intended, by creating a validation plan, generate a validation report.
- Review the validation report and fix all identified issues, update the validation report.
```

### **Activity 7: Build IaC/Rest APIs** (20 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the feedbackAnalyzer/ folder. Create python flask apis for each of the service there.
```

## OPERATIONS PHASE (1.5 hours)

### **Activity 8: Deployment and Testing** (60 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Operations Phase Activities:**
- AI packages feedback system into Deployment Units (Lambda functions, SQS queues, DynamoDB tables)
- AI generates and executes comprehensive test suites:
  - Functional tests for feedback processing workflows
  - Security tests for data handling and API endpoints
  - Performance tests for sentiment analysis throughput
- AI analyzes test results and correlates failures with specific components
- AI proposes fixes for failed tests (e.g., optimizing sentiment analysis performance)
- Developers validate AI's findings and approve fixes

### **Activity 9: Observability and Monitoring** (30 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Advanced Operations Phase:**
- AI analyzes metrics, logs, and traces to identify patterns in feedback processing
- AI detects anomalies in sentiment analysis accuracy and processing latency
- AI integrates with incident runbooks to suggest actions:
  - Scaling Lambda functions during high feedback volume
  - Adjusting DynamoDB throughput for better performance
  - Rebalancing API Gateway traffic distribution
- Developers validate AI's recommendations and approve operational changes
- Focus on proactive issue resolution and continuous system optimization

---

# TIER 3: ADVANCED - COMPLETE END-TO-END
## "Enterprise Digital Asset Management Platform using Full AI-DLC Methodology"

### Duration: 7 hours
### Project: Enterprise-scale platform with compliance, security, and multi-tenant requirements

---

## INCEPTION PHASE (2 hours)

### **Activity 1: Setup Prompt** (20 minutes)
**AI-DLC Personas:** Product Owner + AI

```
We will work on building an application today. For every front end and backend component we will create a project folder. All documents will reside in the aidlc-docs folder. Throughout our session I'll ask you to plan your work ahead and create an md file for the plan. You may work only after I approve said plan. These plans will always be stored in aidlc-docs/plans folder. You will create many types of documents in the md format. Requirement, features changes documents will reside in aidlc-docs/requirements folder. User stories must be stored in the aidlc-docs/story-artifacts folder. Architecture and Design documents must be stored in the aidlc-docs/design-artifacts folder. All prompts in order must be stored in the aidlc-docs/prompts.md file. Confirm your understanding of this prompt. Create the necessary folders and files for storage, if they do not exist already.
```

### **Activity 2: Enterprise User Stories Creation** (70 minutes)
**AI-DLC Personas:** Product Owner (Lead) + Multiple Stakeholders + AI

```
Your Role: You are an expert product manager and are tasked with creating well defined user stories that becomes the contract for developing the system as mentioned in the Task section below. Plan for the work ahead and write your steps in an md file (user_stories_plan.md) with checkboxes for each step in the plan. If any step needs my clarification, add a note in the step to get my confirmation. Do not make critical decisions on your own. Upon completing the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Build user stories for the high-level requirement as described here: "Build an enterprise digital asset management platform for a large financial services company that manages regulatory documents across 15 business units, ensures compliance with multiple jurisdictions (SEC, FINRA, GDPR), provides AI-powered document classification and intelligent search, supports comprehensive audit trails and version control, integrates with existing enterprise systems (Active Directory, SharePoint, Salesforce), and scales to handle 100K+ documents with 500+ concurrent users while maintaining sub-second search response times."
```

**Product Owner Approval Response:**
```
Yes, I like your plan as in the user_stories_plan.md. Now exactly follow the same plan. Interact with me as specified in the plan. Once you finish each step, mark the checkboxes in the plan.
```

### **Activity 3: Enterprise Units Decomposition** (50 minutes)
**AI-DLC Personas:** Developers (Lead) + Product Owner + AI

```
Your Role: You are an experienced software architect. Before you start the task as mentioned below, please do the planning and write your steps in the units_plan.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories mvp_user_stories.md file. Group the user stories into multiple units that can be built independently. Each unit contains highly cohesive user stories that can be built by a single team. The units are loosely coupled with each other. For each unit, write their respective user stories and acceptance criteria in individual md files in the design/ folder.
```

**Developer Approval Response:**
```
I approve. Proceed.
```

## CONSTRUCTION PHASE (3.5 hours)

### **Activity 4: Enterprise Domain Model Creation** (80 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an design/component_model.md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Your Task: Refer to the user stories in the design/document_management_unit.md file. Design the component model to implement all the user stories. This model shall contain all the components, the attributes, the behaviours and how the components interact to implement the user stories. Do not generate any codes yet. Write the component model into a separate md file in the /design folder.
```

**Developer Approval Response:**
```
I approve the plan. Proceed. After completing each step, mark the checkbox in your plan file.
```

### **Activity 5: Enterprise Code Generation** (90 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to component design in the design/document_classifier_component.md file. Generate a very simple and intuitive Python implementation for the Document Classification Component that is in the design. For the classifyDocument() method, use amazon bedrock APIs to extract document type, compliance metadata, and regulatory classification from document content. Generate the classes in respective individual files but keep them in `documentClassifier` directory.

Refer to the generated codes in documentClassifier directory. I want the DocumentAnalyzer component to make a call to GenAI. The current implementation uses basic pattern matching. Can you analyse and give me a plan on how I can leverage GenAI for both Document Classification and Compliance Validation.
```

### **Activity 6: Enterprise Architecture** (40 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

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

### **Activity 7: Enterprise APIs** (20 minutes)
**AI-DLC Personas:** Developers (Lead) + AI

```
Your Role: You are an experienced software engineer. Before you start the task as mentioned below, please do the planning and write your steps in an md file with checkboxes against each step in the plan. If any step needs my clarification, please add it to the step to interact with me and get my confirmation. Do not make critical decisions on your own. Once you produce the plan, ask for my review and approval. After my approval, you can go ahead to execute the same plan one step at a time. Once you finish each step, mark the checkboxes as done in the plan.

Task: Refer to the services.py under the documentClassifier/ folder. Create python flask apis for each of the service there.
```

## OPERATIONS PHASE (1.5 hours)

### **Activity 8: Enterprise Deployment and Validation** (60 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Enterprise Operations Phase Activities:**
- AI packages the enterprise platform into Deployment Units:
  - Container images for Kubernetes environments
  - Serverless functions (AWS Lambda) for document processing
  - Infrastructure components (CDK stacks) for multi-tenant architecture
- AI generates comprehensive enterprise test suites:
  - Functional acceptance tests for document management workflows
  - Static and dynamic security tests for compliance requirements
  - Load testing scenarios for 500+ concurrent users and 100K+ documents
  - Integration tests with enterprise systems (Active Directory, SharePoint)
- AI executes test suites, analyzes results, and correlates failure points with:
  - Code changes in document classification algorithms
  - Configuration issues in multi-tenant settings
  - Performance bottlenecks in search indexing
- AI proposes enterprise-grade fixes and optimizations

### **Activity 9: Enterprise Operations and Monitoring** (30 minutes)
**AI-DLC Personas:** Developers + Product Owner + AI

**Advanced Enterprise Operations:**
- AI analyzes enterprise telemetry data including:
  - Business metrics (document processing accuracy, search relevance)
  - Technical metrics (API latency, database performance, search response times)
  - Compliance metrics (audit trail completeness, data retention compliance)
- AI detects patterns and predicts potential SLA violations:
  - Document classification accuracy degradation
  - Search performance issues during peak usage
  - Compliance violation risks in document handling
- AI integrates with enterprise incident runbooks and proposes actions:
  - Auto-scaling document processing clusters
  - Rebalancing search index distribution
  - Triggering compliance remediation workflows
- AI generates compliance reports and audit documentation
- Developers validate all AI recommendations ensuring enterprise governance requirements

---

## Workshop Series Summary

### **Complete AI-DLC Implementation Across All Tiers**

Each workshop tier implements the **complete end-to-end AI-DLC methodology** with all official prompts from Appendix A:

| **Phase** | **Primary Personas** | **Tier 1 Duration** | **Tier 2 Duration** | **Tier 3 Duration** |
|-----------|---------------------|---------------------|---------------------|---------------------|
| **INCEPTION** | Product Owner + AI | 1.5 hours | 1.5 hours | 2 hours |
| **CONSTRUCTION** | Developers + AI | 2.5 hours | 3 hours | 3.5 hours |
| **OPERATIONS** | All Personas + AI | 1 hour | 1.5 hours | 1.5 hours |

### **Proper AI-DLC Terminology**
- ✅ **Phases**: Inception, Construction, Operations (explicitly called out)
- ✅ **Activities**: Setup, User Stories, Domain Design, etc. (not "steps")
- ✅ **Personas**: Product Owner, Developers, AI (highlighted throughout)
- ✅ **Operations Phase**: Fully implemented with deployment and monitoring

### **Progressive Complexity with Consistent Methodology**
- **Tier 1**: Personal task manager with basic AI integration
- **Tier 2**: Business feedback system with advanced AI features  
- **Tier 3**: Enterprise platform with compliance and scale requirements

All participants experience the complete AI-DLC workflow exactly as designed by AWS, learning authentic methodology that transfers directly to real-world projects.