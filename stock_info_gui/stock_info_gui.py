from tkinter import *
from PIL import ImageTk, Image
import yfinance as yf

root = Tk()
root.title("Stock Valuation Bot")
#root.iconbitmap('/Users/a2b/Desktop/python_projects/stocktools/gui_stock_info/chart_charts_increase_arrow_business_icon_186855.png')
root.iconbitmap(Image.open("/Users/a2b/Desktop/python_projects/stocktools/gui_stock_info/icon.ico"))


# Add Image
#img = ImageTk.PhotoImage(Image.open("/Users/a2b/Desktop/python_projects/stocktools/gui_stock_info/icon.ico"))
#lab = Label(image = img).grid(row = 3, column  = 0)

entry = Entry(root)
entry.grid(row = 0, column  = 1)


def get_current_price(tik):
	stock_data = tik.history(period='1d')
	return stock_data['Close'][0]

def myClick(tckr):

	try:
		tik = yf.Ticker(tckr)
		cmp = get_current_price(tik)
		print(cmp)
		Label(root, text="You just entered a ticker " + tckr).grid(row=2, column=1)
		Label(root, text="Stock is currently trading at: " + str(cmp)).grid(row=3, column=1)
	except:
		Label(root, text="This Stock doesn't exist").grid(row=4, column=1)



mylabel = Label(root, text = "Enter the ticker:").grid(row = 0, column = 0)


mybutton = Button(root, text = "Go!", command=lambda: myClick(str(entry.get()))).grid(row = 1, column  = 0)
quitbutton = Button(root, text = "Quit", command = root.quit).grid(row = 1, column  = 1)

root.mainloop()