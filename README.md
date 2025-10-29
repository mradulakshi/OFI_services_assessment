# 📦 NexGen Warehouse Optimization Tool

### 🚀 Overview

**NexGen Warehouse Optimization Tool** is an interactive, data-driven dashboard designed to help logistics and supply chain teams optimize warehouse operations using **IoT insights** and **data analytics**.

The system analyzes warehouse utilization, cost efficiency, and environmental IoT sensor data to provide **real-time recommendations** for improved storage planning, sustainability, and operational cost reduction.

This project demonstrates how **AI + IoT** can transform traditional warehousing into a **smart and sustainable** ecosystem.

---

## 🧠 Key Features

✅ **Warehouse Utilization Dashboard** — Visualizes stock efficiency across locations.
✅ **IoT Sensor Integration** — Tracks temperature, humidity, and weight sensors in real time.
✅ **Cost Optimization Insights** — Analyzes storage cost per unit and identifies expensive locations.
✅ **Smart Alerts** — Automatically flags low-stock, high-cost, and environmental anomalies.
✅ **Interactive Filters & Visuals** — Built using **Streamlit + Plotly** for intuitive exploration.
✅ **Downloadable Reports** — Export warehouse summaries directly from the dashboard.

---

## 🗂️ Project Structure

```
📁 NexGen-Warehouse-Optimization
│
├── 📄 warehouse_optimizer_app.py                     # Main Streamlit application
├── 📄 requirements.txt                               # Dependencies list
├── 📄 README.md                                      # Project documentation
├── 📄 Innovation_Brief.pdf                           # Project concept + innovation overview
│
├── 📊 warehouse_inventory.csv
├── 📊 sample_iot.csv
├── 📊 routes_distance.csv
├── 📊 delivery_performance.csv
├── 📊 cost_breakdown.csv
├── 📊 customer_feedback.csv
└── 📊 vehicle_fleet.csv
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mradulakshi/OFI_services_assessment
cd NexGen-Warehouse-Optimization
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # For Windows
# OR
source venv/bin/activate   # For macOS/Linux
```

### 3️⃣ Install Dependencies

Install all the required Python libraries using the provided **requirements.txt** file:

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

Launch the dashboard locally with Streamlit:

```bash
streamlit run app.py
```

Once it starts, open the local URL shown in the terminal (usually `http://localhost:8501`) to interact with the tool.

---

## 📊 Data Sources

| File Name                  | Description                                      |
| -------------------------- | ------------------------------------------------ |
| `warehouse_inventory.csv`  | Contains stock and reorder details per warehouse |
| `sample_iot.csv`           | IoT temperature, humidity, and weight data       |
| `routes_distance.csv`      | Warehouse route distances for logistics          |
| `delivery_performance.csv` | Delivery performance and delays                  |
| `cost_breakdown.csv`       | Breakdown of warehouse and transport costs       |
| `customer_feedback.csv`    | Post-delivery satisfaction insights              |
| `vehicle_fleet.csv`        | Vehicle and logistics capacity data              |

---

## 🌱 Sustainability & Innovation

This solution promotes **sustainability** by:

* Minimizing energy waste through IoT-based monitoring.
* Reducing logistics emissions via route optimization.
* Lowering overstocking and underutilization to cut material waste.
* Supporting **data-driven, green warehousing practices**.

---

## 🧩 Tech Stack

| Component         | Technology Used                          |
| ----------------- | ---------------------------------------- |
| Frontend          | Streamlit                                |
| Visualization     | Plotly Express                           |
| Data Handling     | Pandas, NumPy                            |
| Language          | Python                                   |
| IoT Integration   | CSV-based simulation of real sensor data |
| Report Generation | Streamlit Download Feature               |

---

## 🧑‍💻 Developed By

**Mradulakshi Manu**
📍 Manipal University Jaipur
💼 CSE IoT Department

---
