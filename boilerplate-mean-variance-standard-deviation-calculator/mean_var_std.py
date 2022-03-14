import numpy as np

def calculate(list):
    if len(list)!=9:
        # print("List must contain nine numbers.")
       raise ValueError("List must contain nine numbers.")

    
    list1= np.array(list)
    list1= list1.reshape((3,3))
    
    calculations= {
        'mean': [np.mean(list1, axis=0).tolist(), np.mean(list1, axis=1).tolist(), np.mean(list1).tolist()],
        'variance': [np.var(list1, axis=0).tolist(), np.var(list1, axis=1).tolist(), np.var(list1).tolist()],
        'standard deviation': [np.std(list1, axis=0).tolist(), np.std(list1, axis=1).tolist(), np.std(list1).tolist()],
        'max': [np.max(list1, axis=0).tolist(), np.max(list1, axis=1).tolist(), np.max(list1).tolist()],
        'min': [np.min(list1, axis=0).tolist(), np.min(list1, axis=1).tolist(), np.min(list1).tolist()],
        'sum': [np.sum(list1, axis=0).tolist(), np.sum(list1, axis=1).tolist(), np.sum(list1).tolist()]
        }
    return calculations