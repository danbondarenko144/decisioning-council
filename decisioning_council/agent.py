from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import AgentTool, FunctionTool, google_search
from google.genai import types
from .sub_agents.green_councillor import green_councillor
from .sub_agents.blue_councillor import blue_councillor
from .sub_agents.yellow_councillor import yellow_councillor
from .sub_agents.red_councillor import red_councillor
from .sub_agents.arbiter import arbiter


retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

parallel_council= ParallelAgent(
    name="ParallelCouncil",
    description='Allows all council members to work in parallel',
    sub_agents=[green_councillor, 
                blue_councillor, 
                yellow_councillor, 
                red_councillor],
)


decisioning_orchestrator = SequentialAgent(
    name='DecisioningOrchestrator',
    description='Orchestrates the decision-making process',
    sub_agents=[
        parallel_council,
        arbiter
    ]
)

council_proxy = Agent(
    name='CouncilProxy',
    model=Gemini(model='gemini-2.5-flash',retry_options=retry_config),
    description='Orchestrates the decision-making process',
    instruction="""
        Your sole job is to get the user query and to use the decisioning_orchestrator Tool if the user needs help to decide between several courses of action.

        If a user asks you what you can do, you tell them that you can help them decide on a course of action and that you are backed by a council of experts
        that will decide on the best course of action from the options that they provide. 
        Tell them they must provide several courses of action (decisions) with context for each of them.
        Do not answer any other queries from the user. 
        If the user asks you for other queries, tell them you cannot help them with that, repeat the above, 
        and if possible suggest a way to repharese their query so you can answer it.

        Some example queries you should answer:
        -"I am going to a fancy party, should I wear a green, yellow, or white dress?"
        -"I am trying to lose weight, should I eat a pizza or a cheesburger for dinner?"
        These are simple examples. You should be able to help answer much more complicated queries as well with much more options.

        If the user asks yes or no questions, you should answer them as well (here there are two courses of action 1.Yes 2.No). Some examples:
        -"Is oatmeal good for you?"
        -"Is it good to exercise 3 times per week?"

        ONLY pass the user query to the decisioning_orchestrator Tool only if you identified that the user needs help with a decision 
        AND the user has provided at least TWO possible courses of actions. I.e. do not call the decisioning_orchestrator Tool if the user asks open ended questions like:
        -"What should I eat for breakfast this morning"?
        -"What is the best brand of sport's watch"?
        In this case repeat what you can do.

        The decisioning_orchestrator tool will return a preferred course of action based on a ranking done by 4 councillors: red, blue, green, and yellow.
        Each councillor has a distinct personality and looks at the situation from a different angle.
        There is also an arbiter that looks at the rankings and makes sure it is ethical as well as breaking ties before returning the final result.

        Your goal is to summarize in one paragraph what the arbiter decided to the user.
    """,
    tools=[AgentTool(decisioning_orchestrator)],
)

root_agent = council_proxy
