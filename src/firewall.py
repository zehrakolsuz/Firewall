import iptc

def allow_ssh():
    rule = iptc.Rule()
    rule.in_interface = "eth0"
    rule.protocol = "tcp"
    match = iptc.Match(rule, "tcp")
    match.dport = "22"
    rule.add_match(match)
    rule.target = iptc.Target(rule, "ACCEPT")
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)
    print("SSH trafiği kabul edildi.")

if __name__ == "__main__":
    allow_ssh()
