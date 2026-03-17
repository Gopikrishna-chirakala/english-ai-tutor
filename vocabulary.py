dictionary = {
    "curious": "Curious means eager to learn or know something.",
    "ambitious": "Ambitious means having a strong desire to succeed.",
    "confident": "Confident means feeling sure about your abilities.",
    "improve": "Improve means to make something better.",
    "practice": "Practice means doing something repeatedly to get better."
}

def get_meaning(word):
    return dictionary.get(word.lower(), "Word not found in dictionary.")