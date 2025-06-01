from agno.agent import Agent
from agno.models.google import Gemini
from text_to_speech import TextToSpeechToolkit
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key='Your gemini API key here'),
    tools=[TextToSpeechToolkit()],
    add_history_to_messages=True,
    show_tool_calls=True,
)
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "q"]:
        break
    agent.print_response(user_input)
