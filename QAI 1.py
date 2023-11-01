#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ

IBMQ.enable_account('62fa2bb4b28d2cc02387559068c1f665ddb914719151f3ca623911936f153c860754c683bc95c73cd8d0e98c66103330d19681d37d149a322873d67e068b3759')
provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(17,'q')
c = ClassicalRegister(17,'c')
circuit = QuantumCircuit(q,c)
circuit.h(q) # Applies hadamard gate to all qubits
circuit.measure(q,c) # Measures all qubits 

backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=1)
                               
print('Executing Job...\n')                 
result = job.result()
counts = result.get_counts(circuit)

print('RESULT: ',counts,'\n')
print('Press any key to close')


# In[ ]:




