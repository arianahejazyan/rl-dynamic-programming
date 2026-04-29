## Getting Started


Clone the repository:
```bash
git clone https://github.com/arianahejazyan/RL.git
```
Create and activate a virtual environment:
```bash
python3 -m venv venv
```
Install dependencies:
```bash
pip install -r requirements.txt
```
---

| **Algorithm** | **Type** | **Environment** | **Environment GIF** |
| ------------- |--------- | --------------- | ------------------- |
| [Policy Iteration](notebooks/dynamic_programming/policy_iteration.ipynb) | Value Based | **Taxi-v3**: Pick up and drop off passengers at the right location in a 5×5 grid world. | <img src="gif/Taxi.gif" alt="Policy Iteration" width="300"/> |
| [On-Policy First-Visit MC Control](notebooks/monte_carlo/on_policy_first_visit_mc_control.ipynb) | Monte Carlo | **FrozenLake-v1**: A grid-based environment where an elf must reach the present without falling into holes. | <img src="gif/FrozenLake.gif" alt="On-Policy First-Visit MC Control" width="300"/> |

## Credits
This work was inspired by the following repos: </br>
[1] https://github.com/habanoz/reinforcement-learning-an-introduction