# Expense Tracker Setup

The **Expense Tracker** is a simple command-line tool designed to help you manage your expenses efficiently.

The idea for the project comes from [Developer Roadmaps](https://roadmap.sh/backend/projects).

#### Setup Instructions

1. Copy the Project Folder
Copy the folder containing the Expense Tracker project to `/usr/local/bin/`:

```bash
sudo cp -r /path/to/expense-tracker /usr/local/bin/
```
2. Create a bash script 
```sudo nano /usr/local/bin/tracker-wrapper```

```bash
#!/bin/bash
source /usr/local/bin/expense-tracker/venv/bin/activate
python /usr/local/bin/expense-tracker/tracker.py "$@"
```

3. Make the wrapper script executable
```sudo chmod +x /usr/local/bin/tracker-wrapper```

4. Create a symbolic link from tracker to tracker-wrapper:
```sudo ln -s /usr/local/bin/tracker-wrapper /usr/local/bin/tracker```

5. Run 
```tracker -h```