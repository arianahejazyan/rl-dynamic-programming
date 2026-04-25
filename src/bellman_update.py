def bellman_update_deterministic(env, policy, state, V, gamma):

    action = policy(state)
    new_v = 0

    for prob, new_state, reward, done in env.P[state][action]:
        new_v += prob * (reward + gamma * V[new_state])

    return new_v

def bellman_update_stochastic(env, policy, state, V, gamma):

    num_actions = env.action_space.n
    new_v = 0

    for action in range(num_actions):
        pi_action = policy(state, action)

        action_value = 0
        for prob, new_state, reward, done in env.P[state][action]:
            action_value += prob * (reward + gamma * V[new_state])

        new_v += pi_action * action_value 

    return new_v

def bellman_update(env, policy, state, V, gamma, stochastic):
    if (stochastic):
        return bellman_update_stochastic(env, policy, state, V, gamma)
    else:
        return bellman_update_deterministic(env, policy, state, V, gamma)