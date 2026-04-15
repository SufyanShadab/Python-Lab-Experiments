import pandas as pd
import matplotlib.pyplot as plt

# data
Points = [140, 135, 100, 99, 125,90, 90,90,83,83]
Teams = ["Merc", "Ferrari", "Redbull", "Alpine", "McLaren", "Haas", "Audi", "Cadillac", "Williams","Aston Martin"]

# dataframe
df = pd.DataFrame({
    "Points": Points,
    "Teams": Teams
})

print(df)

# plotting
plt.figure()
plt.plot(Teams, Points)
plt.title("GoT")
plt.xlabel("Teams")
plt.ylabel("Points")
plt.show()