import matplotlib.pyplot as plt

__author__ = 'Peter Matthies'


# new_filename = '2016-09-23-pol-xy-axis-QMagnet.txt'
# old_filename = '2015-12-10-closed-2D-QMagnet.txt'

# new_filename = '2016-09-23-spol-xy-axis-QMagnet.txt'
new_filename = '2016-09-23-nopol-xy-axis-QMagnet.txt'
old_filename = '2012-01-27-no-pol-flux-closed-2D-QMagnet.txt'

# old calibration data import
with open(old_filename, 'r') as f:
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


# new calibration data import
with open(new_filename, 'r') as f:
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
fig = plt.figure(num=None, figsize=(8, 7), dpi=100, facecolor='w', edgecolor='k')
fig.suptitle('Calibration Comparison\n nopol flux closed on old, flux open on new', fontsize=12, fontweight='bold')

x_voltage_calib = fig.add_subplot(221)
x_voltage_calib.plot(new_xv, new_xv_field, c='green', alpha=0.5, linestyle='--', linewidth=3, label=new_filename[0:10])
x_voltage_calib.plot(old_xv, old_xv_field, c='red', label=old_filename[0:10])
x_voltage_calib.set_xlabel('Set Voltage (V)')
x_voltage_calib.set_ylabel('Field (mT)')
x_voltage_calib.legend(loc=4, prop={'size': 10})
x_voltage_calib.set_title('X axis calibration')
x_voltage_calib.grid()

x_current_calib = fig.add_subplot(223)
x_current_calib.plot(new_xc, new_xc_field, c='green', linestyle='--', linewidth=3, label=new_filename[0:10])
x_current_calib.plot(old_xc, old_xc_field, c='red', label=old_filename[0:10])
x_current_calib.set_xlabel('Current (A)')
x_current_calib.legend(loc=4, prop={'size': 10})
x_current_calib.set_ylabel('Field (mT)')
x_current_calib.grid()


y_voltage_calib = fig.add_subplot(222)
y_voltage_calib.plot(new_yv, new_yv_field, c='green', label=new_filename[0:10])
y_voltage_calib.plot(old_yv, old_yv_field, c='red', label=old_filename[0:10])
y_voltage_calib.set_xlabel('Set Voltage (V)')
y_voltage_calib.legend(loc=4, prop={'size': 10})
y_voltage_calib.set_title('Y axis calibration')
y_voltage_calib.grid()

y_current_calib = fig.add_subplot(224)
y_current_calib.plot(new_yc, new_yc_field, c='green', label=new_filename[0:10])
y_current_calib.plot(old_yc, old_yc_field, c='red', label=old_filename[0:10])
y_current_calib.set_xlabel('Current (A)')
y_current_calib.legend(loc=4, prop={'size': 10})
y_current_calib.grid()

fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.savefig('nopol_fc_old_fo_new_magnet_compare_calibrations2.eps', format='eps', dpi=1000)
plt.savefig('nopol_fc_old_fo_new_c_magnet_compare_calibrations2.png', format='png', dpi=1000)
plt.show()
