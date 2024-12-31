from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Creating the Web Search Agent
web_serch_agent = Agent(
        name = "Web Search Agent",
        role = "Search the web for information",
        model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
        tools = [DuckDuckGo()],  
        instructions = ["Always include the sources"],
        show_tool_calls = True,
        markdown = True
)

# Creating the Financial Agent
finance_agent = Agent(
    name = "Finance_AI_Agent",
    model = Groq(id = "llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
             company_news=True)],
    instructions = ["Use Tables to display the data"],
    show_tool_calls= True,
    markdown= True
)

# When we combine the above different agents, then it will be a MultiModel Agents
multi_model_agent = Agent(
            team = [web_serch_agent, finance_agent],
            instructions= ["Always include sources", "Use table to display the data"],
            show_tool_calls= True,
            markdown= True
)


input_text = ""
# Initiating the agent
while input_text != "-1":
    input_text = input("Ask any question regarding the Stock Market: ")
    multi_model_agent.print_response(f"{input_text}", stream=True)