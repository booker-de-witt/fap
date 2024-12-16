import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error

#-------------TASK 1 -------------------
data = pd.read_csv("fap\wk2\extended_salary_data.csv")

plt.scatter(data["YearsExperience"], data["Salary"])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Ohhh Salary does depend on Years of Experience")

# plt.show()


matrix = np.array(data.values,'float')
x= matrix[:,0].reshape(-1,1)
y = matrix[:,1].reshape(-1,1)

mean_salary = y.mean()
mean_years_of_xp = x.mean()
median_salary = np.median(y)
median_years_of_xp = np.median(x)
variance_salary = y.var()
variance_years_of_xp = x.var()

# --------------------TASK 2------------------------


x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.2)

reg = LinearRegression()

reg.fit(x_train,y_train)
slope = reg.coef_[0][0]
intercept = reg.intercept_[0]
print("Slope: " , slope)
print("Intercept: ", intercept)


# --------------------TASK 3---------------------------
score = reg.score(x_test,y_test)
y_pred = reg.predict(x_test)


mae = mean_absolute_error(y_true=y_test,y_pred=y_pred)
mse = mean_squared_error(y_true=y_test,y_pred=y_pred)
print(mae)
print(mse)


plt.plot(x_test,y_pred)
plt.scatter(x,y,c="green")
plt.show()

