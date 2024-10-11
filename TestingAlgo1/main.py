import random
from collections import defaultdict, Counter, deque
import sys
# from visualize_gates import draw_gate_packing
'''
Python Code to implement a heap with general comparison function
'''
sys.setrecursionlimit(10000000)
def comp1(a,b):
    return a<b

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        # Write your code here
        self.comparator=comparison_function
        if init_array==None:
            self.stored=[]
        else:
            self.stored=init_array
        self.len=len(self.stored)
        for i in range(self.len-1,-1,-1):
            j=i
            self.downheap(j)
            
    def print_list(self):
        return self.stored
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        # Write your code here
        self.stored.append(value)
        self.len+=1
        k=self.len-1
        while(k!=0):
            if(self.comparator(self.stored[k],self.stored[(k-1)//2])):
                self.stored[k],self.stored[(k-1)//2]=self.stored[(k-1)//2],self.stored[k]
                k=(k-1)//2
            else:
                break
        
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.len==0:
            return None
        if self.len==1:
            self.len=0
            return self.stored.pop()
        el=self.stored.pop()
        answer=self.stored[0]
        self.len-=1
        self.stored[0] = el
        self.downheap(0)
        return answer
        
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if (self.len>0):
            return self.stored[0]
        return None
    
    # You can add more functions if you want to
    def downheap(self,j):
        while(j<self.len):
            left=True
            right=True
            if(j*2 +1 <self.len):
                left=self.comparator(self.stored[j], self.stored[2*j+1])
            if(j*2 +2 <self.len):
                right=self.comparator(self.stored[j], self.stored[2*j+2])
            if ((not(left) or not(right))):
                if(2*j+2<self.len):
                    if self.comparator(self.stored[2*j+1],self.stored[2*j+2]):
                        self.stored[j], self.stored[2*j+1]= self.stored[2*j+1], self.stored[j]
                        j=2*j+1
                    else:
                        self.stored[j], self.stored[2*j+2]= self.stored[2*j+2], self.stored[j]
                        j=2*j+2
                elif(2*j+1<self.len):
                    self.stored[j], self.stored[2*j+1]= self.stored[2*j+1], self.stored[j]
                    j=2*j+1
                else:
                    break
            else:
                break
        return





def aadi_solution(filename):#O(31(n+p+w)) + O(clustering_recursion(label_prop)) + 30*O(clustering_recusrion(adj_clustering))
    best_object=GatePacking()
    best_object.read_input(filename)
    best_object.clustering_recursion(label_propagation)
    length=best_object.wire_length
    best_bounding_box=best_object.bounding_box
    print("Label prop",1,length)
    for i in range(9):
        packing=GatePacking()
        packing.read_input(filename)
        packing.clustering_recursion(label_propagation)
        if length>packing.wire_length:
            best_object=packing
            length=packing.wire_length
            best_bounding_box=packing.bounding_box
        print("Label_prop",i+2,packing.wire_length)
    for i in range(3,31):
        for j in range(1000,1001):
            packing=GatePacking()
            packing.read_input(filename)
            packing.clustering_recursion(adj_clustering,j,i)
            if length>packing.wire_length:
                best_object=packing
                length=packing.wire_length
                best_bounding_box=packing.bounding_box
            print("Adj Clustering",j,i,packing.wire_length)
    return best_object,length,best_bounding_box


def recursive_clustering(gates_list,gates_dict,gates_adj_list,clustering_function,depth,max_cluster_size):
    if (len(gates_list)==1):
        boss_gate=gates_dict[gates_list[0]]
        boss_gate.x=0
        boss_gate.y=0
        return (boss_gate.width,boss_gate.height)
    if (depth==0):
        input_optimal=[]
        for gate in gates_list:
            input_optimal.append((gates_dict[gate],gate))
        output_optimal=optimal_packing(input_optimal)
        for gate in gates_list:
            gates_dict[gate].x=output_optimal[gate][0]
            gates_dict[gate].y=output_optimal[gate][1]
        return (output_optimal["bounding_box"][0],output_optimal["bounding_box"][1])
    if clustering_function!=adj_clustering:
        cluster_to_gate_list=clustering_function(gates_list,gates_adj_list) #returns a dict having cluster names as keys and cluster
    else:
        cluster_to_gate_list=adj_clustering(gates_list,gates_adj_list,max_cluster_size)
    gates_to_cluster_dict={} # for every gate stores which cluster it is in
    clusters_list=[]
    clusters_dict={}
    clusters_adj_list={}

    for cluster in cluster_to_gate_list.keys():
        clusters_list.append(cluster)
        input_optimal=[]
        for gate in cluster_to_gate_list[cluster]:
            gates_to_cluster_dict[gate]=cluster
            input_optimal.append((gates_dict[gate],gate))
        output_optimal=optimal_packing(input_optimal)
        new_gate=Gate(cluster,output_optimal["bounding_box"][0],output_optimal["bounding_box"][1])
        clusters_dict[cluster]=new_gate
        for gate in cluster_to_gate_list[cluster]:
            gates_dict[gate].x=output_optimal[gate][0]
            gates_dict[gate].y=output_optimal[gate][1]
    
    for gate in gates_list:
        for neighbour in (gates_adj_list[gate]):
            cluster1=gates_to_cluster_dict[gate]
            cluster2=gates_to_cluster_dict[neighbour]
            if cluster1!=cluster2:
                clusters_adj_list.setdefault(cluster1,[]).append(cluster2)

    bounding_box=recursive_clustering(clusters_list,clusters_dict,clusters_adj_list,clustering_function,depth-1,max_cluster_size)
    
    for cluster in cluster_to_gate_list.keys():
        for gate in cluster_to_gate_list[cluster]:
            gates_dict[gate].x+=clusters_dict[cluster].x
            gates_dict[gate].y+=clusters_dict[cluster].y

    return bounding_box

def optimal_packing(gates_list):#(sum of heights * n^2logn)
    #initialising parameters
    min_perimeter = float('inf')
    total_area=0
    sum_heights=0
    max_height=-1
    max_width=-1
    min_height=float('inf')
    min_width=float('inf')
    sum_widths=0
    for i in gates_list:
        total_area+=i[0].area
        sum_heights+=i[0].height
        sum_widths+=i[0].width
        max_height=max(max_height,i[0].height)
        min_height=min(min_height,i[0].height)
        min_width=min(min_width,i[0].width)
        max_width=max(max_width,i[0].width)
    final={}
    step = 10 if len(gates_list) >= 100 else 1
    #main algorithm, iterating over height
    top=min(sum_heights, int(2 * (total_area)**0.5))
    if int(2*(total_area)**0.5)<=max_height:
        top=sum_heights
    for height in range(max_height,top + 1, step):
        total_width = 0
        max_stack_height = 0
        gates = {} 
        used_points = Heap(comp1,[]) #stores list as [possible x, -possible y, max width, max height]
        used_points.insert((0, 0, max_width + 1, height))
        sorted_gates_list = sorted(gates_list, key=lambda x: x[0].width, reverse=True)

        for gate in sorted_gates_list:
            l=[] #stores unused points to put back into heap later
            while used_points:

                k = used_points.extract()
                if k[1] == 0:
                    total_width += gate[0].width
                    gates[gate[1]] = [k[0], k[1]]
                    #inserting on top
                    used_points.insert((k[0], -gate[0].height, gate[0].width, height - gate[0].height))
                    #inserting on right
                    used_points.insert((total_width, 0, max_width + 1, height))
                    max_stack_height = max(max_stack_height, gate[0].height)
                    break
                elif gate[0].width <= k[2] and gate[0].height <= k[3]:
                    gates[gate[1]] = [k[0], -k[1]]
                    #inserting at the top
                    if (k[3] - gate[0].height) >= min_height:
                        (used_points.insert((k[0], k[1] - gate[0].height, gate[0].width, k[3] - gate[0].height)))
                    #inserting at the right
                    if k[2] - gate[0].width != 0:
                        (used_points.insert((k[0] + gate[0].width, k[1], k[2] - gate[0].width, k[3])))
                    max_stack_height = max(max_stack_height, gate[0].height - k[1])
                    break
                else:
                    l.append(k)
            #putting back in unused points       
            for j in l:
                (used_points.insert(j))
        gates={'bounding_box':[total_width, max_stack_height],**gates}
        perimeter = total_width + max_stack_height
        if perimeter < min_perimeter:
            min_perimeter = perimeter
            final = gates
    #main algorithm iterating over width

    return final

def label_propagation(elements, adj_list,max_iter=100): #O(g + w*2)
    labels = {node: node for node in elements}
    nodes = list(elements)
    for i in range(max_iter):
        random.shuffle(nodes)
        changed = False
        for node in nodes:
            neighbor_labels = [labels[neighbor] for neighbor in adj_list[node] if neighbor in labels]   
            if not neighbor_labels:
                continue
            most_common_label = Counter(neighbor_labels).most_common(1)[0][0]
            if labels[node] != most_common_label:
                labels[node] = most_common_label
                changed = True
        if not changed:
            break
    clusters = defaultdict(list)
    for node, label in labels.items():
        clusters[label].append(node)
    # print(dict(clusters),len(dict(clusters)))
    return dict(clusters)

def adj_clustering(gates_list,adj_list,max_cluster_size=8):
    gates_visited={}
    output_clusters={}
    for gate in gates_list:
        gates_visited[gate]=0
    random.shuffle(gates_list)
    for gate in gates_list:
        count=0
        if gates_visited[gate]!=1:
            gates_visited[gate]=1
            output_clusters[gate]=[gate]
            count=1
            neighbours=adj_list[gate]
            ind=0
            neighbour_dict={}
            neighbour_list=[]
            for neighbour in neighbours:
                if neighbour_dict.get(neighbour)==None:
                    if gates_visited[neighbour]==0:
                        neighbour_dict[neighbour]=ind
                        ind+=1
                        neighbour_list.append([-1,neighbour])
                else:
                    if gates_visited[neighbour]==0:
                        neighbour_list[neighbour_dict[neighbour]][0]-=1
            neighbour_heap=Heap(comp1,neighbour_list)
            while (len(neighbour_list)!=0) and (count!=max_cluster_size):
                top=neighbour_heap.top()
                
                count+=1
                
                output_clusters[gate].append(top[1])
                gates_visited[top[1]]=1
                neighbour_heap.extract()
                
    
    gate_checker={}
    for i in output_clusters.keys():
        for j in output_clusters[i]:
            if gate_checker.get(j)==None:
                gate_checker[j]=1
            else:
                print("Overlap!!!!")
    return output_clusters




class Gate:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.area=width*height
        self.x=None
        self.y=None
        self.pins={}
        self.pin_count=0
    def insert_pin(self,tuple,pin_name):
        self.pin_count+=1
        self.pins[pin_name]=tuple


class GatePacking:
    def __init__(self): #O(1)
        self.gate_dimensions_dict = {} # [width,height,name] lists stored
        self.gates_dict = {} # key : gate name, value: gate object
        self.wires=[] #(pin1,pin2) stored
        self.ports_adj_list={}
        self.gates_adj_list={}
        self.gates_visited={}
        self.conn_comp_gates=[] #contains lists of connected components of gates
        self.ports_visited={}
        self.conn_comp_ports=[] #contains lists of connected components of ports
        self.bounding_box=[] 
        self.wire_length=0
        self.send_to_draw={}
    def read_input(self, filename): #O(n+p+w)
        #initial reading from the input
        with open(filename , 'r') as f:#O(n+p+w)
            l = f.readlines()
            for i in range(len(l)):
                l[i] = l[i].split()
            for i in l:
                if (i[0] != 'wire'):
                    if (i[0][0] =='g'):
                        new_gate=Gate(i[0],int(i[1]),int(i[2]))
                        self.gates_dict[i[0]] = new_gate
                        self.gate_dimensions_dict[i[0]]=[int(i[1]),int(i[2])]
                    else:
                        for j in range (2 , len(i) , 2):
                            (self.gates_dict[i[1]]).insert_pin((int(i[j]) , int(i[j+1])) , i[1]+'.'+'p'+str(int(j/2)))
                else:
                    self.wires.append((i[1] , i[2]))
        #processing wires into adjacency lists
        for i in self.wires: #O(w)
            self.ports_adj_list.setdefault(i[0], []).append(i[1])
            k1 = i[0].split('.')
            k2 = i[1].split('.')
            self.gates_adj_list.setdefault(k1[0], []).append(k2[0])
            self.gates_adj_list.setdefault(k2[0], []).append(k1[0])
        #processing adjacency lists into connected components lists
        self.connected_components_gates() #O(n + w) #stores connected gate components into self.conn_comp_gates
        # self.connected_components_ports()#stores connected port components into self.conn_comp_ports
    def connected_components_gates(self):
        for i in self.gates_adj_list.keys():
            if not self.gates_visited.get(i):
                self.conn_comp_gates.append(self.dfs_gates(i))
    def dfs_gates(self,i):
        l = []
        l.append(i)
        self.gates_visited[i] = 1
        for j in self.gates_adj_list[i]:
            if not self.gates_visited.get(j):
                l.extend(self.dfs_gates(j))
        return l
    def calculate_wire_length(self): #O(w)
        sum=0
        for in_pin in self.ports_adj_list.keys():
            k=in_pin.split(".")
            x_coord = (self.gates_dict[k[0]]).x + ((self.gates_dict[k[0]]).pins)[k[0]+'.p'+str(int(k[1][1:]))][0]
            y_coord = (self.gates_dict[k[0]]).y + (self.gates_dict[k[0]]).pins[k[0]+'.p'+str(int(k[1][1:]))][1]
            miny=y_coord
            minx=x_coord
            maxx=x_coord
            maxy=y_coord
            for out_pin in self.ports_adj_list[in_pin]:
                k2=out_pin.split(".")
                x_coord = (self.gates_dict[k2[0]]).x + ((self.gates_dict[k2[0]]).pins)[k2[0]+'.p'+str(int(k2[1][1:]))][0]
                y_coord = (self.gates_dict[k2[0]]).y + (self.gates_dict[k2[0]]).pins[k2[0]+'.p'+str(int(k2[1][1:]))][1]
                miny=min(y_coord,miny)
                minx=min(x_coord,minx)
                maxx=max(x_coord,maxx)
                maxy=max(y_coord,maxy)
            sum+= maxx+maxy-minx-miny
        self.wire_length=sum
        return sum
    def send_to_file(self,filename): #O(n)
        with open(filename , 'w') as f:
            f.write(f'bounding_box {self.bounding_box[0]} {self.bounding_box[1]}\n')
            self.send_to_draw['bounding_box']=[self.bounding_box[0],self.bounding_box[1]]
            for key in self.gates_dict.keys():
                if self.gates_dict[key].x!=None:
                    f.write(f'{key} {self.gates_dict[key].x} {self.gates_dict[key].y}\n')
                    self.send_to_draw[key]=[self.gates_dict[key].x,self.gates_dict[key].y]
            f.write(f'wire_length {self.wire_length}\n')
    def optimal_packing_initiator(self):
        #for connected components, bounding box ke constraints keep adding to the output, add coordinates to gate objects and thus be done with it, gates ke coordinates ke saath, update origin etc
        total_width_yet=0
        max_height_yet=0
        for i in self.conn_comp_gates:
            width=0
            height=0
            input_list=[]
            for j in i:
                input_list.append((self.gates_dict[j],j))
            output_dict=optimal_packing(input_list)
            for key in output_dict.keys():
                if key=="bounding_box":
                    width=output_dict[key][0]
                    height=output_dict[key][1]
                else:
                    self.gates_dict[key].x = output_dict[key][0] + total_width_yet
                    self.gates_dict[key].y = output_dict[key][1]
            total_width_yet+=width
            max_height_yet=max(height,max_height_yet)
        self.bounding_box=[total_width_yet,max_height_yet]
        self.calculate_wire_length()   
    def clustering_recursion(self,clustering_function,depth=1000,max_cluster_size=0): #O(c+n+w)+O(recursive_clustering(clustering_function,component))
        total_width_yet=0
        max_height_yet=0

        for comp in self.conn_comp_gates:
            bounding_box=recursive_clustering(comp,self.gates_dict,self.gates_adj_list,clustering_function,depth,max_cluster_size)
            for gate in comp:
                self.gates_dict[gate].x+=total_width_yet
            total_width_yet+=bounding_box[0]
            max_height_yet=max(max_height_yet,bounding_box[1])
        self.bounding_box=[total_width_yet,max_height_yet]
        self.calculate_wire_length()
    def draw(self):
        root = draw_gate_packing(self.gate_dimensions_dict,self.send_to_draw, (600,600))
        root.mainloop()


class EnhancedGreedyGatePacking(GatePacking):
    def __init__(self):
        super().__init__()
        self.pin_groups = {}  # Dictionary to store groups of connected pins and their bounding boxes
        self.occupied_points = set()  # Set to store all occupied points (x, y) to check for overlap
        self.group_bounding_boxes = {}  # Dictionary to track min/max bounding box dimensions by group ID
        self.boundary_points = set()
        self.vis_gates = {}
    def set_pin_groups(self):
        # num = 1
        # for i in self.conn_comp_ports:
        #     for j in i:
        #         self.pin_groups[j] = num
        #     num+=1
        # for i in self.gates_dict.values():
        #     for j in i.pins.keys():
        #         if not self.pin_groups.get(j):
        #             self.pin_groups[j] = num
        #             num = num+1
        for i in self.ports_adj_list.keys():
            for j in self.ports_adj_list[i]:
                self.pin_groups[j] = i
        
        for i in self.ports_adj_list.keys():
            self.group_bounding_boxes[i] = {
                'min_x': float('inf'),
                'max_x': 0,
                'min_y': float('inf'),
                'max_y': 0
            }
    def find_gate_with_most_connections(self , gates):
        """
        Find the gate with the highest number of connections (most connected).
        """
        max_connections = -1
        most_connected_gate = None
        for gate_name in gates:
            connections = len(self.gates_adj_list.get(gate_name, []))
            if connections > max_connections:
                max_connections = connections
                most_connected_gate = gate_name
        return most_connected_gate

    def place_first_gate(self, gates ):
        # print(gates)
        """
        Place the first gate with the most connections at a position (sum_width, sum_height).
        """
        sum_width = sum(gate.width for gate in self.gates_dict.values())
        sum_height = sum(gate.height for gate in self.gates_dict.values())
        self.bounding_box = [2*sum_width , 2*sum_height]
        first_gate = self.find_gate_with_most_connections(gates)
        # Place the first gate at (sum_width, sum_height)
        self.vis_gates[first_gate] = 1
        self.gates_dict[first_gate].x = sum_width
        self.gates_dict[first_gate].y = sum_height
        self.set_pin_groups()
        # Mark the points as occupied and update bounding box
        self.update_bounding_box_and_occupied(first_gate, sum_width, sum_height)
        # Initialize the pin group for this gate
        for pin in self.gates_dict[first_gate].pins.keys():
            if (self.group_bounding_boxes.get(pin)):
                self.group_bounding_boxes[pin ] = {
                    'min_x': sum_width+self.gates_dict[first_gate].pins[pin][0],
                    'max_x': sum_width+self.gates_dict[first_gate].pins[pin][0],
                    'min_y': sum_height+self.gates_dict[first_gate].pins[pin][1],
                    'max_y': sum_height+self.gates_dict[first_gate].pins[pin][1]
                }
            if (self.pin_groups.get(pin)):
                self.group_bounding_boxes[self.pin_groups[pin] ] = {
                    'min_x': sum_width+self.gates_dict[first_gate].pins[pin][0],
                    'max_x': sum_width+self.gates_dict[first_gate].pins[pin][0],
                    'min_y': sum_height+self.gates_dict[first_gate].pins[pin][1],
                    'max_y': sum_height+self.gates_dict[first_gate].pins[pin][1]
                }
        
        return first_gate

    def update_bounding_box_and_occupied(self, gate_name, x, y):
        """
        Update the bounding box of the gate and mark the points as occupied.
        """
        gate = self.gates_dict[gate_name]
        width, height = gate.width, gate.height
        # for i in range(x+1 , x+width):
        #     if (i , y) in self.occupied_points and (i , y) in self.boundary_points:
        #         self.boundary_points.remove((i , y))
        #     else:
        #         self.boundary_points.add((i , y))
        #     if (i , y+height) in self.occupied_points and (i , y+height)  in self.boundary_points:
        #         self.boundary_points.remove((i , y+height))
        #     else:
        #         self.boundary_points.add((i , y+height))
        # for i in range(y+1 , y+height):
        #     if (x , i) in self.occupied_points and (x , i) in self.boundary_points:
        #         self.boundary_points.remove((x , i))
        #     else:
        #         self.boundary_points.add((x , i))
        #     if (x+width, i) in self.occupied_points and (x+width , i) in self.boundary_points:
        #         self.boundary_points.remove((x+width , i))
        #     else:
        #         self.boundary_points.add((x+width , i))
        # # Mark all points occupied
        # if (x , y) in self.boundary_points:
        #     if (x-1 , y) in self.occupied_points and (x , y-1) in self.occupied_points:
        #         self.boundary_points.remove((x , y))
        # else:
        #     self.boundary_points.add((x,y))
        # if (x +width, y+height) in self.boundary_points:
        #     if (x+1+width , y+height) in self.occupied_points and (x+width , y+1+height) in self.occupied_points:
        #         self.boundary_points.remove((x+width , y+height))
        # else:
        #     self.boundary_points.add((x+width,y+height))
        # if (x , y+height) in self.boundary_points:
        #     if (x-1 , y+height) in self.occupied_points and (x , y+height+1) in self.occupied_points:
        #         self.boundary_points.remove((x , y+height))
        # else:
        #     self.boundary_points.add((x,y+height))
        # if (x+width , y) in self.boundary_points:
        #     if (x+width , y-1) in self.occupied_points and (x+width+1 , y) in self.occupied_points:
        #         self.boundary_points.remove((x+width , y))
        # else:
        #     self.boundary_points.add((x+width,y))
        self.boundary_points.add((x , y))
        self.boundary_points.add((x , y+height))
        self.boundary_points.add((x+width , y))
        self.boundary_points.add((x+width , y+height))
        for i in range(x, x + width+1):
            for j in range(y, y + height+1):
                self.occupied_points.add((i, j))
        self.gates_dict[gate_name].x = x
        self.gates_dict[gate_name].y = y
        return (x, y), (x + width, y + height)

    def try_placement(self, gate, boundary_points):
        """
        Try placing the gate at all boundary points and return the one that minimizes the sum of semi-perimeters.
        """
        min_semi_perimeter = float('inf')
        best_placement = None

        for point in boundary_points:
            x, y = point
            check = [(x-gate.width , y) , (x , y) , (x , y-gate.height) , (x-gate.width , y - gate.height)]
            # Check placement in all four directions (bottom, top, left, right)
            for x , y in check:
                if not self.is_overlap(gate, x, y):
                    semi_perimeter = self.calculate_semi_perimeter(gate, x, y )
                    if semi_perimeter < min_semi_perimeter:
                        min_semi_perimeter = semi_perimeter
                        best_placement = (x, y)
        
        return best_placement

    def is_overlap(self, gate, x, y):
        """
        Check if placing the gate at (x, y) with a specific alignment causes overlap.
        """
        width, height = gate.width, gate.height
        
        # # Determine the position based on alignment
        # if alignment == "bottom":
        #     bottom_left_x, bottom_left_y = x, y  # Align bottom-left corner with point (x, y)
        # elif alignment == "top":
        #     bottom_left_x, bottom_left_y = x, y - height  # Align top edge of gate with point (x, y)
        # elif alignment == "left":
        #     bottom_left_x, bottom_left_y = x - width, y  # Align right edge of gate with point (x, y)
        # elif alignment == "right":
        #     bottom_left_x, bottom_left_y = x, y  # Align left edge of gate with point (x, y)

        # Check for overlap inside the boundary of the gate
        for i in range(x+1 , x+width):
            if (i , y+1) in self.occupied_points:
                return True
            if (i , y+height -1) in self.occupied_points:
                return True
        for i in range(y+1 , y+height):
            if (x+1 , i) in self.occupied_points:
                return True
            if (x+width-1 , i) in self.occupied_points:
                return True
        # for i in range(x+1, x + width):
        #     for j in range(y+1, y + height):
        #         if (i, j) in self.occupied_points:
        #             return True
        if height == 1 and width !=1:
            for i in range(x+1 , x+width):
                if (i , y) in self.occupied_points and (i , y+1) in self.occupied_points:
                    return True
        if height != 1 and width ==1:
            for i in range(y+1 , y+height):
                if (x , i) in self.occupied_points and (x+1 , i) in self.occupied_points:
                    return True
        if height == 1 and width ==1:
            if (x , y) in self.occupied_points and (x+1 , y) in self.occupied_points and(x , y+1) in self.occupied_points and(x+1 , y+1) in self.occupied_points:
                return True
        return False

    def calculate_semi_perimeter(self, gate, x, y):
        """
        Calculate the semi-perimeter of the bounding box based on the min/max x and y values.
        """
        # if alignment == "bottom":
        #     bottom_left_x, bottom_left_y = x, y
        # elif alignment == "top":
        #     bottom_left_x, bottom_left_y = x, y - gate.height
        # elif alignment == "left":
        #     bottom_left_x, bottom_left_y = x - gate.width, y
        # elif alignment == "right":
        #     bottom_left_x, bottom_left_y = x, y
        
        # Calculate semi-perimeter based on bounding box
        top_right_x = x + gate.width
        top_right_y = y + gate.height
        width = top_right_x - x
        height = top_right_y - y
        total_semi_perimeter = 0
        for pin in gate.pins.keys():
            group_id = self.pin_groups.get(pin)
            if (group_id):  # Assuming all pins belong to the same group
                group = self.group_bounding_boxes[group_id]

                width = max(group['max_x'] , x+gate.pins[pin][0]) - min(group['min_x'] , x+gate.pins[pin][0])
                height = max(group['max_y'] ,  y+gate.pins[pin][1]) - min(group['min_y'] , y+gate.pins[pin][1])
                total_semi_perimeter += (width + height)
            group_id2 = pin
            group2=  self.group_bounding_boxes.get(group_id2)
            if (group2):
                width = max(group2['max_x'] , x+gate.pins[pin][0]) - min(group2['min_x'] , x+gate.pins[pin][0])
                height = max(group2['max_y'] ,  y+gate.pins[pin][1]) - min(group2['min_y'] , y+gate.pins[pin][1])
                total_semi_perimeter += (width + height)
        return total_semi_perimeter
    def update_pin_group_bounding_box(self, gate, x, y):
        """
        Update the bounding box for each pin group the gate belongs to.
        """
        for pin in gate.pins.keys():
            group_id = self.pin_groups.get(pin)# All pins belong to the same group in this implementation
            if (group_id):
                group = self.group_bounding_boxes[group_id]
                
                # Update min/max values
                group['min_x'] = min(group['min_x'], x+gate.pins[pin][0])
                group['max_x'] = max(group['max_x'], x+gate.pins[pin][0])
                group['min_y'] = min(group['min_y'], y+gate.pins[pin][1])
                group['max_y'] = max(group['max_y'], y+gate.pins[pin][1])
            group_id = pin
            group = self.group_bounding_boxes.get(group_id)
            if (group):
                group['min_x'] = min(group['min_x'], x+gate.pins[pin][0])
                group['max_x'] = max(group['max_x'], x+gate.pins[pin][0])
                group['min_y'] = min(group['min_y'], y+gate.pins[pin][1])
                group['max_y'] = max(group['max_y'], y+gate.pins[pin][1])
    def greedy_packing(self , gates ):
        """
        The main greedy algorithm for placing gates while minimizing the semi-perimeter.
        """
        sum_width = sum(gate.width for gate in self.gates_dict.values())
        sum_height = sum(gate.height for gate in self.gates_dict.values())
       
        # Step 1: Place the first gate
        first_gate = self.place_first_gate(gates )
        min_x = sum_width
        min_y = sum_height
        max_x = sum_width + self.gates_dict[first_gate].width
        max_y = sum_height + self.gates_dict[first_gate].height
        # print(self.occupied_points , self.boundary_points)
        # print(self.gates_adj_list[first_gate])
        # Step 2: Maintain a queue of gates to be placed
        gate_queue = deque()
        for i in self.gates_adj_list[first_gate]:
            if not self.vis_gates.get(i):
                gate_queue.append(i)
                self.vis_gates[i] = 1
        # Step 3: Place each gate by minimizing the sum of bounding box semi-perimeters
        while gate_queue:
            current_gate = gate_queue.popleft()
            boundary_points = self.boundary_points
            
            # Try placing the gate at the best position
            best_placement = self.try_placement(self.gates_dict[current_gate], boundary_points)
            
            if best_placement:
                # print(current_gate)
                x, y = best_placement
                # if (alignment == 'top'): y-=self.gates_dict[current_gate].height
                # if (alignment == 'left'): x-=self.gates_dict[current_gate].width
                # print(x , y)
                min_x = min(x , min_x)
                max_x = max(x +self.gates_dict[current_gate].width, max_x)
                min_y = min(y , min_y)
                max_y = max(y+self.gates_dict[current_gate].height , max_y)
                # Update bounding boxes and occupied point
                self.update_bounding_box_and_occupied(current_gate, x, y)
                self.update_pin_group_bounding_box(self.gates_dict[current_gate], x, y)
                self.vis_gates[current_gate] = 1
                # Add adjacent gates to the queue
                for neighbor in self.gates_adj_list[current_gate]:
                    if not self.vis_gates.get(neighbor):
                        gate_queue.append(neighbor)
                        self.vis_gates[neighbor] = 1
                # print(self.occupied_points , self.boundary_points)
            else:
                print(current_gate)
        return min_x , max_x , min_y , max_y
        # After final placement, calculate the total wire length
        # self.calculate_wire_length()   
    
    def greedy_multiple(self ):
        total_sum1 = 0
        total_sum2 = 0
        # sum_width = sum(gate.width for gate in self.gates_dict.values())
        # sum_height = sum(gate.height for gate in self.gates_dict.values())
        maxy = 0
        for i in self.conn_comp_gates:
            self.occupied_points = set()
            self.boundary_points = set()
            x1 , x2 , y1 , y2 = self.greedy_packing(i )
            maxy = max(maxy , y2-y1)
            for j in i:
                self.gates_dict[j].x-=x1
                self.gates_dict[j].x+=total_sum1
                self.gates_dict[j].y -=y1
            total_sum1+=(x2-x1)
        self.bounding_box = [total_sum1 , maxy]
        self.calculate_wire_length()   
    def is_overlapping(self , gate1, gate2):
    # Calculate the top-right coordinates of both gates
        gate1_x2 = gate1.x + gate1.width
        gate1_y2 = gate1.y + gate1.height
        
        gate2_x2 = gate2.x + gate2.width
        gate2_y2 = gate2.y+ gate2.height

        # Check if the two gates overlap
        if gate1.x >= gate2_x2 or gate2.x >= gate1_x2:
            return False
        if gate1.y >= gate2_y2 or gate2.y >= gate1_y2:
            return False
        
        return True
    def find_overlapping_gates(self ):
        overlapping_pairs = []
        gate_keys = list(self.gates_dict.keys())
        
        for i in range(len(gate_keys)):
            for j in range(i + 1, len(gate_keys)):
                gate1 = self.gates_dict[gate_keys[i]]
                gate2 = self.gates_dict[gate_keys[j]]
                if (gate1.x == None or gate2.x ==  None): continue
                if self.is_overlapping(gate1, gate2):
                    overlapping_pairs.append((gate_keys[i], gate_keys[j]))
        
        return overlapping_pairs , len(overlapping_pairs)


# def main():
#     object,length,bounding_box=aadi_solution()
#     object.send_to_file("output.txt")
#     print(length)
#     print(bounding_box)
def main():
    packing = EnhancedGreedyGatePacking()
    packing.read_input('tests/input2.txt')
     # print(packing.ports_adj_list)
    packing.greedy_multiple()
    packing.send_to_file('output.txt')
    print(packing.wire_length)
    print(packing.bounding_box)
    print((packing.find_overlapping_gates()))

if __name__ == "__main__":
    main()