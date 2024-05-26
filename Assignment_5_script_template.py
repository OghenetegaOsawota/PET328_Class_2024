# A script to classify and count 'active' and 'inactive'
# gridblocks in a discretized reservoir

#################### Task 1 ############################
    # Request for reservoir dimensions and discretization parameters

# Lx
Lx= float(input('what is the length of the block'))
# Ly
Ly= float(input('what is the length of the block'))
# Lz
Lz= float(input('what is the length of the block'))
# nx
nx= int(input('how many blocks are there on the x-axis'))
# ny
ny= int(input('how many blocks are there on the y-axis'))
# nz
nz= int(input('how many blocks are there on the z-axis'))


#################### Task 2 ############################
    # Request for the cut-off value
# cut_off
cut_off= float(input('what is the cutoff value'))

#################### Task 3 ############################
    # Initialize counters

# n_active
n_active=0
# n_inactive
n_inactive=0

#################### Task 4 ############################
    # Loop through all blocks (nested loop)
for k in range(1, nz+1):
    # Initialize layer counter
    layer_active_count = 0
    # two nested loops go here
      for j in range(1,nj+1):
        for i in range(1,nx+1):
          perm = float(input(f'Enter permeability value for block ({i}, {j}, {k}): '))
   
            if perm_list< cut_off:
                n_active= n_active+ 1
            
            else:
                n_inactive= n_inactive + 1
                 layer_active= layer_active + 1
            

    # Print layer count
    print(f'Number of active gridblocks in layer {k}: {layer_active_count}')


#################### Task 5 ############################
    # Print overall counts
total_blocks = n_active + n_inactive
percentage_active = (n_active / total_blocks) * 100
print(percentage_active)

# Print 'active'
print(f'Total number of active gridblocks: {n_active}')

# Print 'inactive'
print(f'Total number of inactive gridblocks: {n_inactive}')

