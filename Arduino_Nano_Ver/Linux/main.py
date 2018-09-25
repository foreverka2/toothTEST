import process
import time

def main():
    print "Code start!"
    while True :
        R0_data1, R0_data2, R0_data3, R0_data4 = process.SetR0()
        if R0_data1 != -1 :
            break
    while True :    
        process.Cloud(R0_data1, R0_data2, R0_data3, R0_data4)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
