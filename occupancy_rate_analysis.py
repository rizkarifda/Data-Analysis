# -*- coding: utf-8 -*-
"""Occupancy Rate Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ukK1l6JiVVBSkr7E_7dAry7PWhN8NXR
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

!wget https://raw.githubusercontent.com/rizkarifda/Project/master/manarul_kuliah.csv

manarul_nov_kul = pd.read_csv('manarul_kuliah.csv')

manarul_nov_kul

fig, ax = plt.subplots(figsize=(20,10))
sns.barplot(x="hari",
                y = "jumlah",
                hue = "jam",
                data = manarul_nov_kul,
                palette = "bright"
                )

tidak_muat=manarul_nov_kul[manarul_nov_kul['jumlah']>38]
tidak_muat

penuh_sekali=manarul_nov_kul[manarul_nov_kul['jumlah']>=30]
penuh_sekali

penuh_sekali[penuh_sekali['jumlah']<=38]

penuh=manarul_nov_kul[manarul_nov_kul['jumlah']>=20]
penuh

penuh[penuh['jumlah']<=29]

terisi=manarul_nov_kul[manarul_nov_kul['jumlah']<=19]
terisi

terisi=manarul_nov_kul[manarul_nov_kul['jumlah']<=19]
terisi

kosong=manarul_nov_kul[manarul_nov_kul['jumlah']==0]
kosong

!wget https://raw.githubusercontent.com/rizkarifda/Project/master/manarul_kuliah_kateg.csv

kuliah_kateg = pd.read_csv('manarul_kuliah_kateg.csv')

senin=kuliah_kateg[kuliah_kateg['hari']=='senin']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = senin,
                palette = "bright"
                )

selasa=kuliah_kateg[kuliah_kateg['hari']=='selasa']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = selasa,
                palette = "bright"
                )

rabu=kuliah_kateg[kuliah_kateg['hari']=='rabu']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = rabu,
                palette = "bright"
                )



kamis=kuliah_kateg[kuliah_kateg['hari']=='kamis']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = kamis,
                palette = "bright"
                )

jumat=kuliah_kateg[kuliah_kateg['hari']=='jumat']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = jumat,
                palette = "bright"
                )

sabtu=kuliah_kateg[kuliah_kateg['hari']=='sabtu']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = sabtu,
                palette = "bright"
                )

minggu=kuliah_kateg[kuliah_kateg['hari']=='minggu']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = minggu,
                palette = "bright"
                )

!wget https://raw.githubusercontent.com/rizkarifda/Project/master/manarul_event_ratarata.csv

manarul_event = pd.read_csv('manarul_event_ratarata.csv')

manarul_event

fig, ax = plt.subplots(figsize=(20,10))
sns.barplot(x="hari",
                y = "jumlah",
                hue = "jam",
                data = manarul_event,
                palette = "bright"
                )

tidak_muat=manarul_event[manarul_event['jumlah']>38]
tidak_muat

penuh_sekali=manarul_event[manarul_event['jumlah']>=30]
penuh_sekali

penuh_sekali[penuh_sekali['jumlah']<=38]

penuh=manarul_event[manarul_event['jumlah']>=20]
penuh

penuh[penuh['jumlah']<=29]

terisi=manarul_event[manarul_event['jumlah']<=19]
terisi

!wget https://raw.githubusercontent.com/rizkarifda/Project/master/manarul_event_kateg.csv

manarul_event_kateg = pd.read_csv('manarul_event_kateg.csv')
manarul_event_kateg

senin=manarul_event_kateg[manarul_event_kateg['hari']=='senin']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = senin,
                palette = "bright"
                )

selasa=manarul_event_kateg[manarul_event_kateg['hari']=='selasa']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = selasa,
                palette = "bright"
                )

rabu=manarul_event_kateg[manarul_event_kateg['hari']=='rabu']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = rabu,
                palette = "bright"
                )

kamis=manarul_event_kateg[manarul_event_kateg['hari']=='kamis']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = kamis,
                palette = "bright"
                )

jumat=manarul_event_kateg[manarul_event_kateg['hari']=='jumat']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = jumat,
                palette = "bright"
                )

sabtu=manarul_event_kateg[manarul_event_kateg['hari']=='sabtu']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = sabtu,
                palette = "bright"
                )

minggu=manarul_event_kateg[manarul_event_kateg['hari']=='minggu']
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x="jam",
                y = "jumlah",
                hue = "kategori",
                data = minggu,
                palette = "bright"
                )