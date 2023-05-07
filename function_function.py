from tqdm import tqdm
import time
from alive_progress import alive_bar


def test(data:list) -> int:
    '''이 곳에 재밌는 내용들을 넣을 수 있다 이말이야~'''
    answer = 0
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            answer += 1
    return answer


def elisa(data:int) -> None:
    '''난 당신의 행동패턴을 다 알고있지'''
    with alive_bar(data) as bar:
        for _ in range(data):
            time.sleep(.01)
            bar()
    print('파 악 완 료')
    
def tqdm_test(data:int) -> None:
    '''이건 tqdm이라는 모듈을 사용한거에요'''
    pbar = tqdm(range(data))
    for _ in pbar:
        time.sleep(0.01)
    print('Loaded')
    pbar.close()
