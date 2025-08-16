from llama_index.core import VectorStoreIndex, Document
from pathlib import Path
import pandas as pd
import docx2txt
import pdfplumber


def load_index_from_docs(doc_path="docs"):
    documents = []

    # Supported extensions
    valid_extensions = [".txt", ".docx", ".pdf", ".csv", ".xlsx"]

    for file_path in Path(doc_path).rglob("*"):
        if file_path.suffix.lower() not in valid_extensions:
            continue

        try:
            if file_path.suffix == ".txt":
                text = file_path.read_text()
            elif file_path.suffix == ".docx":
                text = docx2txt.process(file_path)
            elif file_path.suffix == ".pdf":
                with pdfplumber.open(file_path) as pdf:
                    text = "\n".join(page.extract_text() or '' for page in pdf.pages)
            elif file_path.suffix in [".csv", ".xlsx"]:
                df = pd.read_csv(file_path) if file_path.suffix == ".csv" else pd.read_excel(file_path)
                text = df.to_string(index=False)
            else:
                continue

            documents.append(Document(text=text, metadata={"file_name": str(file_path.name)}))

        except Exception as e:
            print(f"❌ Failed to load {file_path.name}: {e}")

    print(f"\n📚 Loaded {len(documents)} document(s) from `{doc_path}`\n")
    for i, doc in enumerate(documents):
        print(f" - {i+1}: {doc.metadata['file_name']} preview:\n{doc.text[:150]}...\n")

    index = VectorStoreIndex.from_documents(documents)
    return index
