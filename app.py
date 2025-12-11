import gradio as gr
from transformers import pipeline

#load the AI model
print("Loading model....please wait!")
sentiment_analyzer = pipeline("sentiment-analysis")

# 3. Define the logic function
def check_vibe(user_text):
    # Pass the text to the AI model
    raw_result = sentiment_analyzer(user_text)
    
    # Extract the data (The AI returns a list of dictionaries)
    label = raw_result[0]['label']
    score = raw_result[0]['score']
    
    # Return a friendly string
    return f"Result: {label} (Confidence: {score:.0%})"

# 4. Create the Web Interface
demo = gr.Interface(
    fn=check_vibe,
    inputs="text",
    outputs="text",
    title="The Vibe Check AI",
    description="Type a sentence and see if the AI thinks it is Positive or Negative."
)

# 5. Launch the app
demo.launch()
