# a= amplitude
# x= fraction of theoretical maximum population
def log_map(a,x):   
    return float(a*x*(1-x))

def show_list(x, i):
    for j in range(len(x)):
        print(i, x[j])
        i = i+1 

def make_generations(a,i,g):
    
    l = [i]      # Put the initial value in the list 
    print("Amplitude: ", a)
    print("Intial Value: ", i)
    print("Generations: ", g)
    j=0
    for j in range(g):
        p = log_map(a, i) # Calculate using log_map
        i = p       # Set intial value to the new initial value 
        print ("j = ",j, "Appending ", p)
        l.append(p)      # append the value of p to the list 
        #'print(j, p)
        j = j + 1
    return l     # return the list 

def main():
    a = float(input("Enter the amplitude: "))
    i = float(input("Enter the intitial value: "))
    g = int(input("Enter the number of generations: "))
    x = make_generations(a,i,g) # Make generations and put them in list x 
    show_list(x,0)  # x = list, # 1 = starting value 

main()
