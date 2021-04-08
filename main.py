import json
with open('livre/persos.json') as f:
  persos = json.load(f)
with open('livre/specs.json') as f:
  specs = json.load(f)
with open('livre/content.json') as f:
  content = json.load(f)

print(specs, persos, content)

print()