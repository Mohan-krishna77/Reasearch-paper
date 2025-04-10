
from prompt_builder import build_prompt
import openai

openai.api_key = "your-api-key"

def generate_critique(sections):
    prompt = build_prompt(sections)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    output = response.choices[0].message.content

    return {
        "summaries": extract_part(output, "Summary"),
        "gaps": extract_part(output, "Research Gaps"),
        "suggestions": extract_part(output, "Suggestions")
    }

def extract_part(text, keyword):
    start = text.lower().find(keyword.lower())
    if start == -1:
        return "Not found."
    return text[start:]
