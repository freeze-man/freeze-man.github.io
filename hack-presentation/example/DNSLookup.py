# Import libraries
import dns.resolver

"""
It is fundamental type of DNS record,
here A stands for address. It shows the IP address of the domain
"""
result = dns.resolver.resolve('google.com', 'A')

# Printing record
for val in result:
    print('A Record : ', val.to_text())
"""
A Record :  34.218.62.116
"""
"""
This is an IP address record, used to find the IP
of the computer connected to the domain. It is conceptually
similar to A record but specifies only the IPv6 address of
the server rather than IPv4
"""
# Finding AAAA record IP.V6
try:
    result = dns.resolver.resolve('google.com', 'AAAA')

    # Printing record
    for val in result:
        print('AAAA Record : ', ipval.to_text())
except dns.resolver.NoAnswer:
    print("No Record AAAA")
"""
PTR stands for pointer record, used to translate
IP addresses to the domain name or hostname.
It is used to reverse the DNS lookup
"""
try:
    # Finding PTR record
    result = dns.resolver.resolve('google.com', 'PTR')

    # Printing record
    for val in result:
        print('PTR Record : ', val.to_text())
except dns.resolver.NoAnswer:
    print("No Record PTR")
"""
PTR Record :  ec2-34-218-62-116.us-west-2.compute.amazonaws.com.
"""
"""
Nameserver(NS) record gives information that which server
is authoritative for the given domain i.e. which server has
the actual DNS records. Multiple NS records are possible
for a domain including the primary and the backup name servers.
"""
# Finding NS record
result = dns.resolver.resolve('google.com', 'NS')

# Printing record
for val in result:
    print('NS Record : ', val.to_text())
"""
NS Record :  ns-1520.awsdns-62.org.
NS Record :  ns-1569.awsdns-04.co.uk.
NS Record :  ns-245.awsdns-30.com.
NS Record :  ns-869.awsdns-44.net.
"""
"""
MX stands for Mail Exchanger record,
which is a resource record that specifies
the mail server which is responsible for accepting
emails on behalf of the domain. It has preference
values according to the prioritizing mail if multiple
mail servers are present for load balancing and redundancy.
"""
# Finding MX record
result = dns.resolver.resolve('google.com', 'MX')

# Printing record
for val in result:
    print('MX Record : ', val.to_text())
"""
MX Record :  1 aspmx.l.google.com.
MX Record :  10 alt3.aspmx.l.google.com.
MX Record :  10 alt4.aspmx.l.google.com.
MX Record :  5 alt1.aspmx.l.google.com.
MX Record :  5 alt2.aspmx.l.google.com.
"""
# Finding SOA record
result = dns.resolver.resolve('google.com', 'SOA')

# Printing record
for val in result:
    print('SOA Record : ', val.to_text())
"""
SOA Record :  ns-869.awsdns-44.net. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400
"""
"""
CNAME stands for Canonical  Name record,
which is used in mapping the domain name as an alias
for the other domain. It always points to another domain
and never directly points to an IP
"""
try:
    # Finding CNAME record
    result = dns.resolver.resolve('google.com', 'CNAME')

    # Printing record
    for val in result:
        print('CNAME Record : ', val.target)
except dns.resolver.NoAnswer:
    print("No Record CNAME")
"""
------------------------
"""
# Finding TXT record
result = dns.resolver.resolve('google.com', 'TXT')

# Printing record
for val in result:
    print('TXT Record : ', val.to_text())
"""
TXT Record :  “fob1m1abcdp777bf2ncvnjm08n”
TXT Record :  “v=spf1 include:amazonses.com include:_spf.google.com ip4:167.89.66.115 -all” 
"""