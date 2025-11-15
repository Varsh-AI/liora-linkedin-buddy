import json
import pandas as pd


class SampleRetriever:
    """Loads processed posts & retrieves few-shot examples based on filters."""

    def __init__(self, filepath="Data/processed_data.json"):
        self.dataframe = None
        self.tag_list = None
        self._load_posts(filepath)

    def _load_posts(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            posts = json.load(file)

        df = pd.json_normalize(posts)
        df["size_label"] = df["line_count"].apply(self._label_length)
        self.dataframe = df

        # Extract all tags
        combined_tags = df["tags"].apply(lambda t: t).sum()
        self.tag_list = sorted(set(combined_tags))

    def _label_length(self, line_count):
        if line_count < 5:
            return "Short"
        if 5 <= line_count <= 10:
            return "Medium"
        return "Long"

    def fetch_examples(self, size, language, tag):
        subset = self.dataframe[
            (self.dataframe["size_label"] == size)
            & (self.dataframe["language"] == language)
            & (self.dataframe["tags"].apply(lambda lst: tag in lst))
        ]
        return subset.to_dict(orient="records")

    def list_tags(self):
        return self.tag_list
