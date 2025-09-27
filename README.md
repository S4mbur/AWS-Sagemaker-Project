# Project Report: AWS Step Functions Orchestration with SageMaker Integration

## 1. Introduction
This project demonstrates the orchestration of multiple AWS Lambda functions using **AWS Step Functions**.  
The workflow is designed to sequentially invoke Lambda functions, enabling modular processing, logging, and monitoring.  
Development and testing were done in a **SageMaker Notebook (IPYNB file)**.

---

## 2. Project Objectives
- Automate the invocation of multiple Lambda functions in sequence.  
- Leverage **AWS Step Functions** for orchestration, monitoring, and error handling.  
- Demonstrate integration between **SageMaker** and **AWS Lambda**.  
- Provide visual evidence of successful execution, monitoring logs, and event timelines.  

---

## 3. Workflow Design
The workflow consists of three Lambda functions executed sequentially:

1. **Lambda Invoke**
2. **Lambda Invoke (1)**
3. **Lambda Invoke (2)**

Execution begins at **Start** and ends at **End** once all functions succeed.

### Workflow Visualization
![Step Functions Workflow](images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-09-27%20221649.png)

---

## 4. Execution Results

### 4.1 Graph View
The execution graph shows all Lambda functions invoked successfully in sequence.  

![Execution Graph View](images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-09-27%20222012.png)

---

### 4.2 Table View
The table view summarizes status, duration, and log links for each Lambda task.  

![Execution Table View](images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-09-27%20222038.png)

---

### 4.3 Event Timeline
The event log provides a breakdown of scheduling, starting, and successful completion of tasks.  

![Execution Event Timeline](images/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202025-09-27%20222117.png)

---

## 5. Technical Highlights
- **AWS Lambda**: Each step encapsulates serverless logic.  
- **AWS Step Functions**: Provides orchestration, fault tolerance, monitoring.  
- **SageMaker Notebook**: Used for development/testing.  
- **CloudWatch Logs**: Available for debugging and detailed analysis.  

---

## 6. Future Improvements
- Add **parallel execution** for independent tasks.  
- Enhance **error handling** with retries and catchers.  
- Extend steps to trigger **SageMaker training/inference jobs**.  
- Automate **report generation** from execution logs.  

---

## 7. Conclusion
This project successfully demonstrates orchestrating AWS Lambda functions using Step Functions within a SageMaker-driven workflow.  

✅ **Status:** All Lambda invocations succeeded.  
📊 **Total Execution Time:** ~1.5 seconds.  
🔗 **Logs available in CloudWatch.**

---
