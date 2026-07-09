from datetime import datetime


class ExecutionTracer:

    def __init__(self):
        self.events = []


    def add(
        self,
        agent,
        status,
        message,
        metadata=None
    ):
        self.events.append(
            {
                "timestamp": datetime.utcnow().isoformat(),
                "agent": agent,
                "status": status,
                "message": message,
                "metadata": metadata or {},
            }
        )


    def export(self):
        return self.events