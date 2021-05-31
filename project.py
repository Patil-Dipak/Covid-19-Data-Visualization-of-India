import pandas as pd 
from matplotlib import pyplot as plt
import matplotlib.animation as animation
"""
This program draw a graph with the help of csv file
"""
#Path of CSV file 
PATH = "India_daily_cases_data.csv"

def get_data(m):
    """
    Read the data of csv file by object of pandas (class 'pandas.core.frame.DataFrame'>
    and return the value by it's name
    """
    m['Date'] = pd.to_datetime(m['Date']) #convert int datetime of pandas
   
   #store the data into variables of type <class 'pandas.core.series.Series'> and return it
    date = m["Date"]
    daily_cases = m['Daily Confirmed']
    total_cases = m['Total Confirmed']
    daily_recoverd = m['Daily Recovered']
    total_recoverd = m['Total Recovered']
    daily_death = m['Daily Deceased']
    total_death = m['Total Deceased']

    return date, daily_cases, total_cases,daily_recoverd,total_recoverd,daily_death,total_death

def draw_plot(date, cases, recoverd, death):
    """
    Get the variables of type <class 'pandas.core.series.Series'> and plot the graph using matplotlib
    and draw the plot
    """
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    # With help of Animate function we animate the graph using matplotlib.animation
    def animate(i):
        ax1.clear()
        ax1.plot( date[:i],cases[:i], label = cases.name,  color = 'blue', linewidth = 3)
        ax1.plot( date[:i], recoverd[:i], label = recoverd.name, color = "green", linewidth = 3)
        ax1.plot( date[:i], death[:i], label = death.name, color = "red",linewidth = 3)
        plt.title("India Covid-19 Cases Data (30-Jan-2020 to 26-May-2021)")
        plt.xlabel("Date")
        plt.ylabel("Cases")
        ax1.legend(loc = 'upper left')
    
    #Start the animation 
    start = animation.FuncAnimation(fig, animate, frames = 500, repeat = False)
    plt.show() 
  
    



    
def main():
    df = pd.read_csv(PATH) #Read the data of csv file using pandas 
    Date,Daily_cases, Total_cases, Daily_recoverd, Total_recoverd, Daily_death, Total_death = get_data(df)
    draw_plot(Date,Daily_cases,Daily_recoverd,Daily_death)
    draw_plot(Date,Total_cases,Total_recoverd,Total_death )
    
    

if __name__ == "__main__":
    main()