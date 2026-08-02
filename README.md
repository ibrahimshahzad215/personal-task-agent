# Personal Task Agent 🤖

An AI-powered personal task assistant built with Python.
This project uses the Groq API to process user instructions and helps manage tasks through an intelligent agent system.

## 🚀 Features

* AI-powered task assistance
* Natural language interaction
* Task management support
* Configurable AI model settings
* Secure API key handling using environment variables
* Modular agent-based architecture

## 🛠️ Technologies Used

* Python
* Groq API
* python-dotenv
* AI Agent Architecture

## 📂 Project Structure

```
personal-task-agent/
│
├── agent.py          # Main AI agent logic
├── config.py         # Configuration settings
├── .env              # Environment variables (not uploaded)
├── .gitignore        # Ignored files
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ibrahimshahzad215/personal-task-agent.git
```

### 2. Navigate to Project Folder

```bash
cd personal-task-agent
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Groq API key.

### 5. Run the Agent

```bash
python agent.py
```

## 🔒 Security

* API keys are stored securely using environment variables.
* The `.env` file is ignored using `.gitignore` and is not uploaded to GitHub.

## 👨‍💻 Author

**Muhammad Ibrahim Shahzad**

## 📌 Future Improvements

* Add a web-based user interface
* Add database integration
* Add more AI tools and automation capabilities
* Deploy as an online AI assistant
* Improve task memory and personalization
