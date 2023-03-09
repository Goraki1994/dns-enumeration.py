#!/usr/bin/env python3 
# Modules 
import dns.resolver
# Domain and record type variables
target_domain = input("Wat is de domein naam?: ") 
record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

# DNS resolver variable
resolver = dns.resolver.Resolver()
for record_type in record_types:
    # DNS lookup based on the specified domain and record type
    try:
        answers = resolver.resolve(target_domain, record_type) 
    except dns.resolver.NoAnswer:
        continue 
    # Answers 
    print(f"{record_type} records for {target_domain}:")  
    for rdata in answers: 
        print(f" {rdata}") 

