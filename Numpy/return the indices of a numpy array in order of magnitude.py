return the indices of a numpy array in order of magnitude.
def get_top_magnitude_indices(values):
   
    return  np.flip(np.argsort(np.abs(values)))
