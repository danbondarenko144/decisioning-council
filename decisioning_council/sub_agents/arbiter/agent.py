from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from . import prompt

arbiter = Agent(
    model='gemini-2.5-pro',
    name='Arbiter',
    description='Decides on which action to take based on input from council agents',
    instruction=prompt.ARBITER_PROMPT,
    output_key='arbiter_output',
)
