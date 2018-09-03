import process
import time

def main():
    print ("Code start!")
    while True :    
        process.Cloud()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
