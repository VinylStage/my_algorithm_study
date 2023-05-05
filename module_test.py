from progressbar import ProgressBar
from alive_progress import alive_bar
from yaspin import yaspin
import time

# progress = ProgressBar()
# for i in progress(range(100)):
#     time.sleep(0.1)
    
with alive_bar(100) as bar:
    for i in range(100):
        time.sleep(0.1)
        bar()



# with yaspin(text="Loading..."):
#     time.sleep(3)
