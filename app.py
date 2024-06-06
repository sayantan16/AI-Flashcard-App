# app.py
import os
from openai import OpenAI
from flask import Flask, render_template, request, jsonify
from data import flashcards

app = Flask(__name__)

# Set your OpenAI API key here
client = OpenAI(
    # This is the default and can be omitted
    api_key=''
)

@app.route('/')
def index():
    topics = flashcards.keys()
    return render_template('index.html', topics=topics)

@app.route('/flashcards/<topic>')
def flashcards_view(topic):
    if topic in flashcards:
        return render_template('flashcards.html', topic=topic, cards=flashcards[topic])
    else:
        return "Topic not found", 404

@app.route('/get_detailed_answer', methods=['POST'])
def get_detailed_answer():
    data = request.json
    question = data.get('question')
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": "give detailed answer to help me understand a interview question properly using easy to understand explanation and also give an answer that I should give to the interviewer."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=1,
        max_tokens=1104,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    detailed_answer = response.choices[0].message.content
    return jsonify({'detailed_answer': detailed_answer})

if __name__ == '__main__':
    app.run(port=8080, debug=True)
