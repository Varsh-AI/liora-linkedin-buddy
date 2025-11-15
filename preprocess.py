import json
from llm_client import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


def process_posts(raw_file, output_file):
    with open(raw_file, "r", encoding="utf-8") as f:
        raw_posts = json.load(f)

    enriched = []

    # Extract metadata for each post
    for post in raw_posts:
        details = extract_metadata(post["text"])
        enriched.append(post | details)

    # Standardize tags
    mapping = unify_all_tags(enriched)
    for entry in enriched:
        entry["tags"] = [mapping[tag] for tag in entry["tags"]]

    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(enriched, out, indent=4)


def extract_metadata(post_text):
    template = """
Analyze the LinkedIn post and extract:

- line_count: number of lines  
- language: English or Hinglish  
- tags: up to two relevant topic labels  

Return ONLY a valid JSON in this format:
{
  "line_count": <number>,
  "language": "<English/Hinglish>",
  "tags": ["Tag1", "Tag2"]
}

Post:
{post}
"""
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke({"post": post_text})

    try:
        return JsonOutputParser().parse(response.content)
    except Exception:
        raise OutputParserException("Error parsing metadata JSON.")


def unify_all_tags(enriched_posts):
    unique = set()
    for post in enriched_posts:
        unique.update(post["tags"])

    tag_list = ",".join(unique)

    template = """
You will unify the given tags into a consistent mapping.

Rules:
- Merge related/similar tags
- Use Title Case
- Output ONLY JSON:
  {"OldTag": "Unified Tag", ...}

Tags:
{tags}
"""
    chain = PromptTemplate.from_template(template) | llm
    response = chain.invoke({"tags": tag_list})

    return JsonOutputParser().parse(response.content)


if __name__ == "__main__":
    process_posts("data/raw_posts.json", "data/processed_posts.json")
