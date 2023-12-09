#!/usr/bin/python3
# coding=utf-8


def compatibility_graph(donors, recipients, k):
    donor_edges = []
    for donor in donors:
        d_compatibility_list = []
        for r_index, recipient in enumerate(recipients):
            compatibility = 0
            for d_index, d_attribute in enumerate(donor):
                if d_attribute == recipient[d_index]:
                    compatibility += 1
            if compatibility >= k:
                d_compatibility_list.append(r_index)
        donor_edges.append(d_compatibility_list)
    return donor_edges
