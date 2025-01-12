# Financial Agent and Web Search Multi-Model AI System

This project implements a multi-model AI system that combines two specialized agents: a Web Search Agent for retrieving real-time information from the internet and a Financial Analysis Agent for analyzing stock market data. These agents are powered by Groq models and leverage tools like DuckDuckGo and YFinanceTools to provide accurate, structured responses.

---

## Features

### Web Search Agent:
- Uses DuckDuckGo for retrieving up-to-date web information.
- Includes sources for all retrieved data.
- Responds in markdown format for easy readability.

### Financial Analysis Agent:
- Fetches stock prices, analyst recommendations, financial fundamentals, and news using YFinanceTools.
- Displays data in well-structured tables.
- Enables users to analyze market trends effectively.

### Multi-Model Agent:
- Combines the functionalities of the Web Search Agent and Financial Analysis Agent.
- Processes complex queries requiring both web search and financial analytics.
- Provides detailed and actionable insights with clarity.

---

## Financial_Agent Code Explanation

### Setup and Dependencies:
- The project uses the `phi` library to define and manage agents.
- `dotenv` is used to securely load API keys for GROQ and OpenAI from environment variables.

### Agents:
1. **Web Search Agent**:
   - Uses DuckDuckGo to search the web for information.
   - Includes detailed instructions to always provide sources in responses.
2. **Financial Analysis Agent**:
   - Uses YFinanceTools for stock-related queries.
   - Retrieves stock prices, financial fundamentals, analyst recommendations, and company news.
   - Displays the results in tables for clarity.
3. **Multi-Model Agent**:
   - Combines the capabilities of both agents.
   - Coordinates tasks depending on the user's query.

### How It Works:
![image](https://github.com/user-attachments/assets/b1f7d2e3-d3cd-43ba-abd0-32d9cbed8a96)

- The script takes input from the user in a loop, allowing for multiple queries in one session.
- The Multi-Model Agent determines whether the query relates to web search, financial analysis, or both, and uses the appropriate tools and models to generate a response.
- Results are streamed and printed in markdown format for better readability.

![image](https://github.com/user-attachments/assets/4c2f5517-88ae-42da-aff1-1418f759ac31)


---

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.11 or later.**

2. **Necessary libraries installed.** You can install them using:
   ```bash
   pip install phi openai python-dotenv
   ```
3. **Set Up API Keys**
     - Before running the script, set up API keys for **Groq** and **OpenAI** as follows:
         - Create a .env file in the project directory with the following structure:
           ```bash
           OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
           GROQ_API_KEY=<YOUR_GROQ_API_KEY>
           PHI_API_KEY=<YOUR_PHI_API_KEY>
           ```
         - Open your terminal and run these commands:
           ```bash
           setx GROQ_API_KEY <YOUR_GROQ_API_KEY>
           setx OPENAI_API_KEY <YOUR_OPENAI_API_KEY>
           ```

## How to Run
1. Clone the repository and navigate to the project directory.
2. Ensure the API keys are set (as described above).
3. Run the script:
    ```bash
    python financial_agent.py
    ```
4. Enter your queries related to stock market analysis or web search. To exit the program, type -1.

----------------------------------------------------------------------------------------------------------------------------

## Phidata Playground and Application Setup
### 1. **Playground Integration**
- Introduced the **Playground** from the `phi.playground` module.
- The playground provides an interactive web-based interface for testing and querying the agents.
- Allows seamless collaboration between the Web Search Agent and Financial Analysis Agent.

### 2. **Application Serving**
- The application is served using the `serve_playground_app` function.
- It enables hot-reloading (`reload=True`) for easier development and testing of agent interactions.
- The app is accessible through a local server, offering a user-friendly way to interact with the agents.

### How to Run:
1. Run the below command:
   ```bash
   python playground.py
   ```
2. Once the execution is done, we see that the playground is hosted in the local server
![image](https://github.com/user-attachments/assets/37b9935b-f026-4c7d-a1be-dba1cb25e0e1)

Clicking on the server won't directly work.
3. We need to go to the Phidata -> Playground -> select the LocalHost End Point
     ![image](https://github.com/user-attachments/assets/5f89f58f-5a53-4db6-86aa-afb5eab58f31)

  This creates a new chat window with the selected LLM model and we also have the options to select different agents as per our need
  ![image](https://github.com/user-attachments/assets/448db917-ea5b-4001-8053-0d949cb608ef)
  ![image](https://github.com/user-attachments/assets/42a7de3c-f9b6-4b44-a859-7028039045c3)


