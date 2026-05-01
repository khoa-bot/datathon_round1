import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import warnings

# Bỏ qua các cảnh báo không cần thiết
warnings.filterwarnings('ignore')

# Cài đặt style chung cho toàn bộ biểu đồ
plt.style.use('ggplot')
sns.set_palette("husl")

# ==============================================================================
# 1. LOAD DATA (Tải toàn bộ dữ liệu dùng chung cho cả 2 kịch bản)
# ==============================================================================
print("Loading data...")
orders = pd.read_csv('orders.csv', parse_dates=['order_date'])
web_traffic = pd.read_csv('web_traffic.csv', parse_dates=['date'])
order_items = pd.read_csv('order_items.csv', low_memory=False)
products = pd.read_csv('products.csv')
promotions = pd.read_csv('promotions.csv')
returns = pd.read_csv('returns.csv', parse_dates=['return_date'])
reviews = pd.read_csv('reviews.csv', parse_dates=['review_date'])
sales = pd.read_csv('sales.csv', parse_dates=['Date'])
shipments = pd.read_csv('shipments.csv', parse_dates=['ship_date', 'delivery_date'])


try:
    inventory = pd.read_csv('inventory.csv')
    if 'date' in inventory.columns:
        inventory['date'] = pd.to_datetime(inventory['date'])
    elif 'month' in inventory.columns:
        inventory['month'] = pd.to_datetime(inventory['month'])
    print("Inventory columns:", inventory.columns.tolist())
except Exception as e:
    print("Could not load inventory or parse dates:", e)

# ==============================================================================
# PHẦN A: LOGIC TỪ FILE MAIN.PY
# ==============================================================================


# --- 1. TRAFFIC PROBLEM ---
plt.figure(figsize=(15, 10))

# 1.1 Traffic over time (Monthly)
plt.subplot(2, 1, 1)
wt_monthly = web_traffic.set_index('date').resample('M')[['sessions', 'unique_visitors', 'page_views']].sum()
plt.plot(wt_monthly.index, wt_monthly['sessions'], label='Sessions')
plt.plot(wt_monthly.index, wt_monthly['unique_visitors'], label='Unique Visitors')
plt.title('Traffic Over Time (Monthly)')
plt.ylabel('Count')
plt.legend()

# 1.2 Traffic by Source
plt.subplot(2, 1, 2)
wt_source = web_traffic.groupby('traffic_source')['sessions'].sum().sort_values(ascending=False)
sns.barplot(x=wt_source.index, y=wt_source.values)
plt.title('Sessions by Traffic Source')
plt.ylabel('Total Sessions')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('1_Traffic_Problem.png')
plt.close()

# --- 2. CONVERSION PROBLEM ---
daily_orders = orders.groupby('order_date').size().reset_index(name='orders')
daily_traffic = web_traffic.groupby('date')['sessions'].sum().reset_index()
conversion_df = pd.merge(daily_traffic, daily_orders, left_on='date', right_on='order_date', how='left').fillna(0)
conversion_df['conversion_rate'] = (conversion_df['orders'] / conversion_df['sessions']).replace([np.inf, -np.inf], 0).fillna(0)
conv_monthly = conversion_df.set_index('date').resample('M').agg({'sessions':'sum', 'orders':'sum'})
conv_monthly['conversion_rate'] = conv_monthly['orders'] / conv_monthly['sessions']

plt.figure(figsize=(15, 12))

# 2.1 Conversion Rate over time
plt.subplot(2, 1, 1)
plt.plot(conv_monthly.index, conv_monthly['conversion_rate'], marker='o', color='green')
plt.title('Monthly Conversion Rate')
plt.ylabel('Conversion Rate')

# 2.2 Conversion by device and source
plt.subplot(2, 2, 3)
order_by_device = orders['device_type'].value_counts()
sns.barplot(x=order_by_device.index, y=order_by_device.values)
plt.title('Orders by Device Type')

plt.subplot(2, 2, 4)
order_by_source = orders['order_source'].value_counts()
sns.barplot(x=order_by_source.index, y=order_by_source.values)
plt.title('Orders by Source')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('2_Conversion_Problem.png')
plt.close()

# --- 3. PRICE / AOV / DISCOUNT ISSUE ---
item_prod = pd.merge(order_items, products, on='product_id', how='left')
order_item_prod = pd.merge(item_prod, orders, on='order_id', how='left')

plt.figure(figsize=(15, 12))

# 3.1 Average Unit Price by Category
plt.subplot(2, 2, 1)
avg_price_cat = products.groupby('category')['price'].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_cat.index, y=avg_price_cat.values)
plt.title('Average Unit Price by Category')
plt.xticks(rotation=45)

