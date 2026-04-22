import pandas as pd

# Your existing simulation logic here

def run_backtest(top_n):
    # Simulate the trading strategy and return results
    results = []  # Replace with actual results logic
    summary = pd.DataFrame()  # Replace with actual summary logic
    return results, summary

def main():
    top_n_values = [1, 3, 5, 10]
    for top_n in top_n_values:
        results, summary = run_backtest(top_n)
        results.to_csv(f'sim_trade_result_top{top_n}.csv')
        summary.to_csv(f'sim_trade_detail_top{top_n}.csv')
        print(f'Backtest for top-{top_n} completed.')

if __name__ == '__main__':
    main()