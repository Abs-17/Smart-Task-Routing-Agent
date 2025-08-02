class HRTool:
    def run(self, query: str) -> str:
        return "📋 HR has received your query. We'll get back to you soon."

class ITTool:
    def run(self, query: str) -> str:
        return "💻 IT is investigating your technical issue."

class FinanceTool:
    def run(self, query: str) -> str:
        return "💰 Finance is reviewing your request. Expect a follow-up shortly."

tools = {
    "HR": HRTool(),
    "IT": ITTool(),
    "Finance": FinanceTool()
}
