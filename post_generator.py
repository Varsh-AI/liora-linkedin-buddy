from llm_client import llm
from fewshot import SampleRetriever

# Initialize retriever
retriever = SampleRetriever()


def _format_length(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    return "5 to 10 lines"


def build_prompt(length, language, tag):
    length_text = _format_length(length)

    prompt = f"""
Generate a LinkedIn post with these conditions:

1. Topic: {tag}
2. Length: {length_text}
3. Language: {language}
   - Hinglish = mix of Hindi + English
   - Always use English alphabet
"""

    # Fetch few-shot examples
    examples = retriever.fetch_examples(length, language, tag)

    if len(examples) > 0:
        prompt += "\n4. Follow the tone of these examples:\n"

    for i, item in enumerate(examples[:2]):
        text = item.get("cleaned_text", item.get("text", ""))
        prompt += f"\nExample {i+1}:\n{text}\n"

    prompt += "\nNow generate the final post:\n"

    return prompt


def generate_post(length, language, tag):
    prompt = build_prompt(length, language, tag)

    # Use .invoke() → this works for ChatModel
    response = llm.invoke(prompt)

    # response.content = final text output
    return response.content.strip()
