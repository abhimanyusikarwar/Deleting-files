import time
import os
import shutil




path='C:/Users/Abhimanyu/Downloads/project-99'
days = time.time()
os.path.join('C:/Users/Abhimanyu/Downloads/p5.play-boilerplate-master')
st_ctime=os.stat(path)
ctime=os.stat(path).st_ctime
shutil.rmtree('C:/Users/Abhimanyu/Downloads/p5.play-boilerplate-master')



print(ctime)
if os.path.exists:
       print('not found')
