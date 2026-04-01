import pywhatkit as pw

# The text you want to convert to handwriting
# Using triple quotes for multi-line strings (paragraphs)
txt = """Python is an interpreted high-level general-purpose programming language. 
Its design philosophy emphasizes code readability with its use of significant indentation. 
Its language constructs as well as its object-oriented approach aim to help programmers 
write clear, logical code for small and large-scale projects."""

# Function to convert text to handwriting
# Parameters: 
# 1. The text variable
# 2. Path/name of the output image file
# 3. RGB Color code (Optional: default is blue)
try:
    pw.text_to_handwriting(txt, "assignment.png", [0, 0, 138])
    print("Conversion Successful! Check your folder for assignment.png")
except Exception as e:
    print(f"An error occurred: {e}")