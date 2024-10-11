import random

random.seed(42)
def generate_test(filename="input.txt", num_gates=1000, max_pins_per_gate=40, max_coord=100, max_wire=100000):
    gates = {}
    pin_used_as_receiver = set()  # Track pins that have been used as receiver
    used_connections = set()  # Track already used connections to prevent reverse connections

    with open(filename, 'w') as f:
        total_pins = 0  # Track total pins to limit wires

        for gate in range(1, num_gates + 1):
            width = random.randint(2, max_coord)
            height = random.randint(2, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            pins = []
            num_pins = min(random.randint(2, max_pins_per_gate), (height + 1) * 2)
            total_pins += num_pins
            
            # Generate pins randomly on edges
            while len(pins) < num_pins:
                edge = random.choice(["left", "right"])
                y = random.randint(0, height)
                x = 0 if edge == "left" else width
                if (x, y) not in pins:
                    pins.append((x, y))
            
            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        all_gates = list(gates.keys())
        max_wires_possible = total_pins -1
        num_wires = min(max_wire, max_wires_possible)

        # Create connections with reverse connection prevention
        for gate1 in all_gates:
            if len(used_connections) >= num_wires:
                break

            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]

            if available_pins_gate2:
                pin2 = random.choice(available_pins_gate2)
                connection = (gate1, pin1, gate2, pin2)
                reverse_connection = (gate2, pin2, gate1, pin1)

                if connection not in used_connections and reverse_connection not in used_connections:
                    pin_used_as_receiver.add((gate2, pin2))
                    f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                    used_connections.add(connection)

        # Additional connections
        for _ in range(num_wires - len(used_connections)):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]
                    if available_pins_gate2:
                        pin2 = random.choice(available_pins_gate2)
                        connection = (gate1, pin1, gate2, pin2)
                        reverse_connection = (gate2, pin2, gate1, pin1)

                        if connection not in used_connections and reverse_connection not in used_connections:
                            pin_used_as_receiver.add((gate2, pin2))
                            f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                            used_connections.add(connection)
                            break

# Function 2: generate_test2 with a range of dimensions for gates
def generate_test2(filename="input.txt", num_gates=1000, min_coord=2, max_coord=100, max_pins_per_gate=40, max_wire=100000):
    gates = {}
    pin_used_as_receiver = set()
    used_connections = set()

    with open(filename, 'w') as f:
        total_pins = 0

        for gate in range(1, num_gates + 1):
            width = random.randint(min_coord, max_coord)
            height = random.randint(min_coord, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            pins = []
            num_pins = min(random.randint(2, max_pins_per_gate), (height + 1) * 2)
            total_pins += num_pins

            while len(pins) < num_pins:
                edge = random.choice(["left", "right"])
                y = random.randint(0, height)
                x = 0 if edge == "left" else width
                if (x, y) not in pins:
                    pins.append((x, y))

            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        all_gates = list(gates.keys())
        max_wires_possible = total_pins -1
        num_wires = min(max_wire, max_wires_possible)

        for gate1 in all_gates:
            if len(used_connections) >= num_wires:
                break

            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]

            if available_pins_gate2:
                pin2 = random.choice(available_pins_gate2)
                connection = (gate1, pin1, gate2, pin2)
                reverse_connection = (gate2, pin2, gate1, pin1)

                if connection not in used_connections and reverse_connection not in used_connections:
                    pin_used_as_receiver.add((gate2, pin2))
                    f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                    used_connections.add(connection)

        for _ in range(num_wires - len(used_connections)):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]
                    if available_pins_gate2:
                        pin2 = random.choice(available_pins_gate2)
                        connection = (gate1, pin1, gate2, pin2)
                        reverse_connection = (gate2, pin2, gate1, pin1)

                        if connection not in used_connections and reverse_connection not in used_connections:
                            pin_used_as_receiver.add((gate2, pin2))
                            f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                            used_connections.add(connection)
                            break

# Function 3: generate_test3 with exactly the specified number of pins
def generate_test3(filename="input.txt", num_gates=1000, num_pins_per_gate=40, max_coord=100, max_wire=100000):
    gates = {}
    pin_used_as_receiver = set()
    used_connections = set()

    with open(filename, 'w') as f:
        total_pins = 0

        for gate in range(1, num_gates + 1):
            width = random.randint(2, max_coord)
            height = random.randint(2, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            pins = []
            num_pins = min(num_pins_per_gate, (height + 1) * 2)
            total_pins += num_pins

            while len(pins) < num_pins:
                edge = random.choice(["left", "right"])
                y = random.randint(0, height)
                x = 0 if edge == "left" else width
                if (x, y) not in pins:
                    pins.append((x, y))

            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        all_gates = list(gates.keys())
        max_wires_possible = total_pins -1
        num_wires = min(max_wire, max_wires_possible)

        for gate1 in all_gates:
            if len(used_connections) >= num_wires:
                break

            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]

            if available_pins_gate2:
                pin2 = random.choice(available_pins_gate2)
                connection = (gate1, pin1, gate2, pin2)
                reverse_connection = (gate2, pin2, gate1, pin1)

                if connection not in used_connections and reverse_connection not in used_connections:
                    pin_used_as_receiver.add((gate2, pin2))
                    f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                    used_connections.add(connection)

        for _ in range(num_wires - len(used_connections)):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]
                    if available_pins_gate2:
                        pin2 = random.choice(available_pins_gate2)
                        connection = (gate1, pin1, gate2, pin2)
                        reverse_connection = (gate2, pin2, gate1, pin1)

                        if connection not in used_connections and reverse_connection not in used_connections:
                            pin_used_as_receiver.add((gate2, pin2))
                            f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                            used_connections.add(connection)
                            break



