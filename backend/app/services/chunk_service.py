from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text, chunk_size=600):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=50
)
    chunks = text_splitter.split_text(text)
    return chunks