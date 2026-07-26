from openai import OpenAI
from course_catalog import courses

client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

system_prompt = """
You are an intelligent Course Recommendation Agent.

Your job is to:

1. Read the student's profile.
2. Study the course catalogue.
3. Recommend courses in correct order.
4. Follow prerequisites.
5. Explain why every course is recommended.
6. Output in numbered list.
"""

print("=" * 50)
print("COURSE RECOMMENDATION AGENT")
print("=" * 50)

while True:

    background = input("\nEnter Background: ")
    goal = input("Enter Career Goal: ")
    skills = input("Enter Current Skills: ")

    catalog = ""

    for course, details in courses.items():
        catalog += f"""
Course: {course}
Prerequisites: {details['prerequisites']}
Reason: {details['reason']}
"""

    user_prompt = f"""
Student Background:
{background}

Career Goal:
{goal}

Current Skills:
{skills}

Available Courses:

{catalog}

Recommend a personalized learning path.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    print("\n")
    print("Recommended Learning Path")
    print("-" * 50)
    print(response.choices[0].message.content)
    print("-" * 50)