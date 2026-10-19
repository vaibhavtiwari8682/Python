"""
slicing in python is used to extract a portion of string, list, tuple or any other sequence type. It is done by specifying the start and end index of the sequence. The syntax for slicing is as follows:
sequence[start:end:step]
start = the index of the first element to be included in the slice (inclusive)
end = the index of the first element to be excluded from the slice (exclusive)
step = the increment between elements in the slice (default is 1)
"""
text = "this is python the king of AI"
print(text[1:5:1]) 
print(text[1:8:2])#this is p