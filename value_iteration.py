from mdp import MDP
import sys

def value_iteration(mdp, n_iterations=10000, eps=1e-100):
    states = mdp.getStates()
    policy = {s: None for s in states}
    V_opt = {s: 0 for s in states}

    for _ in range(n_iterations):
        max_diff = 0.0

        for state in states:
            max_value = sys.float_info.min

            if not mdp.isEndState(state):
                action_vals = {a: 0 for a in mdp.getActions(state)}

                for action in mdp.getActions(state):
                    for sn, tp, rew in mdp.getSuccessorProbReward(state, action):
                        action_vals[action] += tp * (rew + mdp.getDiscount() * V_opt[sn])

                    if action_vals[action] > max_value:
                        max_value = action_vals[action]
                        policy[state] = action

            V_opt[state] = max_value
            max_diff = max(max_diff, abs(V_opt[state] - max_value))

        if max_diff <= eps:
            break

    return policy, V_opt

if __name__ == "__main__":
    mdp = MDP()
    policy, V_opt = value_iteration(mdp)
    print("Optimal Policy:", policy)
    print("Optimal Value:", V_opt)
