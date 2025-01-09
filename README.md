# Black-Scholes-Merton Option Pricing Model for European Call Options

This project implements the **Black-Scholes-Merton Option Pricing Model** to price **European Call Options**. The application uses **Streamlit** to provide an interactive interface, allowing users to adjust input parameters and visualize the results as a **3D surface plot**. 

The plot shows the relationship between **Spot Price (S)**, **Volatility (σ)**, and the calculated **Call Option Prices**.

---

## Features

- **Black-Scholes-Merton Model**:
  - Computes European Call Option prices based on user-defined parameters:
    - Spot Price (`S`)
    - Strike Price (`K`)
    - Time to Maturity (`T`)
    - Risk-Free Rate (`r`)
    - Volatility (`σ`)

- **Interactive User Interface**:
  - Adjust input parameters in real time using sliders and input fields.
  - Visualize the resulting Call Option prices dynamically.

- **3D Surface Visualization**:
  - The x-axis represents the Spot Price (`S`).
  - The y-axis represents the Volatility (`σ`).
  - The z-axis represents the calculated Call Option Prices.

---

## Installation

### Prerequisites
Ensure you have Python 3.7 or later installed along with the following libraries:

- `numpy`
- `matplotlib`
- `scipy`
- `streamlit`

### Steps

1. Clone this repository:
   ```bash
   git clone <[repository_url](https://github.com/ionutnodis/BS-Vol-Prices/tree/main)>
2. Navigate the project directory
   ```bash
   cd <project_directory>

3. Install required libraries:
   ``` bash
   pip install -r requirements.txt

4. Run the Streamlit app:
   ```bash
   streamlit run bs-vol-prices.py


5. Open the provided URL (default: http://localhost:8501) in your browser.


# Usage 

1. Start the app
   * Run the streamlit app using the command
        ```bash
     streamlit run bs-vol-prices.py

2. Input parameters:
   Use the sidebar to input the following parameters:
   * Strike Price (K): Strike price of the option
   * Time to Maturity (T-t): Time remaining until the option expires (input is years, if T-t < 1 year, use 0.5 for 6 months and so on)
   * Risk-Free Rate (r): The risk free interest rate (APR)
   * Volatility ($\sigma$): Choose the minimum and maximum volatility ranges that you are interested in
   * Spot price (S): Minimum and maximum spot prices
  
3. View the results:
   The app generates a 3D surface plot with the following axis:
   * x-axis: Spot price (S)
   * y-axis: Volatility ($\sigma$)
   * z-axis: Call price of the European option
  
4. Analyze the surface:
   Adjust the input parameters to observe how changes in Spot price (S), Volatility ($\sigma$), Time to Maturity (T-t), and Risk-Free rate (r) affect the price of an European call option


# Example Output

We input the following parameters: 
* Strike price (K) = 100
* Time to Maturity (T-t) = 1 year
* Risk-Free rate (r) = 5%
* Volatility ($\sigma$) = 10% - 100%
* Spot Price (S) = 50 - 150

The app outputs a 3D surface plot that shows different prices for the European Call Option for different volatility ranges and spot prices of the underlying asset. 

# Code Overview 

## The Black Scholes Merton equation for a European Call Option 
The Black-Scholes formula for the price of a European call option is given by:

$$
C = S_0 \Phi(d_1) - K e^{-rT} \Phi(d_2)
$$

where:

$$
d_1 = \frac{\ln\left(\frac{S_0}{K}\right) + \left(r + \frac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T}
$$

### Parameters:
- (C): Price of the call option  
- ($S_0$): Current stock price  
- (K): Strike price  
- (r): Risk-free interest rate  
- ($\sigma$): Volatility of the stock  
- (T): Time to maturity  
- ($\Phi$): Cumulative distribution function of the standard normal distribution

The main function in our code is thus the above equation. First, the function takes as input the 5 parameters described above, next it computes $d1$ and $d2$ and returns the call price using the Black-Scholes-Merton equation. 
 ```bash
          def black_scholes_merton(S, K, T, r, sigma):
          d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
          d2 = d1 - sigma * np.sqrt(T)
          call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
          return call_price
````

# References 
Hull, J. C. (2021). *Options, Futures, and Other Derivatives* (11th ed.). Pearson.


# License 
This project is licensed under the MIT License. See the LICENSE file for details.

# Author 
Developed by Ionut Catalin Nodis. If you have any questions or suggestions, feel free to reach out! 
