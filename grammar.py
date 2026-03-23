import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    if len(text.split()) < 30:
        return "Please enter at least 30 words."
    
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    
    return corrected_text