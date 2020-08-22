import numpy as np
import pendulum as time
import sys
from PyQt5.QtWidgets import QApplication, QWidget
import pandas as pd
import win32com.client as win32


def DRIP(stock_price, num_shares, div_rate, div_period, future_growth_span):
    curr_val = num_shares * stock_price
    div_accum = 0
    year = 1
    if div_period == "m":
        div_period = 12
    else:
        div_period = 4

    while future_growth_span > 0:
        for accum in range(0, div_period):
            div_accum += (num_shares * div_rate)
            curr_val += (num_shares * div_rate)

            if div_accum >= stock_price:
                num_shares += (div_accum//stock_price)
                div_accum = (div_accum % stock_price)

        print("----------------------YEAR",
              year, "----------------------")
        print("Total value: ", curr_val)
        print("Div accumalator: ", div_accum)
        print("Total shares: ", num_shares)
        print("---------------------------------------------------")
        print("\n \n")
        year += 1

        future_growth_span -= 1


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    print("Hello World")
    w.show()

    sys.exit(app.exec_())


def func(*args, **kwargs):
    print(args)


if __name__ == "__main__":
    pass
#DRIP(15.72, 185, 0.12, "m", 5)
