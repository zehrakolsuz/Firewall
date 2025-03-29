import subprocess

def save_rules():
    with open("/etc/iptables/rules.v4", "w") as f:
        subprocess.run(["iptables-save"], stdout=f)
    print("Kurallar kaydedildi.")
