def make_readable(seconds):
      HH = seconds//3600
      mm = (seconds%3600)//60
      ss = (seconds%3600)%60
      result =  str('{:02d}:{:02d}:{:02d}'.format(HH,mm,ss))
      return result