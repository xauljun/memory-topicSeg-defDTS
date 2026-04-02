from src.autoseg import *

agg = agg_result('tiage', 'defdts_tiage', 'test', 10, specified_path='results/test_gemini.json')
pretty_print(agg['performance'])
