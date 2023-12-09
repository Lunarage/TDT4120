# !/usr/bin/python3
# coding=utf-8


def hamming_distance(s1, s2):
    distance = 0
    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            distance += 1
    return distance


def find_clusters(E, n, k):
    clusters = []
    for i in range(n):
        clusters.append([i])
    E_sorted = sorted(E, key=lambda edge: edge[2])
    while len(clusters) > k:
        edge = E_sorted.pop(0)
        for index, cluster in enumerate(clusters):
            if edge[0] in cluster:
                animal1_index = index
            if edge[1] in cluster:
                animal2_index = index
        if animal1_index != animal2_index:
            if animal1_index < animal2_index:
                clusters.append(clusters.pop(animal1_index) +
                                clusters.pop(animal2_index-1))
            else:
                clusters.append(clusters.pop(animal2_index) +
                                clusters.pop(animal1_index-1))
    print(clusters)
    return clusters


def find_animal_groups(animals, k):
    # Lager kanter basert på Hamming-avstand
    E = []
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            E.append((i, j, hamming_distance(animals[i][1], animals[j][1])))

    # Finner klynger
    clusters = find_clusters(E, len(animals), k)

    # Gjøre om fra klynger basert på indekser til klynger basert på dyrenavn
    animal_clusters = [
        [animals[i][0] for i in cluster] for cluster in clusters
    ]
    return animal_clusters
