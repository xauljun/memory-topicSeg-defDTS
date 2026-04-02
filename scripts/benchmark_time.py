import time
from src.autoseg import *

agent = SegAnnotator(key_owner='', template='defdts_tiage', model='gemini-3.1-flash-lite-preview')
dataset = agent.load_data('tiage', 'test', 1, 0)
sample = dataset[0]
prompt = agent.fill_prompt(sample['dialogue'])

times = []
for i in range(10):
    start = time.time()
    agent.infer_gemini(prompt)
    elapsed = time.time() - start
    times.append(elapsed)
    print(f"[{i+1:2d}] {elapsed:.2f}s")

print(f"\n평균: {sum(times)/len(times):.2f}s")
print(f"최소: {min(times):.2f}s")
print(f"최대: {max(times):.2f}s")