# Function 4: generate_test4 with pins evenly spread across left and right sides
def generate_test4(filename="input.txt", num_gates=1000, min_coord=2, max_coord=100, num_pins_per_gate=40, max_wire=100000):
    gates = {}
    pin_used_as_receiver = set()
    used_connections = set()

    with open(filename, 'w') as f:
        total_pins = 0

        for gate in range(1, num_gates + 1):
            width = random.randint(min_coord, max_coord)
            height = random.randint(min_coord, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            pins = []
            num_pins = min(num_pins_per_gate, (height + 1) * 2)
            total_pins += num_pins

            while len(pins) < num_pins:
                edge = random.choice(["left", "right"])
                y = random.randint(0, height)
                x = 0 if edge == "left" else width
                if (x, y) not in pins:
                    pins.append((x, y))

            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        all_gates = list(gates.keys())
        max_wires_possible = total_pins -1
        num_wires = min(max_wire, max_wires_possible)

        for gate1 in all_gates:
            if len(used_connections) >= num_wires:
                break

            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]

            if available_pins_gate2:
                pin2 = random.choice(available_pins_gate2)
                connection = (gate1, pin1, gate2, pin2)
                reverse_connection = (gate2, pin2, gate1, pin1)

                if connection not in used_connections and reverse_connection not in used_connections:
                    pin_used_as_receiver.add((gate2, pin2))
                    f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                    used_connections.add(connection)

        for _ in range(num_wires - len(used_connections)):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    available_pins_gate2 = [i for i in range(1, gates[gate2] + 1) if (gate2, i) not in pin_used_as_receiver]
                    if available_pins_gate2:
                        pin2 = random.choice(available_pins_gate2)
                        connection = (gate1, pin1, gate2, pin2)
                        reverse_connection = (gate2, pin2, gate1, pin1)

                        if connection not in used_connections and reverse_connection not in used_connections:
                            pin_used_as_receiver.add((gate2, pin2))
                            f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                            used_connections.add(connection)
                            break

# every test case has at least n wires where n is number of gates
generate_test('tests/input0.txt' , 1000 , 80 , 100 , 1000)
generate_test('tests/input1.txt' , 1000 , 80 , 100 , 2500)
generate_test('tests/input2.txt' , 1000 , 80 , 100 , 5000)
generate_test('tests/input3.txt' , 1000 , 80 , 100 , 10000)
generate_test('tests/input4.txt' , 1000 , 80 , 100 , 20000)
generate_test('tests/input5.txt' , 1000 , 80 , 100 , 40000)
for i in range(6 , 16):
    filename = 'tests/input'+str(i)+'.txt'
    generate_test(filename , 2**(i-4) , 40 , 100 , 20*2**(i-4))

for i in range(16 , 26):
    filename = 'tests/input'+str(i)+'.txt'
    generate_test2(filename , 1000 ,50,100, 10*(i-15)  , 5000*(i-15))

for i in range(26 , 34):
    filename = 'tests/input'+str(i)+'.txt'
    generate_test2(filename , 1000 , 10*(i-25) , 10*(i-23) , 40,20000  )

generate_test3("tests/input34.txt" , 1000, 40 , 100 , 80000)
generate_test3("tests/input35.txt" , 1000, 10 , 100 , 20000)

generate_test3("tests/input36.txt" , 1000, 30 , 10 , 40000)
generate_test4("tests/input37.txt" , 1000, 80, 100 ,40, 80000)
generate_test4("tests/input38.txt" , 1000, 80, 100 ,100, 200000)#out of pin constraints

generate_test4("tests/input39.txt" , 100, 80, 100 ,200, 40000)
generate_test4("tests/input40.txt" , 100, 60, 80 ,200, 32000)
generate_test4("tests/input41.txt" , 100, 40, 60 ,200, 24000)
generate_test4("tests/input42.txt" , 100, 20, 40 ,200, 16000)
generate_test4("tests/input43.txt" , 100, 1, 20 ,200, 8000)

generate_test("tests/input44.txt", 1000 , 40 , 10 , 20000)
generate_test("tests/input45.txt", 1000 , 10 , 10 , 5000)