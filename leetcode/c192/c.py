class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [homepage]
        self.history_ptr = 0
        

    def visit(self, url: str) -> None:
        self.history_ptr += 1
        self.history = self.history[:self.history_ptr]
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.history_ptr = max(0, self.history_ptr - steps)
        return self.history[self.history_ptr]
        

    def forward(self, steps: int) -> str:
        self.history_ptr = min(len(self.history)-1, self.history_ptr + steps)
        return self.history[self.history_ptr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)