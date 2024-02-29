import pandas as pd
import matplotlib.pyplot as plt

def likelihood_weighting():
    lw_df = pd.read_csv("lw_1.csv", header=None, names=["result", "weight"])
    # print(lw_df["result"].value_counts())
    # print(lw_df["weight"].value_counts())
    num_samples = 0
    val_1_weight, val_2_weight, total_weight = 0, 0, 0
    probs_1, probs_2 = [], []

    for index, row in lw_df.iterrows():
        num_samples += 1
        result = row["result"]
        weight = row["weight"]
        total_weight += weight
        if result == 1:
            val_1_weight += weight
        elif result == 2:
            val_2_weight += weight
        else:
            raise ValueError("")
        prob_1 = val_1_weight / total_weight
        prob_2 = val_2_weight / total_weight
        probs_1.append(prob_1)
        probs_2.append(prob_2)

    assert num_samples == len(lw_df)
    prob_df = pd.DataFrame({"P(R = 1)": probs_1, "P(R = 2)": probs_2})
    print("approximation: ")
    print(prob_df.tail(1))

    plt.title("Likelihood Weighting")
    plt.plot(prob_df["P(R = 1)"], label="P(R = T)")
    plt.xscale("log")
    plt.xlabel("N (logarithmic scale)")
    plt.ylabel("Probability")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    likelihood_weighting()
