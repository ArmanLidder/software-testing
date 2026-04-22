import re
from collections import defaultdict, Counter

# === 1. Lire le fichier logs.txt ===
with open("logs.txt", "r", encoding="utf-16") as f:
    lines = f.readlines()

# === 2. Extraire les infos utiles ===
pattern = re.compile(r"\[INFO\]\[(.*?)\]\s(POST|GET)\s(\/[^\s]+)")
user_requests = defaultdict(list)
all_endpoints = []

for line in lines:
    match = pattern.search(line)
    if match:
        user, method, endpoint = match.groups()
        # Retirer les IDs pour uniformiser (ex: /profile/4 -> /profile/:id)
        endpoint = re.sub(r"/\d+", "/:id", endpoint)
        user_requests[user].append(endpoint)
        all_endpoints.append(endpoint)

# === 3. Charge globale ===
endpoint_counts = Counter(all_endpoints)
total_reqs = sum(endpoint_counts.values())

print("\n=== Charge globale (nombre de requêtes et ratios) ===")
for ep, count in endpoint_counts.most_common():
    ratio = round((count / total_reqs) * 100, 2)
    print(f"{ep:<20} {count:<6} ({ratio}%)")



# === 4. Chaîne de Markov ===
transitions = defaultdict(Counter)

for user, seq in user_requests.items():
    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i + 1]
        transitions[a][b] += 1

# === 5. Calcul des probabilités de transition ===
markov_chain = {}
for src, dests in transitions.items():
    total = sum(dests.values())
    markov_chain[src] = {d: round(c / total, 3) for d, c in dests.items()}

print("\n=== Chaîne de Markov (probabilités de transition) ===")
for src, dests in markov_chain.items():
    for dest, prob in dests.items():
        print(f"{src:20} -> {dest:20} : {prob}")