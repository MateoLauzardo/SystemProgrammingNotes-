
# Round-Robin CPU Scheduler (Queues + Simulation)

from collections import deque

# this class tracks how much time is still needs / remainign
class Process():
    def __init__(self, name, burst_time):
        self.name = name 
        
        self.remaining_time = burst_time
        
    
class Scheduler():
    
    def __init__(self, time_slice):
        self.time_slice = time_slice
        
        self.ready_queue = deque() # filled with process objects 
        self.finished = [] 
        self.total = 0 
    
    
    def add_process(self, name, burst_time):
        
        new_process = Process(name, burst_time) 
        self.ready_queue.append(new_process)
    
    
    # NOTE: the main feature 
    def run(self):
        
        # a list of every time a name is ran, to show the order
        turns = []

        # while there values in que 
        while self.ready_queue:
            
            # removes first value 
            process = self.ready_queue.popleft()

            # grabs the lowest value 
            run_time = min(self.time_slice, process.remaining_time)

            # add name to the turns 
            turns.append(process.name)
            
            # add the lowest value to run time 
            self.total += run_time
            
            # update remainig time 
            process.remaining_time -= run_time
            
            # checks if time is done / if so add to finish
            if process.remaining_time == 0:
                self.finished.append(process.name)
            else:
                self.ready_queue.append(process)

        # returns a list of names 
        return turns
             
    
    
    # returns the names of processes in the order they finished.
    def finished_order(self):
        return self.finished
    
    
    # returns how many time units passed in total.
    def total_time(self):
        return self.total 




s = Scheduler(time_slice=2)
s.add_process("A", 5)
s.add_process("B", 2)
s.add_process("C", 3)
print(s.run())
print(s.finished_order())
print(s.total_time())

# output: 
# ['A', 'B', 'C', 'A', 'C', 'A']
# ['B', 'C', 'A']
# 10