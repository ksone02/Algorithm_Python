import sys
t = int(sys.stdin.readline())
 
for i in range(0, t):
  H, W, N = map(int, input().split())

  if H>=N:
    floor = N
    ho = 1
    print(f'{floor}0{ho}')
  else :
    floor = N%H    
 
    if floor==0:
      floor = H   
      ho = N//H      

      if ho >= 10:
        print(f'{floor}{ho}')
      else:
        print(f'{floor}0{ho}')
 
    else:
      ho = N//H

      if ho >= 9:
        print(f'{floor}{ho+1}')
      else:
        print(f'{floor}0{ho+1}')