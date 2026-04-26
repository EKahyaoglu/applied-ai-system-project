# Simple retrieval module for RAG
import os
from typing import List

class Retriever:
    def __init__(self, data_folder: str = "assets"):
        self.data_folder = data_folder

    def retrieve(self, query: str, top_k: int = 3) -> List[str]:
        """Search all .txt files in the data folder for relevant lines."""
        results = []
        for fname in os.listdir(self.data_folder):
            if fname.endswith(".txt"):
                with open(os.path.join(self.data_folder, fname), encoding="utf-8") as f:
                    for line in f:
                        if query.lower() in line.lower():
                            results.append(line.strip())
        return results[:top_k]
