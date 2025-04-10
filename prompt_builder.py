
def build_prompt(sections):
    prompt = "Analyze the following research paper:\n\n"
    for sec, content in sections.items():
        prompt += f"\n\n## {sec.capitalize()}\n{content}\n"

    prompt += """
1. Summarize each section.
2. Identify any research gaps or areas lacking clarity.
3. Suggest improvements to enhance the research.
"""
    return prompt
