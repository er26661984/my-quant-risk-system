import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def start_analysis():
    print("--- 风险分析系统启动 ---")
    
    # 1. 获取苹果公司(AAPL)的数据
    ticker = "AAPL"
    print(f"正在从 Yahoo Finance 获取 {ticker} 的数据...")
    
    try:
        data = yf.download(ticker, period="1mo")
        
        # 2. 计算每日收益率
        # 我们取 'Close' (收盘价) 这一列来计算
        returns = data['Close'].pct_change()
        
        # 3. 计算标准差（波动率）
        # .std() 算出来是一个数，但我们需要确保它是 Python 的浮点数格式
        volatility = returns.std()
        
        print(f"\n分析结果:")
        print(f"标的代码: {ticker}")
        # 修改这里：确保取到一个具体的数值
        print(f"过去一个月的日均波动率: {float(volatility):.4f}") 
        print("--- 分析完成 ---")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    start_analysis()



# ... 你的量化计算代码 ...

plt.plot(data['Close'])
plt.title("Stock Risk Analysis")

# 关键一步：把图片保存在项目根目录下
plt.savefig('risk_report.png')