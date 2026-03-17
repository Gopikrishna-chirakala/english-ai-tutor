import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    matches = tool.check(text)

    if not matches:
        return "✅ Your sentence looks correct!"

    corrections = []

    for match in matches:
        corrections.append(match.message)

    return corrections