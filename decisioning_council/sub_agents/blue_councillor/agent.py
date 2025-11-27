from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from . import prompt

blue_councillor = Agent(
    model='gemini-2.5-pro',
    name='BlueCouncillor',
    description='Decides which action to vote for based on personality and context',
    instruction=prompt.BLUE_COUNCILLOR_PROMPT,
    tools=[google_search],
    output_key='blue_output',
)
