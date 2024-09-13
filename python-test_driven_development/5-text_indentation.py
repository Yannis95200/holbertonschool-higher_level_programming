def text_indentation(text):
    """
    Formats a given text by adding two new lines after each occurrence
    of '.', '?', or ':' characters, and removes any leading or trailing
    whitespace from each line.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If the input `text` is not a string.

    Example:
        >>> text_indentation("Hello. How are you? Fine: thanks.")
        Hello.

        How are you?

        Fine:

        thanks.
    """
    if not isinstance(text, str):

        raise TypeError("text must be a string")

    text = text.strip()

    for char in ".?:":
        text = text.replace(char, char + "\n\n")


    result = []
    for line in text.split('\n'):
        result.append(line.strip())


    formatted_text = '\n'.join(result)
    print(formatted_text)
