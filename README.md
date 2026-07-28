# 🔐 Enterprise Certificate Management System

An enterprise-inspired SSL/TLS Certificate Management System built using **FastAPI**, **SQLAlchemy**, **SQLite**, and **Bootstrap**.

This project was created to simplify the management of SSL certificates by providing a centralized interface for generating Certificate Signing Requests (CSR), managing private keys, storing certificate metadata, and tracking certificate status.

The idea behind this project came from observing how certificate management is handled in enterprise environments, where teams often perform repetitive manual tasks for certificate requests and tracking. This application focuses on making those day-to-day management tasks easier through a clean and user-friendly interface.

---

## ✨ Features

- 🔑 Generate RSA Private Keys
- 📄 Generate Certificate Signing Requests (CSR)
- 🛡️ Generate Self-Signed Certificates
- 📤 Upload CA-Signed Certificates
- 🔍 Parse Certificate Information
- 📋 Certificate Inventory Dashboard
- 📑 Certificate Details Page
- 🔎 Search Certificates
- 🎯 Filter Certificates by Status
- ⬇️ Download Private Keys
- ⬇️ Download CSR Files
- ⬇️ Download Certificates
- 📊 Dashboard Statistics
- 💾 SQLite Database Integration

---

## 🛠️ Technology Stack

### 🚀 Backend

- FastAPI
- Python
- SQLAlchemy
- SQLite
- Cryptography

### 🎨 Frontend

- Jinja2 Templates
- HTML5
- Bootstrap 5

### 🔧 Tools

- OpenSSL
- Git
- GitHub

---

## 🔄 Application Workflow

```text
Create Certificate Request
            │
            ▼
Generate Private Key
            │
            ▼
Generate CSR
            │
            ▼
Store Certificate Request
            │
            ▼
Upload Signed Certificate
            │
            ▼
Parse Certificate Metadata
            │
            ▼
View Certificate Details
            │
            ▼
Download Certificate / CSR / Key
```

---

## 📁 Project Structure

```text
app/
│
├── database/
├── routers/
├── services/
├── templates/
├── static/
└── main.py

certificates/
```

---

## 📸 Screenshots

### 🏠 Dashboard
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3844a475-c3ba-4ba7-9ac7-c8a104e31d5f" />


### 📋 Certificate Inventory

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8ab63253-ab2d-4482-9dad-ece79437b4de" />


### 📄 Certificate Details

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fb5b545c-7836-4e00-bc2c-e1a4aa8c86a3" />


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7a671447-7e45-4e60-9d0f-8d4aa8a33508" />



---

## 🚀 Getting Started

### 📥 Clone Repository

```bash
git clone <repository-url>
```

### 📂 Navigate to Project

```bash
cd enterprise-certificate-management-system
```

### 🐍 Create Virtual Environment

```bash
python -m venv venv
```

### ▶️ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```
http://127.0.0.1:8000
```

---

## 📦 Current Modules

- 📊 Dashboard
- 📋 Certificate Inventory
- 📄 Certificate Details
- 📝 Certificate Request Generation
- 🛡️ Self-Signed Certificate Generation
- 📤 Certificate Upload
- 🔍 Certificate Metadata Parser
- 🔎 Search & Filtering

---

## 🚀 Future Improvements

This project represents the management side of SSL/TLS certificates.

The next phase of this work is planned as a **separate repository** focused on enterprise-scale automation rather than UI-centric management.

The upcoming platform will include:

- 🤖 Certificate Lifecycle Automation
- ⏰ Automatic Expiry Monitoring
- 🔄 Renewal Workflows
- ✅ Approval Workflows
- 🌐 REST APIs for Multiple Applications
- 📅 Scheduled Jobs
- 📧 Email Notifications
- 🚀 Deployment Automation
- 📝 Audit Logs
- ☁️ Enterprise Infrastructure Integrations

Keeping both projects separate allows each repository to have a clear purpose while demonstrating the evolution from certificate management to enterprise automation.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience with:

- ⚡ FastAPI Development
- 🗄️ SQLAlchemy ORM
- 🎨 Jinja2 Templates
- 🔐 SSL/TLS Certificate Concepts
- 🔑 RSA Key Generation
- 📄 CSR Generation
- 🔍 Certificate Parsing
- 📂 File Handling
- 📝 CRUD Application Development
- 🏢 Enterprise-Inspired System Design

---

## 👨‍💻 Author

**Ajay Kumar Pasunoori**

🚀 DevOps Engineer | ☁️ AWS | 🐧 Linux | 🌍 Terraform | ☸️ Kubernetes | 🐳 Docker | ⚡ FastAPI

🔗 GitHub: https://github.com/Ajaypasunoori2806
