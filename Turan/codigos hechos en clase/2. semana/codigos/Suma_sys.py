import sys

if len(sys.argv) !=3:
    print ('error')
    exit(1)

numero1=int(sys.argv[1])
numero2=int(sys.argv[2])

print(numero1 + numero2)
