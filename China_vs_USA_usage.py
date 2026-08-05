import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data estimated from OpenRouter and industry reports (2025-2026)
data = {
    "Date": [
        "Jan-2025",
        "Jun-2025",
        "Dec-2025",
        "Feb-2026",
        "Apr-2026",
        "Jun-2026",
        "Aug-2026",
    ],
    # Estimated weekly token volume in Trillions (T)
    "China_Volume_T": [0.1, 0.3, 2.5, 8.0, 15.0, 22.0, 28.1],
    "US_Volume_T": [4.5, 5.0, 6.5, 7.8, 7.5, 6.0, 4.4],
}

df = pd.DataFrame(data)

# Set the visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 7))

# Plotting
plt.plot(
    df["Date"],
    df["China_Volume_T"],
    marker="o",
    linewidth=3,
    color="#d62728",
    label="Chinese Models (DeepSeek, Qwen, etc.)",
)
plt.plot(
    df["Date"],
    df["US_Volume_T"],
    marker="o",
    linewidth=3,
    color="#1f77b4",
    label="US Models (OpenAI, Anthropic, etc.)",
)

# Annotate the plotted points
for i, row in df.iterrows():
    plt.annotate(
        f"{row['China_Volume_T']}",
        (row["Date"], row["China_Volume_T"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        color="#d62728",
    )
    plt.annotate(
        f"{row['US_Volume_T']}",
        (row["Date"], row["US_Volume_T"]),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=9,
        color="#1f77b4",
    )

# Highlighting the "Crossover Event"
plt.axvline(x="Feb-2026", color="gray", linestyle="--", alpha=0.6)
plt.text(
    "Feb-2026",
    10,
    '  The "Crossover"\n  (Low-cost models surge)',
    verticalalignment="center",
)

# Labels and Title
plt.title(
    "Weekly AI Token Volume: China vs. US (2025-2026)", fontsize=16, fontweight="bold"
)
plt.ylabel("Weekly Volume (Trillions of Tokens)", fontsize=12)
plt.xlabel("Timeline", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

import os

# Create assets folder if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Save the plot
plt.tight_layout()
plt.savefig("assets/tokens_plot.png", dpi=400)

# Show the plot
plt.show()
