# Future Proof With Python

## Files in this repository

The list_warmup.py ---Part A warmup that creates a fruits list and practices index access, append(),remove(), and len().The shopping_list.py--Part B interactive manager with a loop menu to add,remove,show,and done/quit shopping items.
List_report.py----Part C report that number the items list,counts names longer than 4 letters,and finds the longest name with loop.
-- Screenshots- A folder with screenshots of each program running and shwing required outputs.

### Why is it safer to check in before calling remove()?
In Python,list.remove(x) will crash with a ValueError if 'x' is not in the list,which stops the whole program.By first checking if itemin shopping_list, we make sure the item exists before trying to remove it.If it doesnot exist,we can instead print--That item is not on your list and the program continues running without crashing.