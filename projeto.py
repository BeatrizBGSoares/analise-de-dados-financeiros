import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Baixando dados do Yahoo Finance...")
    
    data = yf.download('AAPL', start='2018-01-01', end='2018-12-31')
    
    
    print("Colunas dos dados baixados:")
    print(data.columns)
    
    
    if 'Adj Close' in data.columns:
        print("Usando 'Adj Close' para calcular o retorno diário.")
        data['Daily Return'] = data['Adj Close'].pct_change()
    else:
        print("Coluna 'Adj Close' não encontrada, usando 'Close'.")
        data['Daily Return'] = data['Close'].pct_change()

   
    print("Dados baixados:")
    print(data.head())

    
    data['Daily Return'].plot(figsize=(10, 4))
    plt.title('Retorno diário da ação AAPL em 2018')
    plt.show()

if __name__ == "__main__":
    main()