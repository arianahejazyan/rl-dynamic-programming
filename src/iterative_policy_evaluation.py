import numpy as np
from tqdm import tqdm
from bellman_update import *

def iterative_policy_evaluation(env, policy, stochastic, theta=1e-6, gamma=1.0, max_iteration = 1000):
    
    num_states = env.observation_space.n
    V = np.zeros(num_states)

    iteration = 0
    with tqdm(desc="Policy Evaluation", unit="iter") as pbar:
        while iteration < max_iteration:
            delta = 0
            for state in range(num_states):
                v_old = V[state]
                v_new = bellman_update(env, policy, state, V, gamma, stochastic)
                V[state] = v_new
                delta = max(delta, abs(v_old - v_new))

            pbar.set_postfix({'delta': f"{delta:.2e}"})
            pbar.update(1)
            iteration += 1
            
            if delta < theta:
                break

    return V