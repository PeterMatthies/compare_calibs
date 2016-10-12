__author__ = 'Peter'

import matplotlib.pyplot as plt


# old calibration data import
with open('2015-12-10-closed-2D-QMagnet.txt', 'r') as f:
    data = f.readlines()

xv_num, xc_num, yv_num, yc_num, end_num = 0, 0, 0, 0, 0
for i, d in enumerate(data):
    if d.startswith('X-channel SetVoltage'):
        xv_num = i
        continue
    if d.startswith('X-channel Current'):
        xc_num = i
        continue
    if d.startswith('Y-channel SetVoltage'):
        yv_num = i
        continue
    if d.startswith('Y-channel Current'):
        yc_num = i
        continue
    if d.startswith('X-FIT'):
        end_num = i
        break

old_xv = [float(d.split('\t')[0]) for d in data[xv_num+1:xc_num]]
old_xv_field = [float(d.split('\t')[1]) for d in data[xv_num+1:xc_num]]

old_xc = [float(d.split('\t')[0]) for d in data[xc_num+1:yv_num]]
old_xc_field = [float(d.split('\t')[1]) for d in data[xc_num+1:yv_num]]

old_yv = [float(d.split('\t')[0]) for d in data[yv_num+1:yc_num]]
old_yv_field = [float(d.split('\t')[1]) for d in data[yv_num+1:yc_num]]

old_yc = [float(d.split('\t')[0]) for d in data[yc_num+1:end_num]]
old_yc_field = [float(d.split('\t')[1]) for d in data[yc_num+1:end_num]]


#new calibration data import
with open('2016-09-23-pol-xy-axis-QMagnet.txt', 'r') as f:
    data = f.readlines()

xv_num, xc_num, yv_num, yc_num, end_num = 0, 0, 0, 0, 0
for i, d in enumerate(data):
    if d.startswith('X-channel SetVoltage'):
        xv_num = i
        continue
    if d.startswith('X-channel Current'):
        xc_num = i
        continue
    if d.startswith('Y-channel SetVoltage'):
        yv_num = i
        continue
    if d.startswith('Y-channel Current'):
        yc_num = i
        continue
    if d.startswith('X-FIT'):
        end_num = i
        break


new_xv = [float(d.split('\t')[0]) for d in data[xv_num+1:xc_num]]
new_xv_field = [float(d.split('\t')[1]) for d in data[xv_num+1:xc_num]]

new_xc = [float(d.split('\t')[0]) for d in data[xc_num+1:yv_num]]
new_xc_field = [float(d.split('\t')[1]) for d in data[xc_num+1:yv_num]]

new_yv = [float(d.split('\t')[0]) for d in data[yv_num+1:yc_num]]
new_yv_field = [float(d.split('\t')[1]) for d in data[yv_num+1:yc_num]]

new_yc = [float(d.split('\t')[0]) for d in data[yc_num+1:end_num]]
new_yc_field = [float(d.split('\t')[1]) for d in data[yc_num+1:end_num]]




# plotting to the the difference
fig = plt.figure()
fig.suptitle('Calibration Comparsion', fontsize=14, fontweight='bold')

x_voltage_calib = fig.add_subplot(221)
x_voltage_calib.plot(new_xv, new_xv_field, c='green', label='new calibration')
x_voltage_calib.plot(old_xv, old_xv_field, c='red', label='old calibration')
x_voltage_calib.set_xlabel('Set Voltage (V)')
x_voltage_calib.set_ylabel('Field (mT)')
x_voltage_calib.legend(loc=4, prop={'size':10})
x_voltage_calib.set_title('X axis calibration')
x_voltage_calib.grid()

x_current_calib = fig.add_subplot(223)
x_current_calib.plot(new_xc, new_xc_field, c = 'green', label='new calibration')
x_current_calib.plot(old_xc, old_xc_field, c = 'red', label='old calibration')
x_current_calib.set_xlabel('Current (A)')
x_current_calib.legend(loc=4, prop={'size':10})
x_current_calib.set_ylabel('Field (mT)')
x_current_calib.grid()


y_voltage_calib = fig.add_subplot(222)
y_voltage_calib.plot(new_yv, new_yv_field, c='green', label='new calibration')
y_voltage_calib.plot(old_yv, old_yv_field, c='red', label='old calibration')
y_voltage_calib.set_xlabel('Set Voltage (V)')
y_voltage_calib.legend(loc=4, prop={'size':10})
y_voltage_calib.set_title('Y axis calibration')
y_voltage_calib.grid()

y_current_calib = fig.add_subplot(224)
y_current_calib.plot(new_yc, new_yc_field, c = 'green', label='new calibration')
y_current_calib.plot(old_yc, old_yc_field, c = 'red', label='old calibration')
y_current_calib.set_xlabel('Current (A)')
y_current_calib.legend(loc=4, prop={'size':10})
y_current_calib.grid()

# plt.grid()
plt.show()