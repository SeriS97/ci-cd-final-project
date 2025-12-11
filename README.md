# CI/CD Final Project

This repository contains a sample **Flask web application** demonstrating Continuous Integration (CI) and Continuous Delivery (CD) workflows using **GitHub Actions** and **OpenShift Pipelines (Tekton)**.

## Project Overview
The purpose of this project is to implement CI/CD automation for a simple application. The workflows ensure:

- Code quality through linting
- Automatic testing
- Deployment automation to OpenShift

## Repository Structure

ci-cd-final-project/
├── .github/
│ └── workflows/
│ └── workflow.yml # GitHub Actions workflow
├── .tekton/
│ └── tasks.yml # Tekton/OpenShift tasks
├── app/
│ └── app.py # Sample Flask app
├── tests/
│ └── test_app.py # Nose tests
├── README.md
└── requirements.txt

markdown
Copy code

## CI/CD Pipelines

### GitHub Actions Workflow
- **Linting Step:** Ensures code style is consistent.
- **Test Step:** Runs unit tests using Nose.
- Screenshot: `cicd-github-validate.png`

### OpenShift Pipelines (Tekton)
- **Tasks:** 
  - Cleanup task
  - Nose test task
- **Pipeline Details:** `oc-pipelines-oc-final.png`
- **Successful Pipeline Run:** `oc-pipelines-oc-green.png`
- **PVC Details:** `oc-pipelines-console-pvc-details.png`

### Running Application
- **Application logs in OpenShift:** `oc-pipelines-app-logs.png`
- Access the running Flask app through OpenShift route.

## How to Use
1. Clone the repository:
```bash
git clone <your-repo-url>
cd ci-cd-final-project
Push changes to trigger GitHub Actions workflow.

Apply Tekton pipelines in OpenShift to deploy the app.

Technologies Used
Python 3.x

Flask

Nose (testing)

GitHub Actions (CI)

Tekton / OpenShift Pipelines (CD)

YAML for pipeline and workflow definitions

vbnet
Copy code

This README **already includes everything your peer reviewers will need to understand your project** and aligns with the tasks (Tasks 1–10).  

If you want, I can now **help you create the actual GitHub Actions workflow and Tekton files step by step** so you can fill in the URLs and screenshots for submission.  

Do you want to do that next?