# 3.2 Discount vs Revenue over time
order_item_prod['revenue'] = order_item_prod['quantity'] * order_item_prod['unit_price']
monthly_rev_disc = order_item_prod.set_index('order_date').resample('M').agg({'revenue':'sum', 'discount_amount':'sum'})
plt.subplot(2, 2, 2)
plt.plot(monthly_rev_disc.index, monthly_rev_disc['revenue'], label='Revenue', color='blue')
plt.plot(monthly_rev_disc.index, monthly_rev_disc['discount_amount'], label='Discount Amount', color='red')
plt.title('Revenue vs Discount Over Time')
plt.legend()

# 3.3 Gross Margin by Category
order_item_prod['cogs_total'] = order_item_prod['quantity'] * order_item_prod['cogs']
order_item_prod['gross_profit'] = order_item_prod['revenue'] - order_item_prod['discount_amount'] - order_item_prod['cogs_total']
cat_margin = order_item_prod.groupby('category').agg({'revenue':'sum', 'gross_profit':'sum'})
cat_margin['gross_margin'] = cat_margin['gross_profit'] / cat_margin['revenue']
plt.subplot(2, 2, 3)
sns.barplot(x=cat_margin.index, y=cat_margin['gross_margin'].sort_values(ascending=False))
plt.title('Gross Margin by Category')
plt.xticks(rotation=45)

# 3.4 Revenue by Promotion Type
item_promo = pd.merge(order_items, promotions, on='promo_id', how='left')
item_promo['revenue'] = item_promo['quantity'] * item_promo['unit_price']
rev_by_promo = item_promo.groupby('promo_type')['revenue'].sum().dropna()
plt.subplot(2, 2, 4)
if not rev_by_promo.empty:
    plt.pie(rev_by_promo.values, labels=rev_by_promo.index, autopct='%1.1f%%')
    plt.title('Revenue by Promo Type')

plt.tight_layout()
plt.savefig('3_AOV_Discount_ProductMix.png')
plt.close()

# --- 4. PROFIT & REVENUE ANALYSIS ---
fig, ax1 = plt.subplots(figsize=(12,6))
sales_monthly = sales.set_index('Date').resample('M').sum()
sales_monthly['Gross Profit'] = sales_monthly['Revenue'] - sales_monthly['COGS']
sales_monthly['Gross Margin'] = sales_monthly['Gross Profit'] / sales_monthly['Revenue']

ax2 = ax1.twinx()
ax1.plot(sales_monthly.index, sales_monthly['Revenue'], label='Revenue', color='blue')
ax1.plot(sales_monthly.index, sales_monthly['COGS'], label='COGS', color='orange')
ax2.plot(sales_monthly.index, sales_monthly['Gross Margin'], label='Gross Margin', color='green', linestyle='--')
ax1.set_ylabel('Amount')
ax2.set_ylabel('Gross Margin')
ax1.set_title('Revenue, COGS & Gross Margin Over Time')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.tight_layout()
plt.savefig('4_Profit_Revenue_Macro.png')
plt.close()

# --- 5. CUSTOMER EXPERIENCE (RETURNS & REVIEWS) ---
plt.figure(figsize=(15, 12))

# 5.1 Return Reasons
plt.subplot(2, 2, 1)
return_reasons = returns['return_reason'].value_counts()
sns.barplot(x=return_reasons.index, y=return_reasons.values)
plt.title('Return Reasons Breakdown')
plt.xticks(rotation=45)

# 5.2 Return Quantity by Category
ret_prod = pd.merge(returns, products, on='product_id', how='left')
ret_cat = ret_prod.groupby('category')['return_quantity'].sum().sort_values(ascending=False)
plt.subplot(2, 2, 2)
sns.barplot(x=ret_cat.index, y=ret_cat.values)
plt.title('Returned Quantity by Category')
plt.xticks(rotation=45)

# 5.3 Average Rating by Category
rev_prod = pd.merge(reviews, products, on='product_id', how='left')
rat_cat = rev_prod.groupby('category')['rating'].mean().sort_values()
plt.subplot(2, 2, 3)
sns.barplot(x=rat_cat.index, y=rat_cat.values)
plt.title('Average Rating by Category')
plt.ylim(1, 5)
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('5_Customer_Experience.png')
plt.close()

# --- 6. SHIPPING IMPACT ---
ship_orders = pd.merge(shipments, orders[['order_id', 'order_date']], on='order_id', how='inner')
ship_orders['delivery_days'] = (ship_orders['delivery_date'] - ship_orders['ship_date']).dt.days
ship_monthly = ship_orders.set_index('order_date').resample('M').agg({'delivery_days':'mean', 'shipping_fee':'mean', 'order_id':'count'}).rename(columns={'order_id':'order_volume'})

plt.figure(figsize=(15, 10))

# 6.1 Avg Delivery Days Over Time
plt.subplot(2, 1, 1)
plt.plot(ship_monthly.index, ship_monthly['delivery_days'], color='purple', marker='o')
plt.title('Average Delivery Days Over Time')
plt.ylabel('Days')

