```py
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        p = self.queue[0]
        self.queue = self.queue[1:]
        return p
    

    def peek(self) -> int:
        """
        Get the front element.
        """
        p = self.queue[0]
        return p

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue) > 0:
            a = False
        else:
            a = True
        return a
        ```
