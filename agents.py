from tools import tools

def route_query(query: str) -> str:
    query_lower = query.lower()

    if any(word in query_lower for word in ["salary", "leave", "promotion", "hr"]):
        print("Routed to: HR")
        return tools["HR"].run(query)

    elif any(word in query_lower for word in ["pc", "laptop", "restart", "freez", "hang", "crash", "it", "computer", "system"]):
        print("Routed to: IT")
        return tools["IT"].run(query)

    elif any(word in query_lower for word in ["reimbursement", "bonus", "expense", "finance"]):
        print("Routed to: Finance")
        return tools["Finance"].run(query)

    return "🤖 Sorry, I couldn't route this task to the correct department."

def agent(user_input: str) -> str:
    return route_query(user_input)
