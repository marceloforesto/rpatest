# Messer Selection Process (RPA Jr)
The proposed solution aims to facilitate the process of cost analysis and formulation of purchase bags, using CSV files.
### How it works

  - Input: A directory with several CSV files
  - Output: A single CSV file with all the data present from the input files
  - The program contains a simple graphic interface
  - A button to select the directory of CSV files
  - A button to select the directory that the final CSV file will be saved
  - A field to type the name of the final CSV file
  - A button to start the process
  - At the end of the CSV file created, a list of all products, prices and available quantity from all suppliers

Adopted Conventions:
  - All incoming CSV files must be in the same directory.
  - The file name is used to detect which supplier is
  - Each CSV file must have three columns, in the following order: Product Name, Available Quantity and Product Value
  - The first line of each CSV file must be a header
### Requerements
  - Python 3
  - Tkinter
```sh
$ sudo apt install python-tk
```
### How to run
```sh
$ python3 solution.py
```
### Flowchart
![GitHub Logo](/flow.png)

### Architecture
![GitHub Logo](/arc.png)

### Testing the application

To test the application, three CSV files were created, following the specifications described.
Select the docs folder and run the program to perform the test.

### Error handling

The following error cases have been handled:
  - Directory without incoming CSV files
  - Invalid directory to save CSV file
  - Invalid CSV file name
