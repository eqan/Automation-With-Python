*** Settings ***
Documentation     Example robot that downloads a remote Excel file and opens it.
Library           RPA.Excel.Files
Library           RPA.HTTP

*** Tasks ***
Download an Excel file, open it, and close it
    Download    https://robotsparebinindustries.com/SalesData.xlsx    overwrite=True
    Open Workbook    Data.xlsx
    Close Workbook
