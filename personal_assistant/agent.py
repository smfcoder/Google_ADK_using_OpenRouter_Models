from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    #model='gemini-3-flash-preview',
    model = LiteLlm(model = "openrouter/mistralai/devstral-2512:free"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)



#pip install google-adk
#pip install litellm
#adk web --port 8001