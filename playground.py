from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()


phi.api_key = os.getenv("PHI_API_KEY")

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

app = Playground(agents=[web_serch_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)