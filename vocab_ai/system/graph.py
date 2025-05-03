from vocab_ai.structure.schema import State
from vocab_ai.agents.nodes import vocab_ai
from langgraph.graph import StateGraph, START, END

def vocab():
    # Build workflow
    builder = StateGraph(State)

    # Add the nodes
    builder.add_node("vocab_ai", vocab_ai)

    # Add edges to connect nodes
    builder.add_edge(START, "vocab_ai")
    builder.add_edge("vocab_ai", END)

    # Compile the workflow
    graph = builder.compile()

    return graph





