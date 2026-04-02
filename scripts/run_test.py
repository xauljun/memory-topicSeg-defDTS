from src.autoseg import *

process('tiage', 'defdts_tiage', 50, 0, 'results/test_gemini_lite_nosub.json', '', False, [], 'gemini-3.1-flash-lite-preview')

agg = agg_result('tiage', 'defdts_tiage', 'test', 50, specified_path='results/test_gemini_lite_nosub.json')
pretty_print(agg['performance'])
