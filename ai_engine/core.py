from flask import Blueprint, request, jsonify
from ai_engine.chains.schedule import schedule_chain
from ai_engine.chains.email import email_chain
from ai_engine.chains.goals import goals_chain
from ai_engine.chains.budget import budget_chain

# Import LangChain/LangGraph components for agentic orchestration
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

# Define tools for the agent
schedule_tool = Tool(
    name="Schedule Builder",
    func=schedule_chain,
    description="Build or update a daily schedule."
)
email_tool = Tool(
    name="Email Assistant",
    func=email_chain,
    description="Draft or send emails."
)
goals_tool = Tool(
    name="Goal Tracker",
    func=goals_chain,
    description="Track or update goals."
)
budget_tool = Tool(
    name="Budget Builder",
    func=budget_chain,
    description="Create or update a budget."
)

tools = [schedule_tool, email_tool, goals_tool, budget_tool]

# Initialize the agent with LangChain (using OpenAI as an example LLM)
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

gigi_router = Blueprint("gigi", __name__)


@gigi_router.route("/schedule", methods=["POST"])
def build_schedule():
    data = request.json
    result = schedule_chain(data)
    return jsonify(result)


@gigi_router.route("/email", methods=["POST"])
def write_email():
    data = request.json
    result = email_chain(data)
    return jsonify(result)


@gigi_router.route("/goals", methods=["POST"])
def track_goals():
    data = request.json
    result = goals_chain(data)
    return jsonify(result)


@gigi_router.route("/budget", methods=["POST"])
def build_budget():
    data = request.json
    result = budget_chain(data)
    return jsonify(result)


@gigi_router.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    # The agent will decide which tool(s) to call based on the chat message
    response = agent.run(user_message)
    return jsonify({"response": response})
