import matplotlib
matplotlib.use('Agg')  # 必须在最前面！解决云端机器人没有显示器的问题
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

def start_analysis():
    print("--- 风险分析系统启动 ---")
    
    ticker = "AAPL"
    print(f"正在从 Yahoo Finance 获取 {ticker} 的数据...")
    
    try:
        # 获取数据
        data = yf.download(ticker, period="1mo")
        
        # 1. 计算波动率
        returns = data['Close'].pct_change()
        volatility = returns.std()
        
        print(f"\n分析结果:")
        print(f"标的代码: {ticker}")
        print(f"过去一个月的日均波动率: {float(volatility):.4f}")

        # 2. 绘图代码必须放在这里（因为 data 在这里才有效）
        print("正在生成分析图表...")
        plt.figure(figsize=(10, 6))
        plt.plot(data['Close'])
        plt.title(f"{ticker} Stock Risk Analysis")
        plt.xlabel("Date")
        plt.ylabel("Price")
        
        # 保存图片到根目录
        plt.savefig('risk_report.png')
        print("--- 分析完成，结果已保存为 risk_report.png ---")
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    start_analysis()