from policy_evaluation import policy_evaluation
from value_iteration import value_iteration
from mdp import MDP

if __name__ == "__main__":
    mdp = MDP()

    # Task 2: Policy Evaluation
    policy = {1: 'd', 2: 'd', 3: 'd', 4: 'r', 5: 'r', 6: 'd', 7: 'u', 8: 'r', 9: 'u'}
    V_opt = policy_evaluation(mdp, policy)
    print("Policy Value:", V_opt)

    # Task 3: Value Iteration
    policy, V_opt = value_iteration(mdp)
    print("Optimal Policy:", policy)
    print("Optimal Value:", V_opt)
