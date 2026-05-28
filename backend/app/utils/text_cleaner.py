import re

def clean_text(text):

    # replace newlines
    text = text.replace("\n", " ")

    # remove non-ascii characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    # remove phone numbers
    text = re.sub(r'\+?\d[\d\s-]{8,}', ' ', text)

    # remove emails
    text = re.sub(r'\S+@\S+', ' ', text)

    # remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # remove linkedin/github leftovers
    text = re.sub(r'github\.com/\S+', ' ', text)
    text = re.sub(r'linkedin\.com/\S+', ' ', text)

    # remove common icon leftovers
    text = re.sub(r'/github\w*', ' ', text)
    text = re.sub(r'/linkedin\w*', ' ', text)
    text = re.sub(r'/envel\w*', ' ', text)
    text = re.sub(r'ap-\s*arker-alt', ' ', text)

    # fix broken PDF hyphenated words
    text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)

    # add spaces between lowercase and uppercase words
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    # fix missing spaces after punctuation
    text = re.sub(r'([.,])([A-Za-z])', r'\1 \2', text)

    # remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()