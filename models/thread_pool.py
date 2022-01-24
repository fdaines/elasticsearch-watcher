from config import threadPoolConfig

class thread_pool_info:
    def __init__(self, nodeline):
        tokens = nodeline.split()
        self.node_name = tokens[0]
        self.thread_name = tokens[1]
        self.active = "-"
        self.queue = "-"
        self.rejected = "-"

        if len(tokens)>2:
            self.active = int(tokens[2])
        if len(tokens)>3:
            self.queue = int(tokens[3])
        if len(tokens)>4:
            self.rejected = int(tokens[4])

    def toDataTable(self):
        return [
          self.node_name,
          self.thread_name,
          str(self.active) if self.active <= threadPoolConfig["active_limit"] else "[bold magenta]"+str(self.active)+"[/]",
          str(self.queue) if self.queue <= threadPoolConfig["queue_limit"] else "[bold magenta]"+str(self.queue)+"[/]",
          str(self.rejected) if self.rejected <= threadPoolConfig["rejected_limit"] else "[bold magenta]"+str(self.rejected)+"[/]",
        ]
