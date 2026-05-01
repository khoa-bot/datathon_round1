import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import svd
import os

class SSA:
    """
    Robust implementation of Singular Spectrum Analysis (SSA)
    """
    def __init__(self, tseries, L):
        """
        :param tseries: 1D array-like time series
        :param L: Window length (N/2 for maximum resolution)
        """
        self.tseries = np.array(tseries)
        self.N = len(self.tseries)
        self.L = L
        self.K = self.N - self.L + 1
        
        # Step 1: Embedding (Create the Trajectory Matrix)
        self.X = np.column_stack([self.tseries[i:i+self.L] for i in range(self.K)])

    def decompose(self):
        """
        Step 2: Singular Value Decomposition (SVD)
        """
        self.U, self.Sigma, self.VT = svd(self.X, full_matrices=False)
        
        # Calculate variance contributions of each component
        self.variance_explained = (self.Sigma ** 2) / np.sum(self.Sigma ** 2)
        self.cumulative_variance = np.cumsum(self.variance_explained)

    def get_components_for_variance(self, threshold=0.95):
        """
        Finds the number of components required to capture the specified variance threshold.
        """
        # np.argmax returns the first index where the condition is True
        k = np.argmax(self.cumulative_variance >= threshold) + 1
        return k

    def reconstruct(self, indices):
        """
        Step 3 & 4: Grouping and Diagonal Averaging
        :param indices: List of singular value indices to reconstruct the trend/cycle
        """
        # If the list is empty (e.g., component 0 alone captured >95%), return zeros
        if not indices:
            return np.zeros(self.N)

        # Grouping
        X_elem = np.zeros_like(self.X, dtype=float)
        for i in indices:
            X_elem += self.Sigma[i] * np.outer(self.U[:, i], self.VT[i, :])

        # Diagonal Averaging
        rec = np.zeros(self.N)
        rec_counts = np.zeros(self.N)
        for i in range(self.L):
            for j in range(self.K):
                rec[i+j] += X_elem[i, j]
                rec_counts[i+j] += 1
                
        return rec / rec_counts


def main():
    # 1. Read the dataset
    print("Loading sales.csv...")
    try:
        df = pd.read_csv('sales.csv', parse_dates=['Date'])
    except FileNotFoundError:
        print("Error: 'sales.csv' not found. Please ensure it's in the same directory.")
        return

    # Extract Revenue for SSA
    series = df['Revenue'].values
    dates = df['Date']

    # 2. Perform robust SSA
    # Set window length L to N/2 for maximum resolution in trend separation
    L = 365  # This is a common choice for daily data to capture yearly seasonality, but you can experiment with this value
    print(f"Executing SSA with window length L = {L}...")
    
    ssa = SSA(series, L)
    ssa.decompose()

    # Determine how many components are needed to reach 95% variance
    k = ssa.get_components_for_variance(0.95)  # You can adjust this threshold if you want to capture more/less variance
    print(f"Components needed to capture >= 95% variance: {k}")
    print(f"Actual variance captured by these {k} components: {ssa.cumulative_variance[k-1]*100:.4f}%")

    # Split the components:
    # Component 0 -> Linear Trend
    # Components 1 through k-1 -> Cyclic Trend
    linear_indices = [0]
    cyclic_indices = list(range(1, k))
    
    # Edge case: If Component 0 alone is >= 95%, cyclic_indices will be empty. 
    # To guarantee we extract a cyclic trend, we force component 1 into it.
    if not cyclic_indices:
        print("Note: Component 0 alone captures >= 95% variance. Forcing Component 1 into the Cyclic trend.")
        cyclic_indices = [1]
        k = 2

    print(f"Linear component index : {linear_indices}")
    print(f"Cyclic component indices: {cyclic_indices}")

    linear_trend = ssa.reconstruct(linear_indices)
    cyclic_trend = ssa.reconstruct(cyclic_indices)

    # 3. Create separated files
    df_linear = pd.DataFrame({'Date': dates, 'Linear_Trend': linear_trend})
    df_cyclic = pd.DataFrame({'Date': dates, 'Cyclic_Trend': cyclic_trend})

    df_linear.to_csv('linear.csv', index=False)
    df_cyclic.to_csv('cyclic.csv', index=False)
    print("Saved 'linear.csv' and 'cyclic.csv'.")

    # 4. Plot the data and save into figures
    if not os.path.exists('figs'):
        os.makedirs('figs')

    # Plot: Overall SSA Decomposition Comparison
    plt.figure(figsize=(12, 8))
    
    plt.subplot(3, 1, 1)
    plt.plot(dates, series, label='Original Revenue', color='black')
    plt.title('Original Time Series')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(dates, linear_trend, label='Linear Trend (Component 0)', color='red')
    plt.title('Linear/Base Trend')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(dates, cyclic_trend, label=f'Cyclic Trend (Components 1 to {k-1})', color='blue')
    plt.title('Cyclic Behavior (Remaining 95% Variance)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('figs/ssa_decomposition.png', dpi=300)
    plt.close()
    
    print("Saved plots in the 'figs' folder (figs/ssa_decomposition.png).")

if __name__ == "__main__":
    main()