from main import *
import matplotlib.pyplot as plt
import time

x = [1000, 2500, 5000, 10000, 20000, 40000]
y1 = []
y2 = []

for i in range(6):
    run = EnhancedGreedyGatePacking()
    filename = 'tests/input' + str(i) + '.txt'
    fileout = 'output_greedy/output' + str(i)+'.txt'
    # Measure the time taken to solve each test case
    start = time.time()
    run.read_input(filename)
    run.greedy_multiple()
    run.send_to_file(fileout)  
    length = run.calculate_wire_length()
    end = time.time()
    
    # Append the time taken and wire length to the respective lists
    y1.append(end - start)
    y2.append(length)
    print(run.find_overlapping_gates())
    print(length)

# Plotting Time Taken vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y1,label="Time Taken")
plt.xlabel('Number of Wires')
plt.ylabel('Time Taken (s)')
plt.title('Time Taken vs Number of Wires')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/time_taken_vs_number_of_wires.png")  # Save the first graph
plt.close()

# Plotting Wire Length vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y2, label="Wire Length")
plt.xlabel('Number of Wires')
plt.ylabel('Wire Length')
plt.title('Wire Length vs Number of Wires')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/wire_length_vs_number_of_wires.png")  # Save the second graph
plt.close()
x = []
y1 = []
y2 = []
for i in range(2 , 12):
    x.append(2**i)
for i in range(6,16):
    run = EnhancedGreedyGatePacking()
    filename = 'tests/input' + str(i) + '.txt'
    fileout = 'output_greedy/output' + str(i)+'.txt'
    # Measure the time taken to solve each test case
    start = time.time()
    run.read_input(filename)
    run.greedy_multiple()
    run.send_to_file(fileout)  
    length = run.calculate_wire_length()
    end = time.time()
    
    # Append the time taken and wire length to the respective lists
    y1.append(end - start)
    y2.append(length)
    print(run.find_overlapping_gates())
    print(length)

# Plotting Time Taken vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y1,label="Time Taken")
plt.xlabel('Number of gates')
plt.ylabel('Time Taken (s)')
plt.title('Time Taken vs Number of gates')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/time_taken_vs_number_of_gates.png")  # Save the first graph
plt.close()

# Plotting Wire Length vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y2, label="Wire Length")
plt.xlabel('Number of gates')
plt.ylabel('Wire Length')
plt.title('Wire Length vs Number of gates')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/wire_length_vs_number_of_gates.png")  # Save the second graph
plt.close()

x = []
y1 = []
y2 = []
for i in range(1 , 11):
    x.append(i*10)
for i in range(16 , 26):
    run = EnhancedGreedyGatePacking()
    filename = 'tests/input' + str(i) + '.txt'
    fileout = 'output_greedy/output' + str(i)+'.txt'
    # Measure the time taken to solve each test case
    start = time.time()
    run.read_input(filename)
    run.greedy_multiple()
    run.send_to_file(fileout)  
    length = run.calculate_wire_length()
    end = time.time()
    
    # Append the time taken and wire length to the respective lists
    y1.append(end - start)
    y2.append(length)
    print(run.find_overlapping_gates())
    print(length)

# Plotting Time Taken vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y1,label="Time Taken")
plt.xlabel('Number of pins')
plt.ylabel('Time Taken (s)')
plt.title('Time Taken vs Number of pins')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/time_taken_vs_number_of_pins.png")  # Save the first graph
plt.close()

# Plotting Wire Length vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y2, label="Wire Length")
plt.xlabel('Number of pins')
plt.ylabel('Wire Length')
plt.title('Wire Length vs Number of pins')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/wire_length_vs_number_of_pins.png")  # Save the second graph
plt.close()
x = []
y1 = []
y2 = []
for i in range(2 , 10):
    x.append(10*i)
for i in range(26 , 34):
    run = EnhancedGreedyGatePacking()
    filename = 'tests/input' + str(i) + '.txt'
    fileout = 'output_greedy/output' + str(i)+'.txt'

    # Measure the time taken to solve each test case
    start = time.time()
    run.read_input(filename)
    run.greedy_multiple()
    run.send_to_file(fileout)  
    length = run.calculate_wire_length()
    end = time.time()
    
    # Append the time taken and wire length to the respective lists
    y1.append(end - start)
    y2.append(length)
    print(run.find_overlapping_gates())
    print(length)

# Plotting Time Taken vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y1,label="Time Taken")
plt.xlabel('avg size of gates')
plt.ylabel('Time Taken (s)')
plt.title('Time Taken vs avg size of gates')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/time_taken_vs_avg_size_of_gates.png")  # Save the first graph
plt.close()

# Plotting Wire Length vs. Number of Wires
plt.figure(figsize=(8, 6))
plt.plot(x, y2, label="Wire Length")
plt.xlabel('avg size of gates')
plt.ylabel('Wire Length')
plt.title('Wire Length vs avg size of gates')
plt.grid(True)
plt.legend()
plt.savefig("graphs_greedy/wire_length_vs_avg_size_of_gates.png")  # Save the second graph
plt.close()
for i in range(34 , 46):
    run = EnhancedGreedyGatePacking()
    filename = 'tests/input' + str(i) + '.txt'
    fileout = 'output_greedy/output' + str(i)+'.txt'
    # Measure the time taken to solve each test case
    start = time.time()
    run.read_input(filename)
    run.greedy_multiple()
    run.send_to_file(fileout)  
    length = run.calculate_wire_length()
    end = time.time()
    
    # Append the time taken and wire length to the respective lists

    
    print("Test case",i,":",length, end-start)