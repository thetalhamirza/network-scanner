import sys
import port_scanner
import os_recon


def main():
    if len(sys.argv) != 4:
        print("Usage: python netscan.py <subnet> <mask> [threads]")
        sys.exit(1)

    subnet = sys.argv[1]
    mask = int(sys.argv[2])
    threads = int(sys.argv[3])
        
    live_hosts = port_scanner.ping_sweep(subnet, str(mask), threads)
    print("[>] Ping sweep completed...\n")

    for host in live_hosts:
        open_ports = port_scanner.port_scan(host, list(range(1, 1024), threads))
        print(f"Open ports on host {host}: {open_ports}\n")

        for port in open_ports:
            host_infos = os_recon.scan_host(host, str(port))
            
            for host_info in host_infos:
                os_recon.output_to_csv("scan_results.csv", host_info)
                print("\nScan results:")
                for k, v in host_info.items():
                    print(f"{k}: {v}")
                

                print()




if __name__=="__main__":
    main()