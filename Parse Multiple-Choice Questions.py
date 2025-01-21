def parse_multiple_choice(text):
    lines = text.splitlines()
    question = lines[0]  # Assume the first line is the question
    options = []
    for line in lines[1:]:
        if line.strip().startswith(("A)", "B)", "C)", "D)")):  # Detect options
            options.append(line.strip())
    return question, options

# Test the function
question, options = parse_multiple_choice(next)
print("Question:", question)
print("Options:", options)