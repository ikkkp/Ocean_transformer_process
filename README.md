# Ocean Toolkit for Document Processing

## Introduction

The Ocean Toolkit is a powerful tool designed for processing PDF documents. It leverages the Xenova/nougat-base model from Transformers to generate summaries of PDF documents based on a specified token length. Additionally, it supports sentence segmentation for both Chinese and English text and efficiently converts summary text data into high-quality vector data. The toolkit seamlessly integrates with the Qdrant vector database, facilitating vector storage and retrieval, ultimately contributing to the construction of a knowledge graph.

## Key Features

- PDF Document Summarization: Utilize the Xenova/nougat-base model to generate document summaries with a specified token length.
- Sentence Segmentation: Support sentence segmentation for both Chinese and English text to enhance text processing accuracy.
- Vector Data Generation: Quickly generate high-quality vector data based on summary text data.
- Vector Database Operations: Leverage the Qdrant vector database for efficient vector storage and retrieval, enabling fast searches and knowledge graph construction.

## Installation

```bash
pip install ocean-toolkit
```

## Usage Example

```python
from ocean_toolkit import OceanToolkit

# Initialize the Ocean Toolkit
ocean_toolkit = OceanToolkit()

# Read a PDF document
pdf_path = "example.pdf"
pdf_content = ocean_toolkit.read_pdf(pdf_path)

# Generate a document summary
summary = ocean_toolkit.generate_summary(pdf_content, max_token_length=200)

# Split the text into sentences
sentences = ocean_toolkit.split_sentences(summary)

# Generate vectors from the text
vectors = ocean_toolkit.generate_vectors(sentences)

# Save vectors to the Qdrant database
ocean_toolkit.save_to_qdrant(vectors, document_ids=range(len(sentences)))

# Search vectors in the Qdrant database
query_vector = ocean_toolkit.generate_vectors(["query sentence"])[0]
result = ocean_toolkit.search_in_qdrant(query_vector)
```

## Contribution

Contributions, questions, and improvement suggestions are welcome. Please refer to the [Contribution Guidelines](CONTRIBUTING.md) for more information.

## License

This toolkit is released under the [MIT License](LICENSE).
