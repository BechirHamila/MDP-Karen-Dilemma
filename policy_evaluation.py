from mdp import MDP

def policy_evaluation(mdp, policy, n_iterations=400):
    states = mdp.getStates()
    V_opt = {s: 0 for s in states}

    for _ in range(n_iterations):
        for state in states:
            newV = 0.0
            if not mdp.isEndState(state):
                a = policy[state]
                for sn, tp, rew in mdp.getSuccessorProbReward(state, a):
                    newV += tp * (rew + mdp.getDiscount() * V_opt[sn])
            V_opt[state] = newV

    return V_opt

if __name__ == "__main__":
    mdp = MDP()
    policy = {1: 'd', 2: 'd', 3: 'd', 4: 'r', 5: 'r', 6: 'd', 7: 'u', 8: 'r', 9: 'u'}
    V_opt = policy_evaluation(mdp, policy)
    print("Policy Value:", V_opt)
