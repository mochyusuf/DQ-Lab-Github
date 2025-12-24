#Impor library pandas sebagai pd
import pandas as pd

#Gunakan pandas untuk membaca dataset roi.csv dan simpan dalam variabel df
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/komdigi/tbl_roi.csv')

#Hitung revenue dengan mengalikan kolom unit_price dengan kolom units_sold dan simpan hasilnya dalam kolom revenue
df['revenue'] = df['unit_price'] * df['units_sold']

#Hitung modal dengan mengalikan kolom unit_cost dengan kolom units_sold dan simpan hasilnya dalam kolom cost
df['cost'] = df['unit_cost']  * df['units_sold']

#Hitung margin percentage berdasarkan rumus yang sudah dijelaskan sebelumnya dan simpan dalam kolom margin_pct
df['margin_pct'] = (df['revenue'] - df['cost']) / df['revenue'] * 100

#Menentukan nilai kerugian akibat refund untuk masing-masing record SKU dan simpan dalam kolom refund_loss
df['refund_loss'] = df['units_refunded'] * df['unit_price']

#Menentukan pendapatan yang sudah dikurangi dengan refund_loss dan simpan dalam kolom adjusted_revenue
df['adjusted_revenue'] = df['revenue'] - df['refund_loss']

#Menandai understock: buat kolom understock_flag (TRUE jika spike_flag == 1 dan units_sold > stock_available)
df['understock_flag'] = (df['spike_flag'] == 1) & (df['units_sold'] > df['stock_available'])

#Menghitung lost_units dan lost_revenue saat understock
df['lost_units'] = df.apply(lambda x: max(0, x['units_sold'] - x['stock_available']) if x['understock_flag'] else 0, axis=1)
df['lost_revenue'] = df['lost_units'] * df['unit_price']

#Menandai overstock: buat kolom overstock_flag (TRUE jika stock_available > units_sold)
df['overstock_flag'] = df['stock_available'] > df['units_sold']

#Menghitung excess_units dan holding_cost (holding_rate = 0.10)
df['excess_units'] = df.apply(lambda x: max(0, x['stock_available'] - x['units_sold']) if x['overstock_flag'] else 0, axis=1)
holding_rate = 0.10
df['holding_cost'] = df['excess_units'] * df['unit_price'] * holding_rate * df['restock_lead_days']

#Impor library train_test_split dari sklearn.model_selection
from sklearn.model_selection import train_test_split

#Impor library RandomForestClassifier dari sklearn.ensemble
from sklearn.ensemble import RandomForestClassifier

#Impor library classification_report dari sklearn.metrics
from sklearn.metrics import classification_report

# Membuat fitur unit_margin sebagai selisih unit_price dan unit_cost.
df['unit_margin'] = df['unit_price'] - df['unit_cost']

# Menghitung refund_rate (%) = units_refunded / units_sold × 100.
df['refund_rate'] = df['units_refunded'] / df['units_sold'].replace(0, 1) * 100

# Menghitung roi_value (%) baris menggunakan rumus sederhana: (revenue−cost−refundloss)÷cost×100
revenue     = df['unit_price'] * df['units_sold']
refund_loss = df['units_refunded'] * df['unit_price']
cost        = df['unit_cost'] * df['units_sold']
df['roi_value']   = (revenue- cost - refund_loss) / cost.replace(0, 1) * 100

# Membuat target biner roi_class (1 jika roi_value ≥ 20, else 0).
df['roi_class'] = (df['roi_value'] >= 20).astype(int)

# Memilih fitur stock_available, unit_margin, refund_rate, restock_lead_days dan target roi_class
feature_cols = ['stock_available','unit_margin','refund_rate','restock_lead_days']
X = df[feature_cols]
y = df['roi_class']

# Membagi data train–test (80 : 20, stratify=y)
X_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.2, random_state=42, stratify=y)

# Melatih RandomForestClassifier dengan class_weight='balanced', jumlah estimator = 100, dan random state di 42
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42, 
    class_weight='balanced'
)
model.fit(X_train, y_train)

# Mencetak classification report untuk evaluasi model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
