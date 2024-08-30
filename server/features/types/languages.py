from typing import Literal, TypedDict

# Define the Languages type using Literal
Languages = Literal[
    'ace_Arab',
    'ace_Latn',
    'acm_Arab',
    'acq_Arab',
    'aeb_Arab',
    'afr_Latn',
    'ajp_Arab',
    'aka_Latn',
    'amh_Ethi',
    'apc_Arab',
    'arb_Arab',
    'arb_Latn',
    'ars_Arab',
    'ary_Arab',
    'arz_Arab',
    'asm_Beng',
    'ast_Latn',
    'awa_Deva',
    'ayr_Latn',
    'azb_Arab',
    'azj_Latn',
    'bak_Cyrl',
    'bam_Latn',
    'ban_Latn',
    'bel_Cyrl',
    'bem_Latn',
    'ben_Beng',
    'bho_Deva',
    'bjn_Arab',
    'bjn_Latn',
    'bod_Tibt',
    'bos_Latn',
    'bug_Latn',
    'bul_Cyrl',
    'cat_Latn',
    'ceb_Latn',
    'ces_Latn',
    'cjk_Latn',
    'ckb_Arab',
    'crh_Latn',
    'cym_Latn',
    'dan_Latn',
    'deu_Latn',
    'dik_Latn',
    'eng_Latn',
    'tur_Latn'
]

# Define the TranslatorOptions TypedDict
class TranslatorOptions(TypedDict, total=False):
    ace_Arab: str
    ace_Latn: str
    acm_Arab: str
    acq_Arab: str
    aeb_Arab: str
    afr_Latn: str
    ajp_Arab: str
    aka_Latn: str
    amh_Ethi: str
    apc_Arab: str
    arb_Arab: str
    arb_Latn: str
    ars_Arab: str
    ary_Arab: str
    arz_Arab: str
    asm_Beng: str
    ast_Latn: str
    awa_Deva: str
    ayr_Latn: str
    azb_Arab: str
    azj_Latn: str
    bak_Cyrl: str
    bam_Latn: str
    ban_Latn: str
    bel_Cyrl: str
    bem_Latn: str
    ben_Beng: str
    bho_Deva: str
    bjn_Arab: str
    bjn_Latn: str
    bod_Tibt: str
    bos_Latn: str
    bug_Latn: str
    eng_Latn: str
    tur_Latn: str
    cat_Latn: str
    ceb_Latn: str
    ces_Latn: str
    cjk_Latn: str
    ckb_Arab: str
    crh_Latn: str
    cym_Latn: str
    dan_Latn: str
    deu_Latn: str
    dik_Latn: str