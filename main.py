import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_exchange_rates():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get("rates")
    else:
        messagebox.showerror("Error", "Could not retrieve exchange rates.")
        return None

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()

        if from_currency != 'USD':
            amount_in_usd = amount / exchange_rates[from_currency]
        else:
            amount_in_usd = amount

        converted_amount = amount_in_usd * exchange_rates[to_currency]
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

    except Exception as e:
        messagebox.showerror("Error", "Invalid input or currency selection")

root=tk.Tk()
root.title("Currency Converter")

exchange_rates = get_exchange_rates()

if exchange_rates:
    tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=10)
    from_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()), state="readonly")
    from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
    from_currency_combobox.set('USD')

    tk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=10)
    to_currency_combobox = ttk.Combobox(root, values = list(exchange_rates.keys()), state="readonly")
    to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
    to_currency_combobox.set('TRY')

    convert_button = tk.Button(root, text="Convert", command=convert_currency)
    convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    result_label=tk.Label(root, text="Converted Amount:")
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()