import pandas as pd


data = {
    'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Bekasi', 
             'Depok', 'Tangerang', 'Semarang', 'Palembang', 'Makassar'],
    'Populasi': [10770487, 2982874, 2394878, 2294081, 2522341, 
                 2063442, 1844747, 1679331, 1641284, 1469011],
    'Luas (km2)': [662, 350, 167, 265, 210, 
                   200, 165, 373, 400, 199]
}

df = pd.DataFrame(data)

print(df)
