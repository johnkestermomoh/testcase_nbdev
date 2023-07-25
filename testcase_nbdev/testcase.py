# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['all', 'load_data', 'say_gday', 'add', 'draw_n', 'shopping']

# %% ../nbs/00_core.ipynb 4
def all(a, # Input array or object that can be converted to an array.
        axis:int|tuple|None=None, # Axis or axes along which a logical AND reduction is performed (default: all).
        out:np.ndarray|None=None, # Alternate output array in which to place the result.
        keepdims:bool=np._NoValue, # Leave reduced one-dimensional axes in the result?
        where=np._NoValue, # Elements to include in reduction. See `numpy.ufunc.reduce` for details. New in version 1.20.0.
        ) -> np.ndarray|bool: # A new boolean or array, or a reference to `out` if its specified.
    "Test whether all array elements along a given axis evaluate to `True`."
    

# %% ../nbs/00_core.ipynb 5
def load_data(
    data: str=None,   # data loaded and needed
    ):
    try:
        if os.path.isfile(data):
            df = pd.read_csv(data, engine='python')
            return df
    except Exception as e:
        logger.info(f'check that {data} exist in environment.yaml file {e}')     

# %% ../nbs/00_core.ipynb 8
def say_gday(
    greeting:str="G'day",  # Greeting to use
    strine:bool=True,      # Use incomprehensible Aussie accent?
    dropbears:bool=False): # Also warn about drop-bears?
    "Says g'day, the classic Aussie greeting"

# %% ../nbs/00_core.ipynb 9
def add(
    a:int, # the 1st number to add
    b=0,   # the 2nd number to add
)->int:    # the result of adding `a` to `b`
    "The sum of two numbers."
    return a+b

# %% ../nbs/00_core.ipynb 10
def draw_n(n:int, # Number of cards to draw
           replace:bool=True # Draw with replacement?
          )->list: # List of cards
    "Draw `n` cards."

# %% ../nbs/00_core.ipynb 12
class shopping:
    """
    class that prints what you have in the shopping basket
    """
    def __init__(self, cart: List):
        self.cart = cart
        print(self.cart)
    def shops(self):
        print(self.cart[0])
show_doc(shopping.shops)
