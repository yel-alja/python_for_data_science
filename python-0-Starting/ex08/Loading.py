import sys
from tqdm import tqdm
import time
def ft_tqdm(lst:range):
    length = len(lst)
    for i in lst:
        yield i
        percentage = i / length * 100
        sys.stdout.write(f"\r {percentage:.1f}% [                   ]  {i} / {len(lst)}")