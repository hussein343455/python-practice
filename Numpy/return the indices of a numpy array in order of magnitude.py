return the indices of a numpy array in order of magnitude.
def get_top_magnitude_indices(values):
    """
    Helper function for get_top_covariances to get indices by magnitude. 
    Parameter: values, a list of values as a numpy array of shape (n_values)
    Returns: numpy array of indices sorted from greatest to least by the magnitudes of their corresponding values
    """
    return  np.flip(np.argsort(np.abs(values)))
