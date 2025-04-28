import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Style

init(autoreset=True)

def scan_port(ip, porta):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as meusocket:
            meusocket.settimeout(0.5)
            if meusocket.connect_ex((ip, porta)) == 0:
                try:
                    service = socket.getservbyport(porta)
                except:  
                    service = "Desconhecido"
                print(f"{Fore.GREEN}[+] Porta {porta} ({service}) [ABERTA] {Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED} [ERRO] Falha ao escanear porta {porta}: {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.YELLOW} === Port Scanner Iniciado === {Style.RESET_ALL}")


    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("--ip", required=True, help="IP address or hostname")
    parser.add_argument("--start-port", type=int, default=1, help="Start port")
    parser.add_argument("--end-port", type=int, default=65535, help="End port")
    args = parser.parse_args()

    with ThreadPoolExecutor(max_workers=100) as executor:
        for porta in range(args.start_port, args.end_port + 1):
            executor.submit(scan_port, args.ip, porta)


if __name__ == "__main__":
    main()