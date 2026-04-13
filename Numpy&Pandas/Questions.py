#
#
# import numpy as np
# import pandas as pd
#
# print("NUMPY")
#
# a = np.array([1, 2, 3])
# print(a)
# b = np.zeros((2, 2))
# print(b)
# c = np.ones((2, 2))
# print(c)
# d = np.eye(3)
# print(d)
# e = np.arange(0, 10, 2)
# f = np.linspace(0, 1, 5)
# g = np.random.rand(2, 2)
# h = np.random.randint(1, 10, (2, 2))
#
# print(a.shape, a.ndim, a.dtype, a.size)
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0,1])
# print(arr[:,1])
#
#
#
# x = np.arange(6)
# print(x)
# print(x.reshape(2,3))
# print(x.flatten())
#
#
#
# a = np.array([1,2,3])
# b = np.array([4,5,6])
#
# print(a + b)
# print(a * b)
# print(np.dot(a, b))
# print(np.sqrt(a))
# print(np.exp(a))
# print(np.log(a))
#
#
#
# arr = np.array([[1,20,3],[4,0,6]])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.std(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.argmin(arr))
# print(np.argmax(arr))
#
#
#
# arr = np.array([[1,2],[3,4]])
# print(arr + 10)
#
#
# arr = np.array([1,2,3,4,5])
# print(arr[arr > 3])
#
#
#
# a = np.array([1,2])
# b = np.array([3,4])
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(np.split(np.array([1,2,3,4]),2))
#
#
#
#
# mat = np.array([[1,2],[3,4]])
# print(np.linalg.inv(mat))
# print(np.linalg.det(mat))
# print(np.linalg.eig(mat))
#
# print("PANDAS")
#
#
# s = pd.Series([10,20,30])
# df = pd.DataFrame({
#     "A":[1,2,3],
#     "B":[4,5,6]
# })
#
#
# print(df.head())
# print(df.tail())
# print(df.info())
# print("===========================")
# print(df.describe())
#
# print(df["A"])
# print(df.loc[0])
# print(df.iloc[0])
# print("===========================")
#
# print(df[df["A"] > 1])
#
# df["C"] = df["A"] + df["B"]
# print(df)
#
# df = df.drop("C", axis=1)
# print(df.sort_values("A"))
#
# df2 = pd.DataFrame({
#     "team":["A","A","B","B"],
#     "score":[10,20,30,40]
# })
#
# print(df2.groupby("team").sum())
#
#
# left = pd.DataFrame({"id":[1,2], "val":[10,20]})
# right = pd.DataFrame({"id":[1,2], "val2":[100,200]})
#
# print(pd.merge(left, right, on="id"))
#
# df = pd.DataFrame({"A":[1,None,3]})
# print(df.isnull())
# print(df.fillna(0))
# print(df.dropna())
#
# df = pd.DataFrame({"A":[1,2,3]})
# print(df["A"].apply(lambda x: x*2))
#
#
# df = pd.DataFrame({"name":["a","b","c"]})
# print(df["name"].str.upper())
#
# dates = pd.date_range("2024-01-01", periods=3)
# df = pd.DataFrame({"date":dates})
# print(df["date"].dt.day)
#
#
#
# df = pd.DataFrame({
#     "A":["foo","foo","bar"],
#     "B":["one","two","one"],
#     "C":[1,2,3]
# })
#
# print(pd.pivot_table(df, values="C", index="A", columns="B"))
#
#
#
# df.to_csv("test.csv", index=False)
# df2 = pd.read_csv("test.csv")
# print(df2)
#
#
import numpy as np
import pandas as pd

image = np.array([[100, 150], [200, 230]])
image2 = np.clip(image + 50, 0, 255)


s = np.array([10, 20, -15, 55, 30, 45])
s2 = s[(s >= -10) & (s <= 50)]
print(s2)
data = np.array([10, 20, 30, 40, 50])
normalized = (data - np.min(data)) / \
             (np.max(data) - np.min(data))
print(normalized)

sales = np.array([
    [100, 200, 150, 300, 250, 400, 350],
    [80, 120, 160, 200, 220, 260, 300],
    [50, 70, 90, 110, 130, 150, 170]
])

total_per_store = np.sum(sales, axis=1)
avg_per_day = np.mean(sales, axis=0)

print(total_per_store)
print(avg_per_day)

user = np.array([[1, 0], [0, 1]])
product= np.array([[5, 10], [2, 3]])

recommendation = np.dot(user, product)

print(recommendation)

df_orders = pd.DataFrame({
    "order_id": [1,2,3,4],
    "customer": ["A","B","C","D"],
    "amount": [100, 200, 150, 300],
    "status": ["completed", "pending", "completed", "completed"]
})

completed = df_orders[df_orders["status"] == "completed"]

total_revenue = completed["amount"].sum()

top3 = completed.sort_values(by="amount", ascending=False).head(3)

print(completed)
print(total_revenue)
print(top3)

df_emp = pd.DataFrame({
    "employee": ["A","B","C","D"],
    "department": ["HR","IT","HR","IT"],
    "salary": [30000, 50000, 35000, 60000]
})

avg_salary = df_emp.groupby("department")["salary"].mean()

highest_dept = avg_salary.idxmax()

print(avg_salary)
print(highest_dept)


df_missing = pd.DataFrame({
    "A": [1, None, 3],
    "B": [4, 5, None]
})

missing = df_missing.isnull()

filled = df_missing.fillna(df_missing.mean())

print(missing)
print(filled)
df_logs = pd.DataFrame({
    "timestamp": pd.to_datetime(["2023-01-01", "2023-05-01", "2024-01-01"]),
    "log_message": ["INFO start", "ERROR failed", "ERROR crash"]
})

df_logs["year"] = df_logs["timestamp"].dt.year

errors = df_logs[df_logs["log_message"].str.contains("ERROR")]

error_count = errors.groupby("year").size()

print(errors)
print(error_count)

customers = pd.DataFrame({
    "customer_id": [1,2],
    "name": ["A","B"]
})

orders = pd.DataFrame({
    "customer_id": [1,1,2],
    "amount": [100, 150, 200]
})

merged = pd.merge(customers, orders, on="customer_id")

total_purchase = merged.groupby("customer_id")["amount"].sum()

print(total_purchase)