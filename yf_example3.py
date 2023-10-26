""" yf_example3.py

The purpose of this module is to download stock price data for Qantas for a given year and save the information in a CSV file
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """
        Download Qantas stock prices for a given year into a CSV file
    """

    # To ensure it downloads only the prices from January 1 to December 31 of the year in year
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"

    # Download the data from 2020-01-01 to 2020-12-31 and tic='QAN.AX',
    df = yf_example2.yf_prc_to_csv('QAN.AX', start_date, end_date) #define df

    # Create the name of the output file. In this case, qan_prc_2020.csv.
    file = f"qan_prc_{year}.csv"

    # Create a path variable making sure that this file will be inside the datafolder.
    pth = os.path.join(cfg.DATADIR, file)

    # Save the downloaded data
    df.to_csv(pth)

if __name__ == "__main__":
    qan_prc_to_csv(2020)