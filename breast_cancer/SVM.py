import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
# 加载数据集，你需要把数据放到目录中
data = pd.read_csv(r"D:\\python_code\\sample\\breast_cancer\\data.csv")
# 数据探索
# 因为数据集中列比较多，我们需要把 dataframe 中的列全部显示出来
# pd.set_option('display.max_columns', None) # 显示所有列,防止DataFrame中的行列数量太多，print打印出来会显示不完全
# print(data.columns)
# print(data.head(5))
# print(data.describe())
# 将特征字段分成 3 组
features_mean= list(data.columns[2:12])
features_se= list(data.columns[12:22])
features_worst=list(data.columns[22:32])
# print(features_mean)
# 数据清洗
# ID 列没有用，删除该列
data.drop("id",axis=1,inplace=True)
# 将 B 良性替换为 0，M 恶性替换为 1
data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
# 将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'],label="Count")
plt.show()
# 用热力图呈现 features_mean 字段之间的相关性
corr = data[features_mean].corr()
plt.figure(figsize=(14,14))
# annot=True 显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()
# 特征选择
features_remain = ['radius_mean','texture_mean', 'smoothness_mean','compactness_mean','symmetry_mean', 'fractal_dimension_mean'] 
# 抽取 30% 的数据作为测试集，其余作为训练集
train, test = train_test_split(data, test_size = 0.3)# in this our main data is splitted into train and test
# 抽取特征选择的数值作为训练和测试数据
train_X = train[features_remain]
train_y=train['diagnosis']
test_X= test[features_remain]
test_y =test['diagnosis']
# 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
ss = preprocessing.StandardScaler()
train_X = ss.fit_transform(train_X)
test_X = ss.transform(test_X)
# 创建 SVM 分类器
model = svm.SVC()
# 用训练集做训练
model.fit(train_X,train_y)
# 用测试集做预测
prediction=model.predict(test_X)
print('准确率: ', accuracy_score(prediction,test_y))
