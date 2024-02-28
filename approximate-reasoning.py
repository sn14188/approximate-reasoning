import pandas as pd
import matplotlib.pyplot as plt

rs_df = pd.read_csv("rs_1.csv", header=None, names=["val"])

num_samples = 0
num_samples_accepted = 0
num_samples_rejected = 0

t_counts = 0
f_counts = 0

prob_1 = []
prob_2 = []

for val in rs_df["val"]:
    num_samples += 1
    if val != -1:
        num_samples_accepted += 1
        if val == 1:
            t_counts += 1
        elif val == 2:
            f_counts += 1
        else:
            raise ValueError

        t_prob = t_counts / num_samples_accepted
        f_prob = f_counts / num_samples_accepted
        assert t_prob + f_prob == 1

        prob_1.append(t_prob)
        prob_2.append(f_prob)
    else:
        num_samples_rejected += 1

assert num_samples_accepted + num_samples_rejected == len(rs_df)

prob_df = pd.DataFrame({
    "P(R = 1)": prob_1,
    "P(R = 2)": prob_2
})

print(prob_df.tail(1))

plt.title("Rejection Sampling")
plt.plot(prob_df["P(R = 1)"], label="P(Rain = T)")
plt.plot(prob_df["P(R = 2)"], label="P(Rain = F)")
plt.xscale("log")
plt.xlabel("N (logarithmic scale)")
plt.ylabel("Probabilities")
plt.legend()
plt.show()
