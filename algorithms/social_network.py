# Name: Can Akkus
# Assignment 1: Social Network
# Description: Finds friend suggestions and shortest paths in a network.

print("Social Network Analysis")

# 1. LOAD THE NETWORK
# I am using a dictionary where Key = User, Value = Set of friends
# Using a Set makes checking connections much faster.
network = {}
file_name = "network.txt"

try:
    file = open(file_name, "r")
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        
        # Expected Format: "User: Friend1 Friend2"
        if ":" in line:
            parts = line.split(":")
            user = parts[0].strip()
            friends_string = parts[1].strip()
            
            # Make sure user is in the network dictionary
            if user not in network:
                network[user] = set()
            
            if len(friends_string) > 0:
                friends_list = friends_string.split()
                for friend in friends_list:
                    # Add friend to user
                    network[user].add(friend)
                    
                    # Mutual friendship (If A is friend of B, B is friend of A)
                    if friend not in network:
                        network[friend] = set()
                    network[friend].add(user)
                    
    file.close()
    print("File loaded successfully.\n")

    # 2. NETWORK STATISTICS
    total_users = len(network)
    total_connections = 0
    for user in network:
        total_connections += len(network[user])
    
    # Divide by 2 because connection is mutual (A-B and B-A is 1 friendship)
    print("Network Statistics:")
    print("Total users:", total_users)
    print("Total friendships:", total_connections // 2)
    print("")

    # 3. FRIEND SUGGESTIONS (Requirement: Rank by mutual friends)
    # Example Target: Finn
    target_user = "Finn"
    
    if target_user in network:
        print(f"Friend suggestions for {target_user}:")
        target_friends = network[target_user]
        suggestions = []

        for person in network:
            # Skip myself and people I am already friends with
            if person == target_user or person in target_friends:
                continue
            
            # Check mutual friends manually
            person_friends = network[person]
            mutuals = []
            
            for f in person_friends:
                if f in target_friends:
                    mutuals.append(f)
            
            # If they have mutual friends, add to suggestions list
            if len(mutuals) > 0:
                suggestions.append([person, len(mutuals), mutuals])
        
        # Sort by count (highest first) - Key requirement
        suggestions.sort(key=lambda x: x[1], reverse=True)
        
        # Print top 3 results
        count = 0
        for item in suggestions:
            if count >= 3: break
            name = item[0]
            num = item[1]
            # Join list into string for clean output
            mutual_names = ", ".join(item[2])
            print(f"{name} ({num} mutual friends: {mutual_names})")
            count += 1
    else:
        print(f"User {target_user} not found.")

    print("")

    # 4. SHORTEST PATH (Requirement: BFS Algorithm)
    # Example Path: Quinn -> Peter
    start_user = "Quinn"
    end_user = "Peter"
    
    print(f"Finding connection between {start_user} and {end_user}:")
    
    if start_user in network and end_user in network:
        # BFS is best for finding shortest path in unweighted graphs
        # Queue stores the path: [[Start], [Start, Next], ...]
        queue = []
        queue.append([start_user]) 
        
        visited = []
        visited.append(start_user)
        
        found_path = None
        
        while len(queue) > 0:
            current_path = queue.pop(0) # Get first item (FIFO)
            last_node = current_path[-1]
            
            if last_node == end_user:
                found_path = current_path
                break
            
            # Add neighbors to queue
            neighbors = network[last_node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        
        if found_path:
            path_str = " -> ".join(found_path)
            print("Shortest path:", path_str)
            print("Path length:", len(found_path) - 1, "connections")
        else:
            print("No connection found.")
    else:
        print("One of the users does not exist.")

except:
    print("Error: network.txt file not found.")