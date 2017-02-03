import sys
import copy
import time

exhaust_Set = []	# closed set that maintains all the visited configurations...
fil = open('ucs_out_2.txt','w')
class Node:
    def __init__(self,config,prev_node = None):
        self.setting = list(config)
        self.pos = -1
        self.cost = 0	# cost associated with the current node...(initially 0 for the parent node).
        self.prev_node = prev_node	# parent reference node that is used while backtracking...
        for i in range(9):
            if self.setting[i] == 0 :
                self.pos = i	# get the initial position of the blank space...
                break
        
    def swap(self,i1,j1):	# swap the space at i1th position with j1th position...
        temp = self.setting[i1]
        self.setting[i1] = self.setting[j1]
        self.setting[j1] = temp
							# update the cost of the node based on the tile being swapped or moved...
        if (self.setting[i1] in [1,2,3]):
            self.cost += 1
        elif (self.setting[i1] in [4,5,6]):
            self.cost += 2
        else :
            self.cost += 3

    def up(self):	# swap the blank space with the top tile...
        k = False
        try:
            if (self.pos - 3 >= 0 ):
                self.swap(self.pos,self.pos-3)
                self.pos = self.pos-3
                k = True
        except:
            pass
        return k

    def down(self):	# swap the blank space with the down tile...
        k = False
        try:
            self.swap(self.pos,self.pos+3)
            self.pos = self.pos+3
            k = True
        except:
            pass
        return k

    def left(self):		# swap the blank space with the left tile...
        k = False
        try:
            if (self.pos % 3 != 0):
                self.swap(self.pos,self.pos-1)
                self.pos = self.pos - 1
                k = True
        except:
            pass
        return k

    def right(self):	# swap the blank space with the right tile...
        k = False
        try:
            if (self.pos % 3 != 2): 
                self.swap(self.pos,self.pos+1)
                self.pos = self.pos + 1
                k = True
        except:
            pass
        return k

    def printconfig(self):	# print the current configuration of the node...
        for i in range(1,10):
            print self.setting[i-1],
            if i%3 == 0:
                print '\r'
        fil.write(str(self.setting[0:3])+'\n')
        fil.write(str(self.setting[3:6])+'\n')
        fil.write(str(self.setting[6:9]))
        fil.write('\n----------V----------\n')
        print '------------------'
        
def ucs(q,start,end):
    q.append(start)	# initial append to the queue...
    notfound = True
    count = 0
    save_start = start
    while(len(q)!=0 and notfound):
        temp = q.pop(0)		# retrieving the top element from the queue...
        exhaust_Set.append(temp.setting)
        if (temp.setting == end):
            print 'found'
            notfound = False
        #temp.printconfig()
        else :
            temp_l = copy.deepcopy(temp)	# creating a copy of the current node to generate child nodes...
            temp_r = copy.deepcopy(temp)
            temp_u = copy.deepcopy(temp)
            temp_d = copy.deepcopy(temp)
            temporary_list = []				# temporary list to sort the child nodes based on the cost...
            if (temp_u.up()):
                if temp_u.setting not in exhaust_Set :
                    temp_u.prev_node = temp
                    temporary_list.append(temp_u)
                    #temp_l.printconfig()
            if (temp_r.right()):
                if temp_r.setting not in exhaust_Set :
                    temp_r.prev_node = temp
                    temporary_list.append(temp_r)
                    #temp_r.printconfig()
            if (temp_d.down()):
                if temp_d.setting not in exhaust_Set :
                    temp_d.prev_node = temp
                    temporary_list.append(temp_d)
                    #temp_u.printconfig()
            if (temp_l.left()):
                if temp_l.setting not in exhaust_Set :
                    temp_l.prev_node = temp
                    temporary_list.append(temp_l)
                    #temp_d.printconfig()       

            temporary_list.sort(key=lambda x:x.cost)	# sorting the temporary list based on the cost assosciated with each nodes...
            q = q + temporary_list						# appending the sorted temporary list to the queue...
            count += 1
    curr_node = None									# reversing the reference nodes from (parent <- child) to (parent -> child)...
    while (temp.prev_node != None and not notfound):
        #temp.printconfig()
        back_node = temp.prev_node
        temp.prev_node = curr_node 
        curr_node = temp
        temp = back_node
    temp.prev_node = curr_node
    #temp.printconfig()
    print '#######################Solution####################'# printing the found solution...
    while (temp.prev_node != None and not notfound):
        temp.printconfig()
        temp = temp.prev_node
    temp.printconfig()
    print 'No. of Steps : ',count
    fil.write('No. of steps : '+str(count)+'\n')
    
end = [1,2,3,
        4,5,6,
        7,8,0]
# the input is the start list...
start = []
#start = [1,2,3,
#        4,0,5,
#        6,7,8]
start = map(int, raw_input().strip().split(' '))
t1 = time.time()	# timestamp before running the function...
q = []
node1 = Node(start)
#k= copy.deepcopy(node1.setting)
ucs(q,node1,end)
t2 = time.time()	# timestamp after running the function...
print 'Time taken : '+str(t2-t1)
fil.write('Time taken : '+str(t2-t1))
