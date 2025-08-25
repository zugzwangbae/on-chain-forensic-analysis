# 🕵️ On-Chain Forensic Analysis: The FTT Post-Collapse Liquidation

A detailed forensic investigation into the on-chain movements and market impact of FTX Token (FTT) following the FTX bankruptcy announcement in November 2022. This project traces the liquidation of massive FTT holdings by a known entity and analyzes the subsequent market manipulation patterns on decentralized exchanges.

## 🎯 Objective

To demonstrate the process of blockchain forensic analysis by:
1.  **Identifying** the key wallets involved in the movement of large FTT sums.
2.  **Tracing** the flow of funds from these wallets to decentralized exchanges (DEXs).
3.  **Analyzing** the market impact of these trades and identifying potential manipulation techniques like wash trading or spoofing on DEX order books.
4.  **Visualizing** the entire narrative with clear, professional charts and graphs.

## 📁 Project Structure

| File | Description |
| :--- | :--- |
| `notebooks/1_ftt_whale_wallet_tracing.ipynb` | Notebook focusing on identifying and tracing the source of FTT sell-offs. |
| `notebooks/2_ftt_market_impact_analysis.ipynb` | Notebook analyzing the price impact and trading patterns on DEXs. |
| `src/data_fetcher.py` | Modular utility functions for fetching data from Etherscan, Dune Analytics, and The Graph. |
| `src/visualizer.py` | Modular utility functions for creating standardized, publication-quality visualizations. |

## 🛠️ Tech Stack

- **Data Analysis:** `Python`, `Pandas`, `NumPy`
- **Blockchain Interaction:** `Web3.py`, `Etherscan API`, `The Graph Protocol`
- **Visualization:** `Matplotlib`, `Seaborn`
- **Environment:** `Jupyter Notebook`, `Poetry` (for dependency management)

## 🚀 Getting Started

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/yourusername/on-chain-forensic-analysis.git
    cd on-chain-forensic-analysis
    ```

2.  **Install dependencies** (using Poetry is recommended):
    ```bash
    poetry install
    ```
    *Alternatively, use pip:*
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```ini
    ETHERSCAN_API_KEY=YourApiKeyToken
    ```

4.  **Run Jupyter Lab:**
    ```bash
    poetry run jupyter lab
    # or
    jupyter lab
    ```

## 📊 Example Findings

*(We will add a small screenshot of a key chart here later, e.g., a price vs. sell volume over time plot)*

![Price Impact Analysis](images/price_impact.png) *Example: FTT price vs. large sell volumes on Uniswap.*

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Author

**Daniel Fortuna** - [LinkedIn](https://www.linkedin.com/in/daniel-fortuna-79b6b5193) | [GitHub](https://github.com/yourusername)

## ⚠️ Disclaimer

This project is for **educational and demonstration purposes only**. The findings are based on public on-chain data and should not be considered financial or investment advice.
