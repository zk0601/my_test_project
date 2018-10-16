import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from io import BytesIO
import base64
from lxml import etree


# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([3,5,7,6,2,6,10,15])
# plt.plot(x, y, 'r', lw=5)
# # plt.plot(x, y, 'g', lw=10)
# plt.bar(x, y, 0.5, color='b')
# plt.show()

# x = np.linspace(-1, 1,5)
# y = x**2
# plt.figure()
# plt.plot(x,y, 'r')
# plt.show()

# x = np.linspace(-1, 1, 50)
# y1 = 2 * x + 1
# y2 = x**2
# plt.figure(num = 5, figsize = (8, 8))
# plt.plot(x, y1)
# plt.plot(x, y2, color = 'red', linewidth = 2.0, linestyle = '--')
# # 轴的显示数值范围
# plt.xlim((-1, 1))
# plt.ylim((0, 3))
# plt.xlabel(u'这是x轴',fontproperties='SimHei',fontsize=22)
# plt.ylabel(u'这是y轴',fontproperties='SimHei',fontsize=14)
# # 设置x轴的精度值
# plt.xticks(np.linspace(-1, 1, 5))
# # 获取当前的坐标轴, gca = get current axis
# ax = plt.gca()
# # 设置右边框和上边框
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# # 设置x坐标轴为下边框
# ax.xaxis.set_ticks_position('bottom')
# # 设置y坐标轴为左边框
# ax.yaxis.set_ticks_position('left')
# # 设置x轴, y周在(0, 0)的位置
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))
#
# x0 = 0
# y0 = 2 * x0 + 1
# plt.scatter(x0, y0, s = 100, color = 'blue')
# plt.plot([x0, x0], [y0, 0], linestyle = '--', linewidth =  2.5, color = 'black')
# plt.text(-0.5, 1.5, r'comment', fontdict = {'size': 32, 'color': 'red'})
# plt.show()

# 定义figure
plt.figure()
# 分隔figure
gs = gridspec.GridSpec(3, 4)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0:2])
ax3 = plt.subplot(gs[1, 2])
ax4 = plt.subplot(gs[2, :])

# 绘制图像
ax1.plot([0, 1], [0, 1])
ax1.set_title('Test')

ax2.plot([0, 1], [0, 1])

ax3.plot([0, 1], [0, 1])

ax4.plot([0, 1], [0, 1])

# plt.show()
# plt.savefig('test.png')
buffer = BytesIO()
plt.savefig(buffer)
plot_data = buffer.getvalue()

imb = base64.b64encode(plot_data)
ims = imb.decode()
imd = "data:image/png;base64,"+ims
iris_im = """<h1>Iris Figure</h1>  """ + """<img src="%s">""" % imd
root = "<title>Iris Dataset</title>"
root = root + iris_im

html = etree.HTML(root)
tree = etree.ElementTree(html)
tree.write('iris.html')
