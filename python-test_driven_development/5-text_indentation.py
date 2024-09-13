#!/usr/bin/python3
"""
    Prints a text with 2 new lines after each of these characters:
    '.', '?', ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?', ':'.
    Args:
        text (str): The text to format.
    Raises:
        TypeError: If the text is not a string.
    Example:
        text_indentation("Hello. How are you? Fine: Great!")
    Output:
        Hello.
        How are you?
        Fine:
        Great!
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(result, end="")
