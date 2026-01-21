# GenAI ETL Agent: The "Self-Healing" Data Pipeline

**A resilient, agentic ETL pipeline designed to ingest complex, semi-structured E-commerce JSON data.**

📊 **[View Project Presentation (Architecture & Design)](https://docs.google.com/presentation/d/1Ffy6olPfLao1BDbxxt5ChNYvj7OpziGRR29O37wdm7g/edit?usp=sharing)**

---

## 🚀 Overview
This project demonstrates a **Next-Gen Data Engineering** approach where the pipeline doesn't just execute hard-coded rules—it *thinks*. 

Using a simulated GenAI Agent, the system:
1.  **Inspects** incoming JSON files with unknown schemas.
2.  **Detects** nested structures (e.g., `customer.details`, `items[]`).
3.  **Dynamically Generates** Python code to flatten and normalize the data.
4.  **Loads** clean, structured data into a SQL Warehouse.

This architecture solves the common problem of **Schema Drift** and **Data Quality** failures in traditional ETL jobs.

---

## ⚡ Key Features
* **🤖 Agentic Intelligence:** Automatically identifies nested objects and lists without manual mapping.
* **🛡️ Self-Healing:** Detects missing fields (e.g., `discount_code`) and fills gaps automatically to prevent pipeline crashes.
* **🧹 Data Quality Circuit Breaker:** Standardizes mixed data types (e.g., converting `"1200.00"` strings to Floats) before loading.
* **📦 Zero-Dependency Deployment:** Runs locally with a simple `pandas` environment.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Core Library:** Pandas (Data Manipulation)
* **Database:** SQLite (In-Memory Relational Store)
* **Architecture:** Agentic ETL / Metadata-Driven Ingestion

---

## 🏁 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Manishkumar82077/Genai-etl-agent.git](https://github.com/Manishkumar82077/Genai-etl-agent.git)
cd Genai-etl-agent
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run the Agent
```bash
python main.py
```
4. View Output
The script will print the execution logs (simulating the Agent's reasoning) and display the final SQL table in your terminal:

```Plaintext
[AGENT] 🔍 Inspecting Schema...
[AGENT] 💡 Plan: Flatten JSON and rename columns.
...
✅ Transformation Successful.
🔎 Verifying SQL Data:
   order_id      cust_name    total_amount
   ORD-001       Manish Kumar     1280.0

```
```Plaintext
📂 Project Structure
main.py: The core logic containing the Agent simulation and ETL orchestrator.

data.json: A sample dataset containing 35 diverse records (including messy data).

requirements.txt: Project dependencies.
```


## 👤 Author
Manish Kumar 

 
