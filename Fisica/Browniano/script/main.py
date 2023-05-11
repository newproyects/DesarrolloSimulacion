import argparse
from configparser import ConfigParser
import simulation
import export

def arg():
    pars=argparse.ArgumentParser()
    pars.add_argument('--inpf',default='null',help='Especifique nombre y extensión del archivo de entrada')
    pars.add_argument('--outf',default='null',help='Especifique nombre y extensión del archivo de salida')
    args=pars.parse_args()

    return (args.inpf,args.outf)

    
def main():
    inpf,outf=arg()
    
    conf=ConfigParser()
    if conf.read(inpf)==[]:
        print(f'Archivo no encontrado: {inpf}')
        exit()

    print(f"\nNombre: {conf.get('meta-data','name')}\n")
    
    print("Parametros Físicos:")
    print(f"C = {conf.get('physical-parameters','C')} [kg/s]")
    print(f"k = {conf.get('physical-parameters','k')} [J/K]")
    print(f"T = {conf.get('physical-parameters','T')} [K]")
    print(f"M = {conf.get('physical-parameters','M')} [kg]")
    print(f"R = {conf.get('physical-parameters','R')}\n")
    
    print("Parametros Computacionales:")
    print(f"h = {conf.get('computational-parameters','h')}")
    print(f"n = {conf.get('computational-parameters','n')}")
    print(f"m = {conf.get('computational-parameters','m')}")

    
    C=float(conf.get('physical-parameters','C'))
    k=float(conf.get('physical-parameters','k'))
    T=float(conf.get('physical-parameters','T'))
    M=float(conf.get('physical-parameters','M'))
    R=int(conf.get('physical-parameters','R'))
    h=float(conf.get('computational-parameters','h'))
    n=int(conf.get('computational-parameters','n'))
    m=int(conf.get('computational-parameters','m'))

    if R<1 or R>3:
        print('Dimensionalidad incorrecta')
        exit()

    data=simulation.simul(C,k,T,R,M,h,n,m)

    if R==1:
        export.export1D(data,m,h,outf)
    elif R==2:
        export.export2D(data,m,h,outf)
    elif R==3:
        export.export3D(data,m,h,outf)
    
    print("------------------------------------finish------------------------------------")


if __name__=='__main__':
    main()
