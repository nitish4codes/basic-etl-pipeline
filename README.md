# Google Play Store ETL Pipeline

## Project Overview
Developed an automated **ETL (Extract, Transform, Load)** pipeline to process and analyze over **10,000+ mobile application records** from the Google Play Store. The project demonstrates real-world data engineering skills by handling "messy" formatting, ensuring high data integrity, and implementing structured storage for relational analysis.

## Key Features
* **Data Ingestion**: Automated extraction of raw application data from CSV format using **Pandas**.
* **Advanced Transformation**: Engineered custom cleaning logic to resolve unit inconsistencies (e.g., converting 'M' and 'k' suffixes in file sizes to a uniform byte count).
* **Data Integrity**: Resolved 100% of formatting discrepancies by stripping special characters ('+', ',') from install counts and currency symbols from pricing.
* **Structured Storage**: Migrated processed data into a **SQLite** relational database, optimizing it for high-performance querying and long-term data persistence.

## Tech Stack
* **Language**: Python
* **Libraries**: Pandas (Data Manipulation), SQLite3 (Database Management)
* **Tools**: Git, GitHub, VS Code

## ETL Workflow
1.  **Extract**: Reads the raw `googleplaystore.csv` containing diverse mobile app metrics.
2.  **Transform**: 
    * Removes duplicate entries and handles missing values to prevent data redundancy.
    * Normalizes the `Installs` and `Price` columns into computable numeric types (integers/floats).
    * Converts human-readable `Size` strings (e.g., '19M') into standardized numeric byte values.
3.  **Load**: Stores the final normalized dataset into a `.db` file for SQL operations and exports a cleaned `.csv` for backup.

## How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/nitish4codes/google-play-store-etl-pipeline.git](https://github.com/nitish4codes/google-play-store-etl-pipeline.git)
    ```
2.  Install required libraries:
    ```bash
    pip install pandas
    ```
3.  Execute the pipeline:
    ```bash
    python etl_pipeline.py
    ```
