```python
# Import necessary libraries
from tkinter import *
import json

class ICPDefinitionInterface:
    def __init__(self, master):
        self.master = master
        master.title("ICP Definition Interface")

        # Define labels
        self.label1 = Label(master, text="Ideal Customer Profile (ICP) Definition")
        self.label2 = Label(master, text="Enter the characteristics of your ideal customer:")

        # Define text entry field
        self.entry = Text(master)

        # Define buttons
        self.save_button = Button(master, text="Save ICP", command=self.save_icp)
        self.clear_button = Button(master, text="Clear", command=self.clear_text)

        # Layout
        self.label1.pack()
        self.label2.pack()
        self.entry.pack()
        self.save_button.pack()
        self.clear_button.pack()

    def save_icp(self):
        # Get text from entry field
        icp_text = self.entry.get("1.0", 'end-1c')

        # Convert text to dictionary
        icp_dict = json.loads(icp_text)

        # Save dictionary to a json file
        with open('icp.json', 'w') as f:
            json.dump(icp_dict, f)

        print("ICP saved successfully!")

    def clear_text(self):
        # Clear the text entry field
        self.entry.delete("1.0", END)

# Create a window
root = Tk()

# Create an instance of the ICPDefinitionInterface class
my_gui = ICPDefinitionInterface(root)

# Start the main loop
root.mainloop()
```