# 6.2 Shipping Fee vs Order Volume over time
ax1 = plt.subplot(2, 1, 2)
ax2 = ax1.twinx()
ax1.plot(ship_monthly.index, ship_monthly['shipping_fee'], color='brown', label='Avg Shipping Fee')
ax2.bar(ship_monthly.index, ship_monthly['order_volume'], alpha=0.3, width=20, label='Order Volume', color='gray')
ax1.set_ylabel('Avg Shipping Fee')
ax2.set_ylabel('Order Volume')
ax1.set_title('Avg Shipping Fee vs Order Volume')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('6_Shipping.png')
plt.close()

print("Charts successfully generated. ")

# ==============================================================================


# ==============================================================================




item_prod2 = pd.merge(order_items, products, on='product_id', how='left')
order_item_prod2 = pd.merge(item_prod2, orders, on='order_id', how='left')
order_item_prod2['revenue'] = order_item_prod2['quantity'] * order_item_prod2['unit_price']
order_item_prod2['discount_pct'] = (order_item_prod2['discount_amount'] / order_item_prod2['revenue']).fillna(0)
order_item_prod2.replace([np.inf, -np.inf], 0, inplace=True)

# ---------------------------------------------------------
# 1. CONVERSION RATE DEEP DIVE (1_Conversion_DeepDive.png)
# ---------------------------------------------------------
plt.figure(figsize=(18, 12))

# 1.1 Conversion Rate by Source
plt.subplot(2, 2, 1)
traffic_by_source = web_traffic.groupby('traffic_source')['sessions'].sum()
orders_by_source = orders.groupby('order_source').size()
cr_by_source = (orders_by_source / traffic_by_source).dropna().sort_values(ascending=False)
if not cr_by_source.empty:
    sns.barplot(x=cr_by_source.index, y=cr_by_source.values, palette='viridis')
    plt.title('Conversion Rate by Traffic Source')
    plt.ylabel('Conversion Rate')
    plt.xticks(rotation=45)

# 1.2 Orders by Device (Zoom in on Mobile)
plt.subplot(2, 2, 2)
device_orders = orders['device_type'].value_counts()
colors = ['red' if dev.lower() == 'mobile' else 'gray' for dev in device_orders.index]
sns.barplot(x=device_orders.index, y=device_orders.values, palette=colors)
plt.title('Orders by Device Type (Mobile Highlighted)')
plt.ylabel('Total Orders')

# 1.3 Monthly Conversion Rate (2018 - 2020)
plt.subplot(2, 1, 2)
daily_orders2 = orders.groupby('order_date').size().reset_index(name='orders')
daily_traffic2 = web_traffic.groupby('date')['sessions'].sum().reset_index()
conversion_df2 = pd.merge(daily_traffic2, daily_orders2, left_on='date', right_on='order_date', how='left').fillna(0)
conv_monthly2 = conversion_df2.set_index('date').resample('M').agg({'sessions':'sum', 'orders':'sum'})
conv_monthly2['conversion_rate'] = conv_monthly2['orders'] / conv_monthly2['sessions']
conv_18_20 = conv_monthly2.loc['2018-01-01':'2020-12-31']

plt.plot(conv_18_20.index, conv_18_20['conversion_rate'], marker='o', color='purple')
plt.title('Monthly Conversion Rate (2018 - 2020)')
plt.ylabel('Conversion Rate')
plt.xlabel('Time')

plt.tight_layout()
plt.savefig('1_Conversion_DeepDive.png')
plt.close()

# ---------------------------------------------------------
# 2. AOV & MACRO COMBINED (2_AOV_Macro.png)
# ---------------------------------------------------------
plt.figure(figsize=(18, 12))

# 2.1 AOV Over Time
plt.subplot(2, 1, 1)
monthly_rev_orders = order_item_prod2.set_index('order_date').resample('M').agg({'revenue':'sum', 'order_id':'nunique'})
monthly_rev_orders['AOV'] = monthly_rev_orders['revenue'] / monthly_rev_orders['order_id']
plt.plot(monthly_rev_orders.index, monthly_rev_orders['AOV'], marker='s', color='teal')
plt.title('Average Order Value (AOV) Over Time')
plt.ylabel('AOV ($)')

# 2.2 Combined Macro: Sessions, Orders, Revenue
ax1 = plt.subplot(2, 1, 2)
macro_monthly = pd.concat([conv_monthly2[['sessions', 'orders']], monthly_rev_orders[['revenue']]], axis=1).dropna()

ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))

l1, = ax1.plot(macro_monthly.index, macro_monthly['sessions'], color='blue', label='Sessions')
l2, = ax2.plot(macro_monthly.index, macro_monthly['orders'], color='orange', label='Orders')
l3, = ax3.plot(macro_monthly.index, macro_monthly['revenue'], color='green', label='Revenue', linestyle='--')

