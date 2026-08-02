import os
from groq import Groq
from dotenv import load_dotenv
from config import MODEL

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def research(topic):
    """
    Research a topic using the AI model and return structured notes.
    """

    prompt = f"""
    Create clear study notes on the following topic:

    {topic}

    Include:
    - Introduction
    - Key Points
    - Important Facts
    - Conclusion

    Keep the notes simple and well organized.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def save_note(filename, content):
    """
    Save the generated notes into the notes folder.
    """

    os.makedirs("notes", exist_ok=True)

    filepath = os.path.join("notes", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return f"Notes saved successfully to {filepath}"

def send_email(to, subject, body):
    """
    Simulate sending an email.
    """

    print("\n========== EMAIL ==========")
    print(f"To      : {to}")
    print(f"Subject : {subject}")
    print("\nBody:\n")
    print(body)
    print("===========================\n")

    return f"Email prepared for {to} (dry run)."

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "research",
            "description": "Research a topic and generate structured notes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic to research"
                    }
                },
                "required": ["topic"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_note",
            "description": "Save notes to a markdown file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": ["filename", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email summary to a recipient.",
            "parameters": {
                "type": "object",
                "properties": {
                    "to": {
                        "type": "string"
                    },
                    "subject": {
                        "type": "string"
                    },
                    "body": {
                        "type": "string"
                    }
                },
                "required": ["to", "subject", "body"]
            }
        }
    }
]