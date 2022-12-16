#!/usr/bin/python3
# coding=utf-8

def compatibility_graph(donors, recipients, k):
    compabilities = [[] for _ in range(len(donors))]
    for i, recipient in enumerate(recipients):
        for j, donor in enumerate(donors):
            match = 0
            for r_attr, d_attr in zip(recipient, donor):
                if r_attr == d_attr:
                    match += 1
            if match >= k:
                compabilities[j].append(i)
    return compabilities
