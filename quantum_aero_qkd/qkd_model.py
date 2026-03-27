import math
import matplotlib.pyplot as plt

class TeleportationMission:
    def __init__(self, entangled_kb=15.0):
        self.resource = entangled_kb # Based on your last graph
        
    def run_teleportation(self):
        # We'll try to teleport 1000 'Quantum Frames'
        frames = list(range(1000))
        fidelities = []
        consumed_resource = []
        
        current_resource = self.resource
        
        for f in frames:
            # Teleportation fidelity is affected by the 'purity' of our entanglement
            # We'll simulate a high-quality link (0.85 average fidelity)
            base_fidelity = 0.85
            noise = (math.sin(f/50) * 0.05) # Simulated environmental jitter
            
            fidelities.append(base_fidelity + noise)
            
            # Each teleportation 'consumes' one entangled pair
            current_resource -= 0.01 # 10 bits per frame
            consumed_resource.append(current_resource)
            
        return frames, fidelities, consumed_resource

# Execute Mission
teleport = TeleportationMission()
f_index, fid, res = teleport.run_teleportation()

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Teleported Quantum Frames')
ax1.set_ylabel('Teleportation Fidelity', color='blue')
ax1.plot(f_index, fid, color='blue', alpha=0.7)
ax1.axhline(y=0.67, color='red', linestyle='--', label='Classical Limit')
ax1.set_ylim(0.5, 1.0)
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.set_ylabel('Remaining Entangled Resource (Kb)', color='green')
ax2.plot(f_index, res, color='green', linewidth=2)

plt.title('Mission Lana: Quantum Teleportation Link')
plt.savefig('qkd_teleportation.png')
plt.show()