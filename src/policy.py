import numpy as np

def random_deterministic_policy(env):
    """
    Create a random deterministic policy
    """
    num_states = env.observation_space.n
    num_actions = env.action_space.n
    
    # Create random action selection for each state
    random_policy = np.random.randint(0, num_actions, size=num_states)
    
    def policy(state):
        return random_policy[state]
    
    return policy

def random_stochastic_policy(env):
    """
    Create a random stochastic policy
    """
    num_states = env.observation_space.n
    num_actions = env.action_space.n

    # Create random probability distributions for each state
    policy_dist = np.random.random((num_states, num_actions))
    policy_dist = policy_dist / policy_dist.sum(axis=1, keepdims=True)
    
    def policy(state, action):
        return policy_dist[state][action]
    
    return policy