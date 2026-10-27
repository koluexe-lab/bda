### Python Code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    'Age': [19, 22, 25, 28, 31, 35, 40, 45, 50, 55],
    'Annual Income': [15, 20, 25, 35, 40, 50, 60, 70, 80, 90],
    'Spending Score': [85, 78, 90, 65, 70, 55, 45, 40, 30, 25]
}

df = pd.DataFrame(data)

# Display dataset
print("Customer Demographic Dataset:")
print(df)

# Calculate correlation
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation.round(2))

# Scatter plots with trend lines
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

sns.regplot(data=df, x='Age', y='Spending Score',
            ax=axes[0], ci=None)
axes[0].set_title('Age vs Spending Score')

sns.regplot(data=df, x='Annual Income', y='Spending Score',
            ax=axes[1], ci=None)
axes[1].set_title('Income vs Spending Score')

sns.regplot(data=df, x='Age', y='Annual Income',
            ax=axes[2], ci=None)
axes[2].set_title('Age vs Annual Income')

plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm',
            vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()
```

Install libraries:

```bash
pip install pandas matplotlib seaborn
```

### R Code

```r
# Create dataset
df <- data.frame(
  Age = c(19, 22, 25, 28, 31, 35, 40, 45, 50, 55),
  Annual_Income = c(15, 20, 25, 35, 40, 50, 60, 70, 80, 90),
  Spending_Score = c(85, 78, 90, 65, 70, 55, 45, 40, 30, 25)
)

# Display dataset
print("Customer Demographic Dataset")
print(df)

# Calculate correlation matrix
correlation <- cor(df, method = "pearson")
print("Correlation Matrix")
print(round(correlation, 2))

# Scatter plots with trend lines
par(mfrow = c(1, 3))

plot(df$Age, df$Spending_Score,
     main = "Age vs Spending Score",
     xlab = "Age", ylab = "Spending Score",
     pch = 19, col = "blue")
abline(lm(Spending_Score ~ Age, data = df), lwd = 2)

plot(df$Annual_Income, df$Spending_Score,
     main = "Income vs Spending Score",
     xlab = "Annual Income", ylab = "Spending Score",
     pch = 19, col = "darkgreen")
abline(lm(Spending_Score ~ Annual_Income, data = df), lwd = 2)

plot(df$Age, df$Annual_Income,
     main = "Age vs Annual Income",
     xlab = "Age", ylab = "Annual Income",
     pch = 19, col = "red")
abline(lm(Annual_Income ~ Age, data = df), lwd = 2)

# Reset plot layout
par(mfrow = c(1, 1))

# Correlation heatmap
heatmap(correlation,
        Rowv = NA, Colv = NA,
        scale = "none",
        main = "Correlation Heatmap",
        margins = c(8, 8))
```








