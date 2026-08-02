import os
import sys
from datetime import datetime

from dotenv import load_dotenv

from config import (
    MAX_ITERATIONS,
    AUTO_APPROVE
)

from tools import (
    research,
    save_note,
    send_email
)

load_dotenv()

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Log file
LOG_FILE = datetime.now().strftime("logs/%Y-%m-%d_%H-%M-%S.log")


def log(message):
    """Write messages to console and log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"

    print(entry)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry + "\n")


def ask_human(tool_name):
    """Approval gate."""

    if tool_name in AUTO_APPROVE:
        log(f"{tool_name} AUTO APPROVED")
        return True

    while True:
        choice = input(f"Approve '{tool_name}'? (y/n): ").strip().lower()

        if choice == "y":
            log(f"{tool_name} APPROVED")
            return True

        if choice == "n":
            log(f"{tool_name} REJECTED")
            return False

        print("Please enter y or n.")

def run_agent(task):
    """
    Simple Reason → Act → Observe loop.
    """

    iteration = 0
    notes = ""

    while iteration < MAX_ITERATIONS:

        iteration += 1
        log(f"Iteration {iteration}")

        # REASON
        if notes == "":
            log("Reason: Research the topic.")

            if ask_human("research"):
                notes = research(task)
                log("Research completed.")
            else:
                log("Research skipped.")
                return

            continue

        # ACT
        filename = task.replace(" ", "_").lower() + ".md"

        log("Reason: Save the notes.")

        if ask_human("save_note"):
            result = save_note(filename, notes)
            log(result)
        else:
            log("Save skipped.")
            return

        # OBSERVE
        log("Notes saved successfully.")

        log("Reason: Prepare email.")

        if ask_human("send_email"):

            result = send_email(
                "me@example.com",
                f"Summary of {task}",
                notes
            )

            log(result)

        else:
            log("Email skipped by user.")

        break

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('python agent.py "Research Artificial Intelligence"')
        return

    task = " ".join(sys.argv[1:]).strip()

    log("=" * 50)
    log("Personal Task Agent Started")
    log(f"Task: {task}")

    run_agent(task)

    log("Personal Task Agent Finished")
    log("=" * 50)


if __name__ == "__main__":
    main()
