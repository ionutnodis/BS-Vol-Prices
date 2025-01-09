

""""
Black Scholes Merton Option Pricing Model for European Call Options using 3D Surface Plot in Streamlit

"""

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm
import streamlit as st

# Define the Black-Scholes Function
def black_scholes_merton(S, K, T, r, sigma):
    """
    Calculate European Call Option prices using Black-Scholes-Merton formula.

The function takes the following input Parameters:

        S (float): Spot price of the underlying asset
        K (float): Strike price 
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate (annualized)
        sigma (float): Volatility of the underlying asset (annualized)

    And outputs the price of an European Call Option according to the Black-Scholes-Merton Model.
    
    """
    
    # We compute d1 and d2 
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

# We then compute the call price using the Black Scholes Merton formula
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# We construct an interface using Streamlit to interact with the model and visualize the 3D surface plot

def main():
    st.title("Black-Scholes Option Pricing Model")

    # User Inputs for Model Parameters
    st.sidebar.header("Model Parameters")
    K = st.sidebar.number_input("Strike Price (K)", value=100.0, step=1.0)
    T = st.sidebar.number_input("Time to Maturity (T in years)", value=1.0, step=0.1)
    r = st.sidebar.number_input("Risk-Free Rate (r in %)", value=5.0, step=0.1) / 100
    vol_min = st.sidebar.slider("Minimum Volatility (σ)", min_value=0.01, max_value=1.0, value=0.01)
    vol_max = st.sidebar.slider("Maximum Volatility (σ)", min_value=0.01, max_value=1.0, value=1.0)
    spot_min = st.sidebar.slider("Minimum Spot Price (S)", min_value=10, max_value=200, value=50)
    spot_max = st.sidebar.slider("Maximum Spot Price (S)", min_value=10, max_value=200, value=150)

    # Create grid for spot prices and volatilities
    volatilities = np.linspace(vol_min, vol_max, 50)
    spot_prices = np.linspace(spot_min, spot_max, 50)
    S, Sigma = np.meshgrid(spot_prices, volatilities)

    # Calculate the call option prices
    call_prices = np.zeros_like(S)
    for i in range(S.shape[0]):
        for j in range(S.shape[1]):
            call_prices[i, j] = black_scholes_merton(S[i, j], K, T, r, Sigma[i, j])

    # Plot the 3D surface
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(S, Sigma, call_prices, cmap='viridis', edgecolor='none')

    ax.set_xlabel('Spot Price (S)')
    ax.set_ylabel('Volatility (σ)')
    ax.set_zlabel('Call Price')
    ax.set_title('Black-Scholes Call Option Price Surface')
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

    # Display the plot 
    st.pyplot(fig)

if __name__ == "__main__":
    main()