ax1.set_ylabel('Sessions', color='blue')
ax2.set_ylabel('Orders', color='orange')
ax3.set_ylabel('Revenue ($)', color='green')
ax1.set_title('Macro View: Sessions vs Orders vs Revenue')

lines = [l1, l2, l3]
ax1.legend(lines, [l.get_label() for l in lines], loc='upper left')

plt.tight_layout()
plt.savefig('2_AOV_Macro.png')
plt.close()

# ---------------------------------------------------------
# 3. PROMO INEFFICIENCY & PRODUCT MIX (3_Promo_ProductMix.png)
# ---------------------------------------------------------
plt.figure(figsize=(18, 12))

# 3.1 Scatter: Discount vs Revenue
plt.subplot(2, 2, 1)
order_level = order_item_prod2.groupby('order_id').agg({'discount_amount':'sum', 'revenue':'sum', 'quantity':'sum'})
sample_orders = order_level.sample(n=min(5000, len(order_level)), random_state=42)
sns.scatterplot(x='discount_amount', y='revenue', data=sample_orders, alpha=0.5, color='coral')
plt.title('Discount Amount vs Revenue (Order Level)')
plt.xlabel('Discount Amount')
plt.ylabel('Revenue')

# 3.2 Avg Discount % Over Time
plt.subplot(2, 2, 2)
monthly_disc_pct = order_item_prod2.set_index('order_date').resample('M')['discount_pct'].mean() * 100
plt.plot(monthly_disc_pct.index, monthly_disc_pct.values, color='red', marker='.')
plt.title('Average Discount % Over Time')
plt.ylabel('Discount %')

# 3.3 Stacked Bar: Revenue by Category Over Time (Yearly)
plt.subplot(2, 1, 2)
order_item_prod2['year'] = order_item_prod2['order_date'].dt.year
yearly_cat_rev = order_item_prod2.groupby(['year', 'category'])['revenue'].sum().unstack().fillna(0)
yearly_cat_rev.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='Set2')
plt.title('Revenue Contribution by Category Over Time')
plt.ylabel('Total Revenue')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('3_Promo_ProductMix.png')
plt.close()

# ---------------------------------------------------------
# 4. RETURN RATE ANALYSIS (4_ReturnRate.png)
# ---------------------------------------------------------
ret_prod2 = pd.merge(returns, products, on='product_id', how='left')

plt.figure(figsize=(18, 12))

# Calculate Overall return quantities and sold quantities
item_sold_monthly = order_item_prod2.set_index('order_date').resample('M')['quantity'].sum()
item_returned_monthly = returns.set_index('return_date').resample('M')['return_quantity'].sum()
return_rate_monthly = (item_returned_monthly / item_sold_monthly).fillna(0)

cat_sold = order_item_prod2.groupby('category')['quantity'].sum()
cat_returned = ret_prod2.groupby('category')['return_quantity'].sum()
return_rate_cat = (cat_returned / cat_sold).fillna(0).sort_values(ascending=False)

# 4.1 Return Rate by Category
plt.subplot(2, 2, 1)
sns.barplot(x=return_rate_cat.index, y=return_rate_cat.values * 100, palette='magma')
plt.title('Return Rate by Category (%)')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=45)

# 4.2 Return Rate Over Time
plt.subplot(2, 2, 2)
plt.plot(return_rate_monthly.index, return_rate_monthly.values * 100, color='brown', marker='o')
plt.title('Overall Return Rate Over Time')
plt.ylabel('Return Rate (%)')

# 4.3 Scatter: Return Rate vs Rating by Product
plt.subplot(2, 1, 2)
prod_sold = order_item_prod2.groupby('product_id')['quantity'].sum()
prod_ret = returns.groupby('product_id')['return_quantity'].sum()
prod_rating = reviews.groupby('product_id')['rating'].mean()
prod_cat = products.set_index('product_id')['category']

prod_stats = pd.DataFrame({'sold': prod_sold, 'returned': prod_ret, 'rating': prod_rating, 'category': prod_cat}).fillna(0)
prod_stats['return_rate'] = (prod_stats['returned'] / prod_stats['sold']).replace([np.inf, -np.inf], 0).fillna(0)
# Filter out products with 0 sales to avoid noise
prod_stats = prod_stats[prod_stats['sold'] > 0]

sns.scatterplot(x='rating', y='return_rate', hue='category', size='sold', data=prod_stats, alpha=0.7, sizes=(20, 200))
plt.title('Return Rate vs Rating by Product')
plt.xlabel('Average Rating')
plt.ylabel('Return Rate')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('4_ReturnRate.png')
plt.close()

print("Initial scripts finished. Checking Inventory data specifically...")