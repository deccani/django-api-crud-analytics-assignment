# 🌐 Django CRUD + External API + Data Analytics Dashboard  
Full Stack Assignment — Using Django, PostgreSQL & Chart.js

🔗 **LIVE DEMO** → https://django-api-crud-analytics.onrender.com

---

## 📸 Screenshots (Replace with Images Later)

| Home | Task CRUD | Analytics |
|------|----------|-----------|
| *(Add Screenshot)* | *(Add Screenshot)* | *(Add Screenshot)* |

---

## 🧾 About This Project

This is a full stack assignment demonstrating **3 key software development modules**:

| Feature | Description |
|--------|------------|
| 🔹 CRUD Task Manager | Create, Update, Delete tasks — no page reload (AJAX + REST APIs) |
| 🌍 External API Integration | Fetch real data from World Bank API, store in DB |
| 📊 Data Analytics | Visualize stored data using Chart.js |

This project simulates real software behavior where a system:
✔ Fetches data from external APIs  
✔ Saves into database without duplicates  
✔ Displays filtered insights visually  

---

## 🧩 Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Django + Django REST Framework |
| Database | PostgreSQL |
| Frontend | HTML, Bootstrap, JavaScript |
| Charts | Chart.js |
| Deployment | Render.com |

---

## 📂 Project Structure — What Each Folder Contains

| File/Folder | Description |
|------------|-------------|
| `/backend` | Project settings, routing, static config |
| `/tasks` | All business logic → CRUD + API Fetch + Analytics |
| `/templates` | HTML UI files for each module |
| `requirements.txt` | Python dependencies |
| `Procfile` | Render deployment instruction |
| `.env (Local)` | Postgres credentials (not shared publicly) |

Inside `tasks/views.py`  
| View | Purpose |
|------|--------|
| `tasksUI()` | Displays CRUD interface |
| `fetch_indicator_dynamic()` | Calls World Bank API |
| `analyticsDashboard()` | Serves visualization dashboard |
| REST API functions | Handle JSON Create/Update/Delete |

Inside `tasks/models.py`
| Model | Purpose |
|-------|--------|
| Task | Stores task details |
| IndicatorData | Stores external API results |

---

## 🛠 Run Project Locally — Step-By-Step

### ✔ Prerequisites
📌 Install the following:

| Software | Required |
|----------|----------|
| Python | 3.10+ |
| PostgreSQL | Installed & Running |

---

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/django-api-crud-analytics.git
cd django-api-crud-analytics
