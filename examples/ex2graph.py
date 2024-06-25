import matplotlib.pyplot as plt
import numpy as np

noise_levels = [0]
normal_errors = [0.0024406534653992327]
buckingham_errors = [1.8118504342111766e-07]
normal_mins = [312.71]
buckingham_mins = [87.92]

barWidth = 0.10
r1 = np.arange(len(noise_levels))
r2 = [x + barWidth for x in r1]

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# First subplot
axes[0].bar(r1, normal_mins, color='#FF6666', width=barWidth, label='Normal Files')
axes[0].bar(r2, buckingham_mins, color='lightgreen', width=barWidth, label='Buckingham π Files')
axes[0].set_xlabel('Noise Level', fontweight='bold')
axes[0].set_ylabel('Solution Time (minutes)', fontweight='bold')
axes[0].set_title('Solution Time vs Noise Level', fontsize=12, fontweight='bold')
axes[0].set_xticks([r + barWidth/2 for r in range(len(noise_levels))])
axes[0].set_xticklabels(noise_levels)
axes[0].legend(fontsize='small')

# Second subplot
r3 = np.arange(len(normal_mins))
r4 = [x + barWidth for x in r3]
axes[1].bar(r3, normal_errors, color='#FF6666', width=barWidth, label='Normal Files')
axes[1].bar(r4, buckingham_errors, color='lightgreen', width=barWidth, label='Buckingham π Files')
axes[1].set_xlabel('Solution Time (minutes)', fontweight='bold')
axes[1].set_ylabel('Error', fontweight='bold')
axes[1].set_title('Time vs Error', fontsize=12, fontweight='bold')
axes[1].set_xticks([r + barWidth/2 for r in range(len(normal_mins))])
axes[1].set_xticklabels(normal_mins)
axes[1].legend(fontsize='small')

# Third subplot
axes[2].bar(r1, normal_errors, color='#FF6666', width=barWidth, label='Normal Files')
axes[2].bar(r2, buckingham_errors, color='lightgreen', width=barWidth, label='Buckingham π Files')
axes[2].set_xlabel('Noise Level', fontweight='bold')
axes[2].set_ylabel('Error', fontweight='bold')
axes[2].set_title('Error vs Noise', fontsize=12, fontweight='bold')
axes[2].set_xticks([r + barWidth/2 for r in range(len(noise_levels))])
axes[2].set_xticklabels(noise_levels)
axes[2].legend(fontsize='small')
plt.show()