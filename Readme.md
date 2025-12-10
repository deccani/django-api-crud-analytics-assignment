
# Django CRUD + API Integration + Analytics Dashboard

Full Stack Assignment — Using Django, PostgreSQL & Chart.js

## 🔗 Live Deployed Project  
The site is hosted on a free service renderer.com It would take a minute or two to start the site and run when the url is opened
👉 **https://django-api-crud-analytics.onrender.com**

---
![home.JPG](attachment:home.JPG)
![crud.JPG](attachment:crud.JPG)
![api.JPG](attachment:api.JPG)
![analytics.JPG](attachment:analytics.JPG)

### ✔ Prerequisites
📌 Install the following:

| Software | Required |
|----------|----------|
| Python | 3.10+ |
| PostgreSQL | Installed & Running |

---

## 🚀 Run This Project Locally (Step-by-Step)

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/deccani/django-api-crud-analytics-assignment.git
cd django-api-crud-analytics-assignment
```

---

### **2️⃣ Create Virtual Environment**

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3️⃣ Install Requirements**

```bash
pip install -r requirements.txt
```

---

### **4️⃣ Configure PostgreSQL connection**

Start your postgres conection. Enter the connection details in `.env` in project root and save
Replace values if your DB details differ

```
DB_NAME=your_DB_name
DB_USER=your_DB_username
DB_PASSWORD=your_DB_passowrd
DB_HOST=localhost
DB_PORT=5432
```
---

### **5️⃣ Run Database Migrations**
Open command promt at the root of our project where .env is located and run

```bash
python manage.py migrate
```

---

### **6️⃣ Start Django Server**

```bash
python manage.py runserver
```

Open in browser:

👉 http://127.0.0.1:8000

---

## 🧩 Project Modules

| Module | Description |
|--------|------------|
| Task Manager (CRUD) | Add, Edit, Delete, List tasks using REST API |
| External API Fetching | Fetch GDP, Population, and Unemployment data from World Bank |
| Analytics Dashboard | Visualize saved data with charts |

---

### Key Django Files

| File | Purpose |
|------|--------|
| tasks/views.py | All CRUD + API + Analytics logic |
| tasks/models.py | Database models |
| backend/settings.py | DB + Static + Deployment configuration |
| templates/* | UI screens |

---

- **Backend:** Django + Django REST Framework
- **Database:** PostgreSQL
- **UI:** Bootstrap + Javascript
- **Charts:** Chart.js
- **Deployment:** Render.com
- **External API:** World Bank API

---
## 🧩 Project Modules Explained

### **1️⃣ Task Manager — CRUD + REST API**
This dashboard lets users create, edit, and delete tasks just like any real project management tool. Although the page looks simple, every action communicates with the backend using REST APIs - i mean the data updates in the database without refreshing the page

✔ How it works:
- When a task is added, edited, or deleted, the page sends a REST API request to the server
- Django REST Framework receives the request and updates the database
- The UI uses JavaScript to instantly refresh the table, creating a smooth experience
- **Satisfies Requirement #1: CRUD via REST APIs**

---

### **2️⃣ External API Integration (World Bank Data Import)**

This feature connects to the official World Bank API to fetch real global economic data. The system imports data according to selected indicators, it ensures the data is not duplicated into Database (It ignores the data rows which are already present in database - we have implemented unique constratints on the table) and saves them into our database, similar to how real applications sync data from third-party services

✔ Steps:
- User selects an economic metric (GDP, Population or Unemployement) and triggers import
- Backend calls World Bank API
- The backend requests real data from the World Bank public API
- Data is cleaned, filtered by year, and stored only if not already saved (Duplicates are avoided)
- **Satisfies Requirement #2: API integration**

---

### **3️⃣ Analytics Dashboard — Visualizations using Chart.js**

This module converts saved database records (From Previous module where we fetched data from world bank API) into visual insights using interactive chart. Instead of calling the external API again, the system reads directly from the database

✔ Steps:
- User selects countries, Data (Economic Indicator) type and year range for analysis. We have implemented range selection using datepicker UI component
- The backend loads filtered data from the database
- The data is displayed visually using Chart.js
- **Satisfies Requirement #3 — Data Reporting & Visualization**

---
## Author

**Prasad Darekar**  
Email: darekarp943@gmail.com
Contact: 9022640542

---
