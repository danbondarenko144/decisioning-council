from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from . import prompt

green_councillor = Agent(
    model='gemini-2.5-pro',
    name='GreenCouncillor',
    description='Decides which action to vote for based on personality and context',
    instruction=prompt.GREEN_COUNCILLOR_PROMPT,
    tools=[google_search],
    output_key='green_output',
)
