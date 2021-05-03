from tkinter import *
from PIL import ImageTk, Image
import yfinance as yf
import mplfinance as mpf

root = Tk()
root.title("Stock Valuation Bot")
#root.iconbitmap('/Users/a2b/Desktop/python_projects/stocktools/gui_stock_info/chart_charts_increase_arrow_business_icon_186855.png')
#root.iconbitmap(Image.open("/Users/a2b/Desktop/python_projects/stocktools/gui_stock_info/icon.ico"))

def get_current_price(tik):
	stock_data = tik.history(period='1d')
	return stock_data['Close'][0]

def display_chart(tckr,year):
	mpf.plot(df, type="candle", volume=True, mav=(20), tight_layout=True,
			 title=tckr, style="yahoo")


def myClick(tckr,year):

	try:
		tik = yf.Ticker(tckr)
		cmp = get_current_price(tik)
		Label(root, text="You just entered a ticker " + tckr).grid(row=2, column=1)
		Label(root, text="Stock is currently trading at: " + str(cmp)).grid(row=3, column=1)
		df = tik.history(period = "max")
		mpf.plot(df.loc[year], type = "candle", volume = True, tight_layout = True)

	except:
		Label(root, text="This Stock doesn't exist").grid(row=4, column=1)


# Add Label
mylabel = Label(root, text = "Enter the ticker:").grid(row = 0, column = 0)
year_sel = Label(root, text = "Select a year:").grid(row = 1, column = 0)

# Add Entry Box
entry = Entry(root)
entry.grid(row = 0, column  = 1)

# Add Dropdown Box
years = ["2015","2016","2017","2018","2019","2020"]
year = StringVar()
year.set(years[-1])
yr = OptionMenu(root, year, *years)
yr.grid(row = 1, column  = 1)

# Add Buttons
mybutton = Button(root, text = "Go!", command=lambda: myClick(str(entry.get()), str(year.get())),
				  height = 1, width = 5).grid(row = 2, column  = 0)
quitbutton = Button(root, text = "Quit", command = root.quit, height = 1, width = 5).grid(row = 3, column  = 0)



root.mainloop()