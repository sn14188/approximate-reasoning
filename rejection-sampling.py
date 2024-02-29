import pandas as pd
import matplotlib.pyplot as plt

REJECTED = -1

def rejection_sampling():
    rs_df = pd.read_csv("rs_1.csv", header=None, names=["result"])
    num_samples, num_samples_accepted, num_samples_rejected = 0, 0, 0
    val_1_counter, val_2_counter = 0, 0
    probs_1, probs_2 = [], []
    upper_confidence_bounds, lower_confidence_bounds = [], []

    for result in rs_df["result"]:
        num_samples += 1
        if result != REJECTED:
            num_samples_accepted += 1
            if result == 1:
                val_1_counter += 1
            elif result == 2:
                val_2_counter += 1
            else:
                raise ValueError("")
            prob_1 = val_1_counter / num_samples_accepted
            prob_2 = val_2_counter / num_samples_accepted
            probs_1.append(prob_1)
            probs_2.append(prob_2)
            epsilon = 1.3581 / num_samples_accepted ** (1 / 2)
            upper_confidence_bounds.append(min(1, prob_1 + epsilon))
            lower_confidence_bounds.append(max(0, prob_1 - epsilon))
        else:
            num_samples_rejected += 1

    assert num_samples_accepted + num_samples_rejected == len(rs_df)
    print(f"accepted samples: n = {num_samples_accepted} out of N = {len(rs_df)}")

    prob_df = pd.DataFrame({"P(R = 1)": probs_1, "P(R = 2)": probs_2})
    print("approximation: ")
    print(prob_df.tail(1))

    plt.title("Rejection Sampling")
    plt.plot(prob_df["P(R = 1)"], label="P(R = T)")
    plt.xscale("log")
    plt.xlabel("N (logarithmic scale)")
    plt.ylabel("Probability and confidence bounds")
    plt.fill_between(range(num_samples_accepted), lower_confidence_bounds, upper_confidence_bounds, alpha=0.2)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    rejection_sampling()
