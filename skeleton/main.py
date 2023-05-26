from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    llm = OpenAI(temperature=0)
    tools = load_tools({{ params.tool_list }})
    memory = ConversationBufferMemory(memory_key="chat_history")
    agent = initialize_agent(tools, llm, agent="conversational-react-description", memory=memory, verbose=False)

    while True:
        user_input = input("Human: ")

        if user_input.lower() == "exit":
            print("Closing chat...")
            break

        response = agent.run(user_input)  # Sends user input to chatbot
        print("Chatbot: " + response)

if __name__ == "__main__":
    main()