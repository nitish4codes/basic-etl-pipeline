# 📊 Google Play Store ETL Pipeline

## 🚀 Project Overview

This project implements an automated **ETL (Extract, Transform, Load) pipeline** to process and analyze **10,000+ mobile application records** from the Google Play Store dataset.

The goal is to handle messy, real-world data and convert it into a clean, structured format suitable for analysis and querying.

---

## ⚙️ Key Features

### 🔹 Data Ingestion

* Automated extraction of raw dataset records from CSV files using **Pandas**

### 🔹 Advanced Transformation

* Custom data cleaning logic to handle inconsistencies:

  * Converted file sizes with `M` and `k` suffixes into standardized byte values
  * Normalized mixed-format fields into consistent numerical formats

### 🔹 Data Integrity

* Cleaned and standardized:

  * Removed special characters (`+`, `,`) from install counts
  * Removed currency symbols from pricing data
* Ensured **100% formatting consistency**

### 🔹 Structured Storage

* Loaded cleaned data into a **SQLite relational database**
* Optimized for efficient querying and long-term storage
* Exported cleaned dataset as a backup CSV file

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * Pandas (Data Manipulation)
  * SQLite3 (Database Management)
* **Tools:** Git, GitHub, VS Code

---

## 🔄 ETL Workflow

### 1️⃣ Extract

* Reads raw dataset from `googleplaystore.csv`

### 2️⃣ Transform

* Removes duplicate entries
* Cleans and standardizes:

  * `Installs` column → numeric format
  * `Price` column → numeric format
  * `Size` column → consistent numeric representation
* Handles missing and inconsistent values

### 3️⃣ Load

* Stores processed data into a `.db` SQLite database
* Exports cleaned dataset into a `.csv` file for backup

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/nitish4codes/basic-etl-pipeline.git
cd basic-etl-pipeline
```

### 2. Install dependencies

```bash
pip install pandas
```

### 3. Run the ETL pipeline

```bash
python etl_script.py
```

---

## 📂 Project Structure

```
├── googleplaystore.csv     # Raw dataset
├── cleaned_data.csv        # Processed dataset
├── database.db             # SQLite database
├── etl_script.py           # Main ETL pipeline script
└── README.md               # Project documentation
```

---

## 📈 Future Improvements

* Add data validation checks and logging
* Integrate visualization dashboards (e.g., Power BI / Tableau)
* Automate pipeline scheduling (e.g., cron jobs / Airflow)
* Extend dataset with real-time API integration

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements.

---

## 📜 License

This project is open-source and available under the MIT License.

---
