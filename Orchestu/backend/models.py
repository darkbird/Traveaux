import datetime

class Agent:
    def __init__(self, agent_id, name, description, status='active', config=None):
        self.agent_id = agent_id
        self.name = name
        self.description = description
        self.creation_date = datetime.datetime.utcnow().isoformat()
        self.status = status
        self.config = config if config is not None else {}

    def to_dict(self):
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "status": self.status,
            "config": self.config
        }

# Example usage (not part of the file, just for illustration):
# new_agent = Agent(agent_id="agent-001", name="Test Agent", description="An agent for testing.")
# print(new_agent.to_dict())
