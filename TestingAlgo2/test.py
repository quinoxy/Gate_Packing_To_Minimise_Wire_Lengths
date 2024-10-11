import random

# Function 1 (original generate_test) with fixed dimensions and random number of pins
def generate_test(filename="input.txt", num_gates=1000, max_pins_per_gate=40, max_coord=100, max_wire=100000):
    gates = {}

    with open(filename, 'w') as f:
        for gate in range(1, num_gates + 1):
            width = random.randint(2, max_coord)
            height = random.randint(2, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            # Ensure at least one pin on left and one on right
            pins = [(0, random.randint(0, height)), (width, random.randint(0, height))]
            
            # Calculate the maximum possible pins based on height
            max_possible_pins = (height + 1) * 2  # Two edges with height + 1 positions

            # Ensure we don't request more pins than possible
            num_pins = min(random.randint(2, max_pins_per_gate), max_possible_pins)

            # Generate additional random pins on left or right edges
            while len(pins) < num_pins:
                edge = random.choice(["left", "right"])
                y = random.randint(0, height)
                x = 0 if edge == "left" else width
                if (x, y) not in pins:  # Check to avoid duplicates
                    pins.append((x, y))

            gates[f"g{gate}"] = len(pins)

            # Write pins to file
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        # Generate wires same as before
        all_gates = list(gates.keys())
        used_connections = set()

        for gate1 in all_gates:
            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            pin2 = random.randint(1, gates[gate2])
            connection = (gate1, pin1, gate2, pin2)

            if connection not in used_connections:
                f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                used_connections.add(connection)

        num_extra_wires = max_wire
        for _ in range(num_extra_wires):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    pin2 = random.randint(1, gates[gate2])
                    connection = (gate1, pin1, gate2, pin2)

                    if connection not in used_connections:
                        f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                        used_connections.add(connection)
                        break


# Function 2 with a range of dimensions for gates instead of max dimension
def generate_test2(filename="input.txt", num_gates=1000, min_coord=2, max_coord=100, max_pins_per_gate=40, max_wire=100000):
    gates = {}

    with open(filename, 'w') as f:
        for gate in range(1, num_gates + 1):
            width = random.randint(min_coord, max_coord)
            height = random.randint(min_coord, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            # Ensure at least one pin on left and one on right
            pins = [(0, random.randint(0, height)), (width, random.randint(0, height))]

            # Calculate the maximum possible pins based on height
            max_possible_pins = (height + 1) * 2  # Two edges with height + 1 positions

            num_pins = min(random.randint(2, max_pins_per_gate), max_possible_pins)

            # Generate additional random pins on left or right edges
            available_positions = set((0, y) for y in range(height + 1)) | set((width, y) for y in range(height + 1))
            available_positions -= set(pins)  # Remove already used positions

            while len(pins) < num_pins and available_positions:
                x, y = random.choice(list(available_positions))
                pins.append((x, y))
                available_positions.remove((x, y))  # Ensure no duplicates

            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        # Generate wires same as in generate_test
        all_gates = list(gates.keys())
        used_connections = set()

        for gate1 in all_gates:
            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            pin2 = random.randint(1, gates[gate2])
            connection = (gate1, pin1, gate2, pin2)

            if connection not in used_connections:
                f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                used_connections.add(connection)

        num_extra_wires = max_wire
        for _ in range(num_extra_wires):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    pin2 = random.randint(1, gates[gate2])
                    connection = (gate1, pin1, gate2, pin2)

                    if connection not in used_connections:
                        f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                        used_connections.add(connection)
                        break


# Function 3 to generate exactly the specified number of pins
def generate_test3(filename="input.txt", num_gates=1000, num_pins_per_gate=40, max_coord=100, max_wire=100000):
    gates = {}

    with open(filename, 'w') as f:
        for gate in range(1, num_gates + 1):
            width = random.randint(2, max_coord)
            height = random.randint(2, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            # Ensure at least one pin on left and one on right
            pins = [(0, random.randint(0, height)), (width, random.randint(0, height))]

            # Calculate the maximum possible pins based on height
            max_possible_pins = (height + 1) * 2

            num_pins = min(num_pins_per_gate, max_possible_pins)

            # Create a set of available positions
            available_positions = set((0, y) for y in range(height + 1)) | set((width, y) for y in range(height + 1))
            available_positions -= set(pins)  # Remove already used positions

            # Generate exactly the specified number of pins
            while len(pins) < num_pins and available_positions:
                x, y = random.choice(list(available_positions))
                pins.append((x, y))
                available_positions.remove((x, y))  # Ensure no duplicates

            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        # Generate wires same as before
        all_gates = list(gates.keys())
        used_connections = set()

        for gate1 in all_gates:
            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            pin2 = random.randint(1, gates[gate2])
            connection = (gate1, pin1, gate2, pin2)

            if connection not in used_connections:
                f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                used_connections.add(connection)

        num_extra_wires = max_wire
        for _ in range(num_extra_wires):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    pin2 = random.randint(1, gates[gate2])
                    connection = (gate1, pin1, gate2, pin2)

                    if connection not in used_connections:
                        f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                        used_connections.add(connection)
                        break


# Function 4 to generate exactly the number of pins with a range of dimensions
def generate_test4(filename="input.txt", num_gates=1000, min_coord=2, max_coord=100, num_pins_per_gate=40, max_wire=100000):
    gates = {}

    with open(filename, 'w') as f:
        for gate in range(1, num_gates + 1):
            width = random.randint(min_coord, max_coord)
            height = random.randint(min_coord, max_coord)
            f.write(f"g{gate} {width} {height}\n")

            # Ensure at least one pin on left and one on right
            pins = [(0, random.randint(0, height)), (width, random.randint(0, height))]

            # Calculate the maximum possible pins based on height
            max_possible_pins = (height + 1) * 2

            num_pins = min(num_pins_per_gate, max_possible_pins)

            # Create a set of available positions
            available_positions = set((0, y) for y in range(height + 1)) | set((width, y) for y in range(height + 1))
            available_positions -= set(pins)  # Remove already used positions

            # Generate exactly the specified number of pins
            while len(pins) < num_pins and available_positions:
                x, y = random.choice(list(available_positions))
                pins.append((x, y))
                available_positions.remove((x, y))  # Ensure no duplicates

            gates[f"g{gate}"] = len(pins)
            pin_str = " ".join(f"{x} {y}" for x, y in pins)
            f.write(f"pins g{gate} {pin_str}\n")

        # Generate wires same as before
        all_gates = list(gates.keys())
        used_connections = set()

        for gate1 in all_gates:
            gate2 = random.choice([g for g in all_gates if g != gate1 and gates[g] > 0])
            pin1 = random.randint(1, gates[gate1])
            pin2 = random.randint(1, gates[gate2])
            connection = (gate1, pin1, gate2, pin2)

            if connection not in used_connections:
                f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                used_connections.add(connection)

        num_extra_wires = max_wire
        for _ in range(num_extra_wires):
            while True:
                gate1, gate2 = random.sample(all_gates, 2)
                if gate1 != gate2 and gates[gate1] > 0 and gates[gate2] > 0:
                    pin1 = random.randint(1, gates[gate1])
                    pin2 = random.randint(1, gates[gate2])
                    connection = (gate1, pin1, gate2, pin2)

                    if connection not in used_connections:
                        f.write(f"wire {gate1}.p{pin1} {gate2}.p{pin2}\n")
                        used_connections.add(connection)
                        break


# every test case has at least n wires where n is number of gates
generate_test('input0.txt' , 1000 , 40 , 100 , 1000000)
generate_test('input1.txt' , 1000 , 40 , 100 , 100000)
generate_test('input2.txt' , 1000 , 40 , 100 , 30000)
generate_test('input3.txt' , 1000 , 40 , 100 , 10000)
generate_test('input4.txt' , 1000 , 40 , 100 , 1000)
generate_test('input5.txt' , 1000 , 40 , 100 , 100)
for i in range(6 , 14):
    filename = 'input'+str(i)+'.txt'
    generate_test(filename , 1000//2**(i-5) , 40 , 100 , 30000//2**(i-5))