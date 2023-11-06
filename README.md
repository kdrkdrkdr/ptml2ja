# Phonemic Transcription from Multi-Language to JApanese (ptml2ja)
The project mainly focuses on developing an IPA cleaner that uses only Japanese datasets and phonemes to induce pronunciation of foreign languages.

---
## Pre-requisites
- Python >= 3.7

---
## Installation
**Install with github project**
```sh
pip install git+https://github.com/kdrkdrkdr/ptml2ja
```
**Install with pypi project**
```sh
pip install ptml2ja
```

---
## Code Example
```python
from ptml2ja import ml2ja_ipa
ipa = ml2ja_ipa('''
[KO]안녕하세요. 만나서 반가워요.[KO]
[JA]こんにちは. お会いできて嬉しいです.[JA]
[EN]Hello, Nice to meet you.[EN]
[ID]Halo. Senang bertemu dengan Anda.[ID]
[VI]Xin chào. Rất vui được gặp bạn.[VI]
[DE]Hallo. Schön, dich kennenzulernen[DE]
[NL]Hallo. Aangenaam.[NL]
[UK]привіт. приємно познайомитись.[UK]
[SV]Hallå. Trevligt att träffas.[SV]
[CS]Ahoj. Rád vás poznávám.[CS]
[FI]Kamusta. Ikinagagalak kitang makilala.[FI]
[LA]Salve. Vos noscere.[LA]
''')
print(ipa)
# Results (IPA)
# aNnyoNNhaseyo.maNnasabaNgawoyo. 
# koNniʧiwa. oaidekIte ureʃiidesU. 
# haaro,naisUtumitouyu. 
# haro.senaNNbeetemudeaNaNda. 
# QʃiNQʦuao.raQQpuiduaQQkaQQpaN. 
# haaro.soiN,dihIkeneNʦuureruneN. 
# haaro.aNenaNN. 
# puribitu.puriieNNnopozunayomitisu. 
# haaro.turebuuriQtuatuturepasu. 
# ahoi.ratubasUpozunabaNN. 
# kamusuta.ikinagagaarakukitaNNmakiiraara. 
# saabe.bosunosUkere. 
```

---
## Support Language List
|Country|Language Code (ISO 639-1)|
|---|---|
|Korean|KO|
|Japanese|JA|
|English|EN|
|Indonesian|ID|
|Vietnamese|VI|
|Russian|RU|
|Turkish|TR|
|Spainish|ES|
|Portugese|PT|
|Italian|IT|
|Poland|PO|
|German|DE|
|Dutch|NL|
|Ukrainian|UK|
|Swedish|SV|
|Czech|CS|
|Finnish|FI|
|Latin|LA|
|Hungarian|HU|

---
## References
For more information, please refer to the following repositories.
- [sublee/hangulize](https://github.com/sublee/hangulize)

- [Kyubyong/g2pK](https://github.com/Kyubyong/g2pK)
