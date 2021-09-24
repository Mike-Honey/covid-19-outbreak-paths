# %% [markdown]
import datetime
import numpy
import os
import pandas
import requests
import json
from selenium import webdriver
import shutil 
import time


# %% 
def processWebPage(driver, webpageURL, datadir, filename, table_instance, check_diff):

    driver.get(webpageURL)
    time.sleep(20)
    html_page_df = pandas.read_html(driver.page_source)
    print ( html_page_df )
    html_table_df = html_page_df[table_instance]
    print ( html_table_df )

    # strip unicode characters
    html_table_cols = html_table_df.select_dtypes(include=[numpy.object]).columns.tolist()
    html_table_df[html_table_cols] = html_table_df[html_table_cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    html_table_df = html_table_df.sort_values(by=html_table_cols)

    if check_diff:
        shutil.copy2(datadir + filename, datadir + str.replace(filename, ".xlsx", "_prior.xlsx"))
        input_xlsx_df = pandas.read_excel(datadir + filename)
        # print ( input_xlsx_df )

        diff_df = pandas.merge(input_xlsx_df, html_table_df, how='outer', indicator='Exist')

        diff_df = diff_df.loc[diff_df['Exist'] != 'both']
        diff_df['Exist'] = diff_df['Exist'].replace('left_only', 'old')
        diff_df['Exist'] = diff_df['Exist'].replace('right_only', 'new')
        diff_df = diff_df.sort_values(by=diff_df.columns.tolist())
        diff_file_name = datadir + str.replace(filename, '.xlsx', '_diff.xlsx')
        if len(diff_df.index) > 0:
            print(str(datetime.datetime.now()) + ' Differences found, wrote to file: ' + diff_file_name )
            diff_df.to_excel (diff_file_name, index=False)

    # write current data to excel file for next comparison run, also to timestamped file.
    html_table_df.to_excel (datadir + filename, index=False)
    html_table_df.to_excel (datadir + 'archive/' + str.replace(filename, '.xlsx', '_' + datetime.datetime.now().strftime('%y-%m-%d_%H_%M_%S') + '.xlsx'), index=False)

# %% 
def main():
    """
    Main - program execute
    """
    print (str(datetime.datetime.now()) + ' Starting ...')
    webpageURL = 'https://www.coronavirus.vic.gov.au/additional-covid-19-case-data'
    datadir = 'C:/Dev/covid-19-outbreak-paths/'
    check_diff = True

    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : r"C:\Dev\covid-19-genomes\vmt", 
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True}
    chromeOptions.add_experimental_option("prefs",prefs)
    chromedriver = "C:/Dev/ChromeDriver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

    filename = 'vic-key-outbreaks_0.xlsx'
    table_instance = 0
    processWebPage(driver, webpageURL, datadir, filename, table_instance, check_diff)

    driver.close()

    print (str(datetime.datetime.now()) + ' Finished!')
    exit()

if __name__ == '__main__':
    main()

# %%
