import numpy as np
import matplotlib.pyplot as plt
import os

# original_data = np.loadtxt('./data/synthetic_data_1_new.csv')
#
# fake_data = np.loadtxt('fake1/fake_data_14.csv')
#
#
#
# data_min = np.min(original_data)
# data_max = np.max(original_data)
#
#
# scaled_data = (original_data - data_min) / (data_max - data_min)
#
#
# plt.figure(figsize=(5, 12))
# plt.subplot(3, 1, 1)
# plt.plot(original_data)
# plt.title('Original Data')
# plt.xlabel('Sample')
# plt.ylabel('Value')
#
#
# plt.subplot(3, 1, 2)
# plt.plot(scaled_data)
# plt.title('Scaled Data')
# plt.xlabel('Sample')
# plt.ylabel('Value')
#
#
#
# plt.subplot(3, 1, 3)
# plt.plot(fake_data)
# plt.title('Fake Data')
# plt.xlabel('Sample')
# plt.ylabel('Value')
#
#
# plt.tight_layout()
#
#
# plt.show()




original_data_dir = './data'
scaled_data_dir = './scale'


if not os.path.exists(scaled_data_dir):
    os.makedirs(scaled_data_dir)


for filename in os.listdir(original_data_dir):
    if filename.endswith('.csv'):

        original_data = np.loadtxt(os.path.join(original_data_dir, filename))

        data_min = np.min(original_data)
        data_max = np.max(original_data)

        scaled_data = (original_data - data_min) / (data_max - data_min)
        scaled_filename = os.path.splitext(filename)[0] + '_scaled.csv'
        scaled_filepath = os.path.join(scaled_data_dir, scaled_filename)
        np.savetxt(scaled_filepath, scaled_data, delimiter=',')

        print(f'Scaled data saved to {scaled_filepath}')
