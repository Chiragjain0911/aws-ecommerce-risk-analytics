# AWS E-Commerce Product Risk Analytics

An end-to-end cloud analytics project designed to proactively identify high-risk products and customer dissatisfaction patterns using AWS data lake architecture and Power BI.

---

## Business Problem

E-commerce platforms often struggle to detect problematic products early — leading to:

- Poor customer experience  
- Increased return rates  
- Vendor quality issues  
- Revenue leakage  

This project builds a **data-driven risk intelligence system** that helps teams monitor product health and prioritize corrective actions.

---

## Solution Overview

The pipeline ingests raw product review data, processes it using AWS Glue, performs risk analytics in Amazon Athena, and delivers actionable insights through an interactive Power BI dashboard.

**End-to-end flow:**

CSV → S3 → Glue ETL → Glue Crawler → Athena → Power BI

---

## Architecture

View architecture diagram:  
![`architecture/architecture_diagram.png`](Project_Architectuer.png)

---

## Tech Stack

- **Amazon S3** — Data lake storage  
- **AWS Glue** — ETL & data cleaning  
- **AWS Glue Crawler** — Metadata catalog  
- **Amazon Athena** — SQL analytics  
- **Power BI** — Executive dashboard  
- **SQL** — Risk scoring logic  

---


---

## Key Analytics Implemented

### Product Risk Leaderboard  
Identifies products with highest complaint severity.

### Category Risk Exposure  
Highlights which product categories contribute most to business risk.

### Category Satisfaction Analysis  
Compares customer sentiment across categories.

### Risk Classification Model  
Rule-based scoring using:

- Average rating  
- Discount behavior  
- Complaint ratio  
- Minimum review threshold  

---

## Dashboard Preview

![Overview1](Overview1.png)
![Overview2](Overview2.png)


Suggested screenshots:

- Executive Overview  
- Product Dissatisfaction Analysis  
- Category Risk Exposure  

---

## How to Reproduce (High Level)

1. Upload dataset to S3  
2. Run AWS Glue ETL job  
3. Execute Athena SQL queries  
4. Export aggregated dataset  
5. Load into Power BI  

---

## Important SQL Files

Quick access:

- Risk Scoring Logic → [`sql_queries/return_risk_scoring.sql`](Return_Risk_Scoring_Model.sql)  
- Dashboard Dataset → [`sql_queries/dashboard_dataset.sql`](dashboard_dataset.sql)  
- Dissatisfaction Analysis → [`sql_queries/most_dissatisfying_products.sql`](Most_satisfying_products.sql)  

---

##  Author

**Chirag Jain**  
Aspiring Data Analyst | Cloud Analytics Enthusiast | 
Gmail : *jainchirag9575@gmail.com*

Connect on LinkedIn: *https://www.linkedin.com/in/chirag-jain-406145276/*

---

##  If You Found This Useful

Consider giving the repository a star — it helps the project reach more learners.

---

This project is shows my entry level data engineering skills. These skills also help me to sharpen my knowledge in data science.
At the moment I am ready to contribute my analytical skills in real world projects.



