from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text, chunk_size=400):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=60
    )
    chunks = text_splitter.split_text(text)
    return chunks