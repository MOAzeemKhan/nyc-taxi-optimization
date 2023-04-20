# NYC Taxi Transportation Optimization
![image](https://user-images.githubusercontent.com/102454617/233381160-fb86597a-b159-4b80-a8c2-9c244bee7e8b.png)

This project presents an optimization strategy for New York City taxis by considering historical data. The aim of the strategy is to increase the earnings of taxi drivers by allocating taxis depending on location and time so more passengers can be transported.

## Getting Started

This repository contains the code for the NYC Taxi Transportation Optimization Problem. To get started, clone the repository to your local machine.
```
git clone https://github.com/MOAzeemKhan/nyc-taxi-optimization.git
```
## Installation

First, install Python 3 on your machine. You can download it from the [official Python website](https://www.python.org/downloads/)

Next, install Jupyter Notebook. You can do this by running the following command:
```
pip install notebook
```
Next, install the required dependencies using this command:
```
pip install -r requirements.txt
```

## Dataset Details

The dataset used in this project is the New York City Taxi and Limousine Commission (TLC) Trip Record Data. The dataset provides information on taxi trips in New York City, including pickup and dropoff locations, trip distance, fare amount, and more. 
The data is available on the [TLC website](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## Flask Functionality

This project includes a Flask web application that allows users to upload their own CSV files of demand and cost matrix data. The web application uses the uploaded data to generate an optimized allocation of taxis based on the historical data.

To run the web application:
1) Clone this repository to your local machine
2) Run the command below to start the Flask application:
 ```
 python app.py
 ```
3) Navigate to http://localhost:5000/ in a web browser to use the application

### Requirements
The program requires two input excel files in order to function properly:

1) A [demand excel file](https://github.com/MOAzeemKhan/nyc-taxi-optimization/blob/main/Cost_Matrix_Supply_Demand_Only_.xlsx) containing the demand data with column headers "Pick up location" and "Demand".
2) A [cost excel file]()https://github.com/MOAzeemKhan/nyc-taxi-optimization/blob/main/Cost_Matrix_Only.xlsx containing the cost matrix with no column or row headers. The order of the rows and columns should correspond to the order of the supply nodes and demand nodes in the demand excel file.

## Contributors

This project was developed by:
1) [Mohammed Azeem Khan](https://www.linkedin.com/in/mohammed-azeem-khan/) 
2) [Harsh Ahire](https://www.linkedin.com/in/harsh-ahire-ba821122b/)
3) [Shwetha Iyer](https://www.linkedin.com/in/s-shwetha-iyer-5aa5791aa/)
4) [Rishabh Kinhikar](https://www.linkedin.com/in/rishabh-kinhikar-61130113a/)
5) [Daivik Jayan Mampally](https://www.linkedin.com/in/daivik-jayan-65ba57224/)
6) [Jhalak Mishra](https://www.linkedin.com/in/jhalak-mishra-94594525a/)

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:
1) Fork this repository to your account.
2) Create a branch for your changes.
3) Make your changes and commit them.
4) Push your changes to your fork.
5) Create a pull request to this repository.

## Files

The following files are available in a [Google Drive folder](https://drive.google.com/drive/folders/1tlOaI-7mzUxnzjBS_ftPhVkUDGYqoUK9?usp=sharing):

1) **Project Report** - a detailed report on the project
2) **Screenshot Of QM** - a screenshot of the optimization model created in QM software
3) **Profit and Cost Matrix** - an Excel file containing the profit and cost matrix data used in the optimization
4) **Excel Solving file** - an Excel file used to solve the optimization problem using the Solver add-in in Excel

Note that you will need to request access to the Google Drive folder to download these files.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/MOAzeemKhan/nyc-taxi-optimization/blob/main/License) file for details.
